# The Negro Travelers' Green Book: 1952 - Green Book Atlas (First 'Negro Travelers' Title Edition)

**TL;DR:** Published in 1952 (84 pages, 4,161 geocoded listings), marking the official title transition from 'The Negro Motorist Green Book' to 'The Negro Travelers' Green Book'. Total geocoded establishments: *4,161* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/0387d5f0-1a72-0132-c0b2-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1952_mymaps_part1_of_3.kml`
  - `mymaps/greenbook_1952_mymaps_part2_of_3.kml`
  - `mymaps/greenbook_1952_mymaps_part3_of_3.kml`
- `listings.csv` and `listings.json` - structured dataset (4,161 records)
- [NYPL original PDF (15.7 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1952.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 84 pages
- `ocr/` - 84 page-level `.txt` and 84 `.hocr` OCR files

### Supplemental files
- `supplemental/GreenBook_city_noGeo_52.csv`
- `supplemental/GreenBook_city_noGeo_52.ods`
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Nightlife: Taverns & Clubs | 860 |
| Personal Care: Barber, Beauty & Tailors | 797 |
| Lodging: Hotels & Motels | 628 |
| Lodging: Tourist Homes | 612 |
| Dining: Restaurants | 528 |
| Retail, Services & Other | 392 |
| Auto: Gas, Garages & Transport | 344 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 614 |
| NJ | 353 |
| OH | 273 |
| TX | 200 |
| NC | 193 |
| MO | 191 |
| CA | 169 |
| MI | 144 |
| PA | 137 |
| VA | 127 |
| MA | 111 |
| AR | 107 |
| LA | 105 |
| IN | 97 |
| SC | 97 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
