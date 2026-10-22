# The Negro Motorist Green Book: 1937 - Green Book Atlas (Earliest Surviving Edition)

**TL;DR:** Published in 1937 by Victor H. Green in New York City (16 pages, price 25 cents). While the 1936 first edition has no known surviving copies in public archives, this 1937 volume is the earliest extant edition, covering the New York metropolitan area, Westchester, and northern New Jersey. Total geocoded establishments: *86* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive](https://digitalcollections.nypl.org/items/88223f10-8936-0132-0483-58d385a7b928)).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
  - `mymaps/greenbook_1937_mymaps_all.kml`
- `listings.csv` and `listings.json` - structured dataset (86 records)
- [NYPL original PDF (4.3 MB)](https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/1937.pdf) - digitized PDF hosted by NYPL Labs (CC0 1.0)
- `full_text.txt` - concatenated OCR text across all 15 pages
- `ocr/` - 15 page-level `.txt` and 15 `.hocr` OCR files

### Supplemental files
- `supplemental/GreenBook1937.csv`
- `supplemental/GreenBook1937.ods`
- `supplemental/GreenBook1937Notes.md`
- `supplemental/GreenBook_city_withGeo_37-39.csv`
- `supplemental/GreenBook_city_noGeo_37-39.csv`
- `supplemental/GreenBook_city_noGeo_37-39.ods`
- `supplemental/archival_metadata.json`

## Breakdown by category

| Category | Listings |
| :--- | ---: |
| Dining: Restaurants | 37 |
| Retail, Services & Other | 18 |
| Auto: Gas, Garages & Transport | 18 |
| Personal Care: Barber, Beauty & Tailors | 8 |
| Nightlife: Taverns & Clubs | 5 |

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
| NY | 84 |
| NJ | 2 |

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
