# The Negro Travelers' Green Book: 1957 - Green Book Atlas (Civil Rights Act of 1957 Era Edition)

**TL;DR:** Published in 1957 (84 pages, 2,113 geocoded listings), providing coast-to-coast lodging and dining listings during the Little Rock Nine and Civil Rights Act of 1957 era. Total geocoded establishments: *2,113* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/639fc110-1a75-0132-d5bf-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1957_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1957_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (2,113 records)
- [NYPL original PDF (14.8 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1957.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 84 pages
- `ocr/` - 84 page-level `.txt` and 84 `.hocr` OCR files

### Supplemental files
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Hotels & Motels | 943 |
| Lodging: Tourist Homes | 557 |
| Dining: Restaurants | 339 |
| Retail, Services & Other | 264 |
| Nightlife: Taverns & Clubs | 4 |
| Personal Care: Barber, Beauty & Tailors | 3 |
| Auto: Gas, Garages & Transport | 3 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 211 |
| NJ | 148 |
| MI | 105 |
| TX | 97 |
| OH | 86 |
| PA | 84 |
| CA | 80 |
| VA | 72 |
| MA | 60 |
| AR | 58 |
| IL | 58 |
| LA | 57 |
| MO | 56 |
| NC | 55 |
| SC | 52 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
