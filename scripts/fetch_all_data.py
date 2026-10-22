#!/usr/bin/env python3
# Copyright 2026 The Green Book Atlas Authors.
# SPDX-License-Identifier: Apache-2.0
"""Fetches and organizes archival and spatial Green Book data for all 24 surviving editions (1937-1967).

Includes:
  - All 21 complete NYPL Schomburg Center CC0 1.0 public-domain volumes (PDFs + page-level .txt & .hocr OCR)
  - All 24 geocoded editions from the University of Redlands / Library of Congress / NYPL collection (68,330 total establishments)
  - Open-licensed supplemental datasets from NYPL Labs (CC0 1.0), University of South Carolina (CC0 1.0), and Claudia Engel / Stanford University (CC BY-SA 4.0)
  - Explicitly excludes third-party NonCommercial/NoDerivatives (CC BY-NC-ND) uploads
"""

import csv
import json
import os
import shutil
import urllib.parse
import urllib.request

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRATCH_REPOS = os.environ.get(
    "GREENBOOK_SCRATCH_REPOS", os.path.join(BASE_DIR, ".scratch_repos")
)

ARCGIS_QUERY_URL = (
    "https://services.arcgis.com/o6oETlrWetREI1A2/arcgis/rest/services/"
    "GreenbookLocations1937_1966/FeatureServer/0/query"
)

