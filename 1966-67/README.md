# Travelers' Green Book: 1966-67 International Edition - Green Book Atlas (Latest & Final Published Edition)

**TL;DR:** Subtitled 'For Vacation Without Aggravation' (3,300 geocoded listings), the 1966-67 International Edition was the final issue published after the Civil Rights Act of 1964 outlawed racial discrimination in public accommodations. Total geocoded establishments: *3,300* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/27516920-8308-0132-5063-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1966-67_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1966-67_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (3,300 records)
- *Note*: NYPL does not provide 1966-1967 scans because they are still under copyright. We include the non-copyrightable factual directory listings (`listings.*` and `overlay.*`).

### Supplemental files
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Hotels & Motels | 2,119 |
| Dining: Restaurants | 416 |
| Lodging: Tourist Homes | 410 |
| Retail, Services & Other | 149 |
| Nightlife: Taverns & Clubs | 93 |
| Auto: Gas, Garages & Transport | 81 |
| Personal Care: Barber, Beauty & Tailors | 32 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 583 |
| NJ | 105 |
| VA | 91 |
| TX | 90 |
| IL | 83 |
| NC | 78 |
| CA | 77 |
| FL | 75 |
| TN | 75 |
| OH | 69 |
| MO | 67 |
| Jamaica | 64 |
| England | 63 |
| AR | 61 |
| MI | 61 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
