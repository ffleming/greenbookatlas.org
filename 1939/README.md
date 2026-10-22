# The Negro Motorist Green Book: 1939 - Green Book Atlas (1939 New York World's Fair Edition)

**TL;DR:** Published in 1939 (52 pages) with a special New York World's Fair supplement and nearly double the previous year's coverage (2,006 geocoded establishments). Total geocoded establishments: *2,006* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/2dacae50-1a75-0132-d154-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1939_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1939_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (2,006 records)
- [NYPL original PDF (9.0 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1939.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 52 pages
- `ocr/` - 52 page-level `.txt` and 52 `.hocr` OCR files

### Supplemental files
- `supplemental/GreenBook_city_withGeo_37-39.csv`
- `supplemental/GreenBook_city_noGeo_37-39.csv`
- `supplemental/GreenBook_city_noGeo_37-39.ods`
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Tourist Homes | 756 |
| Lodging: Hotels & Motels | 511 |
| Nightlife: Taverns & Clubs | 227 |
| Personal Care: Barber, Beauty & Tailors | 193 |
| Dining: Restaurants | 141 |
| Auto: Gas, Garages & Transport | 107 |
| Retail, Services & Other | 71 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NJ | 274 |
| NY | 254 |
| PA | 144 |
| OH | 95 |
| VA | 91 |
| TX | 66 |
| IL | 63 |
| NC | 62 |
| OK | 62 |
| SC | 61 |
| GA | 52 |
| MI | 51 |
| CA | 49 |
| MO | 45 |
| AR | 43 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
