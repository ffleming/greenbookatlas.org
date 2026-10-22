# The Negro Travelers' Green Book: 1955 International Edition - Green Book Atlas (1955 Airline & International Edition)

**TL;DR:** Published in 1955 (84 pages, 3,979 geocoded listings), featuring expanded air travel and international destination listings. Total geocoded establishments: *3,979* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/7d566930-1a76-0132-4e16-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1955_mymaps_part1_of_3.kml`
  - `mymaps/greenbook_1955_mymaps_part2_of_3.kml`
  - `mymaps/greenbook_1955_mymaps_part3_of_3.kml`
- `listings.csv` and `listings.json` - structured dataset (3,979 records)
- [NYPL original PDF (14.5 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1955.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 84 pages
- `ocr/` - 84 page-level `.txt` and 84 `.hocr` OCR files

### Supplemental files
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Nightlife: Taverns & Clubs | 773 |
| Lodging: Hotels & Motels | 735 |
| Personal Care: Barber, Beauty & Tailors | 725 |
| Lodging: Tourist Homes | 597 |
| Dining: Restaurants | 444 |
| Retail, Services & Other | 417 |
| Auto: Gas, Garages & Transport | 288 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 624 |
| NJ | 340 |
| OH | 227 |
| TX | 196 |
| NC | 163 |
| MO | 158 |
| CA | 148 |
| PA | 140 |
| MI | 129 |
| VA | 120 |
| WI | 113 |
| MA | 110 |
| AR | 108 |
| SC | 94 |
| LA | 91 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