EDITIONS = [
    {
        "dir": "1937",
        "arcgis_year": 1937,
        "nypl_dir": "1937",
        "title": "The Negro Motorist Green Book: 1937",
        "role": "Earliest Surviving Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/88223f10-8936-0132-0483-58d385a7b928",
        "historical_context": (
            "Published in 1937 by Victor H. Green in New York City (16 pages, price 25 cents). "
            "While the 1936 first edition has no known surviving copies in public archives, "
            "this 1937 volume is the earliest extant edition, covering the New York metropolitan "
            "area, Westchester, and northern New Jersey."
        ),
    },
    {
        "dir": "1938",
        "arcgis_year": 1938,
        "nypl_dir": "1938",
        "title": "The Negro Motorist Green Book: 1938",
        "role": "First Multi-Region Expansion Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/bdc16d00-1a74-0132-a071-58d385a7bbd0",
        "historical_context": (
            "Published in 1938 (36 pages), expanding beyond the New York metropolitan area to "
            "1,013 listings across 21 states and the District of Columbia through collaboration "
            "with the U.S. Postal Service letter-carrier network."
        ),
    },
    {
        "dir": "1939",
        "arcgis_year": 1939,
        "nypl_dir": "1939",
        "title": "The Negro Motorist Green Book: 1939",
        "role": "1939 New York World's Fair Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/2dacae50-1a75-0132-d154-58d385a7bbd0",
        "historical_context": (
            "Published in 1939 (52 pages) with a special New York World's Fair supplement and "
            "nearly double the previous year's coverage (2,006 geocoded establishments)."
        ),
    },
    {
        "dir": "1940",
        "arcgis_year": 1940,
        "nypl_dir": "1940",
        "title": "The Negro Motorist Green Book: 1940",
        "role": "Pre-WWII National Expansion Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/dc858eb0-8936-0132-128f-58d385a7bbd0",
        "historical_context": (
            "Published in 1940 (52 pages), demonstrating rapid national expansion across 43 states "
            "and the District of Columbia before World War II."
        ),
    },
    {
        "dir": "1941",
        "arcgis_year": 1941,
        "nypl_dir": "1941",
        "title": "The Negro Motorist Green Book: 1941",
        "role": "Final Pre-WWII Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/47e874a0-1a74-0132-a7fb-58d385a7bbd0",
        "historical_context": (
            "Published in 1941 (52 pages) with sponsorship from Esso Standard Oil marketer "
            "James A. Jackson ('The Esso Man'), just before wartime gasoline and paper rationing "
            "suspended annual publication from 1942 through 1945."
        ),
    },
    {
        "dir": "1946",
        "arcgis_year": 1946,
        "nypl_dir": None,
        "title": "The Negro Motorist Green Book: 1946",
        "role": "Post-WWII Resumption Edition",
        "nypl_collection_url": "https://www.loc.gov/item/2016298176/",
        "historical_context": (
            "Published in 1946 as the first post-World War II edition following the 1942-1945 "
            "wartime hiatus, introducing the motto 'Carry your Green Book with you... you may need it' "
            "and expanding to 3,335 listings. Preserved in the Library of Congress collection."
        ),
    },
    {
        "dir": "1947",
        "arcgis_year": 1947,
        "nypl_dir": "1947",
        "title": "The Negro Motorist Green Book: 1947",
        "role": "Post-WWII Boom & Vacation Reservation Service Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/2bc77d90-8937-0132-c56c-58d385a7b928",
        "historical_context": (
            "Published in 1947 (84 pages) as post-war automobile travel surged and Victor Green "
            "launched his Vacation Reservation Service in Harlem."
        ),
    },
    {
        "dir": "1948",
        "arcgis_year": 1948,
        "nypl_dir": "1948",
        "title": "The Negro Motorist Green Book: 1948",
        "role": "United States & Alaska Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/3a67a6d0-1a73-0132-91e7-58d385a7bbd0",
        "historical_context": (
            "Subtitled 'A Classified Motorist & Tourist Guide Covering the United States & Alaska' "
            "(84 pages, 3,912 geocoded listings)."
        ),
    },
    {
        "dir": "1949",
        "arcgis_year": 1949,
        "nypl_dir": "1949",
        "title": "The Negro Motorist Green Book: 1949",
        "role": "First International Travel Guide Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/092a3710-1a73-0132-fdcf-58d385a7bbd0",
        "historical_context": (
            "Subtitled 'An International Travel Guide' (84 pages, 3,936 geocoded listings), "
            "containing Victor H. Green's famous foreword: 'There will be a day sometime in the "
            "near future when this guide will not have to be published.'"
        ),
    },
    {
        "dir": "1950",
        "arcgis_year": 1950,
        "nypl_dir": "1950",
        "title": "The Negro Motorist Green Book: 1950",
        "role": "Mid-Century Peak Listings Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/96738510-8937-0132-5591-58d385a7b928",
        "historical_context": (
            "Published in 1950 (92 pages), representing the highest total business listing count "
            "(4,315 geocoded locations) across the United States, Canada, Mexico, and Bermuda."
        ),
    },
    {
        "dir": "1951",
        "arcgis_year": 1951,
        "nypl_dir": "1951",
        "title": "The Negro Motorist Green Book: 1951 Railroad Edition",
        "role": "1951 Railroad & International Travel Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/6c5ccbe0-1a73-0132-b81d-58d385a7bbd0",
        "historical_context": (
            "Published in 1951 (84 pages, 4,229 geocoded listings), incorporating rail travel "
            "features alongside motorist accommodations across North America."
        ),
    },
    {
        "dir": "1952",
        "arcgis_year": 1952,
        "nypl_dir": "1952",
        "title": "The Negro Travelers' Green Book: 1952",
        "role": "First 'Negro Travelers' Title Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/0387d5f0-1a72-0132-c0b2-58d385a7bbd0",
        "historical_context": (
            "Published in 1952 (84 pages, 4,161 geocoded listings), marking the official title "
            "transition from 'The Negro Motorist Green Book' to 'The Negro Travelers' Green Book'."
        ),
    },
    {
        "dir": "1953",
        "arcgis_year": 1953,
        "nypl_dir": "1953",
        "title": "The Negro Travelers' Green Book: 1953",
        "role": "1953 Regular Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/d440c0b0-1a71-0132-7f48-58d385a7bbd0",
        "historical_context": (
            "Published in 1953 (84 pages, 3,991 geocoded listings), documenting nearly four "
            "thousand Black-friendly hotels, tourist homes, restaurants, and service stations."
        ),
    },
    {
        "dir": "1954",
        "arcgis_year": 1954,
        "nypl_dir": "1954",
        "title": "The Negro Travelers' Green Book: 1954",
        "role": "Brown v. Board of Education Era Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/40a8efd0-1a71-0132-336d-58d385a7bbd0",
        "historical_context": (
            "Subtitled 'The Guide to Travel & Vacations' (84 pages, 4,071 geocoded listings), "
            "published in the year of the landmark Supreme Court decision Brown v. Board of Education."
        ),
    },
    {
        "dir": "1955",
        "arcgis_year": 1955,
        "nypl_dir": "1955",
        "title": "The Negro Travelers' Green Book: 1955 International Edition",
        "role": "1955 Airline & International Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/7d566930-1a76-0132-4e16-58d385a7bbd0",
        "historical_context": (
            "Published in 1955 (84 pages, 3,979 geocoded listings), featuring expanded air travel "
            "and international destination listings."
        ),
    },
    {
        "dir": "1956",
        "arcgis_year": 1956,
        "nypl_dir": "1956",
        "title": "The Negro Travelers' Green Book: 1956",
        "role": "Interstate Highway Act & 20th Anniversary Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/3ef663c0-8938-0132-e036-58d385a7bbd0",
        "historical_context": (
            "Published in Spring 1956 (84 pages, 1,942 geocoded listings), streamlining directory "
            "categories to focus on lodging, dining, and service stations during the birth of the "
            "Interstate Highway System."
        ),
    },
    {
        "dir": "1957",
        "arcgis_year": 1957,
        "nypl_dir": "1957",
        "title": "The Negro Travelers' Green Book: 1957",
        "role": "Civil Rights Act of 1957 Era Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/639fc110-1a75-0132-d5bf-58d385a7bbd0",
        "historical_context": (
            "Published in 1957 (84 pages, 2,113 geocoded listings), providing coast-to-coast "
            "lodging and dining listings during the Little Rock Nine and Civil Rights Act of 1957 era."
        ),
    },
    {
        "dir": "1958",
        "arcgis_year": 1958,
        "nypl_dir": None,
        "title": "The Negro Travelers' Green Book: 1958",
        "role": "1958 Pocket-Format Transition Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/b4affe50-7ca3-013f-af86-0242ac110002",
        "historical_context": (
            "Published in 1958 (2,147 geocoded listings), digitized by the NYPL Schomburg Center "
            "(item b4affe50-7ca3-013f-af86-0242ac110002) following the 2016 bulk OCR release."
        ),
    },
    {
        "dir": "1959",
        "arcgis_year": 1959,
        "nypl_dir": "1959",
        "title": "The Negro Travelers' Green Book: 1959",
        "role": "Final Edition Under Victor H. Green's Lifetime",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/8bf60a70-1a75-0132-d6c0-58d385a7bbd0",
        "historical_context": (
            "Published in 1959 (88 pages, 2,118 geocoded listings) in compact pocket format "
            "shortly before founder Victor Hugo Green's passing in October 1960."
        ),
    },
    {
        "dir": "1960",
        "arcgis_year": 1960,
        "nypl_dir": "1960",
        "title": "The Travelers' Green Book: 1960",
        "role": "Sit-In Movement Era Edition (Alma D. Green, Publisher)",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/1f0653d0-1a74-0132-69ff-58d385a7bbd0",
        "historical_context": (
            "Published in 1960 (132 pocket pages, 2,205 geocoded listings), dropping 'Negro' from "
            "the cover title as Alma Duke Green assumed leadership as publisher."
        ),
    },
    {
        "dir": "1961",
        "arcgis_year": 1961,
        "nypl_dir": "1961",
        "title": "The Travelers' Green Book: 1961",
        "role": "Freedom Rides Era Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/dcf5d950-1a73-0132-6a76-58d385a7bbd0",
        "historical_context": (
            "Published in 1961 (132 pocket pages, 2,321 geocoded listings) during the year of "
            "the CORE/SNCC Freedom Rides desegregating interstate bus terminals."
        ),
    },
    {
        "dir": "1962",
        "arcgis_year": 1962,
        "nypl_dir": "1962",
        "title": "Travelers' Green Book: 1962",
        "role": "1962 Guide for Travel & Vacations",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/9ab2e8f0-1a73-0132-95bd-58d385a7bbd0",
        "historical_context": (
            "Published in 1962 (130 pocket pages, 2,250 geocoded listings) under Alma D. Green, "
            "covering U.S. states, Canada, the Caribbean, and Western Europe."
        ),
    },
    {
        "dir": "1963-64",
        "arcgis_year": 1963,
        "nypl_dir": "1963-64",
        "title": "Travelers' Green Book: 1963-64 International Edition",
        "role": "March on Washington & Civil Rights Act Eve Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/6fa5be40-8939-0132-9c3c-58d385a7b928",
        "historical_context": (
            "Published in 1963 (113 digitized pages, 3,202 geocoded listings) on the eve of the "
            "Civil Rights Act of 1964, featuring an article on the 1963–1965 Centennial of the "
            "Emancipation Proclamation."
        ),
    },
    {
        "dir": "1966-67",
        "arcgis_year": 1966,
        "nypl_dir": None,
        "title": "Travelers' Green Book: 1966-67 International Edition",
        "role": "Latest & Final Published Edition",
        "nypl_collection_url": "https://digitalcollections.nypl.org/items/27516920-8308-0132-5063-58d385a7bbd0",
        "historical_context": (
            "Subtitled 'For Vacation Without Aggravation' (3,300 geocoded listings), the 1966-67 "
            "International Edition was the final issue published after the Civil Rights Act of 1964 "
            "outlawed racial discrimination in public accommodations."
        ),
    },
]

