# Licenses, attributions, and excluded datasets

**TL;DR:** Every file in **Green Book Atlas** ([greenbookatlas.org](https://greenbookatlas.org)) is cleared for public release under public-domain (U.S. public domain or CC0 1.0) or permissive open-access terms (public academic release, CC BY-SA 4.0 for isolated supplemental tables, and BSD 2-Clause for web map libraries). Datasets with non-commercial or no-derivatives restrictions are excluded.

## 1. Original historical volumes (24 editions, 1937-1967)
- *Work*: *The Negro Motorist Green Book* (1937-1951), *The Negro Travelers' Green Book* (1952-1959), and *Travelers' Green Book* (1960-1966/67).
- *Creator and publisher*: Victor H. Green & Co. (Victor Hugo Green, Alma Duke Green, Novera C. Dashiell, Langley Waller), Harlem, New York City.
- *Legal status*:
  - *1937-1963/64 editions (23 editions)*: In the United States public domain (published prior to January 1, 1964 without copyright renewal, as verified by The New York Public Library).
  - *1966-67 edition (1 edition)*: We include the non-copyrightable factual directory listings. Full-page image scans for 1966-67 are excluded from this repository.

## 2. Digitized volumes, OCR text, hOCR, and 1947 GeoJSON - NYPL (CC0 1.0)
- *Source*: Schomburg Center for Research in Black Culture (Jean Blackwell Hutson Research and Reference Division), The New York Public Library, and NYPL Labs (Brian Foo).
- *Repositories*: <https://github.com/NYPL-publicdomain/greenbooks>, <https://github.com/NYPL-publicdomain/greenbook-map>, and <https://digitalcollections.nypl.org/collections/the-green-book>.
- *Files covered*:
  - 1,734 page-level OCR files (`<edition>/ocr/*.txt`, `<edition>/ocr/*.hocr`, and `<edition>/full_text.txt` across `1937`-`1941`, `1947`-`1957`, `1959`-`1962`, and `1963-64`)
  - `1947/supplemental/nypl_labs_1947.geojson` and `1947/supplemental/nypl_map_greenbook_1947.json`
  - External links to NYPL's 21 CC0 PDFs (`https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/<edition>.pdf`)
- *License*: [CC0 1.0 Universal Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).

## 3. Geocoded establishments dataset (24 editions, 68,330 sites) - University of Redlands & Library of Congress
- *Source*: Center for Spatial Studies, University of Redlands (*Mapping the Green Books*, `GreenbookLocations1937_1966`, curated by Lisa Benvenuti et al.) and the Library of Congress (<https://www.loc.gov/item/2016298176/>).
- *Files covered*: `<edition>/listings.csv`, `<edition>/listings.json`, `<edition>/overlay.kml`, `<edition>/overlay.kmz`, `<edition>/overlay.geojson`, and `<edition>/mymaps/*.kml` across all 24 editions.
- *License*: Public educational and research release with no license restrictions (`access: "public"`, `licenseInfo: "None"`).

## 4. 1956 Spring edition dataset - University of South Carolina Libraries (CC0 1.0)
- *Source*: University of South Carolina Libraries Digital Collections (<https://digital.library.sc.edu/collections/the-negro-travelers-green-book-1956/>), structured for web mapping by NYPL Labs.
- *Files covered*: `1956/supplemental/uofsc_nypl_greenbook_1956.json` and `1956/supplemental/library_sc_edu_greenbookmap_*.json`.
- *License*: Released via `NYPL-publicdomain/greenbook-map` under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

## 5. Supplemental 1937-1952 tables and notes - Claudia Engel / Stanford University (CC BY-SA 4.0)
- *Source*: Claudia Engel, *GreenBook: Addresses from the Negro Motorist Green Book* (<https://github.com/cengel/GreenBook>).
- *Files covered*: `GreenBook*` files inside `<edition>/supplemental/` for 11 editions (`1937`-`1941`, `1946`-`1950`, and `1952`).
- *License*: [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
  - NB: Only the `GreenBook*` files in `<edition>/supplemental/` derive from `cengel/GreenBook`. The primary `listings.*` and `overlay.*` files in each edition directory derive independently from the University of Redlands and NYPL public-domain sources and are not subject to ShareAlike requirements.

## 6. Mapping software and basemap providers
- *Leaflet 1.9.4 and Leaflet.heat 0.2.0*: Copyright (c) 2010-2023 Volodymyr Agafonkin. Licensed under the [BSD 2-Clause License](https://opensource.org/licenses/BSD-2-Clause).
- *Basemap tiles*: Google Maps (&copy; Google, per [Google Maps Terms of Service](https://www.google.com/help/terms_maps/)); OpenStreetMap (&copy; [OpenStreetMap contributors](https://www.openstreetmap.org/copyright), ODbL); CARTO (&copy; [CARTO](https://carto.com/attributions), CC BY 3.0).

## 7. Excluded datasets

- The 1938 and 1940 versions available on Internet Archive prohibit derivative works. As such, we use NYPL's public-domain scans instead.
- NYPL does not provide 1966-1967 scans because they are still under copyright. We include the non-copyrightable factual directory listings.
