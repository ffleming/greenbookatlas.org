# The Negro Motorist Green Book: 1948 - Green Book Atlas (United States & Alaska Edition)

**TL;DR:** Subtitled 'A Classified Motorist & Tourist Guide Covering the United States & Alaska' (84 pages, 3,912 geocoded listings). Total geocoded establishments: *3,912* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/3a67a6d0-1a73-0132-91e7-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1948_mymaps_part1_of_3.kml`
  - `mymaps/greenbook_1948_mymaps_part2_of_3.kml`
  - `mymaps/greenbook_1948_mymaps_part3_of_3.kml`
- `listings.csv` and `listings.json` - structured dataset (3,912 records)
- [NYPL original PDF (13.9 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1948.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 84 pages
- `ocr/` - 84 page-level `.txt` and 84 `.hocr` OCR files

### Supplemental files
- `supplemental/GreenBook_city_noGeo_48.csv`
- `supplemental/GreenBook_city_noGeo_48.ods`
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Nightlife: Taverns & Clubs | 838 |
| Personal Care: Barber, Beauty & Tailors | 779 |
| Lodging: Tourist Homes | 646 |
| Dining: Restaurants | 573 |
| Lodging: Hotels & Motels | 571 |
| Auto: Gas, Garages & Transport | 355 |
| Retail, Services & Other | 150 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 612 |
| NJ | 323 |
| OH | 245 |
| TX | 224 |
| MO | 197 |
| CA | 168 |
| NC | 159 |
| PA | 143 |
| AR | 128 |
| SC | 108 |
| VA | 107 |
| MI | 106 |
| MA | 98 |
| LA | 97 |
| GA | 95 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