CENGEL_SUPPLEMENTAL_MAP = {
    "1937": [
        "addresses/GreenBook1937.csv",
        "addresses/GreenBook1937.ods",
        "addresses/GreenBook1937Notes.md",
        "city_aggregate/GreenBook_city_withGeo_37-39.csv",
        "city_aggregate/GreenBook_city_noGeo_37-39.csv",
        "city_aggregate/GreenBook_city_noGeo_37-39.ods",
    ],
    "1938": [
        "city_aggregate/GreenBook_city_withGeo_37-39.csv",
        "city_aggregate/GreenBook_city_noGeo_37-39.csv",
        "city_aggregate/GreenBook_city_noGeo_37-39.ods",
    ],
    "1939": [
        "city_aggregate/GreenBook_city_withGeo_37-39.csv",
        "city_aggregate/GreenBook_city_noGeo_37-39.csv",
        "city_aggregate/GreenBook_city_noGeo_37-39.ods",
    ],
    "1940": [
        "city_aggregate/GreenBook_city_noGeo_40.csv",
        "city_aggregate/GreenBook_city_noGeo_40.ods",
    ],
    "1941": [
        "city_aggregate/GreenBook_city_noGeo_41.csv",
        "city_aggregate/GreenBook_city_noGeo_41.ods",
    ],
    "1947": [
        "addresses/GreenBook1947Notes.md",
        "addresses/GreenBook1947_inProcess.ods",
        "city_aggregate/GreenBook_city_noGeo_47.csv",
        "city_aggregate/GreenBook_city_noGeo_47.ods",
    ],
    "1948": [
        "city_aggregate/GreenBook_city_noGeo_48.csv",
        "city_aggregate/GreenBook_city_noGeo_48.ods",
    ],
    "1949": [
        "city_aggregate/GreenBook_city_noGeo_49.csv",
        "city_aggregate/GreenBook_city_noGeo_49.ods",
    ],
    "1950": [
        "city_aggregate/GreenBook_city_noGeo_50.csv",
        "city_aggregate/GreenBook_city_noGeo_50.ods",
    ],
    "1951": [
        "city_aggregate/GreenBook_city_noGeo_51.csv",
        "city_aggregate/GreenBook_city_noGeo_51.ods",
    ],
    "1952": [
        "city_aggregate/GreenBook_city_noGeo_52.csv",
        "city_aggregate/GreenBook_city_noGeo_52.ods",
    ],
}


