# The Negro Travelers' Green Book: 1954 - Green Book Atlas (Brown v. Board of Education Era Edition)

**TL;DR:** Subtitled 'The Guide to Travel & Vacations' (84 pages, 4,071 geocoded listings), published in the year of the landmark Supreme Court decision Brown v. Board of Education. Total geocoded establishments: *4,071* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/40a8efd0-1a71-0132-336d-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1954_mymaps_part1_of_3.kml`
  - `mymaps/greenbook_1954_mymaps_part2_of_3.kml`
  - `mymaps/greenbook_1954_mymaps_part3_of_3.kml`
- `listings.csv` and `listings.json` - structured dataset (4,071 records)
- [NYPL original PDF (14.3 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1954.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 84 pages
- `ocr/` - 84 page-level `.txt` and 84 `.hocr` OCR files

### Supplemental files
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Nightlife: Taverns & Clubs | 809 |
| Personal Care: Barber, Beauty & Tailors | 761 |
| Lodging: Hotels & Motels | 689 |
| Lodging: Tourist Homes | 620 |
| Dining: Restaurants | 472 |
| Retail, Services & Other | 410 |
| Auto: Gas, Garages & Transport | 310 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 628 |
| NJ | 331 |
| OH | 239 |
| TX | 192 |
| NC | 174 |
| CA | 169 |
| MO | 163 |
| PA | 133 |
| MI | 130 |
| WI | 124 |
| VA | 123 |
| MA | 119 |
| AR | 104 |
| SC | 98 |
| LA | 90 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
