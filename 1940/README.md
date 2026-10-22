# The Negro Motorist Green Book: 1940 - Green Book Atlas (Pre-WWII National Expansion Edition)

**TL;DR:** Published in 1940 (52 pages), demonstrating rapid national expansion across 43 states and the District of Columbia before World War II. Total geocoded establishments: *2,059* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/dc858eb0-8936-0132-128f-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1940_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1940_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (2,059 records)
- [NYPL original PDF (8.1 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1940.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 52 pages
- `ocr/` - 52 page-level `.txt` and 52 `.hocr` OCR files

### Supplemental files
- `supplemental/GreenBook_city_noGeo_40.csv`
- `supplemental/GreenBook_city_noGeo_40.ods`
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Tourist Homes | 733 |
| Lodging: Hotels & Motels | 440 |
| Nightlife: Taverns & Clubs | 268 |
| Personal Care: Barber, Beauty & Tailors | 265 |
| Auto: Gas, Garages & Transport | 148 |
| Dining: Restaurants | 145 |
| Retail, Services & Other | 60 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 298 |
| NJ | 230 |
| PA | 128 |
| OH | 103 |
| VA | 91 |
| TX | 89 |
| NC | 67 |
| MI | 64 |
| IL | 63 |
| CA | 57 |
| AR | 53 |
| OK | 53 |
| SC | 53 |
| LA | 52 |
| MO | 52 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
