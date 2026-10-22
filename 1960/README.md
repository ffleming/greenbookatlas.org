# The Travelers' Green Book: 1960 - Green Book Atlas (Sit-In Movement Era Edition (Alma D. Green, Publisher))

**TL;DR:** Published in 1960 (132 pocket pages, 2,205 geocoded listings), dropping 'Negro' from the cover title as Alma Duke Green assumed leadership as publisher. Total geocoded establishments: *2,205* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/1f0653d0-1a74-0132-69ff-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1960_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1960_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (2,205 records)
- [NYPL original PDF (21.5 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1960.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 132 pages
- `ocr/` - 132 page-level `.txt` and 132 `.hocr` OCR files

### Supplemental files
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Hotels & Motels | 944 |
| Lodging: Tourist Homes | 484 |
| Dining: Restaurants | 405 |
| Retail, Services & Other | 272 |
| Auto: Gas, Garages & Transport | 67 |
| Nightlife: Taverns & Clubs | 22 |
| Personal Care: Barber, Beauty & Tailors | 11 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 201 |
| NJ | 137 |
| TN | 135 |
| TX | 116 |
| AR | 87 |
| MI | 87 |
| OH | 84 |
| AL | 72 |
| CA | 70 |
| VA | 68 |
| LA | 63 |
| IL | 59 |
| MO | 54 |
| NC | 53 |
| MA | 51 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
