# The Negro Travelers' Green Book: 1959 - Green Book Atlas (Final Edition Under Victor H. Green's Lifetime)

**TL;DR:** Published in 1959 (88 pages, 2,118 geocoded listings) in compact pocket format shortly before founder Victor Hugo Green's passing in October 1960. Total geocoded establishments: *2,118* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/8bf60a70-1a75-0132-d6c0-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1959_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1959_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (2,118 records)
- [NYPL original PDF (14.9 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1959.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 88 pages
- `ocr/` - 88 page-level `.txt` and 88 `.hocr` OCR files

### Supplemental files
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Hotels & Motels | 936 |
| Lodging: Tourist Homes | 509 |
| Dining: Restaurants | 358 |
| Retail, Services & Other | 289 |
| Nightlife: Taverns & Clubs | 13 |
| Auto: Gas, Garages & Transport | 10 |
| Personal Care: Barber, Beauty & Tailors | 3 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 215 |
| NJ | 143 |
| TX | 105 |
| MI | 98 |
| OH | 86 |
| IL | 83 |
| CA | 72 |
| VA | 72 |
| MO | 62 |
| AR | 55 |
| NC | 55 |
| LA | 54 |
| SC | 54 |
| MA | 53 |
| PA | 50 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
