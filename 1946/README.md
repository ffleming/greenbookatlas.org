# The Negro Motorist Green Book: 1946 - Green Book Atlas (Post-WWII Resumption Edition)

**TL;DR:** Published in 1946 as the first post-World War II edition following the 1942-1945 wartime hiatus, introducing the motto 'Carry your Green Book with you... you may need it' and expanding to 3,335 listings. Preserved in the Library of Congress collection. Total geocoded establishments: *3,335* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://www.loc.gov/item/2016298176/)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1946_mymaps_part1_of_2.kml`
  - `mymaps/greenbook_1946_mymaps_part2_of_2.kml`
- `listings.csv` and `listings.json` - structured dataset (3,335 records)
- *NB*: The 1946 edition is preserved in the [NYPL Digital Collections](https://www.loc.gov/item/2016298176/) and all 3,335 establishments are included in `listings.*` and `overlay.*`, though its bulk PDF/hOCR files were not included in NYPL's 21-volume `NYPL-publicdomain/greenbooks` release.

### Supplemental files
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Tourist Homes | 699 |
| Nightlife: Taverns & Clubs | 648 |
| Personal Care: Barber, Beauty & Tailors | 566 |
| Lodging: Hotels & Motels | 530 |
| Dining: Restaurants | 452 |
| Auto: Gas, Garages & Transport | 241 |
| Retail, Services & Other | 199 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 482 |
| NJ | 322 |
| TX | 184 |
| OH | 164 |
| PA | 158 |
| CA | 142 |
| NC | 140 |
| MO | 123 |
| VA | 110 |
| SC | 108 |
| AR | 107 |
| LA | 97 |
| IL | 90 |
| OK | 80 |
| MA | 77 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
