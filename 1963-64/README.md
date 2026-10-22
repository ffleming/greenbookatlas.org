# Travelers' Green Book: 1963-64 International Edition - Green Book Atlas (March on Washington & Civil Rights Act Eve Edition)

**TL;DR:** Published in 1963 (113 digitized pages, 3,202 geocoded listings) on the eve of the Civil Rights Act of 1964, featuring an article on the 1963–1965 Centennial of the Emancipation Proclamation. Total geocoded establishments: *3,202* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/6fa5be40-8939-0132-9c3c-58d385a7b928)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1963-64_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1963-64_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (3,202 records)
- [NYPL original PDF (17.5 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1963-64.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 113 pages
- `ocr/` - 113 page-level `.txt` and 113 `.hocr` OCR files

### Supplemental files
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Hotels & Motels | 2,043 |
| Lodging: Tourist Homes | 410 |
| Dining: Restaurants | 391 |
| Retail, Services & Other | 152 |
| Nightlife: Taverns & Clubs | 93 |
| Auto: Gas, Garages & Transport | 81 |
| Personal Care: Barber, Beauty & Tailors | 32 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 533 |
| NJ | 103 |
| VA | 89 |
| TX | 88 |
| IL | 83 |
| NC | 78 |
| TN | 77 |
| CA | 76 |
| FL | 74 |
| OH | 69 |
| MO | 66 |
| Jamaica | 64 |
| England | 63 |
| MI | 61 |
| AR | 60 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
