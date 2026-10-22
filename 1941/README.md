# The Negro Motorist Green Book: 1941 - Green Book Atlas (Final Pre-WWII Edition)

**TL;DR:** Published in 1941 (52 pages) with sponsorship from Esso Standard Oil marketer James A. Jackson ('The Esso Man'), just before wartime gasoline and paper rationing suspended annual publication from 1942 through 1945. Total geocoded establishments: *1,990* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/47e874a0-1a74-0132-a7fb-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1941_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1941_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (1,990 records)
- [NYPL original PDF (8.6 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1941.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 52 pages
- `ocr/` - 52 page-level `.txt` and 52 `.hocr` OCR files

### Supplemental files
- `supplemental/GreenBook_city_noGeo_41.csv`
- `supplemental/GreenBook_city_noGeo_41.ods`
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Tourist Homes | 642 |
| Lodging: Hotels & Motels | 426 |
| Nightlife: Taverns & Clubs | 288 |
| Personal Care: Barber, Beauty & Tailors | 271 |
| Dining: Restaurants | 159 |
| Auto: Gas, Garages & Transport | 143 |
| Retail, Services & Other | 61 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 272 |
| NJ | 233 |
| PA | 131 |
| VA | 90 |
| OH | 88 |
| TX | 88 |
| NC | 66 |
| CA | 60 |
| IL | 60 |
| MI | 55 |
| MO | 54 |
| OK | 54 |
| LA | 50 |
| MA | 44 |
| AR | 42 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
