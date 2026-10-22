# Travelers' Green Book: 1962 - Green Book Atlas (1962 Guide for Travel & Vacations)

**TL;DR:** Published in 1962 (130 pocket pages, 2,250 geocoded listings) under Alma D. Green, covering U.S. states, Canada, the Caribbean, and Western Europe. Total geocoded establishments: *2,250* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/9ab2e8f0-1a73-0132-95bd-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1962_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1962_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (2,250 records)
- [NYPL original PDF (18.2 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1962.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 130 pages
- `ocr/` - 130 page-level `.txt` and 130 `.hocr` OCR files

### Supplemental files
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Hotels & Motels | 930 |
| Lodging: Tourist Homes | 399 |
| Dining: Restaurants | 395 |
| Retail, Services & Other | 359 |
| Nightlife: Taverns & Clubs | 83 |
| Auto: Gas, Garages & Transport | 73 |
| Personal Care: Barber, Beauty & Tailors | 11 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 361 |
| NJ | 131 |
| VA | 99 |
| TX | 94 |
| MI | 85 |
| IL | 82 |
| TN | 76 |
| FL | 71 |
| OH | 71 |
| CA | 62 |
| AR | 59 |
| LA | 57 |
| PA | 56 |
| MA | 49 |
| NC | 47 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
