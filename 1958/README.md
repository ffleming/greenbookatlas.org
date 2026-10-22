# The Negro Travelers' Green Book: 1958 - Green Book Atlas (1958 Pocket-Format Transition Edition)

**TL;DR:** Published in 1958 (2,147 geocoded listings), digitized by the NYPL Schomburg Center (item b4affe50-7ca3-013f-af86-0242ac110002) following the 2016 bulk OCR release. Total geocoded establishments: *2,147* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/b4affe50-7ca3-013f-af86-0242ac110002)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1958_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1958_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (2,147 records)
- *NB*: The 1958 edition is preserved in the [NYPL Digital Collections](https://digitalcollections.nypl.org/items/b4affe50-7ca3-013f-af86-0242ac110002) and all 2,147 establishments are included in `listings.*` and `overlay.*`, though its bulk PDF/hOCR files were not included in NYPL's 21-volume `NYPL-publicdomain/greenbooks` release.

### Supplemental files
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Hotels & Motels | 986 |
| Lodging: Tourist Homes | 533 |
| Dining: Restaurants | 366 |
| Retail, Services & Other | 256 |
| Nightlife: Taverns & Clubs | 3 |
| Auto: Gas, Garages & Transport | 2 |
| Personal Care: Barber, Beauty & Tailors | 1 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 217 |
| NJ | 150 |
| MI | 107 |
| TX | 100 |
| OH | 84 |
| PA | 79 |
| CA | 77 |
| VA | 73 |
| IL | 62 |
| AR | 56 |
| LA | 55 |
| SC | 55 |
| MA | 54 |
| NC | 54 |
| MO | 53 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
