# The Negro Motorist Green Book: 1938 - Green Book Atlas (First Multi-Region Expansion Edition)

**TL;DR:** Published in 1938 (36 pages), expanding beyond the New York metropolitan area to 1,013 listings across 21 states and the District of Columbia through collaboration with the U.S. Postal Service letter-carrier network. Total geocoded establishments: *1,013* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/bdc16d00-1a74-0132-a071-58d385a7bbd0)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1938_mymaps_all.kml`
- `listings.csv` and `listings.json` - structured dataset (1,013 records)
- [NYPL original PDF (5.9 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1938.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 36 pages
- `ocr/` - 36 page-level `.txt` and 36 `.hocr` OCR files

### Supplemental files
- `supplemental/GreenBook_city_withGeo_37-39.csv`
- `supplemental/GreenBook_city_noGeo_37-39.csv`
- `supplemental/GreenBook_city_noGeo_37-39.ods`
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Lodging: Hotels & Motels | 330 |
| Lodging: Tourist Homes | 204 |
| Nightlife: Taverns & Clubs | 173 |
| Personal Care: Barber, Beauty & Tailors | 145 |
| Dining: Restaurants | 104 |
| Auto: Gas, Garages & Transport | 38 |
| Retail, Services & Other | 19 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 343 |
| NJ | 172 |
| PA | 108 |
| VA | 53 |
| GA | 36 |
| CT | 30 |
| NC | 28 |
| AL | 25 |
| SC | 25 |
| OH | 24 |
| FL | 21 |
| MD | 21 |
| TN | 20 |
| DC | 19 |
| IL | 19 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
