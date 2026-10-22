# The Negro Motorist Green Book: 1951 Railroad Edition - Green Book Atlas (1951 Railroad & International Travel Edition)

**TL;DR:** Published in 1951 (84 pages, 4,229 geocoded listings), incorporating rail travel features alongside motorist accommodations across North America. Total geocoded establishments: *4,229* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/6c5ccbe0-1a73-0132-b81d-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1951_mymaps_part1_of_3.kml`
  - `mymaps/greenbook_1951_mymaps_part2_of_3.kml`
  - `mymaps/greenbook_1951_mymaps_part3_of_3.kml`
- `listings.csv` and `listings.json` - structured dataset (4,229 records)
- [NYPL original PDF (15.3 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1951.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 84 pages
- `ocr/` - 84 page-level `.txt` and 84 `.hocr` OCR files

### Supplemental files
- `supplemental/GreenBook_city_noGeo_51.csv`
- `supplemental/GreenBook_city_noGeo_51.ods`
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Nightlife: Taverns & Clubs | 874 |
| Personal Care: Barber, Beauty & Tailors | 844 |
| Lodging: Tourist Homes | 614 |
| Lodging: Hotels & Motels | 610 |
| Dining: Restaurants | 565 |
| Auto: Gas, Garages & Transport | 367 |
| Retail, Services & Other | 355 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 616 |
| NJ | 339 |
| OH | 284 |
| TX | 210 |
| MO | 208 |
| NC | 195 |
| CA | 163 |
| MI | 147 |
| PA | 141 |
| VA | 132 |
| MA | 122 |
| AR | 111 |
| IN | 109 |
| LA | 106 |
| SC | 99 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