def classify_category(btype: str) -> str:
    """Normalizes the 82 raw BusinessType strings into 7 clear map categories."""
    if not btype:
        return "Retail, Services & Other"
    t = btype.strip().lower()
    if any(k in t for k in ["tourist home", "guest house", "private residence", "lodging", "ymca", "ywca", "y.m.c.a", "y.w.c.a"]):
        return "Lodging: Tourist Homes"
    if any(k in t for k in ["hotel", "motel", "inn", "resort", "cabin", "cottage", "court", "camp", "ranch", "lodge"]):
        return "Lodging: Hotels & Motels"
    if any(k in t for k in ["restaurant", "dining", "cafe", "tea room", "barbecue", "bbq", "lunch", "eat", "grille", "grill", "chicken", "drive-in", "drive in", "snack", "coffee", "chili", "pizzeria", "chop suey"]):
        return "Dining: Restaurants"
    if any(k in t for k in ["tavern", "night club", "nightclub", "bar ", "lounge", "liquor", "wine", "road house", "roadhouse", "club", "cocktail", "tap room", "beer"]):
        return "Nightlife: Taverns & Clubs"
    if any(k in t for k in ["service station", "garage", "auto", "gas", "battery", "batteries", "tire", "taxi", "cab", "car ", "motor", "filling station", "body shop", "repair", "chauffeur", "parking", "trailer"]):
        return "Auto: Gas, Garages & Transport"
    if any(k in t for k in ["barber", "beauty", "hair", "tailor", "cleaner", "valet", "hatter", "laundry", "pressing", "shoe"]):
        return "Personal Care: Barber, Beauty & Tailors"
    return "Retail, Services & Other"


