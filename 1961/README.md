# The Travelers' Green Book: 1961 - Green Book Atlas (Freedom Rides Era Edition)

**TL;DR:** Published in 1961 (132 pocket pages, 2,321 geocoded listings) during the year of the CORE/SNCC Freedom Rides desegregating interstate bus terminals. Total geocoded establishments: *2,321* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/dcf5d950-1a73-0132-6a76-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1961_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1961_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (2,321 records)
- [NYPL original PDF (20.0 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1961.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 132 pages
- `ocr/` - 132 page-level `.txt` and 132 `.hocr` OCR files

### Supplemental files
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Hotels & Motels | 984 |
| Lodging: Tourist Homes | 463 |
| Dining: Restaurants | 426 |
| Retail, Services & Other | 288 |
| Auto: Gas, Garages & Transport | 85 |
| Nightlife: Taverns & Clubs | 56 |
| Personal Care: Barber, Beauty & Tailors | 19 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 217 |
| NJ | 141 |
| TN | 129 |
| TX | 113 |
| AR | 95 |
| IL | 92 |
| MI | 91 |
| VA | 89 |
| OH | 80 |
| CA | 70 |
| AL | 69 |
| NC | 69 |
| LA | 68 |
| PA | 59 |
| MO | 53 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
