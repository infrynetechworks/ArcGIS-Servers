import asyncio
import re
import aiohttp
from datetime import datetime

README_FILE = "README.md"
OUTPUT_FILE = "SERVER_STATUS.md"
TIMEOUT_SECONDS = 12
CONCURRENCY_LIMIT = 25  # Limit concurrent connections to avoid rate limiting


def extract_server_urls(filepath: str) -> list[str]:
    """Extract unique ArcGIS REST URLs from markdown links or text."""
    url_pattern = re.compile(r"https?://[^\s\)\]\"']+/rest/services[^\s\)\]\"']*")
    urls = set()
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            for match in url_pattern.finditer(line):
                urls.add(match.group(0).rstrip("/"))
    return sorted(list(urls))


async def check_endpoint(session: aiohttp.ClientSession, url: str, semaphore: asyncio.Semaphore) -> dict:
    test_url = f"{url}?f=pjson"
    headers = {"User-Agent": "ArcGIS-Server-Monitor/1.0"}

    async with semaphore:
        try:
            start_time = asyncio.get_event_loop().time()
            async with session.get(test_url, headers=headers, ssl=False) as resp:
                elapsed_ms = round((asyncio.get_event_loop().time() - start_time) * 1000)
                if resp.status == 200:
                    try:
                        data = await resp.json(content_type=None)
                        if "error" in data:
                            return {"url": url, "status": "Error Response", "code": data.get("error", {}).get("code", 400), "latency": elapsed_ms}
                        return {"url": url, "status": "Online", "code": 200, "latency": elapsed_ms}
                    except Exception:
                        # Responded 200 HTML or raw text
                        return {"url": url, "status": "Online (HTML/TOC)", "code": 200, "latency": elapsed_ms}
                elif resp.status in (401, 403):
                    return {"url": url, "status": "Restricted/Auth", "code": resp.status, "latency": elapsed_ms}
                else:
                    return {"url": url, "status": "Down/Error", "code": resp.status, "latency": elapsed_ms}
        except asyncio.TimeoutError:
            return {"url": url, "status": "Timeout", "code": "N/A", "latency": "Timed Out"}
        except Exception as e:
            return {"url": url, "status": f"Unreachable ({type(e).__name__})", "code": "ERR", "latency": "N/A"}


async def main():
    urls = extract_server_urls(README_FILE)
    print(f"Discovered {len(urls)} unique ArcGIS servers in {README_FILE}. Checking health...")

    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
    timeout = aiohttp.ClientTimeout(total=TIMEOUT_SECONDS)

    connector = aiohttp.TCPConnector(limit=CONCURRENCY_LIMIT, ssl=False)
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        tasks = [check_endpoint(session, url, semaphore) for url in urls]
        results = await asyncio.gather(*tasks)

    # Summarize stats
    online_count = sum(1 for r in results if "Online" in r["status"])
    total_count = len(results)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write(f"# ArcGIS Server Status Report\n\n")
        out.write(f"- **Last Updated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
        out.write(f"- **Online Servers:** {online_count} / {total_count} ({round((online_count/total_count)*100, 1) if total_count else 0}%)\n\n")
        out.write("| Server Endpoint | Status | HTTP Code | Latency |\n")
        out.write("| :--- | :---: | :---: | :---: |\n")
        for r in results:
            badge = "🟢" if "Online" in r["status"] else ("🟡" if "Auth" in r["status"] else "🔴")
            out.write(f"| `{r['url']}` | {badge} {r['status']} | {r['code']} | {r['latency']} ms |\n")

    print(f"Done! Status report written to {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(main())