def fetch_arcgis_year(year: int) -> list[dict]:
    """Paginates through the University of Redlands ArcGIS FeatureServer for a given year."""
    records = []
    offset = 0
    batch_size = 1000
    while True:
        params = {
            "where": f"Year = {year}",
            "outFields": "*",
            "orderByFields": "OBJECTID ASC",
            "resultOffset": str(offset),
            "resultRecordCount": str(batch_size),
            "outSR": "4326",
            "f": "json",
        }
        url = f"{ARCGIS_QUERY_URL}?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        features = data.get("features", [])
        if not features:
            break
        for feat in features:
            attr = feat.get("attributes", {})
            geom = feat.get("geometry") or {}
            lon = attr.get("X") if attr.get("X") is not None else geom.get("x")
            lat = attr.get("Y") if attr.get("Y") is not None else geom.get("y")
            btype = (attr.get("BusinessType") or "Unspecified").strip()
            records.append({
                "id": attr.get("OBJECTID"),
                "year": attr.get("Year"),
                "business_name": (attr.get("BusinessName") or "Unnamed Establishment").strip(),
                "business_type": btype,
                "category_group": classify_category(btype),
                "owner_name": (attr.get("OwnerName") or "").strip(),
                "owner_gender": (attr.get("OwnerGender") or "").strip(),
                "address": (attr.get("Address") or "").strip(),
                "address2": (attr.get("Address2") or "").strip(),
                "city": (attr.get("City") or "").strip(),
                "state": (attr.get("State") or "").strip(),
                "country": (attr.get("Country") or "").strip(),
                "latitude": float(lat) if lat is not None else None,
                "longitude": float(lon) if lon is not None else None,
                "source_type": (attr.get("SourceType") or "").strip(),
                "book_notes": (attr.get("BookNotes") or "").strip(),
                "data_editor_notes": (attr.get("DataEditorNotes") or "").strip(),
                "info_link": (attr.get("InfoLink") or "").strip(),
                "photo_link": (attr.get("PhotoLink") or "").strip(),
            })
        if len(features) < batch_size:
            break
        offset += batch_size
    return records


def copy_nypl_assets(edition: dict, ed_path: str) -> dict:
    """Copies NYPL .txt and .hocr files into the edition directory, creates full_text.txt, and records the NYPL PDF URL."""
    nypl_dir = edition["nypl_dir"]
    stats = {"pdf_file": None, "pdf_url": None, "pdf_bytes": 0, "txt_count": 0, "hocr_count": 0, "pages": []}
    if not nypl_dir:
        return stats

    gb_repo = os.path.join(SCRATCH_REPOS, "greenbooks")
    pdf_src = os.path.join(gb_repo, f"{nypl_dir}.pdf")
    pdf_dst = os.path.join(ed_path, f"{nypl_dir}.pdf")
    if os.path.exists(pdf_dst):
        os.remove(pdf_dst)
    if os.path.exists(pdf_src):
        stats["pdf_url"] = f"https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/{nypl_dir}.pdf"
        stats["pdf_bytes"] = os.path.getsize(pdf_src)

    src_ocr_dir = os.path.join(gb_repo, nypl_dir)
    if os.path.isdir(src_ocr_dir):
        dst_ocr_dir = os.path.join(ed_path, "ocr")
        os.makedirs(dst_ocr_dir, exist_ok=True)
        files = sorted(os.listdir(src_ocr_dir))
        full_text_parts = []
        for fname in files:
            src_f = os.path.join(src_ocr_dir, fname)
            if not os.path.isfile(src_f):
                continue
            dst_f = os.path.join(dst_ocr_dir, fname)
            shutil.copy2(src_f, dst_f)
            if fname.endswith(".txt"):
                stats["txt_count"] += 1
                capture_id = fname.replace("g.txt", "")
                stats["pages"].append({
                    "page_index": stats["txt_count"],
                    "capture_id": capture_id,
                    "txt_file": f"ocr/{fname}",
                    "hocr_file": f"ocr/{capture_id}g.hocr",
                    "nypl_image_url": f"https://images.nypl.org/index.php?id={capture_id}&t=w",
                    "nypl_digital_collections_url": f"https://digitalcollections.nypl.org/items/image_id/{capture_id}",
                })
                with open(src_f, "r", encoding="utf-8", errors="replace") as tf:
                    page_text = tf.read().strip()
                full_text_parts.append(
                    f"========================================================================\n"
                    f"PAGE {stats['txt_count']} (NYPL Capture ID: {capture_id})\n"
                    f"Image URL: https://images.nypl.org/index.php?id={capture_id}&t=w\n"
                    f"========================================================================\n"
                    f"{page_text}\n"
                )
            elif fname.endswith(".hocr"):
                stats["hocr_count"] += 1

        if full_text_parts:
            with open(os.path.join(ed_path, "full_text.txt"), "w", encoding="utf-8") as ftf:
                ftf.write("\n".join(full_text_parts))

    return stats


