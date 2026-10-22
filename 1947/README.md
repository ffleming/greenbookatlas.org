# The Negro Motorist Green Book: 1947 - Green Book Atlas (Post-WWII Boom & Vacation Reservation Service Edition)

**TL;DR:** Published in 1947 (84 pages) as post-war automobile travel surged and Victor Green launched his Vacation Reservation Service in Harlem. Total geocoded establishments: *3,649* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/2bc77d90-8937-0132-c56c-58d385a7b928)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1947_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1947_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (3,649 records)
- [NYPL original PDF (20.7 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1947.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 84 pages
- `ocr/` - 84 page-level `.txt` and 84 `.hocr` OCR files

### Supplemental files
- `supplemental/GreenBook1947Notes.md`
- `supplemental/GreenBook1947_inProcess.ods`
- `supplemental/GreenBook_city_noGeo_47.csv`
- `supplemental/GreenBook_city_noGeo_47.ods`
- `supplemental/nypl_labs_1947.geojson`
- `supplemental/nypl_map_greenbook_1947.json`
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Nightlife: Taverns & Clubs | 754 |
| Personal Care: Barber, Beauty & Tailors | 667 |
| Lodging: Tourist Homes | 645 |
| Lodging: Hotels & Motels | 568 |
| Dining: Restaurants | 526 |
| Auto: Gas, Garages & Transport | 302 |
| Retail, Services & Other | 187 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 527 |
| NJ | 300 |
| MO | 191 |
| OH | 188 |
| CA | 186 |
| TX | 174 |
| PA | 149 |
| NC | 146 |
| AR | 127 |
| VA | 117 |
| SC | 113 |
| LA | 105 |
| MI | 97 |
| MA | 95 |
| IL | 82 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
