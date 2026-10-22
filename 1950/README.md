# The Negro Motorist Green Book: 1950 - Green Book Atlas (Mid-Century Peak Listings Edition)

**TL;DR:** Published in 1950 (92 pages), representing the highest total business listing count (4,315 geocoded locations) across the United States, Canada, Mexico, and Bermuda. Total geocoded establishments: *4,315* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/96738510-8937-0132-5591-58d385a7b928)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1950_mymaps_part1_of_3.kml`
  - `mymaps/greenbook_1950_mymaps_part2_of_3.kml`
  - `mymaps/greenbook_1950_mymaps_part3_of_3.kml`
- `listings.csv` and `listings.json` - structured dataset (4,315 records)
- [NYPL original PDF (16.7 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1950.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 92 pages
- `ocr/` - 92 page-level `.txt` and 92 `.hocr` OCR files

### Supplemental files
- `supplemental/GreenBook_city_noGeo_50.csv`
- `supplemental/GreenBook_city_noGeo_50.ods`
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Nightlife: Taverns & Clubs | 908 |
| Personal Care: Barber, Beauty & Tailors | 836 |
| Lodging: Tourist Homes | 639 |
| Lodging: Hotels & Motels | 601 |
| Dining: Restaurants | 597 |
| Auto: Gas, Garages & Transport | 372 |
| Retail, Services & Other | 362 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 605 |
| NJ | 342 |
| OH | 284 |
| MO | 244 |
| TX | 223 |
| NC | 195 |
| CA | 172 |
| PA | 153 |
| MI | 150 |
| VA | 140 |
| AR | 117 |
| MA | 117 |
| IN | 111 |
| LA | 109 |
| SC | 109 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
