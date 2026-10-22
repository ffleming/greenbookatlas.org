# The Negro Travelers' Green Book: 1956 - Green Book Atlas (Interstate Highway Act & 20th Anniversary Edition)

**TL;DR:** Published in Spring 1956 (84 pages, 1,942 geocoded listings), streamlining directory categories to focus on lodging, dining, and service stations during the birth of the Interstate Highway System. Total geocoded establishments: *1,942* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/3ef663c0-8938-0132-e036-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1956_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1956_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (1,942 records)
- [NYPL original PDF (14.6 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1956.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 84 pages
- `ocr/` - 84 page-level `.txt` and 84 `.hocr` OCR files

### Supplemental files
- `supplemental/uofsc_nypl_greenbook_1956.json`
- `supplemental/library_sc_edu_greenbookmap_0.json`
- `supplemental/library_sc_edu_greenbookmap_500.json`
- `supplemental/library_sc_edu_greenbookmap_1000.json`
- `supplemental/library_sc_edu_greenbookmap_1500.json`
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Hotels & Motels | 753 |
| Lodging: Tourist Homes | 587 |
| Dining: Restaurants | 346 |
| Retail, Services & Other | 251 |
| Nightlife: Taverns & Clubs | 4 |
| Personal Care: Barber, Beauty & Tailors | 1 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 207 |
| NJ | 142 |
| MI | 99 |
| TX | 98 |
| OH | 94 |
| PA | 78 |
| VA | 72 |
| MO | 63 |
| CA | 62 |
| IL | 56 |
| LA | 56 |
| MA | 56 |
| NC | 53 |
| SC | 52 |
| AR | 50 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
