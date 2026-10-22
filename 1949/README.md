# The Negro Motorist Green Book: 1949 - Green Book Atlas (First International Travel Guide Edition)

**TL;DR:** Subtitled 'An International Travel Guide' (84 pages, 3,936 geocoded listings), containing Victor H. Green's famous foreword: 'There will be a day sometime in the near future when this guide will not have to be published.' Total geocoded establishments: *3,936* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/092a3710-1a73-0132-fdcf-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1949_mymaps_part1_of_3.kml`
  - `mymaps/greenbook_1949_mymaps_part2_of_3.kml`
  - `mymaps/greenbook_1949_mymaps_part3_of_3.kml`
- `listings.csv` and `listings.json` - structured dataset (3,936 records)
- [NYPL original PDF (12.7 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1949.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 84 pages
- `ocr/` - 84 page-level `.txt` and 84 `.hocr` OCR files

### Supplemental files
- `supplemental/GreenBook_city_noGeo_49.csv`
- `supplemental/GreenBook_city_noGeo_49.ods`
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Nightlife: Taverns & Clubs | 831 |
| Personal Care: Barber, Beauty & Tailors | 779 |
| Lodging: Tourist Homes | 640 |
| Lodging: Hotels & Motels | 578 |
| Dining: Restaurants | 574 |
| Auto: Gas, Garages & Transport | 358 |
| Retail, Services & Other | 176 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 547 |
| NJ | 315 |
| OH | 245 |
| MO | 218 |
| TX | 212 |
| CA | 166 |
| NC | 166 |
| PA | 143 |
| AR | 131 |
| VA | 122 |
| IL | 108 |
| MI | 107 |
| SC | 104 |
| MA | 97 |
| LA | 96 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
