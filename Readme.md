# Public ArcGIS REST Services Directory

A curated collection of public-facing federal, state, county, regional, and municipal ArcGIS REST service directories across the United States, U.S. Territories, and select organizations.
---

## Table of Contents
1. [Usage & Tips](#usage--tips)
2. [Federal GIS Servers](#federal-gis-servers)
3. [State, County & City GIS Servers](#state-county--city-gis-servers)
   - [Alabama](#alabama) | [Alaska](#alaska) | [Arizona](#arizona) | [Arkansas](#arkansas) | [California](#california)
   - [Colorado](#colorado) | [Connecticut](#connecticut) | [Delaware](#delaware) | [Florida](#florida) | [Georgia](#georgia)
   - [Hawaii](#hawaii) | [Idaho](#idaho) | [Illinois](#illinois) | [Indiana](#indiana) | [Iowa](#iowa)
   - [Kansas](#kansas) | [Kentucky](#kentucky) | [Louisiana](#louisiana) | [Maine](#maine) | [Maryland](#maryland)
   - [Massachusetts](#massachusetts) | [Michigan](#michigan) | [Minnesota](#minnesota) | [Mississippi](#mississippi) | [Missouri](#missouri)
   - [Montana](#montana) | [Nebraska](#nebraska) | [Nevada](#nevada) | [New Hampshire](#new-hampshire) | [New Jersey](#new-jersey)
   - [New Mexico](#new-mexico) | [New York](#new-york) | [North Carolina](#north-carolina) | [North Dakota](#north-dakota) | [Ohio](#ohio)
   - [Oklahoma](#oklahoma) | [Oregon](#oregon) | [Pennsylvania](#pennsylvania) | [Rhode Island](#rhode-island) | [South Carolina](#south-carolina)
   - [South Dakota](#south-dakota) | [Tennessee](#tennessee) | [Texas](#texas) | [Utah](#utah) | [Vermont](#vermont)
   - [Virginia](#virginia) | [Washington](#washington) | [West Virginia](#west-virginia) | [Wisconsin](#wisconsin) | [Wyoming](#wyoming)
4. [Washington D.C.](#washington-dc)
5. [Native American Tribes](#native-american-tribes)
6. [U.S. Territories](#us-territories)
7. [Multi-State & Regional Planning](#multi-state--regional-planning)
8. [Environmental & Non-Profit Organizations](#environmental--non-profit-organizations)
9. [National & Miscellaneous Collections](#national--miscellaneous-collections)
10. [International & Canada](#international--canada)

---

## Usage & Tips

- **Table of Contents Disabled:** When an ArcGIS server shows `Services Directory has been disabled`, you can query the endpoints directly as JSON by appending `?f=pjson` (e.g., `https://[server]/arcgis/rest/services?f=pjson`).
- **Data Layers:** Endpoints ending in `/MapServer`, `/FeatureServer`, or `/ImageServer` can be consumed directly by client libraries like Leaflet (via Esri-Leaflet), OpenLayers, QGIS, ArcGIS Pro, and Python (via `geopandas` or `restgdf`).
- **Tiled Data:** Servers hosting WMTS or cached vector/raster tiles can often be identified by replacing or appending `/tile/{z}/{y}/{x}`.

---

## Federal GIS Servers

### U.S. Congress & Legislative
| Agency / Department | Service URL |
| :--- | :--- |
| House of Representatives | `https://services1.arcgis.com/o90r8yeUBWgKSezU/ArcGIS/rest/services` |
| House of Representatives (Tiles) | `https://tiles.arcgis.com/tiles/o90r8yeUBWgKSezU/arcgis/rest/services` |
| Library of Congress | `https://services5.arcgis.com/ohAFyIFvXFRGcC67/ArcGIS/rest/services` |
| Library of Congress (Tiles) | `https://tiles.arcgis.com/tiles/ohAFyIFvXFRGcC67/arcgis/rest/services` |

### Department of Agriculture (USDA)
| Agency / Unit | Service URL |
| :--- | :--- |
| General Agriculture Data | `https://services1.arcgis.com/SyUSN23vOoYdfLC8/arcgis/rest/services` |
| General Agriculture (Tiles) | `https://tiles.arcgis.com/tiles/SyUSN23vOoYdfLC8/arcgis/rest/services` |
| Enterprise Geospatial Management | `https://services8.arcgis.com/5vMtpwj1mnc06Rmi/arcgis/rest/services` |
| Foreign Agricultural Service (FAS) 1 | `https://geo.fas.usda.gov/arcgis1/rest/services` |
| Foreign Agricultural Service (FAS) 2 | `https://geo.fas.usda.gov/arcgis2/rest/services` |
| Foreign Agricultural Service (FAS) Cloud | `https://services.arcgis.com/Z58T9dmhcpCmous1/arcgis/rest/services` |
| Foreign Agricultural Service (Tiles) | `https://tiles.arcgis.com/tiles/Z58T9dmhcpCmous1/arcgis/rest/services` |
| Economic Research Service (ERS) | `https://gisportal.ers.usda.gov/server/rest/services` |
| FPAC Business Center (NAIP Imagery) | `https://gis.apfo.usda.gov/arcgis/rest/services` |
| Marketing and Regulatory Programs | `https://services7.arcgis.com/2C1NQ7u6M6SXoa8p/ArcGIS/rest/services` |
| USFS Enterprise Data Warehouse (EDW) | `https://apps.fs.usda.gov/arcx/rest/services/EDW` |
| USFS Geodata Hub | `https://apps.fs.usda.gov/arcx/rest/services` |
| USFS Forest Health | `https://apps.fs.usda.gov/fsgisx02/rest/services/foresthealth` |
| USFS Services 01 | `https://apps.fs.usda.gov/fsgisx01/rest/services` |
| USFS Services 02 | `https://apps.fs.usda.gov/fsgisx02/rest/services` |
| USFS Services 03 | `https://apps.fs.usda.gov/fsgisx03/rest/services` |
| USFS Services 04 | `https://apps.fs.usda.gov/fsgisx04/rest/services` |
| USFS Services 05 | `https://apps.fs.usda.gov/fsgisx05/rest/services` |
| USFS NWCG Fire Applications | `https://fsapps.nwcg.gov/psp/arcgis/rest/services` |
| USFS Region 6 | `https://services1.arcgis.com/gGHDlz6USftL5Pau/arcgis/rest/services` |
| USFS Region 6 (Tiles) | `https://tiles.arcgis.com/tiles/gGHDlz6USftL5Pau/arcgis/rest/services` |
| USFS DMSM | `https://apps.fs.usda.gov/dmsm/rest/services` |
| NRCS Cloud | `https://services.arcgis.com/SXbDpmb7xQkk44JV/arcgis/rest/services` |
| NRCS (Tiles) | `https://tiles.arcgis.com/tiles/SXbDpmb7xQkk44JV/arcgis/rest/services` |
| Rural Development | `https://rdgdwe.sc.egov.usda.gov/arcgis/rest/services` |
| Rural Development Cloud | `https://services.arcgis.com/UbyviKPk0x1UemzF/arcgis/rest/services` |
| SciNet Computing Facility | `https://pdi.scinet.usda.gov/image/rest/services` |

### Department of Commerce (DOC) & NOAA
| Agency / Program | Service URL |
| :--- | :--- |
| Census Bureau (TIGERweb) | `https://tigerweb.geo.census.gov/arcgis/rest/services` |
| Census Bureau Services | `https://services8.arcgis.com/DlJzJLOZpPXmMpWi/ArcGIS/rest/services` |
| Census Bureau (Tiles) | `https://tiles.arcgis.com/tiles/DlJzJLOZpPXmMpWi/arcgis/rest/services` |
| NOAA Water Center (Flood Data) | `https://maps.water.noaa.gov/server/rest/services` |
| NOAA Coastal Imagery | `https://imagery.coast.noaa.gov/arcgis/rest/services` |
| NOAA Weather & Fire Perimeters | `https://services9.arcgis.com/RHVPKKiFTONKtxq3/ArcGIS/rest/services` |
| NOAA Office for Coastal Management | `https://www.coast.noaa.gov/arcgis/rest/services` |
| NOAA Coastal Geospatial Hub | `https://coast.noaa.gov/arcgismc/rest/services` |
| NOAA Fisheries | `https://maps.fisheries.noaa.gov/server/rest/services` |
| NOAA Seamless Nautical Charts | `https://seamlessrnc.nauticalcharts.noaa.gov/arcgis/rest/services` |
| NOAA Coastal Maps | `https://maps.coast.noaa.gov/arcgis/rest/services` |
| NOAA Coastal Maps 1 | `https://maps1.coast.noaa.gov/arcgis/rest/services` |
| NOAA Coastal Maps 2 | `https://maps2.coast.noaa.gov/arcgis/rest/services` |
| NOAA Maritime Boundaries | `https://maritimeboundaries.noaa.gov/arcgis/rest/services` |
| NOAA Chart Tools & NGS Benchmarks | `https://gis.charttools.noaa.gov/arcgis/rest/services` |
| NOAA NESDIS Satellite Maps | `https://satellitemaps.nesdis.noaa.gov/arcgis/rest/services` |
| NOAA Storm Damage Assessment (DAT) | `https://services.dat.noaa.gov/arcgis/rest/services` |
| NOAA Operational Cloud Services | `https://services2.arcgis.com/C8EMgrsFcRFL6LrL/arcgis/rest/services` |
| NOAA NNVL Global Data | `https://gis.nnvl.noaa.gov/arcgis/rest/services` |
| NWS NCEP Static Services | `https://mapservices.weather.noaa.gov/static/rest/services` |
| NWS NCEP Experimental (Flood Outlook) | `https://mapservices.weather.noaa.gov/experimental/rest/services` |
| NWS NCEP Event-Driven (Hazards) | `https://mapservices.weather.noaa.gov/eventdriven/rest/services` |
| NWS NCEP Tropical | `https://mapservices.weather.noaa.gov/tropical/rest/services` |
| NWS NCEP Raster (Winter & Snow) | `https://mapservices.weather.noaa.gov/raster/rest/services` |
| NOAA NCEI (formerly NGDC Hazards) | `https://gis.ngdc.noaa.gov/arcgis/rest/services` |
| NOAA NCDC Climatic Data | `https://gis.ncdc.noaa.gov/arcgis/rest/services` |
| NOAA Electronic Nautical Charts (ENC) | `https://encdirect.noaa.gov/arcgis/rest/services` |
| NOAA Wrecks & Obstructions | `https://wrecks.nauticalcharts.noaa.gov/arcgis/rest/services` |

### Department of Defense (DOD)
| Division | Service URL |
| :--- | :--- |
| USACE Inland Electronic Nav Charts | `https://ienccloud.us/arcgis/rest/services` |
| USACE River Mile Markers | `https://services7.arcgis.com/n1YM8pTrFmm7L4hs/ArcGIS/rest/services` |
| USACE River Mile Markers (Tiles) | `https://tiles.arcgis.com/tiles/n1YM8pTrFmm7L4hs/arcgis/rest/services` |
| USACE Geospatial Center (Districts) | `https://geospatial.sec.usace.army.mil/server/rest/services` |
| USACE National Inventory of Dams (DLS) | `https://geospatial.sec.usace.army.mil/dls/rest/services` |
| USACE Spatial Services | `https://spatial.usace.army.mil/opjarcgis/rest` |
| USACE Charleston District | `https://services7.arcgis.com/woolevDLYznutGEM/ArcGIS/rest/services` |
| USACE Kansas City District | `https://services5.arcgis.com/W7M7ugHEl8tg1wcM/ArcGIS/rest/services` |
| USACE Los Angeles District | `https://services6.arcgis.com/wyJygLsBd4XEYUkl/ArcGIS/rest/services` |
| USACE Norfolk District | `https://services5.arcgis.com/NCw7W7TLyX11Qly1/ArcGIS/rest/services` |
| USACE Rock Island District | `https://services7.arcgis.com/zv5PbHd04c1UNAiH/ArcGIS/rest/services` |
| National Geospatial-Intelligence Agency | `https://geonames.nga.mil/geon-ags/rest/services` |
| Arlington National Cemetery (ANC) | `https://ancexplorer.army.mil/arcgis/rest/services` |

### Department of Energy (DOE) & Interior (DOI)
| Organization / Bureau | Service URL |
| :--- | :--- |
| Bonneville Power Administration (BPA) | `https://services3.arcgis.com/Iz3chmSt4P7oOoZy/arcgis/rest/services` |
| National Energy Technology Lab (NETL) | `https://prod.arcgis.netl.doe.gov/server/rest/services` |
| Office of Legacy Management (GEMS) | `https://gems.lm.doe.gov/arcgis/rest/services` |
| Argonne National Laboratory | `https://disgeoportal.egs.anl.gov/arcgis/rest/services` |
| Energy Information Administration (EIA) | `https://services.arcgis.com/jDGuO8tYggdCCnUJ/arcgis/rest/services` |
| Bureau of Land Management (BLM) National | `https://gis.blm.gov/arcgis/rest/services` |
| BLM Alaska | `https://gis.blm.gov/akarcgis/rest/services` |
| BLM Arizona | `https://gis.blm.gov/azarcgis/rest/services` |
| BLM California | `https://gis.blm.gov/caarcgis/rest/services` |
| BLM Colorado | `https://gis.blm.gov/coarcgis/rest/services` |
| BLM Idaho | `https://gis.blm.gov/idarcgis/rest/services` |
| BLM Oregon | `https://gis.blm.gov/orarcgis/rest/services` |
| BLM Montana | `https://gis.blm.gov/mtarcgis/rest/services` |
| BLM Nevada | `https://gis.blm.gov/nvarcgis/rest/services` |
| BLM New Mexico | `https://gis.blm.gov/nmarcgis/rest/services` |
| BLM Utah | `https://gis.blm.gov/utarcgis/rest/services` |
| BLM Wyoming | `https://gis.blm.gov/wyarcgis/rest/services` |
| BLM Alaska Fire Service | `https://fire.ak.blm.gov/arcgis/rest/services` |
| Bureau of Ocean Energy Mgmt (BOEM) | `https://gis.boem.gov/arcgis/rest/services` |
| Bureau of Reclamation (USBR) | `https://geo.usbr.gov/server/rest/services` |
| U.S. Fish & Wildlife (Wetlands) | `https://www.fws.gov/wetlandsmapservice/rest/services` |
| USFWS Critical Habitat & Datasets | `https://services.arcgis.com/QVENGdaPbd4LUkLV/ArcGIS/rest/services` |
| Bureau of Indian Affairs (BIA) | `https://biamaps.geoplatform.gov/server/rest/services` |
| National Park Service (NPS Datasets) | `https://mapservices.nps.gov/arcgis/rest/services` |
| NPS Park Operations & Portals | `https://services1.arcgis.com/fBc8EJBxQRMcHlei/ArcGIS/rest/services` |
| NPS IRMA Services | `https://irmaservices.nps.gov/arcgis/rest/services` |
| Office of Surface Mining (OSMRE) | `https://geoservices.osmre.gov/arcgis/rest/services` |

### USGS & The National Map
| Program / Mission | Service URL |
| :--- | :--- |
| USGS Basemaps (US Topo) | `https://basemap.nationalmap.gov/arcgis/rest/services` |
| USGS Map Indexes | `https://index.nationalmap.gov/arcgis/rest/services` |
| USGS National Digital Trails | `https://partnerships.nationalmap.gov/arcgis/rest/services` |
| USGS Hydrography (NHD) | `https://hydro.nationalmap.gov/arcgis/rest/services` |
| USGS 3D Hydrography Program (3DHP) | `https://3dhp.nationalmap.gov/arcgis/rest/services` |
| USGS Cartographic Services | `https://carto.nationalmap.gov/arcgis/rest/services` |
| USGS Elevation Services | `https://elevation.nationalmap.gov/arcgis/rest/services` |
| USGS Imagery Services (NAIP) | `https://imagery.nationalmap.gov/arcgis/rest/services` |
| USGS Wind Turbine Database | `https://eerscmap.usgs.gov/arcgis/rest/services` |
| USGS Reference & Lat/Long Grids | `https://nimbus.cr.usgs.gov/arcgis/rest/services` |
| USGS Earthquakes & Landslides | `https://earthquake.usgs.gov/arcgis/rest/services` |
| USGS National Geologic Map Database | `https://ngmdb.usgs.gov/arcgis/rest/services` |
| USGS Energy Resources | `https://energy.usgs.gov/arcgis/rest/services` |
| USGS Grand Canyon Studies | `https://grandcanyon.usgs.gov/server/rest/services` |

### EPA, NASA, FEMA, Transportation & Others
| Entity | Service URL |
| :--- | :--- |
| FEMA Hazus & Flood (NFHL) | `https://hazards.fema.gov/arcgis/rest/services` |
| FEMA Operational GIS | `https://gis.fema.gov/arcgis/rest/services/` |
| FEMA Cloud Services | `https://services.arcgis.com/XG15cJAlne2vxtgt/ArcGIS/rest/services` |
| HUD Geospatial Storefront | `https://egis.hud.gov/arcgis/rest/services` |
| CDC OneMap | `https://onemap.cdc.gov/onemapservices/rest/services` |
| HRSA Spatial Portal | `https://gisportal.hrsa.gov/server/rest/services` |
| Indian Health Service (IHS) | `https://maps.ihs.gov/server/rest/services` |
| Bureau of Transportation Stats (NTAD) | `https://services.arcgis.com/xOilkZaI0eWDREZv/ArcGIS/rest/services` |
| Federal Highway Admin (HSIP / Pipelines) | `https://geo.dot.gov/server/rest/services` |
| Federal Aviation Admin (UAS Drone Zones) | `https://services6.arcgis.com/ssFJjBXIUyZDrSYZ/arcgis/rest/services` |
| Federal Railroad Admin (FRA) | `https://fragis.fra.dot.gov/arcgis/rest/services` |
| EPA Environmental Data Gateway (EDG) | `https://edg.epa.gov/arcgis/rest/services` |
| EPA EnviroAtlas | `https://enviroatlas.epa.gov/arcgis/rest/services` |
| EPA WATERS Geodatabase | `https://watersgeo.epa.gov/arcgis/rest/services` |
| EPA ECHO Compliance History | `https://echogeo.epa.gov/arcgis/rest/services` |
| EPA GeoPub Public Services | `https://geopub.epa.gov/arcgis/rest/services` |
| EPA GISPub | `https://gispub.epa.gov/arcgis/rest/services` |
| EPA GeoData | `https://geodata.epa.gov/arcgis/rest/services` |
| NASA SERVIR Global | `https://gis1.servirglobal.net/arcgis/rest/services` |
| NASA MODIS & VIIRS Imagery | `https://modis.arcgis.com/arcgis/rest/services` |
| NASA Langley Earth Science | `https://gis.earthdata.nasa.gov/image/rest/services` |
| NASA GIBS Mapping Services | `https://gis.earthdata.nasa.gov/maphost/rest/services` |
| NASA Landsat Imagery | `https://landsat2.arcgis.com/arcgis/rest/services` |
| USPS Delivery / ZIP Boundaries | `https://gis.usps.com/arcgis/rest/services` |

---

## State, County & City GIS Servers

### Alabama
- **State Conservation (ADCNR):** `https://conservationgis.alabama.gov/adcnrweb/rest/services`
- **Economic & Community Affairs (ADECA):** `https://services7.arcgis.com/ecupH7bxameyeamw/ArcGIS/rest/services`
- **Environmental Management (ADEM):** `https://gis.adem.alabama.gov/arcgis/rest/services`
- **Department of Transportation (ALDOT):** `https://aldotgis.dot.state.al.us/pubgis1/rest/services`
- **ALDOT Imagery:** `https://aldotgis.dot.state.al.us/imggis/rest/services`
- **Emergency Management (EMA):** `https://services5.arcgis.com/Z9xwByitYQVMAR7n/ArcGIS/rest/services`
- **Forestry Commission:** `https://gis.forestry.alabama.gov/arcgis/rest/services`
- **Geological Survey (GSA):** `https://map.gsa.state.al.us/arcgis/rest/services`
- **Alabama Enterprise Services:** `https://maps.alabama.gov/algogis/rest/services`
- **Counties:**
  - Autauga: `https://maps.capturecama.com/arcgis/rest/services/Autauga`
  - Baldwin: `https://web5.kcsgis.com/kcsgis/rest/services/Baldwin`
  - Barbour: `https://maps.capturecama.com/arcgis/rest/services/Barbour`
  - Cherokee: `https://web3.kcsgis.com/kcsgis/rest/services/Cherokee`
  - Cullman: `https://al25portal.kcsgis.com/al25server/rest/services`
  - Dallas: `https://maps.capturecama.com/arcgis/rest/services/Dallas`
  - Elmore: `https://maps.capturecama.com/arcgis/rest/services/Elmore`
  - Etowah: `https://web3.kcsgis.com/kcsgis/rest/services/Etowah`
  - Franklin: `https://web5.kcsgis.com/kcsgis/rest/services/Franklin`
  - Jefferson: `https://jccgis.jccal.org/server/rest/services`
  - Lauderdale: `https://web5.kcsgis.com/kcsgis/rest/services/Lauderdale`
  - Lawrence: `https://web6.kcsgis.com/kcsgis/rest/services/Lawrence`
  - Madison: `https://maps.madisonal.gov/server/rest/services`
  - Marshall: `https://web5.kcsgis.com/kcsgis/rest/services/Marshall`
  - Mobile: `https://gis.mobilecountyal.gov/server/rest/services`
  - Montgomery: `https://gis.montgomeryal.gov/server/rest/services`
  - Shelby: `https://maps.shelbyal.com/gisserver/rest/services`
  - Tuscaloosa: `https://arcgis.tuscco.com/arcgis5/rest/services`
- **Cities:**
  - Auburn: `https://gis.auburnalabama.org/public/rest/services`
  - Birmingham: `https://gisweb.birminghamal.gov/arcgis/rest/services`
  - Foley: `https://arcgis.cityoffoley.org/server/rest/services`
  - Gadsden: `https://coggis.cityofgadsden.com/arcgis/rest/services`
  - Huntsville: `https://maps.huntsvilleal.gov/server/rest/services`
  - Mobile: `https://maps.cityofmobile.org/arcgis/rest/services`

---

### Alaska
- **State Enterprise Portal:** `https://geoportal.alaska.gov/arcgis/rest/services`
- **DGGS Geological Survey:** `https://geoportal.dggs.dnr.alaska.gov/arcgis/rest/services`
- **Commerce & Economic Development:** `https://maps.commerce.alaska.gov/server/rest/services`
- **Environmental Conservation (DEC):** `https://dec.alaska.gov/arcgis/rest/services`
- **Fish and Game (ADFG):** `https://gis.adfg.alaska.gov/mapping/rest/services`
- **Natural Resources (DNR):** `https://arcgis.dnr.alaska.gov/arcgis/rest/services`
- **Elevation Portal:** `https://elevation.alaska.gov/arcgis/rest/services`
- **Boroughs & Cities:**
  - Fairbanks North Star Borough: `https://gisportal.fnsb.gov/referenced/rest/services`
  - Matanuska-Susitna Borough: `https://maps.matsugov.us/map/rest/services`
  - Anchorage (City): `https://www.ancgis.com/arcgis/rest/services`
  - Juneau: `https://epv.ci.juneau.ak.us/arcgis/rest/services`

---

### Arizona
- **AZGeo Open Data:** `https://azgeo.az.gov/arcgis/rest/services`
- **Game and Fish Department:** `https://maps.azgfd.com/server/rest/services`
- **Department of Water Resources:** `https://azwatermaps.azwater.gov/arcgis/rest/services`
- **Maricopa Association of Governments (MAG):** `https://geo.azmag.gov/arcgis/rest/services`
- **Counties:**
  - Gila: `https://gis.gilacountyaz.gov/arcgis/rest/services`
  - La Paz: `https://gis.lapazcountyaz.org/server/rest/services`
  - Maricopa: `https://gis.mcassessor.maricopa.gov/arcgis/rest/services`
  - Mohave: `https://mcgis.mohave.gov/arcgis/rest/services`
  - Pima: `https://pimamaps.pima.gov/arcgis/rest/services`
  - Pinal: `https://gis.pinal.gov/mapping/rest/services`
  - Santa Cruz: `https://mapservices.santacruzcountyaz.gov/wagis01/rest/services`
  - Yavapai: `https://gis.yavapaiaz.gov/arcgis/rest/services`
  - Yuma: `https://arcgis.yumacountyaz.gov/webgis/rest/services`
- **Cities:**
  - Buckeye: `https://maps.buckeyeaz.gov/server/rest/services`
  - Chandler: `https://gis.chandleraz.gov/images/rest/services`
  - Flagstaff: `https://gis.flagstaffaz.gov/arcgisserver/rest/services`
  - Florence: `https://arcgis.florenceaz.gov/arcgis/rest/services`
  - Gilbert: `https://maps.gilbertaz.gov/arcgis/rest/services`
  - Glendale: `https://gismaps.glendaleaz.com/gisserver/rest/services`
  - Goodyear: `https://maps.goodyearaz.gov/server/rest/services`
  - Mesa: `https://gis.mesaaz.gov/mesaaz/rest/services`
  - Peoria: `https://gis.peoriaaz.gov/arcgis/rest/services`
  - Phoenix: `https://maps.phoenix.gov/pub/rest/services`
  - Scottsdale: `https://maps.scottsdaleaz.gov/arcgis/rest/services`
  - Tempe: `https://gis.tempe.gov/arcgis/rest/services`
  - Tucson: `https://mapdata.tucsonaz.gov/arcgis/rest/services`

---

### Arkansas
- **Arkansas GIS Office:** `https://gis.arkansas.gov/arcgis/rest/services`
- **Environmental Quality (ADEQ):** `https://gis.adeq.state.ar.us/arcgis/rest/services`
- **Department of Transportation (ARDOT):** `https://gis.ardot.gov/hosting/rest/services`
- **Game and Fish Commission:** `https://gisec2.agfc.com/arcgis/rest/services`
- **Counties & Regions:**
  - Pulaski (PAGIS): `https://www.pagis.org/arcgis/rest/services`
  - Benton: `https://gis.bentoncountyar.gov/arcgis/rest/services`
- **Cities:**
  - Bentonville: `https://gis.bentonvillear.com/arcgis/rest/services`
  - Conway: `https://data.conwayarkansas.gov/arcgis/rest/services`
  - Fayetteville: `https://maps.fayetteville-ar.gov/server/rest/services`
  - Fort Smith: `https://gis.fortsmithar.gov/arcgis/rest/services`
  - Little Rock: `https://maps.littlerock.gov/server/rest/services`
  - Rogers: `https://gis.rogersar.gov/gis/rest/services`

---

### California
- **Conservation (Earthquake Hazards):** `https://gis.conservation.ca.gov/server/rest/services`
- **Caltrans Enterprise GIS:** `https://caltrans-gis.dot.ca.gov/arcgis/rest/services`
- **Department of Water Resources (DWR):** `https://gis.water.ca.gov/arcgis/rest/services`
- **DWR Imagery & Levees:** `https://gis.water.ca.gov/arcgisimg/rest/services`
- **State Water Resources Control Board:** `https://gispublic.waterboards.ca.gov/arcgis/rest/services`
- **Natural Resources Agency (CNRA):** `https://gis.cnra.ca.gov/arcgis/rest/services`
- **Regional Agencies:**
  - San Diego Association of Governments (SANDAG): `https://gis.sandag.org/sdgis/rest/services`
  - Southern California Association of Governments (SCAG): `https://maps.scag.ca.gov/scaggis/rest/services`
  - Coastal Water Research (SCCWRP): `https://gis.sccwrp.org/arcgis/rest/services`
- **Counties:**
  - Butte: `https://gisportal.buttecounty.net/arcgis/rest/services`
  - Contra Costa: `https://ccmap.cccounty.us/arcgis/rest/services`
  - El Dorado: `https://see-eldorado.edcgov.us/arcgis/rest/services`
  - Fresno: `https://gisprod10.co.fresno.ca.us/server/rest/services`
  - Inyo: `https://gis.inyo.gov/server/rest/services`
  - Kern: `https://maps.co.kern.ca.us/arcgis/rest/services`
  - Los Angeles County: `https://public.gis.lacounty.gov/public/rest/services`
  - Los Angeles County Assessor: `https://assessor.gis.lacounty.gov/assessor/rest/services`
  - Los Angeles County Public Works: `https://dpw.gis.lacounty.gov/dpw/rest/services`
  - Marin: `https://gis.marinpublic.com/arcgis/rest/services`
  - Merced: `https://gis.countyofmerced.com/server/rest/services`
  - Mono: `https://gis.mono.ca.gov/webgis/rest/services`
  - Monterey: `https://maps.co.monterey.ca.us/server/rest/services`
  - Napa: `https://gis.napa.ca.gov/arcgis/rest/services`
  - Nevada: `https://maps.nevadacountyca.gov/arcgis/rest/services`
  - Orange: `https://www.ocgis.com/arcpub/rest/services`
  - Riverside: `https://gis.countyofriverside.us/arcgis_public/rest/services`
  - Riverside County Flood: `https://content.rcflood.org/arcgis/rest/services`
  - Sacramento: `https://mapservices.gis.saccounty.net/arcgis/rest/services`
  - San Benito: `https://gisweb.cosb.us/arcgis/rest/services`
  - San Bernardino: `https://maps.sbcounty.gov/arcgis/rest/services`
  - San Diego: `https://gis-public.sandiegocounty.gov/arcgis/rest/services`
  - San Francisco Planning: `https://sfplanninggis.org/arcgiswa/rest/services`
  - San Joaquin: `https://sjmap.org/ArcGIS/rest/services`
  - San Luis Obispo: `https://gis.slocounty.ca.gov/arcgis/rest/services`
  - San Mateo: `https://gis.smcgov.org/image/rest/services`
  - Santa Cruz: `https://gis.santacruzcounty.us/arcserver/rest/services`
  - Shasta: `https://gis.shastacounty.gov/arcgis/rest/services`
  - Solano: `https://solanocountygis.com/server/rest/services`
  - Sonoma: `https://socogis.sonomacounty.ca.gov/map/rest/services`
  - Ventura: `https://maps.ventura.org/arcgis/rest/services`
  - Yolo: `https://gis.yolocounty.gov/ext/rest/services`
- **Cities:**
  - Bakersfield: `https://gis.bakersfieldcity.us/webmaps/rest/services`
  - Berkeley: `https://gis.cityofberkeley.info/arcgis3/rest/services`
  - Carlsbad: `https://gisportals.carlsbadca.gov/arcgis/rest/services`
  - Fresno (City): `https://gis4u.fresno.gov/arcgis/rest/services`
  - Glendale: `https://gismap.glendaleca.gov/arcgis/rest/services`
  - Irvine: `https://gis.cityofirvine.org/arcgis/rest/services`
  - Los Angeles (City): `https://maps.lacity.org/arcgis/rest/services`
  - Oakland: `https://gismaps.oaklandca.gov/oaklandgis/rest/services`
  - Pasadena: `https://services2.arcgis.com/zNjnZafDYCAJAbN0/arcgis/rest/services`
  - Roseville: `https://ags.roseville.ca.us/arcgis/rest/services`
  - San Diego (City): `https://webmaps.sandiego.gov/arcgis/rest/services`
  - San Jose: `https://geo.sanjoseca.gov/server/rest/services`
  - Santa Monica: `https://gis.santamonica.gov/server/rest/services`

---

### Colorado
- **Colorado Public Health:** `https://www.cohealthmaps.dphe.state.co.us/arcgis/rest/services`
- **Colorado State University (Atlas/Hunting):** `https://ndismaps.nrel.colostate.edu/arcgis/rest/services`
- **Denver Regional Council of Gov (DRCOG):** `https://gis.drcog.org/server/rest/services`
- **Counties:**
  - Adams: `https://gisapp.adcogov.org/arcgis/rest/services`
  - Arapahoe: `https://gis.arapahoegov.com/arcgis/rest/services`
  - Boulder: `https://maps.bouldercounty.org/arcgis/rest/services`
  - Delta: `https://maps.deltacountyco.gov/arcgis/rest/services`
  - Douglas: `https://apps.douglas.co.us/gisis/rest/services`
  - Eagle: `https://map.eaglecounty.us/arcgiswa/rest/services`
  - El Paso: `https://gisservices.elpasoco.com/arcgis2/rest/services`
  - Fremont: `https://fremontgis.com/server/rest/services`
  - Garfield: `https://maps.garfield-county.com/arcgis/rest/services`
  - Jefferson: `https://gisportal.jeffco.us/server/rest/services`
  - La Plata: `https://gis.laplata.co.us/arcgis/rest/services`
  - Larimer: `https://maps1.larimer.org/arcgis/rest/services`
  - Mesa: `https://mcgis.mesacounty.us/arcgis/rest/services`
  - Pitkin: `https://maps.pitkincounty.com/arcgis/rest/services`
  - Pueblo: `https://maps.co.pueblo.co.us/outside/rest/services`
  - Summit: `https://gis.summitcountyco.gov/arcgis/rest/services`
- **Cities:**
  - Aurora: `https://ags.auroragov.org/aurora/rest/services/OpenData/MapServer`
  - Boulder (City): `https://maps.bouldercolorado.gov/arcgis/rest/services`
  - Breckenridge: `https://maps.townofbreckenridge.com/arcgis/rest/services`
  - Castle Rock: `https://maps.crgov.com/web/rest/services`
  - Colorado Springs: `https://gis.coloradosprings.gov/arcgis/rest/services`
  - Lakewood: `https://egis.lakewood.org/server/rest/services`
  - Longmont: `https://maps.ci.longmont.co.us/arcgis_public/rest/services`
  - Loveland: `https://mapserv.cityofloveland.org/arcgis/rest/services`
  - Westminster: `https://maps.cityofwestminster.us/server/rest/services`

---

### Connecticut
- **State Open Data Services:** `https://maps.ct.gov/arcgis/rest/services`
- **Department of Transportation:** `https://gisportal.dot.ct.gov/server/rest/services`
- **UConn CT ECO (Environmental Conditions):** `https://cteco.uconn.edu/ctmaps/rest/services/`
- **UConn CLEAR Program:** `https://clear3.uconn.edu/arcgis/rest/services`
- **Capitol Region COG (CRCOG):** `https://gis.crcog.org/arcgis/rest/services`
- **Municipal Services:**
  - Bristol: `https://arcgis.vgsi.com/server/rest/services/Bristol_CT`
  - Enfield: `https://gis.enfield.org/enfieldgis/rest/services`
  - Glastonbury: `https://gisarc2022.glastonbury-ct.gov/server/rest/services`
  - Hartford: `https://gis.hartford.gov/arcgis/rest/services`
  - Meriden: `https://gis.meridenct.gov/server/rest/services`
  - Stamford / MetroCOG: `https://maps.ctmetro.org/server/rest/services`

---

### Delaware
- **FirstMap State Enterprise:** `https://enterprise.firstmap.delaware.gov/arcgis/rest/services`
- **FirstMap Imagery:** `https://imagery.firstmap.delaware.gov/imagery/rest/services`
- **DelDOT:** `https://deldot.kci.com/arcgis/rest/services`
- **Counties & Cities:**
  - Kent County: `https://gis.kentcountyde.gov/server/rest/services`
  - New Castle County: `https://gis.nccde.org/agsserver/rest/services`
  - Sussex County: `https://map.sussexcountyde.gov/server/rest/services`
  - Dover: `https://gis.dover.de.us/arcgis/rest/services`

---

### Florida
- **Department of Agriculture (FDACS):** `https://gis.fdacs.gov/mapping/rest/services`
- **Department of Environmental Protection (FDEP):** `https://ca.dep.state.fl.us/arcgis/rest/services`
- **Florida DOT (FDOT):** `https://gis.fdot.gov/arcgis/rest/services`
- **Fish and Wildlife Commission (FWC Marine):** `https://ocean.floridamarine.org/arcgis/rest/services`
- **FSU LABINS (PLSS & Land Records):** `https://maps.freac.fsu.edu/arcgis/rest/services`
- **Water Management Districts:**
  - South Florida (SFWMD): `https://geoweb.sfwmd.gov/agsext1/rest/services`
  - Southwest Florida (SWFWMD): `https://www25.swfwmd.state.fl.us/arcgis12/rest/services`
- **Counties:**
  - Bay: `https://gis.baycountyfl.gov/arcgis/rest/services`
  - Brevard: `https://gis.brevardfl.gov/gissrv/rest/services`
  - Charlotte: `https://agis3.charlottecountyfl.gov/arcgis/rest/services`
  - Escambia: `https://gismaps.myescambia.com/arcgis/rest/services`
  - Highlands: `https://gis.highlandsfl.gov/server/rest/services`
  - Hillsborough: `https://maps.hillsboroughcounty.org/arcgis/rest/services`
  - Lake: `https://gis.lakecountyfl.gov/lakegis/rest/services`
  - Lee: `https://gismapserver.leegov.com/gisserver910/rest/services`
  - Leon: `https://intervector.leoncountyfl.gov/intervector/rest/services`
  - Marion: `https://gis.marionfl.org/public/rest/services`
  - Martin: `https://geoweb.martin.fl.us/arcgis/rest/services`
  - Miami-Dade: `https://gisms.miamidade.gov/arcgis/rest/services`
  - Monroe (Keys): `https://mcgis4.monroecounty-fl.gov/public/rest/services`
  - Okaloosa: `https://gis.myokaloosa.com/arcgis/rest/services`
  - Orange: `https://ocgis4.ocfl.net/arcgis/rest/services`
  - Palm Beach: `https://maps.co.palm-beach.fl.us/arcgis/rest/services`
  - Pinellas: `https://egis.pinellas.gov/gis/rest/services`
  - Polk: `https://gis.polk-county.net/image/rest/services`
  - St. Johns: `https://www.gis.sjcfl.us/portal_sjcgis/rest/services`
  - St. Lucie: `https://map.paslc.gov/arcgis/rest/services`
  - Volusia: `https://maps1.vcgov.org/arcgis/rest/services`
- **Cities:**
  - Cape Coral: `https://capeims.capecoral.gov/arcgis/rest/services`
  - Fort Lauderdale: `https://gis.fortlauderdale.gov/arcgis/rest/services`
  - Jacksonville: `https://maps.coj.net/coj/rest/services`
  - Miami (City): `https://gis.miami.gov/gis/rest/services`
  - Orlando: `https://gis.orlando.gov/server/rest/services`
  - St. Petersburg: `https://egis.stpete.org/arcgis/rest/services`
  - Tampa: `https://arcgis.tampagov.net/arcgis/rest/services`

---

### Georgia
- **Emergency Management (GEMA):** `https://gis.gema.ga.gov/ags/rest/services`
- **Department of Transportation (GDOT):** `https://egis.dot.ga.gov/arcgis/rest/services`
- **University of Georgia ITOS:** `https://maps.itos.uga.edu/arcgis/rest/services`
- **Georgia Tech:** `https://geospat.gatech.edu/arcgis/rest/services`
- **Regional & Municipalities:**
  - Atlanta Regional Commission (ARC): `https://arcgis.atlantaregional.com/arcgis/rest/services`
  - Coastal Regional Commission: `https://maps.crc.ga.gov/crcarcgis/rest/services`
  - Southern Georgia Regional Commission: `https://www.sgrcmaps.com/arcgis/rest/services`
  - Clarke County (Athens): `https://enigma.accgov.com/server/rest/services`
  - DeKalb County: `https://dcgis.dekalbcountyga.gov/mapping/rest/services`
  - Fulton County: `https://gismaps.fultoncountyga.gov/arcgispub/rest/services`
  - Gwinnett County: `https://gis3.gwinnettcounty.com/mapvis/rest/services`
  - Henry County: `https://arcgis.co.henry.ga.us/server/rest/services`
  - Atlanta (City): `https://gis.atlantaga.gov/dpcd/rest/services`
  - Augusta: `https://gismap.augustaga.gov/arcgis/rest/services`
  - Columbus: `https://ccggisprod.columbusga.org/server/rest/services`
  - Savannah / SAGIS: `https://pub.sagis.org/arcgis/rest/services`

---

### Hawaii
- **State Enterprise GIS:** `https://geodata.hawaii.gov/arcgis/rest/services`
- **Hawai'i County (Big Island):** `https://gis.hawaiicounty.gov/arcgis/rest/services`
- **Kauai County:** `https://maps.kauai.gov/server/rest/services`

---

### Idaho
- **INSIDE Idaho Clearinghouse:** `https://insideidaho.org/arcgis/rest/services`
- **Department of Environmental Quality:** `https://global.deq.idaho.gov/arcgis/rest/services`
- **Department of Lands (IDL):** `https://gis1.idl.idaho.gov/arcgis/rest/services`
- **Idaho Transportation Department (ITD):** `https://gis.itd.idaho.gov/arcgisprod/rest/services`
- **Department of Water Resources (IDWR):** `https://gis.idwr.idaho.gov/hosting/rest/services`
- **Fish and Game (IDFG):** `https://gisportal-idfg.idaho.gov/hosting/rest/services`
- **Counties & Cities:**
  - Bannock County: `https://maps.bannockcounty.us/server/rest/services`
  - Bonner County: `https://cloudgis.bonnercountyid.gov/server/rest/services`
  - Latah County: `https://gis.latah.id.us/arcgis/rest/services`
  - Boise (City): `https://gismaps.cityofboise.org/arcgis/rest/services`
  - Coeur d’Alene: `https://gis.cdaid.org/server/rest/services`
  - Lewiston: `https://webadaptor.cityoflewiston.org/server/rest/services`
  - Pocatello: `https://map.pocatello.us/arcgis/rest/services`

---

### Illinois
- **IEMA Disaster Management:** `https://maps.iema.state.il.us/arcgis/rest/services`
- **Natural Resources (IDNR):** `https://maps.dnr.illinois.gov/geoservices/rest/services`
- **Department of Transportation (IDOT):** `https://gis1.dot.illinois.gov/arcgis/rest/services`
- **State Geological Survey (ISGS):** `https://data.isgs.illinois.gov/arcgis/rest/services`
- **State Water Survey (ISWS):** `https://gismaps.isws.illinois.gov/arcgis/rest/services`
- **Regional Consortiums:**
  - Northern Illinois GIS Consortium: `https://ags.gisconsortium.org/arcgis/rest/services`
  - Tri-County Regional Planning: `https://www.centralilmaps.com/arcgis/rest/services`
- **Counties:**
  - Boone: `https://maps.boonecountyil.org/arcgis/rest/services`
  - Cook County: `https://gis11.cookcountyil.gov/arcgis/rest/services`
  - Cook County Imagery: `https://img.cookcountyil.gov/arcgis/rest/services`
  - DuPage: `https://gis.dupageco.org/arcgis/rest/services`
  - Grundy: `https://maps.grundyco.org/arcgis/rest/services`
  - Kane: `https://gistech.countyofkane.org/arcgis/rest/services`
  - Kankakee: `https://k3gis.com/arcgis/rest/services`
  - Kendall: `https://maps.co.kendall.il.us/server/rest/services`
  - Lake County: `https://maps.lakecountyil.gov/arcgis/rest/services`
  - LaSalle: `https://gis.lasallecounty.org/arcgis/rest/services`
  - McHenry: `https://www.mchenrycountygis.org/arcgis/rest/services`
  - McLean: `https://www.mcgisweb.org/mcgc/rest/services`
  - Peoria County: `https://gis.peoriacounty.gov/arcgis/rest/services`
  - Rock Island: `https://gis.rockislandcountyil.gov/arcgis/rest/services`
  - Will: `https://gis.willcountyillinois.com/server/rest/services`
- **Cities:**
  - Champaign: `https://gisweb.champaignil.gov/cb/rest/services`
  - Chicago: `https://gisapps.cityofchicago.org/arcgis/rest/services`
  - Evanston: `https://maps.cityofevanston.org/arcgis/rest/services`
  - Naperville: `https://portal.naperville.il.us/arcgis/rest/services`
  - Springfield: `https://maps.springfield.il.us/server/rest/services`

---

### Indiana
- **IndianaMap Enterprise:** `https://gisdata.in.gov/server/rest/services`
- **Department of Homeland Security:** `https://gis.dhs.in.gov/arcgis/rest/services`
- **Department of Transportation (INDOT):** `https://gis.indot.in.gov/ro/rest/services`
- **Counties & Cities:**
  - Allen County / Fort Wayne: `https://gis.acimap.us/projectservicesadmin/rest/services`
  - Dearborn County: `https://gis.dearborncounty.in.gov/arcgis/rest/services`
  - Hamilton County: `https://gis1.hamiltoncounty.in.gov/arcgis/rest/services`
  - Marion County / Indianapolis: `https://xmaps.indy.gov/arcgis/rest/services`
  - Porter County: `https://gispro.porterco.org/server/rest/services`
  - Bloomington: `https://bloomington.in.gov/arcgis-server/rest/services`
  - Evansville: `https://maps.evansvillegis.com/arcgis_server/rest/services`
  - Fishers: `https://maps.fishers.in.us/arcgis/rest/services`
  - South Bend: `https://gis.southbendin.gov/arcgis/rest/services`

---

### Iowa
- **Homeland Security & Emergency Mgmt:** `https://eoc.iowa.gov/arcgis/rest/services`
- **Department of Natural Resources (IDNR):** `https://programs.iowadnr.gov/geospatial/rest/services`
- **Department of Transportation (Iowa DOT):** `https://gis.iowadot.gov/agshost/rest/services`
- **Iowa State University Orthos:** `https://ortho.gis.iastate.edu/arcgis/rest/services`
- **Counties & Cities:**
  - Dallas County: `https://gis.dallascountyiowa.gov/arcgis/rest/services`
  - Dubuque County: `https://gis.dubuquecounty.us/server/rest/services`
  - Johnson County: `https://gis.johnsoncountyiowa.gov/arcgis/rest/services`
  - Linn County: `https://gis.linncountyiowa.gov/ags/rest/services`
  - Polk County: `https://gis4.polkcountyiowa.gov/server/rest/services`
  - Pottawattamie County: `https://gis.pottcounty-ia.gov/arcgis/rest/services`
  - Cedar Rapids: `https://crgis.cedar-rapids.org/arcgis/rest/services`
  - Council Bluffs: `https://gispublic.councilbluffs-ia.gov/publicserver/rest/services`
  - Des Moines: `https://maps.dsm.city/p2/rest/services`

---

### Kansas
- **DASC Data Access & Support Center:** `https://services.kansasgis.org/arcgis/rest/services`
- **Department of Agriculture (KDA):** `https://gis2.kda.ks.gov/arcgis/rest/services`
- **Health & Environment (KDHE):** `https://maps.kdhe.ks.gov/kdhe_doe/rest/services`
- **Applied Remote Sensing (KARS):** `https://services.kars.geoplatform.ku.edu/arcgis/rest/services`
- **Counties & Cities:**
  - Douglas County: `https://gis.dgcoks.gov/server/rest/services`
  - Finney County: `https://www.finneycountygis.com/arcgis/rest/services`
  - Johnson County: `https://maps.jocogov.org/arcgis/rest/services`
  - Riley County: `https://gis.rileycountyks.gov/arcgis/rest/services`
  - Shawnee County: `https://gis.sncoapps.us/arcgis2/rest/services`
  - Wyandotte County / KCK: `https://gisweb.wycokck.org/arcgis/rest/services`
  - Lenexa: `https://gis.lenexa.com/arcgis/rest/services`
  - Overland Park: `https://maps.opkansas.org/mapping/rest/services`
  - Wichita: `https://gismaps.wichita.gov/ageweb/rest/services`

---

### Kentucky
- **State GIS Clearinghouse:** `https://kygisserver.ky.gov/arcgis/rest/services`
- **Kentucky Raster Imagery:** `https://kyraster.ky.gov/arcgis/rest/services`
- **Kentucky Transportation Cabinet (KYTC):** `https://maps.kytc.ky.gov/arcgis/rest/services`
- **Kentucky Geological Survey (KGS):** `https://kgs.uky.edu/arcgis/rest/services`
- **Regional & Local:**
  - Northern Kentucky (LinkGIS): `https://maps.linkgis.org/server/rest/services`
  - Louisville / Jefferson County (LOJIC): `https://services.lojic.org/arcgis/rest/services`
  - Boone County: `https://secure.boonecountygis.com/server/rest/services`
  - Bowling Green / Warren County: `https://webgis.bgky.org/server/rest/services`
  - Owensboro: `https://gis.owensboro.org/arcgis/rest/services`
  - Paducah: `https://gis.paducahky.gov/arcgis/rest/services`

---

### Louisiana
- **Environmental Quality (LDEQ):** `https://arcgis.deq.louisiana.gov/ldeq/rest/services`
- **Wildlife and Fisheries (LDWF):** `https://gis.wlf.la.gov/arcgis/rest/services`
- **Coastal Protection & Restoration (CIMS):** `https://cimsgeo.coastal.louisiana.gov/arcgis/rest/services`
- **LSU AgCenter:** `https://services.maps.lsuagcenter.com/arcgis/rest/services`
- **Parishes & Municipalities:**
  - Ascension Parish: `https://gis.ascensionparishla.gov/server/rest/services`
  - Jefferson Parish: `https://eweb.jeffparish.net/arcgis/rest/services`
  - Terrebonne Parish: `https://gis.tpcg.org/server/rest/services`
  - Baton Rouge: `https://maps.brla.gov/gis/rest/services`
  - New Orleans: `https://gis.nola.gov/arcgis/rest/services`

---

### Maine
- **Maine GIS (MEGIS):** `https://arcgisserver.maine.gov/arcgis/rest/services`
- **Maine GeoData Server:** `https://gis.maine.gov/arcgis/rest/services`
- **Municipalities:**
  - Auburn: `https://maps2.auburnmaine.gov/arcgis/rest/services`
  - Bangor: `https://mapping.bangormaine.gov/server/rest/services`
  - Lewiston: `https://maps2.lewistonmaine.gov/arcgis/rest/services`
  - Portland: `https://gis.portlandmaine.gov/maps/rest/services`

---

### Maryland
- **MD iMap Enterprise:** `https://mdgeodata.md.gov/imap/rest/services`
- **MD iMap Imagery:** `https://mdgeodata.md.gov/imagery/rest/services`
- **Department of Planning:** `https://mdpgis.mdp.state.md.us/arcgis/rest/services`
- **Natural Resources (DNR):** `https://dnr.geodata.md.gov/dnrdata/rest/services`
- **State Highway Administration (MDOT):** `https://maps.roads.maryland.gov/arcgis/rest/services`
- **Department of the Environment:** `https://mdewin64.mde.state.md.us/arcgis/rest/services`
- **Counties & Cities:**
  - Anne Arundel: `https://gis.aacounty.org/arcgis/rest/services`
  - Baltimore County: `https://bcgis.baltimorecountymd.gov/arcgis/rest/services`
  - Calvert: `https://gis.calvertcountymd.gov/server/rest/services`
  - Frederick: `https://fcgis.frederickcountymd.gov/server/rest/services`
  - Harford: `https://hcggis.harfordcountymd.gov/public/rest/services`
  - Montgomery County: `https://gis.montgomerycountymd.gov/ArcGIS/rest/services`
  - Prince George's County (PGAtlas): `https://gisdata.pgplanning.org/arcgis/rest/services`
  - Baltimore City: `https://gis.baltimorecity.gov/egis/rest/services`
  - Rockville: `https://maps.rockvillemd.gov/arcgis/rest/services`

---

### Massachusetts
- **MassGIS Digital Services:** `https://arcgisserver.digital.mass.gov/arcgisserver/rest/services`
- **MassDOT:** `https://gis.massdot.state.ma.us/arcgis/rest/services`
- **Energy & Environmental Affairs:** `https://gis.eea.mass.gov/imgsvr/rest/services`
- **Regional Commissions:**
  - Cape Cod Commission: `https://gis-services.capecodcommission.org/arcgis/rest/services`
  - Metropolitan Area Planning Council (MAPC): `https://geo.mapc.org/server/rest/services`
  - Montachusett Regional Planning: `https://mrmapper.mrpc.org/arcgis6443/rest/services`
- **Municipalities:**
  - Boston: `https://gis.boston.gov/arcgis/rest/services`
  - Cambridge: `https://gis.cambridgema.gov/arcgis/rest/services`
  - Concord: `https://gis.concordma.gov/arcgis/rest/services`
  - Newton: `https://gisweb.newtonma.gov/server/rest/services`
  - Springfield: `https://maps.springfield-ma.gov/arcgis/rest/services`
  - Wellesley: `https://maps.wellesleyma.gov/server/rest/services`

---

### Michigan
- **State GIS Gateway (DTMB):** `https://gisp.mcgi.state.mi.us/arcgis/rest/services`
- **MDOT GIS:** `https://mdotgis.state.mi.us/arcgis/rest/services`
- **State Imagery:** `https://imagery.michigan.gov/server/rest/services`
- **Western Michigan University (Earth Sciences):** `https://www.esrs.wmich.edu/arcgis/rest/services`
- **Counties & Regions:**
  - SEMCOG (Southeast Michigan COG): `https://arcgisserver.semcog.org/arcgis/rest/services`
  - Eaton County: `https://ecgis.eatoncounty.org/ecgis_ssl/rest/services`
  - Emmet County: `https://gis.emmetcounty.org/arcgis/rest/services`
  - Grand Traverse County: `https://gis.gtcountymi.gov/arcgis/rest/services`
  - Jackson County: `https://gis.mijackson.org/countygis/rest/services`
  - Kent County: `https://gis.kentcountymi.gov/agisprod/rest/services`
  - Macomb County: `https://gis.macombgov.org/arcgis1/rest/services`
  - Monroe County: `https://gis.monroemi.gov/server/rest/services`
  - Oakland County: `https://gisservices.oakgov.com/arcgis/rest/services`
  - Ottawa County: `https://gis.miottawa.org/arcgis/rest/services`
  - Washtenaw County: `https://webmapssecure.ewashtenaw.org/arcgisshared/rest/services`
- **Cities:**
  - Ann Arbor: `https://a2maps.a2gov.org/a2arcgis/rest/services`
  - Detroit: `https://egis.detroitmi.gov/image/rest/services`
  - Grand Rapids: `https://maps.grcity.us/arcgis/rest/services`
  - Holland: `https://gis.hollandbpw.com/arcgis/rest/services`
  - Traverse City: `https://tcgis.traversecitymi.gov/arcgis/rest/services`

---

### Minnesota
- **Minnesota Geospatial Commons (MnGeo):** `https://enterprise.gisdata.mn.gov/aghost/rest/services`
- **Department of Agriculture:** `https://gis.mda.state.mn.us/arcgis/rest/services`
- **Pollution Control Agency (MPCA):** `https://pca-gis02.pca.state.mn.us/arcgis/rest/services`
- **University of Minnesota (U-Spatial):** `https://gis6.uspatial.umn.edu/arcgis/rest/services`
- **Twin Cities Metropolitan Council:** `https://gis.metc.state.mn.us/arcgis/rest/services`
- **Counties:**
  - Anoka: `https://gis.anokacountymn.gov/anoka_gis/rest/services`
  - Carver: `https://gis.co.carver.mn.us/arcgis_ea/rest/services`
  - Crow Wing: `https://gis.crowwing.us/cwc_external_main/rest/services`
  - Dakota: `https://gis2.co.dakota.mn.us/arcgis/rest/services`
  - Hennepin: `https://gis.hennepin.us/arcgis/rest/services`
  - Olmsted: `https://gis.co.olmsted.mn.us/arcgis/rest/services`
  - Ramsey: `https://maps.co.ramsey.mn.us/arcgis/rest/services`
  - St. Louis County (Duluth area): `https://gis.stlouiscountymn.gov/server2/rest/services`
  - Scott County: `https://gis.co.scott.mn.us/arcgis/rest/services`
  - Stearns: `https://gis.co.stearns.mn.us/arcgis/rest/services`
  - Washington: `https://maps.co.washington.mn.us/arcgis/rest/services`
- **Cities:**
  - Bloomington: `https://gis.bloomingtonmn.gov/arcgis/rest/services`
  - Eagan: `https://gis.cityofeagan.com/arcgis/rest/services`
  - Eden Prairie: `https://gis.edenprairie.org/maps/rest/services`
  - Minneapolis: `https://eagsprod.ci.minneapolis.mn.us/arcgis/rest/services`

---

### Mississippi
- **MARIS Clearinghouse:** `https://gis.mississippi.edu/server/rest/services`
- **Environmental Quality (MDEQ):** `https://gis.deq.ms.gov/ArcGIS/rest/services`
- **Department of Transportation (MDOT):** `https://www.gisonline.ms.gov/arcgis/rest/services`
- **Marine Resources:** `https://gis.dmr.ms.gov/server/rest/services`
- **Forestry Commission:** `https://arcsrv.mfc.ms.gov/server/rest/services`
- **Central MS Planning & Development (CMPDD):** `https://gis.cmpdd.org/server/rest/services`
- **Counties & Cities:**
  - DeSoto County: `https://maps.desotocountyms.gov/arcgis/rest/services`
  - Harrison County: `https://geo.co.harrison.ms.us/server/rest/services`
  - Jackson County: `https://webmap.co.jackson.ms.us/arcgis107/rest/services`
  - Gulfport: `https://maps.gulfport-ms.gov/arcgis/rest/services`

---

### Missouri
- **State GIS Gateway:** `https://gis.mo.gov/arcgis/rest/services`
- **Department of Conservation (MDC):** `https://gisblue.mdc.mo.gov/arcgis/rest/services`
- **Department of Natural Resources:** `https://gis.dnr.mo.gov/server/rest/services`
- **MoDOT Highway Services:** `https://mapping.modot.org/arcgis/rest/services`
- **MSDIS State Imagery (Univ of Missouri):** `https://stateimagery.msdis.missouri.edu/arcgis/rest/services`
- **Southeast Missouri Regional Planning:** `https://maps.semogis.com/server/rest/services`
- **Counties & Cities:**
  - Boone County: `https://gis.showmeboone.com/arcgis/rest/services`
  - Jackson County: `https://jcgis.jacksongov.org/arcgis/rest/services`
  - St. Charles County: `https://gis.sccmo.org/scc_gis/rest/services`
  - St. Louis County: `https://maps.stlouisco.com/hosting/rest/services`
  - Branson: `https://gis.bransonmo.gov/application/rest/services`
  - Columbia: `https://gis.gocolumbiamo.com/arcgis/rest/services`
  - Kansas City: `https://mapd.kcmo.org/kcgis/rest/services`
  - Kirkwood: `https://gis.kirkwoodmo.org/arcgis/rest/services`
  - St. Louis (City): `https://maps6.stlouis-mo.gov/arcgis/rest/services`

---

### Montana
- **State Library Clearinghouse:** `https://gisservice.mt.gov/arcgis/rest/services`
- **Department of Natural Resources (DNRC):** `https://gis.dnrc.mt.gov/arcgis/rest/services`
- **DNRC Imagery:** `https://gis.dnrc.mt.gov/imagery/rest/services`
- **Montana DOT (MDT):** `https://app.mdt.mt.gov/arcgis/rest/services`
- **Fish, Wildlife and Parks (FWP):** `https://fwp-gis.mt.gov/arcgis/rest/services`
- **Bureau of Mines and Geology (MBMG):** `https://mbmgmap.mtech.edu/server/rest/services`
- **Counties & Cities:**
  - Flathead County: `https://maps.flathead.mt.gov/server/rest/services`
  - Missoula County: `https://gis.missoulacounty.us/arcgis/rest/services`
  - Yellowstone County: `https://gis.yellowstonecountymt.gov/arcgis/rest/services`
  - Billings: `https://billingsgis.com/arcgis_public/rest/services`
  - Bozeman: `https://gisweb.bozeman.net/arcgis/rest/services`
  - Helena / Lewis & Clark: `https://helenamontanamaps.org/arcgisadp/rest/services`

---

### Nebraska
- **Department of Transportation (NDOT):** `https://giscat.ne.gov/agency/rest/services`
- **Nebraska Enterprise Agency Services:** `https://gis.ne.gov/agency/rest/services`
- **Counties & Cities:**
  - Adams County: `https://gis.adamscounty.org/arcgis/rest/services`
  - Douglas County / Omaha (DOGIS): `https://gis.dogis.org/arcgis/rest/services`
  - Sarpy County: `https://geodata.sarpy.com/arcgis/rest/services`
  - Grand Island: `https://gis.grand-island.com/arcgis/rest/services`
  - Lincoln: `https://gis.lincoln.ne.gov/public/rest/services`
  - gWorks Municipal/County Network: `https://mapserver01.gworks.com/arcgis/rest/services`

---

### Nevada
- **Division of Water Resources:** `https://arcgis.water.nv.gov/arcgis/rest/services`
- **Division of Environmental Protection:** `https://ndep-emap.ndep.nv.gov/arcgis/rest/services`
- **Nevada DOT (NDOT):** `https://gis.dot.nv.gov/arcgis/rest/services`
- **Bureau of Mines & Geology (UNR):** `https://gisweb.unr.edu/nbmg/rest/services`
- **Regional Transportation Commission of Southern NV:** `https://gis.rtcsnv.com/arcgis/rest/services`
- **Counties & Cities:**
  - Clark County: `https://maps.clarkcountynv.gov/arcgis/rest/services`
  - Lyon County: `https://gis.lyon-county.org/server/rest/services`
  - Washoe County: `https://gis.washoecounty.us/arcgis/rest/services`
  - Henderson: `https://maps.cityofhenderson.com/arcgis/rest/services`
  - Las Vegas: `https://mapdata.lasvegasnevada.gov/clvgis/rest/services`
  - Reno: `https://citymaps.reno.gov/server/rest/services`

---

### New Hampshire
- **GRANIT Statewide Clearinghouse:** `https://nhgeodata.unh.edu/nhgeodata/rest/services`
- **GRANIT Imagery:** `https://nhgeodata.unh.edu/image/rest/services`
- **Department of Environmental Services (NHDES):** `https://gis.des.nh.gov/server/rest/services`
- **Municipalities:**
  - Concord: `https://gis.concordnh.gov/arc1061/rest/services`
  - Manchester: `https://ags.manchesternh.gov/agsgis7/rest/services`
  - Nashua: `https://newgis.nashuanh.gov/arcgisapp3/rest/services`

---

### New Jersey
- **NJGIN Enterprise:** `https://maps.nj.gov/arcgis/rest/services`
- **NJDEP Environmental Protection:** `https://mapsdep.nj.gov/arcgis/rest/services`
- **Rutgers Center for Remote Sensing (NJ Maps):** `https://njmaps1.rad.rutgers.edu/arcgis/rest/services`
- **North Jersey Transportation Planning (NJTPA):** `https://gis.njtpa.org/arcgis/rest/services`
- **Counties & Municipalities:**
  - Bergen County: `https://bchapeweb.co.bergen.nj.us/arcgis/rest/services`
  - Burlington County: `https://gisportal.co.burlington.nj.us/hosting/rest/services`
  - Cape May County: `https://ims.capemaycountynj.gov/arcgisweb/rest/services`
  - Hudson County: `https://gis.hcnj.us/arcgis/rest/services`
  - Mercer County: `https://maps.mercercounty.org/arcgis/rest/services`
  - Morris County: `https://morrisgisapps.co.morris.nj.us/arcgis105/rest/services`
  - Passaic County: `https://gis.passaiccountynj.org/arcgis/rest/services`
  - Newark: `https://njgin.ci.newark.nj.us/arcgis/rest/services`

---

### New Mexico
- **Environment Department (NMED):** `https://mercator.env.nm.gov/server/rest/services`
- **State Land Office:** `https://mapservice.nmstatelands.org/arcgis/rest/services`
- **Office of State Engineer:** `https://gis.ose.nm.gov/server_s/rest/services`
- **Earth Data Analysis Center (UNM EDAC):** `https://edacarc.unm.edu/arcgis/rest/services`
- **Counties & Cities:**
  - Bernalillo County: `https://pdsmaps.bernco.gov/server/rest/services`
  - Curry County: `https://maps.currycounty.org/server/rest/services`
  - Los Alamos: `https://gis.losalamosnm.us/securegis/rest/services`
  - San Juan County: `https://webmaps.sjcounty.net/arcgis/rest/services`
  - Santa Fe County: `https://sfcomaps.santafecountynm.gov/restsvc/rest/services`
  - Albuquerque: `https://abqgis01.cabq.gov/arcgis/rest/services`
  - Las Cruces: `https://maps.las-cruces.org/gis/rest/services`
  - Rio Rancho: `https://gis.rrnm.gov/arcgis/rest/services`
  - Santa Fe (City): `https://gis.santafenm.gov/server/rest/services`

---

### New York
- **NYS ITS Public GIS Services (Tax Parcels):** `https://gisservices.its.ny.gov/arcgis/rest/services`
- **NYS Orthoimagery:** `https://orthos.its.ny.gov/arcgis/rest/services`
- **NYS Elevation Services:** `https://elevation.its.ny.gov/arcgis/rest/services`
- **Department of Environmental Conservation (DEC):** `https://gisservices.dec.ny.gov/arcgis/rest/services`
- **Department of Transportation (NYSDOT):** `https://gis.dot.ny.gov/hostingny/rest/services`
- **Counties & Regional:**
  - Development Authority of North Country (DANC): `https://maps.dancgis.org/server/rest/services`
  - Broome County: `https://gis.broomecountyny.gov/arcgis/rest/services`
  - Cattaraugus County: `https://maps2.cattco.org/arcgiswebadaptor/rest/services`
  - Cayuga County: `https://ccgis.cayugacounty.us/arcgis/rest/services`
  - Chautauqua County: `https://maps.chautauquacounty.com/server/rest/services`
  - Dutchess County: `https://gis.dutchessny.gov/server/rest/services`
  - Erie County: `https://gis.erie.gov/server/rest/services`
  - Essex County: `https://essex-gis.co.essex.ny.us/arcgis/rest/services`
  - Monroe County: `https://maps.monroecounty.gov/server/rest/services`
  - Nassau County: `https://gis.nassaucountyny.gov/server/rest/services`
  - Niagara County: `https://gis.niagaracounty.com/arcgis/rest/services`
  - Oneida County: `https://maps.ocgov.net/arcgis/rest/services`
  - Ontario County: `https://oncorng.co.ontario.ny.us/arcgis/rest/services`
  - Orange County: `https://gis.orangecountygov.com/arcgis/rest/services`
  - Suffolk County: `https://gis.suffolkcountyny.gov/server/rest/services`
  - Ulster County: `https://gis.ulstercountyny.gov/server/rest/services`
  - Westchester County: `https://giswww.westchestergov.com/arcgis/rest/services`
- **Cities:**
  - Huntington: `https://geo.huntingtonny.gov/arcgis/rest/services`
  - Rochester: `https://maps.cityofrochester.gov/server/rest/services`
  - Watertown: `https://maps.watertown-ny.gov/server/rest/services`

---

### North Carolina
- **NC OneMap Enterprise:** `https://services.nconemap.gov/secure/rest/services`
- **Emergency Management (SPARTA):** `https://spartagis.ncem.org/arcgis/rest/services/Public`
- **Department of Environmental Quality (NC DEQ):** `https://maps.deq.nc.gov/arcgis/rest/services`
- **Department of Transportation (NCDOT):** `https://gis11.services.ncdot.gov/arcgis/rest/services`
- **UNC Chapel Hill:** `https://gismaps.unc.edu/arcgis/rest/services`
- **Counties:**
  - Alamance: `https://apps.alamance-nc.com/arcgis/rest/services`
  - Brunswick: `https://geo.brunswickcountync.gov/arcgis/rest/services`
  - Buncombe: `https://gis.buncombecounty.org/arcgis/rest/services`
  - Burke: `https://gis.burkenc.org/arcgis/rest/services`
  - Cabarrus: `https://location.cabarruscounty.us/arcgisservices/rest/services`
  - Catawba: `https://arcgis2.catawbacountync.gov/arcgis/rest/services`
  - Chatham: `https://gisservices.chathamcountync.gov/chathamgis/rest/services`
  - Craven: `https://gis.cravencountync.gov/arcgis/rest/services`
  - Cumberland: `https://gis.co.cumberland.nc.us/server/rest/services`
  - Currituck: `https://maps.currituckcountync.gov/arcgis/rest/services`
  - Durham County / City: `https://webgis.durhamnc.gov/server/rest/services`
  - Forsyth: `https://maps.co.forsyth.nc.us/arcgis/rest/services`
  - Guilford: `https://gcgis.guilfordcountync.gov/arcgis/rest/services`
  - Harnett: `https://gis.harnett.org/arcgis/rest/services`
  - Iredell: `https://icgis.co.iredell.nc.us/arcgis/rest/services`
  - Mecklenburg (Charlotte): `https://meckgis.mecklenburgcountync.gov/server/rest/services`
  - Moore: `https://gis.moorecountync.gov/server/rest/services`
  - New Hanover (Wilmington): `https://gis.nhcgov.com/server/rest/services`
  - Orange: `https://gis.orangecountync.gov/arcgis/rest/services`
  - Pitt: `https://gis.pittcountync.gov/gis/rest/services`
  - Randolph: `https://gis.randolphcountync.gov/arcgis/rest/services`
  - Rowan: `https://gis.rowancountync.gov/arcgis/rest/services`
  - Union: `https://atlas.unioncountync.gov/server/rest/services`
  - Wake (Raleigh): `https://maps.wakegov.com/arcgis/rest/services`
- **Cities:**
  - Asheville: `https://gis.ashevillenc.gov/server/rest/services`
  - Charlotte: `https://gis.charlottenc.gov/arcgis/rest/services`
  - Greensboro: `https://gis.greensboro-nc.gov/arcgis/rest/services`
  - Raleigh: `https://maps.raleighnc.gov/arcgis/rest/services`
  - Wilmington: `https://gis.wilmingtonnc.gov/arcgis/rest/services`

---

### North Dakota
- **ND GIS Hub:** `https://ndgishub.nd.gov/arcgis/rest/services`
- **NDDOT External Services:** `https://gis.dot.nd.gov/arcgis/rest/services/external`
- **LoadPass Permits:** `https://maps.loadpasspermits.com/arcgis/rest/services`
- **Counties & Cities:**
  - Cass County: `https://gisweb.casscountynd.gov/arcgis/rest/services`
  - Grand Forks County: `https://gfgis1.nd.gov/arcgis/rest/services`
  - McKenzie County: `https://mckenziegis.co.mckenzie.nd.us/server/rest/services`
  - Ramsey County: `https://gis.co.ramsey.nd.us/server/rest/services`
  - Richland County: `https://gis.co.richland.nd.us/arcgis/rest/services`
  - Williams County: `https://willgis.co.williams.nd.us/willgis/rest/services`
  - Bismarck: `https://bisgis.bismarcknd.gov/server/rest/services`
  - Dickinson: `https://gis.dickinsongov.com/server/rest/services`
  - Fargo: `https://gis.cityoffargo.com/arcgis/rest/services`

---

### Ohio
- **OGRIP Spatial Information Portal:** `https://maps.ohio.gov/arcgis/rest/services`
- **Department of Natural Resources (ODNR):** `https://gis2.ohiodnr.gov/arcgis/rest/services`
- **Ohio DOT (ODOT TIMS):** `https://odotgis.dot.state.oh.us/arcgis/rest/services`
- **Environmental Protection Agency (Ohio EPA):** `https://geo.epa.ohio.gov/arcgis/rest/services`
- **Public Utilities Commission (PUCO):** `https://maps.puco.ohio.gov/arcgis/rest/services`
- **Regional & Metropolitan:**
  - Mid-Ohio Regional Planning Commission (MORPC): `https://arcserver.morpc.org/arcgis/rest/services`
  - Northeast Ohio Regional Sewer (NEORSD): `https://neogis.neorsd.org/arcgis/rest/services`
  - OKI Regional Council: `https://gis.oki.org/server/rest/services`
- **Counties:**
  - Allen: `https://gis.allencountyohio.com/arcgis/rest/services`
  - Butler: `https://maps.butlercountyauditor.org/arcgis/rest/services`
  - Clark: `https://ago.clarkcountyohio.gov/ccoarcgis/rest/services`
  - Clermont: `https://maps.clermontauditor.org/arcgis/rest/services`
  - Cuyahoga (Cleveland): `https://gis.cuyahogacounty.us/server/rest/services`
  - Erie: `https://maps.eriecounty.oh.gov/arcgis/rest/services`
  - Fairfield: `https://gis.co.fairfield.oh.us/arcgis/rest/services`
  - Franklin (Columbus): `https://gis.franklincountyohio.gov/hosting/rest/services`
  - Greene: `https://gis.greenecountyohio.gov/webgis2/rest/services`
  - Lake: `https://gis.lakecountyohio.gov/arcgis/rest/services`
  - Lorain: `https://maps.lcauditor.com/hosting/rest/services`
  - Lucas (Toledo): `https://lcaudgis.co.lucas.oh.us/gisaudserver/rest/services`
  - Stark: `https://scgisa.starkcountyohio.gov/arcgis/rest/services`
  - Summit: `https://scgis.summitoh.net/hosted/rest/services`
  - Warren: `https://gisportal.co.warren.oh.us/server/rest/services`
- **Cities:**
  - Cincinnati: `https://arcgis.cincinnati-oh.gov/arcgis/rest/services`
  - Columbus: `https://maps.columbus.gov/arcgis/rest/services`
  - Dayton: `https://maps.daytonohio.gov/gisservices/rest/services`
  - Dublin: `https://mapping.dublin.oh.us/arcgis/rest/services`
  - Toledo: `https://gis.toledo.oh.gov/arcgis/rest/services`

---

### Oklahoma
- **Department of Environmental Quality (ODEQ):** `https://gis.deq.ok.gov/server/rest/services`
- **Water Resources Board (OWRB):** `https://owrb.csa.ou.edu/server/rest/services`
- **Commissioners of the Land Office:** `https://gis.clo.ok.gov/server/rest/services`
- **Corporation Commission:** `https://gis.occ.ok.gov/server/rest/services`
- **INCOG Regional Services:** `https://map11.incog.org/arcgis11wa/rest/services`
- **Counties & Cities:**
  - Edmond: `https://gis.edmondok.gov/arcgis/rest/services`
  - Midwest City: `https://maps.midwestcityok.org/arcgis/rest/services`
  - Moore: `https://gis.cityofmoore.com/arcgis/rest/services`
  - Norman: `https://maps.normanok.gov/arcgis/rest/services`
  - Oklahoma City: `https://gis.okc.gov/arcgis/rest/services`

---

### Oregon
- **Department of Forestry (ODF):** `https://gis.odf.oregon.gov/ags1/rest/services`
- **DOGAMI Geology & Mining:** `https://gis.dogami.oregon.gov/arcgis/rest/services`
- **Department of Transportation (ODOT):** `https://gis.odot.state.or.us/arcgis1006/rest/services`
- **Statewide Imagery:** `https://imagery.oregonexplorer.info/arcgis/rest/services`
- **Portland Metro:** `https://gis.oregonmetro.gov/arcgis/rest/services`
- **Counties:**
  - Benton: `https://gis.co.benton.or.us/arcgis/rest/services`
  - Clatsop: `https://delta.co.clatsop.or.us/server/rest/services`
  - Columbia: `https://gis.columbiacountymaps.com/server/rest/services`
  - Crook: `https://gis.crookcountyor.gov/server/rest/services`
  - Deschutes: `https://maps.deschutes.org/arcgis/rest/services`
  - Douglas: `https://gis.co.douglas.or.us/server/rest/services`
  - Jackson: `https://spatial.jacksoncountyor.gov/arcgis/rest/services`
  - Josephine: `https://gis.co.josephine.or.us/arcgis/rest/services`
  - Lane: `https://lcmaps.lanecounty.org/arcgis/rest/services`
  - Multnomah: `https://www3.multco.us/arcgis/rest/services`
  - Polk: `https://maps.co.polk.or.us/gis/rest/services`
  - Washington County: `https://gispub.co.washington.or.us/server/rest/services`
- **Cities:**
  - Corvallis: `https://gis.corvallisoregon.gov/pub2/rest/services`
  - Eugene: `https://gis.eugene-or.gov/arcgis/rest/services`
  - Hillsboro: `https://gis.hillsboro-oregon.gov/public/rest/services`
  - Portland: `https://www.portlandmaps.com/arcgis/rest/services`
  - Tigard: `https://svr.tigardmaps.com/arcgis/rest/services`

---

### Pennsylvania
- **PASDA Spatial Data Access (PSU):** `https://maps.pasda.psu.edu/ArcGIS/rest/services`
- **PASDA Applications / Parcels:** `https://apps.pasda.psu.edu/ArcGIS/rest/services`
- **DCNR Conservation & Natural Resources:** `https://maps.dcnr.pa.gov/agsprod/rest/services`
- **Department of Environmental Protection:** `https://gis.dep.pa.gov/depgisprd/rest/services`
- **PennDOT Transportation Services:** `https://gis.penndot.gov/arcgis/rest/services`
- **Fish and Boat Commission:** `https://fbweb.pa.gov/arcgis/rest/services`
- **Game Commission:** `https://pgcmaps.pa.gov/arcgis/rest/services`
- **DVRPC Regional Council:** `https://arcgis.dvrpc.org/portal/rest/services`
- **Counties:**
  - Adams: `https://mapping.adamscountypa.gov/arcgis/rest/services`
  - Allegheny (Pittsburgh): `https://gisdata.alleghenycounty.us/arcgis/rest/services`
  - Berks: `https://gis.co.berks.pa.us/arcgis/rest/services`
  - Butler: `https://geo.co.butler.pa.us/server/rest/services`
  - Carbon: `https://gis.carboncounty.com/arcgis/rest/services`
  - Centre: `https://gissites4.centrecountypa.gov/arcgis/rest/services`
  - Chester: `https://gisprodops.chesco.org/server/rest/services`
  - Cumberland: `https://gis.ccpa.net/arcgiswebadaptor/rest/services`
  - Dauphin: `https://gis.dauphincounty.org/arcgis/rest/services`
  - Delaware: `https://gis.delcopa.gov/arcgis/rest/services`
  - Lancaster: `https://arcgis.lancastercountypa.gov/arcgis/rest/services`
  - Lehigh: `https://gis.lehighcounty.org/arcgis/rest/services`
  - Luzerne: `https://gis.luzernecounty.org/server/rest/services`
  - Monroe: `https://www.monroegis.org/webadaptor/rest/services`
  - Northampton: `https://gis.northamptoncounty.org/arcgisweb/rest/services`
  - Pike: `https://gis.pikepa.org/arcgis/rest/services`
  - Westmoreland: `https://gis.westmorelandcountypa.gov/arcgis/rest/services`
  - York: `https://arcweb1.ycpc.org/server/rest/services/OPEN_DATA`

---

### Rhode Island
- **RIGIS State Geographic Base:** `https://risegis.ri.gov/hosting/rest/services`
- **URI Environmental Data Center:** `https://maps.edc.uri.edu/arcgis/rest/services`
- **Municipalities:**
  - Providence: `https://webgis.providenceri.gov/server/rest/services`
  - Providence Water: `https://engineering.provwater.com/arconline/rest/services`

---

### South Carolina
- **SC Enterprise Services:** `https://ags3.scgov.net/agsfed/rest/services`
- **DNR Natural Resources:** `https://arcweb.dnr.sc.gov/server/rest/services`
- **Counties:**
  - Anderson: `https://propertyviewer.andersoncountysc.org/arcgis/rest/services`
  - Beaufort: `https://gis.beaufortcountysc.gov/server/rest/services`
  - Berkeley: `https://gis.berkeleycountysc.gov/arcgis/rest/services`
  - Charleston: `https://gisccapps.charlestoncounty.org/arcgis/rest/services`
  - Dorchester: `https://gisportal.dorchestercounty.net/hosting/rest/services`
  - Florence: `https://arc2000.florenceco.org/arcgis/rest/services`
  - Georgetown: `https://gis1.georgetowncountysc.gov/portal/rest/services`
  - Horry (Myrtle Beach): `https://www.horrycounty.org/gisweb/rest/services`
  - Oconee: `https://arcserver2.oconeesc.com/arcgis/rest/services`
  - Spartanburg: `https://maps.spartanburgcounty.org/server/rest/services`
  - York: `https://maps.yorkcounty.gov/arcgis/rest/services`
- **Cities:**
  - Aiken: `https://gis.cityofaikensc.gov/arcgis/rest/services`
  - Charleston: `https://gis.charleston-sc.gov/arcgis/rest/services`
  - Greenville: `https://citygis.greenvillesc.gov/arcgis/rest/services`
  - Mount Pleasant: `https://maps.tompsc.com/arcgis/rest/services`
  - Rock Hill: `https://rockhillgis.cityofrockhill.com/arcgis/rest/services`

---

### South Dakota
- **SD Department of Transportation:** `https://sdgis.sd.gov/dot/rest/services`
- **SD Game, Fish and Parks:** `https://gfpgis.sd.gov/arcgis/rest/services`
- **University of South Dakota:** `https://gis.usd.edu/arcgis/rest/services`
- **District III Planning:** `https://gis.districtiii.org/server/rest/services`
- **Counties & Cities:**
  - Lincoln County: `https://gis.lincolncountysd.gov/arcgis/rest/services`
  - Rapid City: `https://gis.rcgov.org/server/rest/services`
  - Sioux Falls: `https://gis.siouxfalls.gov/arcgis/rest/services`

---

### Tennessee
- **Tennessee Map (TNM):** `https://tnmap.tn.gov/arcgis/rest/services`
- **Department of Environment & Conservation (TDEC):** `https://tdeconline.tn.gov/arcgis/rest/services`
- **Department of Transportation (TDOT):** `https://spatial.tdot.tn.gov/arcgis/rest/services`
- **Counties:**
  - Blount: `https://com.blountgis.org/server/rest/services`
  - Greene: `https://www.gcgis.org/arcgis/rest/services`
  - Hamilton: `https://mapsdev.hamiltontn.gov/hcwa03/rest/services`
  - Rutherford: `https://imagery.rutherfordcountytn.gov/img/rest/services`
  - Shelby (Memphis): `https://gis.shelbycountytn.gov/arcgis/rest/services`
  - Williamson: `https://arcgis2.williamson-tn.org/arcgis/rest/services`
- **Cities:**
  - Brentwood: `https://maps.brentwoodtn.gov/arcgis/rest/services`
  - Chattanooga: `https://pwgis.chattanooga.gov/arcgis/rest/services`
  - Franklin: `https://publicmaps.franklintn.gov/arcgis/rest/services`
  - Johnson City: `https://gis.johnsoncitytn.org/arcgis/rest/services`
  - Memphis: `https://maps.memphistn.gov/hosted/rest/services`
  - Murfreesboro: `https://mwrdmaps.murfreesborotn.gov/server/rest/services`
  - Nashville: `https://maps.nashville.gov/arcgis/rest/services`

---

### Texas
- **Parks and Wildlife (TPWD):** `https://tpwd.texas.gov/arcgis/rest/services`
- **Texas DOT (TxDOT):** `https://maps.dot.state.tx.us/arcgis/rest/services`
- **TNRIS / GLO Geographic Services:** `https://feature.geographic.texas.gov/arcgis/rest/services`
- **Texas Legislative Council:** `https://giswebe.tlc.texas.gov/ArcGIS/rest/services`
- **Commission on Environmental Quality (TCEQ):** `https://gisweb.tceq.texas.gov/arcgis/rest/services`
- **Texas A&M Forest Service:** `https://tfsgis02.tfs.tamu.edu/arcgis/rest/services`
- **Regional Planning:**
  - North Central Texas COG (NCTCOG): `https://geospatial.nctcog.org/server/rest/services`
  - Houston-Galveston Area Council (H-GAC): `https://gis.h-gac.com/arcgis/rest/services`
  - San Antonio River Authority: `https://gis.sara-tx.org/ags1/rest/services`
- **Counties:**
  - Bexar (San Antonio): `https://maps.bexar.org/arcgis/rest/services`
  - Brazoria: `https://maps.brazoriacountytx.gov/arcgis/rest/services`
  - Collin: `https://maps.collincountytx.gov/server/rest/services`
  - Dallas County: `https://services3.arcgis.com/zqe2kwz79KUqUvxC/ArcGIS/rest/services`
  - Denton: `https://gis.dentoncounty.gov/arcgis/rest/services`
  - El Paso CAD: `https://gis.epcad.org/arcgis/rest/services`
  - Ellis: `https://maps.co.ellis.tx.us/arcgis/rest/services`
  - Grayson: `https://maps.co.grayson.tx.us/arcgis/rest/services`
  - Harris County: `https://www.gis.hctx.net/arcgis/rest/services`
  - Lubbock: `https://pubgis.ci.lubbock.tx.us/server/rest/services`
  - Montgomery CAD: `https://services1.arcgis.com/PRoAPGnMSUqvTrzq/ArcGIS/rest/services`
  - Tarrant (Fort Worth): `https://mapit.tarrantcounty.com/arcgis/rest/services`
  - Travis (Austin): `https://gis.traviscountytx.gov/server1/rest/services`
  - Williamson: `https://gis.wilco.org/arcgis/rest/services`
- **Cities:**
  - Addison: `https://gis.addisontx.gov/arcgis/rest/services`
  - Allen: `https://gismaps.cityofallen.org/arcgis/rest/services`
  - Arlington: `https://gis2.arlingtontx.gov/agsext2/rest/services`
  - Austin: `https://coagiswebadaptor.austintexas.gov/awgisago/rest/services`
  - Beaumont: `https://gis.beaumonttexas.gov/arcgis/rest/services`
  - Bryan: `https://maps.bryantx.gov/server/rest/services`
  - College Station: `https://gis.cstx.gov/csgis/rest/services`
  - Dallas: `https://egis.dallascityhall.com/arcgis/rest/services`
  - El Paso: `https://gis.elpasotexas.gov/arcgis/rest/services`
  - Fort Worth: `https://mapit.fortworthtexas.gov/ags/rest/services`
  - Garland: `https://maps.garlandtx.gov/arcgis/rest/services`
  - Georgetown: `https://gis.georgetown.org/arcgis/rest/services`
  - Grand Prairie: `https://gis.gptx.org/srv105/rest/services`
  - Houston: `https://mycity2.houstontx.gov/pubgis01/rest/services`
  - Plano: `https://maps.planogis.org/arcgiswad/rest/services`
  - Round Rock: `https://maps.roundrocktexas.gov/arcgis/rest/services`
  - San Antonio: `https://qagis.sanantonio.gov/arcgis/rest/services`

---

### Utah
- **Utah DNR:** `https://dwrmapserv.utah.gov/dwrarcgis/rest/services`
- **Utah DOT (UDOT Central):** `https://central.udot.utah.gov/server/rest/services`
- **UDOT Highways & Roads:** `https://roads.udot.utah.gov/server/rest/services`
- **Trust Lands Administration (SITLA):** `https://gis.trustlands.utah.gov/mapping/rest/services`
- **Utah Geological Survey:** `https://webmaps.geology.utah.gov/arcgis/rest/services`
- **Greater Salt Lake Municipal Services District:** `https://gis.msd.utah.gov/server/rest/services`
- **Counties & Cities:**
  - Cache County: `https://gis.cachecounty.gov/arcgis/rest/services`
  - Salt Lake County: `https://slco.org/slcogcs/rest/services`
  - Summit County: `https://maps.summitcounty.org/arcgis/rest/services`
  - Utah County: `https://maps.utahcounty.gov/arcgis/rest/services`
  - Weber County: `https://maps.webercountyutah.gov/arcgis/rest/services`
  - Ogden: `https://arcgis.ogdencity.com/arcgis/rest/services`
  - Provo: `https://gispublicweb.provo.org/arcgis/rest/services`
  - South Jordan: `https://gis2.southjordanutah.gov/server/rest/services`
  - Spanish Fork: `https://gis.spanishfork.gov/arcgis/rest/services`
  - West Valley City: `https://gisserver.wvc-ut.gov/server/rest/services`

---

### Vermont
- **VCGI Vermont Center for Geographic Information:** `https://maps.vcgi.vermont.gov/arcgis/rest/services`
- **Agency of Transportation (VTrans):** `https://maps.vtrans.vermont.gov/arcgis/rest/services`
- **Agency of Natural Resources (ANR):** `https://anrmaps.vermont.gov/arcgis/rest/services`
- **Green Mountain Power:** `https://maps.gmpvt.com/arcgis/rest/services`
- **Regional & Local:**
  - Chittenden County / Central VT RPC: `https://map.ccrpcvt.org/arcgis/rest/services`
  - Burlington: `https://maps.burlingtonvt.gov/arcgis/rest/services`

---

### Virginia
- **VGIN Base Layers (Parcels & Imagery):** `https://vginmaps.vdem.virginia.gov/arcgis/rest/services`
- **Department of Conservation and Recreation (DCR):** `https://casdsis.dcr.virginia.gov/arcgis/rest/services`
- **Department of Environmental Quality (VDEQ):** `https://apps.deq.virginia.gov/arcgis/rest/services`
- **Department of Energy:** `https://energy.virginia.gov/gis/rest/services`
- **Virginia Tech Enterprise GIS:** `https://arcgis-central.gis.vt.edu/arcgis/rest/services`
- **HRSD Wastewater (Hampton Roads):** `https://geo.hrsd.com/hrgeo/rest/services`
- **Counties:**
  - Arlington: `https://arlgis.arlingtonva.us/arcgis/rest/services`
  - Augusta: `https://gis.co.augusta.va.us/arcgis/rest/services`
  - Campbell: `https://gis.co.campbell.va.us/arcgis/rest/services`
  - Chesterfield: `https://services3.arcgis.com/TsynfzBSE6sXfoLq/ArcGIS/rest/services`
  - Fairfax County: `https://www.fairfaxcounty.gov/gisimagery/rest/services`
  - Frederick: `https://fredcogis.fcva.us/maps/rest/services`
  - Goochland: `https://gis.co.goochland.va.us/arcgis/rest/services`
  - James City: `https://property.jamescitycountyva.gov/arcgis/rest/services`
  - Loudoun: `https://logis.loudoun.gov/gis/rest/services`
  - Montgomery: `https://maps.montva.com/server/rest/services`
  - Orange: `https://gis.orangecountyva.gov/arcgis/rest/services`
  - Prince William: `https://gisweb.pwcva.gov/arcgis/rest/services`
  - Roanoke County: `https://arcgis.roanokecountyva.gov/arcgisweb/rest/services`
  - Spotsylvania: `https://gis.spotsylvania.va.us/arcgis/rest/services`
  - Stafford: `https://gismapping.stafford.va.us/arcgis/rest/services`
  - York: `https://maps.yorkcounty.gov/arcgis/rest/services`
- **Cities:**
  - Alexandria: `https://maps.alexandriava.gov/arcgis/rest/services`
  - Blacksburg: `https://tobmaps.blacksburg.gov/server/rest/services`
  - Charlottesville: `https://gisweb.charlottesville.org/cvgisweb/rest/services`
  - Chesapeake: `https://gis.cityofchesapeake.net/mapping/rest/services`
  - Danville: `https://gis.danvilleva.gov/server/rest/services`
  - Fredericksburg: `https://maps.fredericksburgva.gov/arcgis/rest/services`
  - Hampton: `https://webgis2.hampton.gov/server/rest/services`
  - Harrisonburg: `https://gis.harrisonburgva.gov/arcgis/rest/services`
  - Lynchburg: `https://mapviewer.lynchburgva.gov/arcgis/rest/services`
  - Newport News: `https://maps.nnva.gov/arcgis/rest/services`
  - Norfolk: `https://gisshare.norfolk.gov/pubserver/rest/services`
  - Roanoke: `https://gis03.roanokeva.gov/arcgis/rest/services`
  - Virginia Beach: `https://geo.vbgov.com/mapservices/rest/services`

---

### Washington
- **Department of Ecology:** `https://gis.ecology.wa.gov/serverext/rest/services`
- **Fish and Wildlife (WDFW):** `https://geodataservices.wdfw.wa.gov/arcgis/rest/services`
- **Department of Natural Resources (DNR):** `https://gis.dnr.wa.gov/site1/rest/services`
- **DNR Wildfire & Forestry:** `https://gis.dnr.wa.gov/site3/rest/services`
- **Department of Transportation (WSDOT Data):** `https://data.wsdot.wa.gov/arcgis/rest/services`
- **Recreation and Conservation Office (RCO):** `https://gismanager.rco.wa.gov/arcgis/rest/services`
- **Sound Transit (Puget Sound):** `https://rtamaps2.soundtransit.org/arcgis/rest/services`
- **Counties:**
  - Chelan: `https://atlas.co.chelan.wa.us/arcgis/rest/services`
  - Clallam: `https://websrv31.clallamcountywa.gov/server/rest/services`
  - Island: `https://maps.islandcountywa.gov/arcgis/rest/services`
  - Jefferson: `https://gisweb.jeffcowa.us/server/rest/services`
  - King County (Seattle): `https://gismaps.kingcounty.gov/arcgis/rest/services`
  - Kitsap: `https://ags.kitsapgov.com/arcgis/rest/services`
  - Kittitas: `https://gis.co.kittitas.wa.us/kcgis/rest/services`
  - Lewis: `https://arcgis.lewiscountywa.gov/arcgispublic/rest/services`
  - Mason: `https://gis.masoncountywa.gov/arcgis/rest/services`
  - Pend Oreille: `https://gis.pendoreilleco.org/arcgis/rest/services`
  - Pierce (Tacoma): `https://services2.arcgis.com/1UvBaQ5y1ubjUPmd/arcgis/rest/services`
  - San Juan: `https://gis.sanjuancountywa.gov/arcgis/rest/services`
  - Skagit: `https://gis.skagitcountywa.gov/arcgis/rest/services`
  - Snohomish: `https://gis.snoco.org/scd/rest/services`
  - Spokane County: `https://gismo.spokanecounty.org/arcgis/rest/services`
  - Stevens: `https://gis.stevenscountywa.gov/server/rest/services`
  - Thurston (Olympia): `https://map.co.thurston.wa.us/arcgis/rest/services`
  - Whatcom: `https://gis.whatcomcounty.us/arcgis/rest/services`
  - Yakima County: `https://maps.yakimacounty.us/server/rest/services`
- **Cities:**
  - Anacortes: `https://arcgiscoa.cityofanacortes.org/arcgiscoa/rest/services`
  - Arlington: `https://gis.arlingtonwa.gov/arcgisserver/rest/services`
  - Auburn: `https://gis.auburnwa.gov/mapping/rest/services`
  - Bellevue: `https://portal-web.bellevuewa.gov/gisext/rest/services`
  - Bellingham: `https://maps.cob.org/arcgis2/rest/services`
  - Bothell: `https://gisweb.bothellwa.gov/server/rest/services`
  - Bremerton: `https://imagegis.bremertonwa.gov/arcgis/rest/services`
  - Edmonds: `https://maps.edmondswa.gov/gis/rest/services`
  - Everett: `https://gismaps.everettwa.gov/manarcgis/rest/services`
  - Kennewick: `https://maps.ci.kennewick.wa.us/server/rest/services`
  - Kirkland: `https://maps.kirklandwa.gov/host/rest/services`
  - Lynnwood: `https://gis.lynnwoodwa.gov/gis_server/rest/services`
  - Olympia: `https://gis.olympiawa.gov/arcgis/rest/services`
  - Pullman: `https://gis.pullman-wa.gov/arcgis/rest/services`
  - Puyallup: `https://gis.puyallupwa.gov/arcgis/rest/services`
  - Redmond: `https://maps.redmond.gov/server/rest/services`
  - Renton: `https://gismaps.rentonwa.gov/as03/rest/services`
  - Richland: `https://imaps.ci.richland.wa.us/arcgis1081/rest/services`
  - Seattle: `https://gisdata.seattle.gov/server/rest/services`
  - Spokane: `https://services.spokanegis.org/arcgis/rest/services`
  - Vancouver: `https://gis.cityofvancouver.us/arcgis/rest/services`
  - Wenatchee: `https://maps.wenatcheewa.gov/server/rest/services`

---

### West Virginia
- **Department of Environmental Protection (TAGIS):** `https://tagis.dep.wv.gov/arcgis/rest/services`
- **TAGIS Imagery:** `https://tagis.dep.wv.gov/image/rest/services`
- **Department of Transportation:** `https://gis.transportation.wv.gov/arcgis/rest/services`
- **Office of Environmental Health Services:** `https://oehsportal.wvdhhr.org/arcgis/rest/services`
- **Statewide Addressing Project (WVSAMS):** `https://wvsams.mapwv.org/arcgis/rest/services`
- **WVU Technical Center (Parcels):** `https://services.wvgis.wvu.edu/ArcGIS/rest/services`
- **Geological and Economic Survey:** `https://atlas.wvgs.wvnet.edu/arcgis/rest/services`
- **Counties & Cities:**
  - Harrison County: `https://gismaps.harrisoncountywv.com/server/rest/services`
  - Kanawha County Assessor: `https://kanawhacountyassessorgis.com/server/rest/services`
  - Martinsburg: `https://services6.arcgis.com/deAS8KeQ1ASFd1S2/ArcGIS/rest/services`

---

### Wisconsin
- **Department of Agriculture, Trade & Consumer (DATCP):** `https://datcpgis.wi.gov/arcgis/rest/services`
- **Department of Health Services:** `https://dhsgis.wi.gov/server/rest/services`
- **Department of Natural Resources (WDNR):** `https://dnrmaps.wi.gov/arcgis/rest/services`
- **WDNR Services 2:** `https://dnrmaps.wi.gov/arcgis2/rest/services`
- **Wisconsin State Legislature (WLIP Parcels):** `https://mapservices.legis.wisconsin.gov/arcgis/rest/services`
- **Public Service Commission:** `https://maps.psc.wi.gov/server/rest/services`
- **University of Wisconsin:** `https://webgis.uwm.edu/arcgisuwm/rest/services`
- **Counties:**
  - Ashland: `https://gis.ashlandcountywi.gov/arcgis/rest/services`
  - Bayfield: `https://maps.bayfieldcounty.wi.gov/arcgis/rest/services`
  - Brown (Green Bay): `https://gis.browncountywi.gov/arcgis/rest/services`
  - Calumet: `https://calmaps.co.calumet.wi.us/server/rest/services`
  - Columbia: `https://lrs.co.columbia.wi.us/server/rest/services`
  - Dodge: `https://geo2.co.dodge.wi.us/arcgis/rest/services`
  - Eau Claire: `https://gis.co.eau-claire.wi.us/agsserver/rest/services`
  - Fond du Lac: `https://gisweb.fdlco.wi.gov/server/rest/services`
  - Grant: `https://gcarcgis.co.grant.wi.gov/server/rest/services`
  - Jefferson: `https://jeffarcgis.jeffersoncountywi.gov/arcgis/rest/services`
  - Juneau: `https://gismap.co.juneau.wi.us/server/rest/services`
  - Kenosha: `https://mapping.kenoshacountywi.gov/server/rest/services`
  - La Crosse: `https://gis.lacrossecounty.org/gisserver/rest/services`
  - Lafayette: `https://gis.lafayettecountywi.org/arcgis/rest/services`
  - Lincoln: `https://maps.co.lincoln.wi.us/arcgis/rest/services`
  - Manitowoc: `https://manitowocmaps.info/arcgis/rest/services`
  - Marathon: `https://gis2.co.marathon.wi.us/arcgis/rest/services`
  - Marquette: `https://webportal.co.marquette.wi.us/publicags/rest/services`
  - Milwaukee County LIO: `https://lio.milwaukeecountywi.gov/arcgis/rest/services`
  - Oconto: `https://oc17maps.co.oconto.wi.us/arcgis/rest/services`
  - Outagamie: `https://gis.outagamie.org/arcgis/rest/services`
  - Ozaukee: `https://gis2.co.ozaukee.wi.us/arcgis/rest/services`
  - Pepin: `https://gis.co.pepin.wi.us/arcgis/rest/services`
  - Pierce: `https://gis.co.pierce.wi.us/arcgis/rest/services`
  - Portage: `https://gisinfo.co.portage.wi.gov/server/rest/services`
  - Racine: `https://arcgis.racinecounty.com/arcgis/rest/services`
  - Richland: `https://gis.co.richland.wi.us/arcgis/rest/services`
  - Sauk: `https://gis.co.sauk.wi.us/arcgis/rest/services`
  - Shawano: `https://maps.co.shawano.wi.us/server/rest/services`
  - Vilas: `https://maps.vilascountywi.gov/vilasgis/rest/services`
  - Walworth: `https://gisinfo.co.walworth.wi.us/arcgis/rest/services`
  - Washington: `https://maps.washcowisco.gov/server/rest/services`
  - Waukesha: `https://gis.waukeshacounty.gov/host/rest/services`
  - Waupaca: `https://public1.co.waupaca.wi.us/arcgis/rest/services`
  - Waushara: `https://gis.co.waushara.wi.us/arcgis/rest/services`
  - Winnebago: `https://wcgis3.co.winnebago.wi.us/wings/rest/services`
  - Wood: `https://gis.woodcountywi.gov/gis/rest/services`
- **Cities:**
  - Appleton: `https://gis.appleton.org/pubserver/rest/services`
  - Green Bay: `https://map.greenbaywi.gov/server/rest/services`
  - Madison: `https://maps.cityofmadison.com/arcgis/rest/services`
  - Milwaukee (City): `https://milwaukeemaps.milwaukee.gov/arcgis/rest/services`
  - Oshkosh: `https://www.ci.oshkosh.wi.us/arcgis/rest/services`
  - Racine (City): `https://gis.cityofracine.org/arcgis/rest/services`
  - Watertown: `https://gis.watertownwi.gov/arcgis/rest/services`
  - Waukesha: `https://gis.waukesha-wi.gov/server/rest/services`
  - Wausau: `https://gis.ci.wausau.wi.us/server/rest/services`
  - West Allis: `https://gis.westalliswi.gov/server/rest/services`
  - West Bend: `https://gis.ci.west-bend.wi.us/arcgis/rest/services`
  - Weston: `https://gis.westonwi.gov/arcgis/rest/services`
  - Wisconsin Rapids: `https://gis.wirapids.org/arcgis/rest/services`

---

### Wyoming
- **Department of Environmental Quality:** `https://gis.deq.wyo.gov/arcgis/rest/services`
- **WYDOT WyoRoad:** `https://map.wyoroad.info/ags/rest/services`
- **State Geological Survey (WSGS):** `https://portal.wsgs.wyo.gov/ags/rest/services`
- **University of Wyoming (WyGISC):** `https://services.wygisc.org/hostgis/rest/services`
- **Counties & Cities:**
  - Campbell County: `https://gis.campbellcountywy.gov/arcgis/rest/services`
  - Laramie County (Cheyenne): `https://maps.laramiecounty.com/arcgis/rest/services`
  - Lincoln County: `https://maps.lcwy.org/arcgis/rest/services`
  - Gillette: `https://gisportal.gillettewy.gov/arcgisserver/rest/services`
  - Sheridan: `https://gismaps.sheridanwy.net/arcgis/rest/services`

---

## Washington D.C.
| Unit | Service URL |
| :--- | :--- |
| DC OCTO Geographic Services | `https://maps2.dcgis.dc.gov/dcgis/rest/services` |
| DC Imagery | `https://imagery.dcgis.dc.gov/dcgis/rest/services` |
| DC Roadway / Highway | `https://rh.dcgis.dc.gov/dcgis/rest/services` |
| DC Emergency Management | `https://em.dcgis.dc.gov/dcgis/rest/services` |
| Metropolitan Washington COG | `https://services.arcgis.com/n8kgWFr4EwFGg3zA/arcgis/rest/services` |

---

## Native American Tribes
| Nation / Tribal Council | Service URL |
| :--- | :--- |
| Coeur d'Alene Tribe | `https://gis.cdatribe-nsn.gov/arcgis/rest/services` |
| Coeur d'Alene Imagery | `https://gis.cdatribe-nsn.gov/arcgisimage/rest/services` |
| Navajo Nation | `https://services1.arcgis.com/jj1iIK6we0wGtl1K/arcgis/rest/services` |
| Saint Regis Mohawk Tribe | `https://services6.arcgis.com/xo0Sli3SaYPY0VRz/arcgis/rest/services` |
| Snoqualmie Tribe | `https://gis.snoqualmietribe.us/arcgis/rest/services` |
| Tanana Chiefs Conference | `https://gis.tananachiefs.org/arcgisserver/rest/services` |
| Tulalip Tribes | `https://gismaps2.tulaliptribes-nsn.gov/arcgis/rest/services` |
| Seneca Nation | `https://services8.arcgis.com/OX5r7ewGgTojKuuK/ArcGIS/rest/services` |
| Nez Perce Tribe | `https://services7.arcgis.com/iICsLMZKYMImM2LL/arcgis/rest/services` |

---

## U.S. Territories
| Territory | Service URL |
| :--- | :--- |
| American Samoa | `https://services5.arcgis.com/ugcD1wqDyNIfJ9ce/ArcGIS/rest/services` |
| Guam EPA | `https://gis.epa.guam.gov/arcgis/rest/services` |
| Northern Mariana Islands | `https://services.arcgis.com/qchgHH9IIeiivY5M/ArcGIS/rest/services` |
| Puerto Rico (SIGELA) | `https://www.sigela.pr.gov/arcgis/rest/services` |
| Puerto Rico (SIGE) | `https://sige.pr.gov/server/rest/services` |
| U.S. Virgin Islands (CAMA) | `https://maps.capturecama.com/arcgis/rest/services/USVI` |

---

## Multi-State & Regional Planning
| Body / Program | Region / Scope | Service URL |
| :--- | :--- | :--- |
| Susquehanna River Basin Commission | NY, PA, MD | `https://gis.srbc.gov/arcgis/rest/services` |
| Mid-America Regional Council (MARC) | KS, MO | `https://gis2.marc2.org/arcgis/rest/services` |
| OKI Regional Council | OH, KY, IN | `https://gis.oki.org/server/rest/services` |
| Northeast Regional Ocean Council | Northeast US | `https://services.northeastoceandata.org/arcgis1/rest/services` |
| Pacific Disaster Center | Multi-State / Global | `https://arcgis.pdc.org/arcgis/rest/services` |
| Data Basin | Continental US | `https://padags.databasin.org/arcgis/rest/services` |

---

## Environmental & Non-Profit Organizations
| Organization | Service URL |
| :--- | :--- |
| Center for Biological Diversity | `https://services.arcgis.com/HoKuy8MaByQZ1OQ9/arcgis/rest/services` |
| Chesapeake Bay Foundation | `https://gis.cbf.org/arcgis/rest/services` |
| Chesapeake Conservancy | `https://cicgis.org/arcgis/rest/services` |
| Continental Divide Trail Coalition | `https://services8.arcgis.com/WyuHwdftppQLa5KO/ArcGIS/rest/services` |
| Ducks Unlimited | `https://services2.arcgis.com/5I7u4SJE1vUr79JC/arcgis/rest/services` |
| National Audubon Society | `https://gis.audubon.org/arcgisweb/rest/services` |
| NatureServe | `https://services.arcgis.com/EVsTT4nNRCwmHNyb/arcgis/rest/services` |
| The Nature Conservancy (TNC) | `https://cirrus.tnc.org/arcgis/rest/services` |
| The Trust for Public Land (TPL) | `https://server5.tplgis.org/arcgis5/rest/services` |
| Trout Unlimited & Wilderness Society | `https://services1.arcgis.com/754BERmVIq3RqSf8/ArcGIS/rest/services` |

---

## National & Miscellaneous Collections
*ESRI-hosted ArcGIS Online hubs carrying nationwide layers (weather feeds, wildland fires, active shelters, parcel composites, and building footprints):*

- **Esri Live Feeds & Weather:** `https://services9.arcgis.com/RHVPKKiFTONKtxq3/ArcGIS/rest/services`
- **NIFC Interagency Fire Perimeters (WFIGS):** `https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services`
- **USA Structures & USNG Grids:** `https://services2.arcgis.com/FiaPA4ga0iQKduv3/arcgis/rest/services`
- **Federal HILFD Historical Archives:** `https://services1.arcgis.com/Hp6G80Pky0om7QvQ/ArcGIS/rest/services`
- **General Aggregation Hub 1:** `https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services`
- **General Aggregation Hub 2:** `https://services.arcgis.com/0ZRg6WRC7mxSLyKX/ArcGIS/rest/services`

---

## International & Canada
- **International Boundary and Water Commission (US–Mexico):** `https://gisserver.ibwc.gov/agsserver/rest/services/USIBWCPublic/US_MexicoIB/FeatureServer`
- **ArcGIS Online World Base Services:** `https://services.arcgisonline.com/arcgis/rest/services`
- **Natural Resources Canada Geospatial Web Services:** `https://natural-resources.canada.ca/science-data/science-research/geomatics/geospatial-web-services`