def copy_supplemental_assets(edition: dict, ed_path: str) -> list[str]:
    """Copies edition-specific supplemental datasets from NYPL Labs, UofSC, and Stanford."""
    ed_dir = edition["dir"]
    supp_dir = os.path.join(ed_path, "supplemental")
    os.makedirs(supp_dir, exist_ok=True)
    copied = []

    gb_repo = os.path.join(SCRATCH_REPOS, "greenbooks")
    gb_map_repo = os.path.join(SCRATCH_REPOS, "greenbook-map")
    cengel_repo = os.path.join(SCRATCH_REPOS, "cengel-greenbook")

    for rel in CENGEL_SUPPLEMENTAL_MAP.get(ed_dir, []):
        src = os.path.join(cengel_repo, rel)
        if os.path.exists(src):
            fname = os.path.basename(rel)
            shutil.copy2(src, os.path.join(supp_dir, fname))
            copied.append(f"supplemental/{fname}")

    if ed_dir == "1947":
        src_geojson = os.path.join(gb_repo, "geojson/1947.geojson")
        if os.path.exists(src_geojson):
            shutil.copy2(src_geojson, os.path.join(supp_dir, "nypl_labs_1947.geojson"))
            copied.append("supplemental/nypl_labs_1947.geojson")
        src_mapjson = os.path.join(gb_map_repo, "data/greenbook_1947.json")
        if os.path.exists(src_mapjson):
            shutil.copy2(src_mapjson, os.path.join(supp_dir, "nypl_map_greenbook_1947.json"))
            copied.append("supplemental/nypl_map_greenbook_1947.json")

    elif ed_dir == "1956":
        src_mapjson = os.path.join(gb_map_repo, "data/greenbook_1956.json")
        if os.path.exists(src_mapjson):
            shutil.copy2(src_mapjson, os.path.join(supp_dir, "uofsc_nypl_greenbook_1956.json"))
            copied.append("supplemental/uofsc_nypl_greenbook_1956.json")
        for idx in [0, 500, 1000, 1500]:
            src_raw = os.path.join(gb_map_repo, f"scripts/data/library_sc_edu_greenbookmap_{idx}.json")
            if os.path.exists(src_raw):
                fname = os.path.basename(src_raw)
                shutil.copy2(src_raw, os.path.join(supp_dir, fname))
                copied.append(f"supplemental/{fname}")

    # Write archival_metadata.json for all editions
    catalog_meta = {
        "edition": edition["title"],
        "year": edition["arcgis_year"],
        "role": edition["role"],
        "archive_url": edition["nypl_collection_url"],
        "loc_catalog_url": "https://www.loc.gov/item/2016298176/",
        "nypl_cc0_release_included": bool(edition["nypl_dir"]),
        "license_summary": (
            "NYPL CC0 1.0 Universal Public Domain Dedication (PDF/OCR) + "
            "University of Redlands / Library of Congress public educational release (geocoded directory listings)"
            if edition["nypl_dir"]
            else "U.S. Public Domain / Uncopyrightable Factual Directory Listings (University of Redlands & Library of Congress / NYPL Digital Collections)"
        ),
    }
    if ed_dir == "1941":
        catalog_meta["smithsonian_nmaahc_url"] = "https://www.si.edu/object/nmaahc_2015.97.42"
        catalog_meta["wikimedia_commons_nmaahc_pdf"] = (
            "https://commons.wikimedia.org/wiki/File:The_Negro_Motorist_Green_Book_1941_(NMAAHC).pdf"
        )
    with open(os.path.join(supp_dir, "archival_metadata.json"), "w", encoding="utf-8") as mf:
        json.dump(catalog_meta, mf, indent=2)
    copied.append("supplemental/archival_metadata.json")

    return copied


def main():
    summary = []
    csv_fields = [
        "id",
        "year",
        "business_name",
        "business_type",
        "category_group",
        "owner_name",
        "owner_gender",
        "address",
        "address2",
        "city",
        "state",
        "country",
        "latitude",
        "longitude",
        "source_type",
        "book_notes",
        "data_editor_notes",
        "info_link",
        "photo_link",
    ]

    for ed in EDITIONS:
        ed_dir = ed["dir"]
        ed_path = os.path.join(BASE_DIR, ed_dir)
        os.makedirs(ed_path, exist_ok=True)
        print(f"[*] Processing edition {ed_dir} (ArcGIS Year={ed['arcgis_year']})...")

        records = fetch_arcgis_year(ed["arcgis_year"])
        print(f"    -> Fetched {len(records)} geocoded records from ArcGIS FeatureServer.")

        # Write listings.csv
        csv_path = os.path.join(ed_path, "listings.csv")
        with open(csv_path, "w", encoding="utf-8", newline="") as cf:
            writer = csv.DictWriter(cf, fieldnames=csv_fields)
            writer.writeheader()
            for r in records:
                writer.writerow(r)

        # Copy NYPL PDF, OCR .txt, and .hocr files
        nypl_stats = copy_nypl_assets(ed, ed_path)
        print(
            f"    -> NYPL assets: PDF={nypl_stats['pdf_file']} ({nypl_stats['pdf_bytes']} bytes), "
            f"txt={nypl_stats['txt_count']}, hocr={nypl_stats['hocr_count']}"
        )

        # Copy supplemental datasets
        supp_files = copy_supplemental_assets(ed, ed_path)
        print(f"    -> Supplemental files: {len(supp_files)}")

        # Compute breakdowns
        by_category = {}
        by_state = {}
        by_country = {}
        valid_coords = 0
        for r in records:
            cat = r["category_group"]
            by_category[cat] = by_category.get(cat, 0) + 1
            st = r["state"] or r["country"] or "Unspecified"
            by_state[st] = by_state.get(st, 0) + 1
            ctry = r["country"] or "United States"
            by_country[ctry] = by_country.get(ctry, 0) + 1
            if r["latitude"] is not None and r["longitude"] is not None:
                valid_coords += 1

        ed_payload = {
            "edition": ed_dir,
            "arcgis_year": ed["arcgis_year"],
            "title": ed["title"],
            "role": ed["role"],
            "nypl_collection_url": ed["nypl_collection_url"],
            "historical_context": ed["historical_context"],
            "total_records": len(records),
            "valid_coordinates_count": valid_coords,
            "category_counts": dict(sorted(by_category.items(), key=lambda x: -x[1])),
            "state_counts": dict(sorted(by_state.items(), key=lambda x: -x[1])),
            "country_counts": dict(sorted(by_country.items(), key=lambda x: -x[1])),
            "nypl_archival_assets": nypl_stats,
            "supplemental_files": supp_files,
            "records": records,
        }
        with open(os.path.join(ed_path, "listings.json"), "w", encoding="utf-8") as jf:
            json.dump(ed_payload, jf, indent=2)

        summary.append({
            "edition": ed_dir,
            "title": ed["title"],
            "role": ed["role"],
            "total_records": len(records),
            "valid_coordinates_count": valid_coords,
            "pdf_file": nypl_stats["pdf_file"],
            "pdf_bytes": nypl_stats["pdf_bytes"],
            "txt_count": nypl_stats["txt_count"],
            "hocr_count": nypl_stats["hocr_count"],
            "supplemental_files": supp_files,
        })

    with open(os.path.join(BASE_DIR, "editions_summary.json"), "w", encoding="utf-8") as sf:
        json.dump(summary, sf, indent=2)
    print(f"[+] Completed fetching and organizing all {len(EDITIONS)} editions.")


if __name__ == "__main__":
    main()
