#!/usr/bin/env python3
# Copyright 2026 The Green Book Atlas Authors.
# SPDX-License-Identifier: Apache-2.0
"""Generates KML, KMZ, My Maps split KMLs, GeoJSON, interactive HTML maps, and READMEs."""

import html
import json
import math
import os
import re
import shutil
import zipfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OVERLAYS_DIR = os.path.join(BASE_DIR, "overlays")

EDITION_DIRS = [
    "1937",
    "1938",
    "1939",
    "1940",
    "1941",
    "1946",
    "1947",
    "1948",
    "1949",
    "1950",
    "1951",
    "1952",
    "1953",
    "1954",
    "1955",
    "1956",
    "1957",
    "1958",
    "1959",
    "1960",
    "1961",
    "1962",
    "1963-64",
    "1966-67",
]

CATEGORY_STYLES = {
    "Lodging: Tourist Homes": {
        "id": "cat_tourist_home",
        "hex": "#2E7D32",
        "kml_color": "ff327d2e",  # AABBGGRR
        "icon": "http://maps.google.com/mapfiles/kml/paddle/grn-circle.png",
        "short": "Tourist Homes",
    },
    "Lodging: Hotels & Motels": {
        "id": "cat_hotel_motel",
        "hex": "#1565C0",
        "kml_color": "ffc06515",
        "icon": "http://maps.google.com/mapfiles/kml/paddle/blu-Blank.png",
        "short": "Hotels & Motels",
    },
    "Dining: Restaurants": {
        "id": "cat_restaurant",
        "hex": "#EF6C00",
        "kml_color": "ff006cef",
        "icon": "http://maps.google.com/mapfiles/kml/paddle/orange-circle.png",
        "short": "Restaurants",
    },
    "Nightlife: Taverns & Clubs": {
        "id": "cat_nightlife",
        "hex": "#8E24AA",
        "kml_color": "ffaa248e",
        "icon": "http://maps.google.com/mapfiles/kml/paddle/purple-stars.png",
        "short": "Taverns & Nightlife",
    },
    "Auto: Gas, Garages & Transport": {
        "id": "cat_auto",
        "hex": "#C62828",
        "kml_color": "ff2828c6",
        "icon": "http://maps.google.com/mapfiles/kml/paddle/red-diamond.png",
        "short": "Gas & Automotive",
    },
    "Personal Care: Barber, Beauty & Tailors": {
        "id": "cat_personal_care",
        "hex": "#00838F",
        "kml_color": "ff8f8300",
        "icon": "http://maps.google.com/mapfiles/kml/paddle/ltblu-circle.png",
        "short": "Barber, Beauty & Tailors",
    },
    "Retail, Services & Other": {
        "id": "cat_other",
        "hex": "#6D4C41",
        "kml_color": "ff414c6d",
        "icon": "http://maps.google.com/mapfiles/kml/paddle/ylw-circle.png",
        "short": "Retail & Other Services",
    },
}


def valid_records(records: list[dict]) -> list[dict]:
    """Filters records with valid numeric latitude and longitude."""
    out = []
    for r in records:
        lat = r.get("latitude")
        lon = r.get("longitude")
        if lat is None or lon is None:
            continue
        if math.isnan(lat) or math.isnan(lon):
            continue
        if not (-90.0 <= lat <= 90.0 and -180.0 <= lon <= 180.0):
            continue
        out.append(r)
    return out


def build_geojson(ed_data: dict, records: list[dict]) -> dict:
    """Builds a RFC 7946 GeoJSON FeatureCollection for Google Maps Data Layer."""
    features = []
    for r in records:
        cat = r["category_group"]
        style = CATEGORY_STYLES.get(cat, CATEGORY_STYLES["Retail, Services & Other"])
        features.append({
            "type": "Feature",
            "id": r["id"],
            "geometry": {
                "type": "Point",
                "coordinates": [round(r["longitude"], 6), round(r["latitude"], 6)],
            },
            "properties": {
                "id": r["id"],
                "edition": ed_data["edition"],
                "year": r["year"],
                "name": r["business_name"],
                "business_type": r["business_type"],
                "category_group": cat,
                "owner_name": r["owner_name"],
                "owner_gender": r["owner_gender"],
                "address": r["address"],
                "address2": r["address2"],
                "city": r["city"],
                "state": r["state"],
                "country": r["country"],
                "source_type": r["source_type"],
                "book_notes": r["book_notes"],
                "data_editor_notes": r["data_editor_notes"],
                "info_link": r["info_link"],
                "photo_link": r["photo_link"],
                "marker-color": style["hex"],
                "marker-symbol": style["short"],
            },
        })
    return {
        "type": "FeatureCollection",
        "metadata": {
            "edition": ed_data["edition"],
            "title": ed_data["title"],
            "role": ed_data["role"],
            "feature_count": len(features),
            "nypl_collection_url": ed_data["nypl_collection_url"],
        },
        "features": features,
    }


def format_placemark_xml(r: dict, edition_label: str) -> str:
    """Formats a single KML <Placemark> with rich HTML description and ExtendedData."""
    cat = r["category_group"]
    style = CATEGORY_STYLES.get(cat, CATEGORY_STYLES["Retail, Services & Other"])
    name_esc = html.escape(r["business_name"] or "Unnamed Establishment")
    btype_esc = html.escape(r["business_type"] or "")
    cat_esc = html.escape(cat)
    addr_parts = [p for p in [r["address"], r["address2"]] if p]
    addr_str = ", ".join(addr_parts) if addr_parts else "Address not specified"
    loc_parts = [p for p in [r["city"], r["state"], r["country"]] if p]
    loc_str = ", ".join(loc_parts)

    desc_rows = [
        f"<tr><td><b>Edition:</b></td><td>{html.escape(edition_label)}</td></tr>",
        f"<tr><td><b>Category:</b></td><td>{btype_esc} ({cat_esc})</td></tr>",
        f"<tr><td><b>Address:</b></td><td>{html.escape(addr_str)}</td></tr>",
        f"<tr><td><b>Location:</b></td><td>{html.escape(loc_str)}</td></tr>",
    ]
    if r["owner_name"] and r["owner_name"].lower() != "unknown":
        owner_txt = html.escape(r["owner_name"])
        if r["owner_gender"] and r["owner_gender"].lower() != "unknown":
            owner_txt += f" ({html.escape(r['owner_gender'])})"
        desc_rows.append(f"<tr><td><b>Proprietor:</b></td><td>{owner_txt}</td></tr>")
    if r["source_type"]:
        desc_rows.append(f"<tr><td><b>Entry Type:</b></td><td>{html.escape(r['source_type'])}</td></tr>")
    if r["book_notes"]:
        desc_rows.append(f"<tr><td><b>Book Notes:</b></td><td>{html.escape(r['book_notes'])}</td></tr>")
    if r["data_editor_notes"]:
        desc_rows.append(f"<tr><td><b>Archival Notes:</b></td><td>{html.escape(r['data_editor_notes'])}</td></tr>")
    if r["info_link"]:
        link_esc = html.escape(r["info_link"])
        desc_rows.append(f"<tr><td><b>Info Link:</b></td><td><a href=\"{link_esc}\">{link_esc}</a></td></tr>")

    desc_html = (
        f"<div style=\"font-family:Arial,sans-serif;font-size:13px;line-height:1.4;\">"
        f"<h3 style=\"margin:0 0 6px 0;color:{style['hex']};\">{name_esc}</h3>"
        f"<table style=\"border-collapse:collapse;width:100%;\">{''.join(desc_rows)}</table>"
        f"</div>"
    )

    ext_fields = [
        ("Edition", edition_label),
        ("BusinessType", r["business_type"]),
        ("CategoryGroup", cat),
        ("OwnerName", r["owner_name"]),
        ("OwnerGender", r["owner_gender"]),
        ("Address", addr_str),
        ("City", r["city"]),
        ("State", r["state"]),
        ("Country", r["country"]),
        ("SourceType", r["source_type"]),
        ("BookNotes", r["book_notes"]),
        ("DataEditorNotes", r["data_editor_notes"]),
    ]
    ext_xml = "".join(
        f"<Data name=\"{k}\"><value>{html.escape(str(v or ''))}</value></Data>"
        for k, v in ext_fields
    )

    lon = round(r["longitude"], 6)
    lat = round(r["latitude"], 6)
    return (
        f"      <Placemark id=\"gb_{r['id']}\">\n"
        f"        <name>{name_esc}</name>\n"
        f"        <styleUrl>#{style['id']}</styleUrl>\n"
        f"        <description><![CDATA[{desc_html}]]></description>\n"
        f"        <ExtendedData>{ext_xml}</ExtendedData>\n"
        f"        <Point><coordinates>{lon},{lat},0</coordinates></Point>\n"
        f"      </Placemark>\n"
    )


def build_kml_document(doc_name: str, doc_desc: str, records: list[dict], edition_label: str, group_by_category: bool = True) -> str:
    """Builds a complete KML 2.2 XML string."""
    styles_xml = []
    for cat_name, st in CATEGORY_STYLES.items():
        styles_xml.append(
            f"    <Style id=\"{st['id']}\">\n"
            f"      <IconStyle>\n"
            f"        <color>{st['kml_color']}</color>\n"
            f"        <scale>1.0</scale>\n"
            f"        <Icon><href>{st['icon']}</href></Icon>\n"
            f"      </IconStyle>\n"
            f"      <LabelStyle><scale>0.8</scale></LabelStyle>\n"
            f"      <BalloonStyle><text><![CDATA[$[description]]]></text></BalloonStyle>\n"
            f"    </Style>\n"
        )

    body_xml = []
    if group_by_category:
        by_cat = {}
        for r in records:
            by_cat.setdefault(r["category_group"], []).append(r)
        for cat_name in CATEGORY_STYLES:
            cat_recs = by_cat.get(cat_name, [])
            if not cat_recs:
                continue
            body_xml.append(f"    <Folder>\n      <name>{html.escape(cat_name)} ({len(cat_recs)})</name>\n")
            for r in cat_recs:
                body_xml.append(format_placemark_xml(r, edition_label))
            body_xml.append("    </Folder>\n")
    else:
        for r in records:
            body_xml.append(format_placemark_xml(r, edition_label))

    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        "<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n"
        "  <Document>\n"
        f"    <name>{html.escape(doc_name)}</name>\n"
        f"    <description>{html.escape(doc_desc)}</description>\n"
        + "".join(styles_xml)
        + "".join(body_xml)
        + "  </Document>\n"
        "</kml>\n"
    )


def write_mymaps_splits(ed_path: str, ed_data: dict, records: list[dict]) -> list[str]:
    """Writes <=1,900-feature KML files in mymaps/ so each file imports cleanly into Google My Maps."""
    mymaps_dir = os.path.join(ed_path, "mymaps")
    os.makedirs(mymaps_dir, exist_ok=True)
    max_per_file = 1900
    ed_dir = ed_data["edition"]
    written = []

    if len(records) <= max_per_file:
        fname = f"greenbook_{ed_dir}_mymaps_all.kml"
        fpath = os.path.join(mymaps_dir, fname)
        kml_str = build_kml_document(
            f"{ed_data['title']} (All {len(records)} Listings)",
            ed_data["historical_context"],
            records,
            ed_dir,
            group_by_category=False,
        )
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(kml_str)
        written.append(f"mymaps/{fname}")
    else:
        num_parts = math.ceil(len(records) / max_per_file)
        for i in range(num_parts):
            chunk = records[i * max_per_file : (i + 1) * max_per_file]
            fname = f"greenbook_{ed_dir}_mymaps_part{i+1}_of_{num_parts}.kml"
            fpath = os.path.join(mymaps_dir, fname)
            kml_str = build_kml_document(
                f"{ed_data['title']} - Part {i+1} of {num_parts} ({len(chunk)} Listings)",
                f"Google My Maps layer {i+1}/{num_parts} (<=2,000 feature limit). {ed_data['historical_context']}",
                chunk,
                ed_dir,
                group_by_category=False,
            )
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(kml_str)
            written.append(f"mymaps/{fname}")
    return written


def build_edition_map_html(ed_data: dict, records: list[dict], mymaps_files: list[str]) -> str:
    """Creates a standalone interactive HTML map for a single edition."""
    ed_dir = ed_data["edition"]
    compact_pts = []
    for r in records:
        compact_pts.append([
            round(r["latitude"], 5),
            round(r["longitude"], 5),
            r["business_name"],
            r["business_type"],
            r["category_group"],
            r["address"],
            r["city"],
            r["state"],
            r["country"],
            r["owner_name"],
            r["owner_gender"],
            r["book_notes"],
            r["data_editor_notes"],
            r["source_type"],
        ])

    pages_json = json.dumps(ed_data.get("nypl_archival_assets", {}).get("pages", []))
    pts_json = json.dumps(compact_pts)
    styles_json = json.dumps(CATEGORY_STYLES)
    nypl_assets = ed_data.get("nypl_archival_assets", {})
    pdf_url = nypl_assets.get("pdf_url") or (
        f"https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/{ed_dir}.pdf"
        if nypl_assets.get("pdf_file")
        else None
    )
    has_ocr = ed_data.get("nypl_archival_assets", {}).get("txt_count", 0) > 0
    ocr_tab_html = (
        '<button class="dl-tab" type="button" data-dltab="ocr">OCR text</button>'
        if has_ocr
        else ""
    )
    pdf_tab_html = (
        f'<a class="dl-tab" href="{pdf_url}" target="_blank">PDF ({round(nypl_assets["pdf_bytes"]/1048576, 1)} MB) &nearr;</a>'
        if pdf_url
        else ""
    )
    ocr_panel_html = (
        f'<div class="dl-panel" data-dlpanel="ocr"><a class="btn btn-primary" href="full_text.txt" download="greenbook_{ed_dir}_ocr.txt">Download OCR text</a></div>'
        if has_ocr
        else ""
    )
    total_splits = len(mymaps_files)
    mymaps_links = " ".join(
        f'<a class="btn btn-primary" href="{mf}" download>Download {ed_dir} KML {idx + 1} of {total_splits}</a>'
        for idx, mf in enumerate(mymaps_files)
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Green Book Atlas - {ed_dir} Edition</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet.heat@0.2.0/dist/leaflet-heat.js"></script>
<style>
  :root {{
    --bg: #111618;
    --panel: #1a2124;
    --border: #2c373c;
    --accent: #2e7d32;
    --accent-light: #66bb6a;
    --text: #eaeff2;
    --muted: #9aa8b0;
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: var(--bg); color: var(--text); display: flex; height: 100vh; overflow: hidden; }}
  #sidebar {{ width: 370px; background: var(--panel); border-right: 1px solid var(--border); display: flex; flex-direction: column; z-index: 1000; }}
  .header {{ padding: 12px 16px; border-bottom: 1px solid var(--border); background: #141b1d; display: flex; justify-content: space-between; align-items: baseline; gap: 8px; }}
  h1 {{ font-size: 16px; margin: 0; line-height: 1.25; }}
  .controls {{ padding: 12px 16px; border-bottom: 1px solid var(--border); overflow-y: auto; flex: 1; }}
  .section-title {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; color: var(--muted); margin: 12px 0 6px 0; }}
  .section-title:first-child {{ margin-top: 0; }}
  input[type="text"], select {{ width: 100%; padding: 7px 10px; background: #0f1416; border: 1px solid var(--border); color: var(--text); border-radius: 6px; font-size: 13px; margin-bottom: 6px; }}
  .cat-item {{ display: flex; align-items: center; justify-content: space-between; padding: 4px 0; font-size: 13px; cursor: pointer; }}
  .cat-left {{ display: flex; align-items: center; gap: 8px; }}
  .swatch {{ width: 12px; height: 12px; border-radius: 50%; display: inline-block; border: 1px solid rgba(255,255,255,0.4); }}
  .count-pill {{ background: #0f1416; color: var(--muted); padding: 1px 7px; border-radius: 10px; font-size: 11.5px; }}
  .btn-group {{ display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; }}
  .btn {{ display: inline-block; background: #243035; color: var(--text); text-decoration: none; padding: 5px 9px; border-radius: 5px; font-size: 12px; border: 1px solid var(--border); cursor: pointer; transition: background 0.15s; }}
  .btn:hover {{ background: #314148; }}
  .btn-primary {{ background: var(--accent); border-color: #388e3c; color: #fff; }}
  .btn-sm {{ padding: 4px 8px; font-size: 11px; }}
  #map {{ flex: 1; height: 100vh; }}
  .stats-bar {{ padding: 8px 16px; background: #0f1416; border-top: 1px solid var(--border); font-size: 12px; color: var(--muted); display: flex; justify-content: space-between; }}
  .leaflet-popup-content-wrapper {{ background: #1a2124; color: #eaeff2; border: 1px solid #2c373c; border-radius: 8px; }}
  .leaflet-popup-tip {{ background: #1a2124; }}
  .popup-title {{ font-size: 14.5px; font-weight: 700; margin: 0 0 4px 0; color: #81c784; }}
  .popup-meta {{ font-size: 12.5px; line-height: 1.45; }}
  .popup-meta b {{ color: #b0bec5; }}
  .page-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 5px; max-height: 130px; overflow-y: auto; padding: 4px; background: #0f1416; border-radius: 6px; border: 1px solid var(--border); }}
  .page-link {{ font-size: 11px; color: var(--accent-light); text-decoration: none; padding: 3px; text-align: center; background: #1a2124; border-radius: 4px; }}
  .page-link:hover {{ background: #263238; }}
  .license-box {{ font-size: 11px; color: var(--muted); line-height: 1.4; background: #0f1416; padding: 8px 10px; border-radius: 6px; border: 1px solid var(--border); margin-top: 8px; }}
  .license-box a {{ color: var(--accent-light); text-decoration: none; }}
  .modal-backdrop {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.72); z-index: 3000; align-items: center; justify-content: center; padding: 24px; }}
  .modal-backdrop.open {{ display: flex; }}
  .modal-content {{ background: var(--panel); border: 1px solid var(--border); border-radius: 10px; max-width: 680px; width: 100%; max-height: 85vh; overflow-y: auto; padding: 20px 24px; color: var(--text); box-shadow: 0 16px 48px rgba(0,0,0,0.6); font-size: 13px; line-height: 1.5; }}
  .modal-content h2 {{ margin: 0 0 10px 0; font-size: 18px; color: var(--accent-light); }}
  .modal-content h3 {{ margin: 14px 0 6px 0; font-size: 14px; color: #fff; }}
  .modal-content ol {{ margin: 6px 0 10px 0; padding-left: 20px; }}
  .modal-content li {{ margin-bottom: 6px; }}
  .modal-content a {{ color: var(--accent-light); }}
  .guide-card {{ background: #12181b; border: 1px solid var(--border); border-radius: 8px; padding: 12px 14px; margin-bottom: 10px; }}
  .dl-tabs {{ display: flex; flex-wrap: wrap; gap: 4px; border-bottom: 1px solid var(--border); margin: 12px 0 14px 0; }}
  .dl-tab {{ background: transparent; border: none; border-bottom: 2px solid transparent; color: var(--muted); padding: 8px 12px; font-size: 13px; font-weight: 600; cursor: pointer; text-decoration: none; border-radius: 6px 6px 0 0; transition: all 0.15s; font-family: inherit; }}
  .dl-tab:hover {{ color: var(--text); background: rgba(255,255,255,0.04); }}
  .dl-tab.active {{ color: var(--accent-light); border-bottom-color: var(--accent-light); background: rgba(46, 125, 50, 0.15); }}
  .dl-panel {{ display: none; background: #12181b; border: 1px solid var(--border); border-radius: 8px; padding: 14px 16px; }}
  .dl-panel.active {{ display: block; }}
  .dl-panel h3:first-child {{ margin-top: 0; }}
  .dl-panel .btn-primary {{ color: #fff; }}
  #faqModal .modal-content {{ padding: 26px 32px; font-size: 14px; line-height: 1.65; }}
  #faqModal h3 {{ margin: 24px 0 8px 0; padding-top: 18px; border-top: 1px solid var(--border); font-size: 15.5px; color: #fff; }}
  #faqModal h3:first-of-type {{ margin-top: 16px; padding-top: 0; border-top: none; }}
  #faqModal p {{ margin: 8px 0 12px 0; color: #d8e2e7; line-height: 1.65; }}
  #faqModal ul, #faqModal ol {{ margin: 8px 0 12px 0; padding-left: 22px; color: #d8e2e7; line-height: 1.65; }}
  #faqModal li {{ margin-bottom: 10px; }}
</style>
</head>
<body>
<div id="sidebar">
  <div class="header">
    <h1>Green Book Atlas &middot; {ed_dir}</h1>
    <a href="../index.html" style="color:var(--accent-light);font-size:12px;text-decoration:none;white-space:nowrap;">&larr; All editions</a>
  </div>
  <div class="controls">
    <div class="section-title">Filter</div>
    <input type="text" id="searchInput" placeholder="Search name, owner, street, city..."/>
    <select id="stateSelect"><option value="">All states &amp; countries</option></select>
    <div style="display:flex;gap:8px;margin-bottom:4px;">
      <label style="font-size:12px;cursor:pointer;"><input type="checkbox" id="heatToggle"/> Heatmap</label>
    </div>

    <div class="section-title">Categories</div>
    <div id="categoryList"></div>

    <div id="ocrSection" style="display:none;">
      <div class="section-title">OCR pages (<span id="pageCount">0</span>)</div>
      <div class="page-grid" id="pageGrid"></div>
    </div>

    <div style="display:flex;gap:6px;margin-top:14px;">
      <button class="btn btn-primary" id="openDownloadsModalBtn" type="button" style="flex:1;text-align:center;font-weight:600;">Downloads</button>
      <a class="btn" href="map.html" title="Standalone {ed_dir} map link" aria-label="Standalone {ed_dir} map link" style="display:inline-flex;align-items:center;justify-content:center;padding:5px 9px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>
    </div>

    <div class="license-box">
      Data: Victor H. Green &amp; Co. &middot; <a href="https://digitalcollections.nypl.org/collections/the-green-book" target="_blank">NYPL</a> (CC0) &middot; <a href="https://storymaps.arcgis.com/stories/a96fdcea2e9a4f7bb8da1220f76f1ec8" target="_blank">U. Redlands</a> &amp; <a href="https://www.loc.gov/item/2016298176/" target="_blank">LoC</a> &middot; <a href="https://github.com/cengel/GreenBook" target="_blank">C. Engel</a> (CC BY-SA 4.0)
      <div style="display:flex;gap:5px;flex-wrap:wrap;margin-top:6px;">
        <button class="btn" id="openFaqModalBtn" type="button" style="font-size:11px;padding:3px 7px;">About / FAQ</button>
        <a class="btn" href="../LICENSE.md" target="_blank" style="font-size:11px;padding:3px 7px;">LICENSE.md &nearr;</a>
        <a class="btn" href="README.md" target="_blank" style="font-size:11px;padding:3px 7px;">README.md &nearr;</a>
      </div>
    </div>
  </div>
  <div class="stats-bar">
    <span id="visibleCount">{len(records):,} / {len(records):,} shown</span>
    <span>{ed_dir}</span>
  </div>
</div>
<div id="map"></div>

<div class="modal-backdrop" id="downloadsModal">
  <div class="modal-content">
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <h2>Downloads ({ed_dir})</h2>
      <button class="btn" id="closeDownloadsModalBtn" type="button">Close &times;</button>
    </div>
    <div class="dl-tabs" id="dlTabs">
      <button class="dl-tab active" type="button" data-dltab="kml">KML</button>
      <button class="dl-tab" type="button" data-dltab="kmz">KMZ</button>
      <button class="dl-tab" type="button" data-dltab="geojson">GeoJSON</button>
      <button class="dl-tab" type="button" data-dltab="csv">CSV</button>
      <button class="dl-tab" type="button" data-dltab="json">JSON</button>
      {ocr_tab_html}
      {pdf_tab_html}
    </div>
    <div class="dl-panel active" data-dlpanel="kml">
      <h3>Download full KML</h3>
      <div class="btn-group">
        <a class="btn btn-primary" href="overlay.kml" download="greenbook_{ed_dir}.kml">Download full KML</a>
      </div>
      <h3>Download Google Maps split KML</h3>
      <div class="btn-group">{mymaps_links}</div>
    </div>
    <div class="dl-panel" data-dlpanel="kmz">
      <a class="btn btn-primary" href="overlay.kmz" download="greenbook_{ed_dir}.kmz">Download KMZ</a>
    </div>
    <div class="dl-panel" data-dlpanel="geojson">
      <a class="btn btn-primary" href="overlay.geojson" download="greenbook_{ed_dir}.geojson">Download GeoJSON</a>
    </div>
    <div class="dl-panel" data-dlpanel="csv">
      <a class="btn btn-primary" href="listings.csv" download="greenbook_{ed_dir}.csv">Download CSV</a>
    </div>
    <div class="dl-panel" data-dlpanel="json">
      <a class="btn btn-primary" href="listings.json" download="greenbook_{ed_dir}.json">Download JSON</a>
    </div>
    {ocr_panel_html}
  </div>
</div>

<div class="modal-backdrop" id="faqModal">
  <div class="modal-content">
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <h2>About and frequently-asked questions</h2>
      <button class="btn" id="closeFaqModalBtn" type="button">Close &times;</button>
    </div>
    <h3>What is Green Book Atlas?</h3>
    <p><b>Green Book Atlas</b> (<a href="https://greenbookatlas.org" target="_blank">greenbookatlas.org</a>) contains interactive map overlays, geocoded directory datasets, and page-level OCR transcriptions for all 24 surviving geocoded editions of <i>The Negro Motorist Green Book</i> and <i>Travelers' Green Book</i>. This totals 13,696 unique establishments across 68,330 total listings, 1,734 OCR page pairs, and links to NYPL's 21 CC0 PDF volumes.</p>

    <h3>How do I use these overlays with Google Maps?</h3>
    <ol>
      <li>Click <b>Downloads</b> in the sidebar and download the split, Google-compatible KML files for your chosen edition.</li>
      <li>Open <a href="https://www.google.com/mymaps" target="_blank">Google My Maps</a>, click <i>Create a new map</i> &rarr; <i>Add layer</i> &rarr; <i>Import</i>, and upload the file(s) from (1).</li>
      <li>Open regular Google Maps (under <i>Saved</i> &rarr; <i>Maps</i>) and select your newly-created map. Enter your trip in <i>Directions</i>, tap any Green Book pin along your route line, and select <i>Add stop</i>.</li>
    </ol>
    <p style="font-size:12px;color:var(--muted);">Note: Google Maps enforces a cap on features per layer, so some editions are split across multiple KML files.</p>

    <h3>Why does the "ALL" tab have 13,696 sites instead of 68,330?</h3>
    <p>The "All" tab is deduplicated.</p>

    <h3>Why are 1936, 1942-1945, and 1965 missing?</h3>
    <p>Those editions either do not survive or were never published:</p>
    <ul>
      <li><b>1936</b>: No copy of the 1936 New York prototype edition is known to survive in any public archive.</li>
      <li><b>1942-1945</b>: Publication was suspended during World War II due to wartime rationing.</li>
      <li><b>1965</b>: The final two issues were published as multi-year editions (1963-64 and 1966-67).</li>
    </ul>

    <h3>Why are the 1966-67 PDF and some Internet Archive scans excluded?</h3>
    <ul>
      <li>The 1938 and 1940 versions available on Internet Archive prohibit derivative works. As such, we use NYPL's public-domain scans instead.</li>
      <li>NYPL does not provide 1966-1967 scans because they are still under copyright. We include the non-copyrightable factual directory listings.</li>
    </ul>

    <h3>Where can I find the raw data and source code?</h3>
    <p>On GitHub at <a href="https://github.com/ffleming/greenbookatlas.org" target="_blank">github.com/ffleming/greenbookatlas.org</a>.</p>
  </div>
</div>

<script>
const POINTS = {pts_json};
const STYLES = {styles_json};
const PAGES = {pages_json};

// Basemaps including Google Maps Roadmap, Terrain, Hybrid/Satellite, and Carto Dark/Light
const mapLang = encodeURIComponent(navigator.language || 'en');
const googleStreets = L.tileLayer(`https://mt1.google.com/vt/lyrs=m&hl=${{mapLang}}&gl=US&x={{x}}&y={{y}}&z={{z}}`, {{
  maxZoom: 20,
  attribution: '&copy; Google Maps | NYPL Schomburg Center | Univ. of Redlands'
}});
const googleTerrain = L.tileLayer(`https://mt1.google.com/vt/lyrs=p&hl=${{mapLang}}&gl=US&x={{x}}&y={{y}}&z={{z}}`, {{
  maxZoom: 20,
  attribution: '&copy; Google Maps Terrain'
}});
const googleHybrid = L.tileLayer(`https://mt1.google.com/vt/lyrs=y&hl=${{mapLang}}&gl=US&x={{x}}&y={{y}}&z={{z}}`, {{
  maxZoom: 20,
  attribution: '&copy; Google Maps Satellite/Hybrid'
}});
const cartoDark = L.tileLayer('https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
  maxZoom: 20,
  attribution: '&copy; OpenStreetMap &copy; CARTO'
}});
const cartoLight = L.tileLayer('https://{{s}}.basemaps.cartocdn.com/light_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
  maxZoom: 20,
  attribution: '&copy; OpenStreetMap &copy; CARTO'
}});

const map = L.map('map', {{
  center: [38.5, -92.0],
  zoom: 4,
  layers: [googleStreets],
  preferCanvas: true
}});

L.control.layers({{
  "Google Maps Roadmap": googleStreets,
  "Google Maps Terrain": googleTerrain,
  "Google Maps Satellite Hybrid": googleHybrid,
  "Dark Historical Theme": cartoDark,
  "Light Minimalist Theme": cartoLight
}}, null, {{ position: 'topright' }}).addTo(map);

const markerLayer = L.layerGroup().addTo(map);
let heatLayer = null;

// Populate state dropdown
const stateCounts = {{}};
const catCounts = {{}};
POINTS.forEach(p => {{
  const st = p[7] ? `${{p[7]}} (${{p[8] || 'USA'}})` : (p[8] || 'Unspecified');
  stateCounts[st] = (stateCounts[st] || 0) + 1;
  catCounts[p[4]] = (catCounts[p[4]] || 0) + 1;
}});

const stateSelect = document.getElementById('stateSelect');
Object.keys(stateCounts).sort().forEach(st => {{
  const opt = document.createElement('option');
  opt.value = st;
  opt.textContent = `${{st}} (${{stateCounts[st]}})`;
  stateSelect.appendChild(opt);
}});

// Populate categories
const activeCats = new Set(Object.keys(STYLES));
const catList = document.getElementById('categoryList');
Object.entries(STYLES).forEach(([catName, st]) => {{
  const cnt = catCounts[catName] || 0;
  const row = document.createElement('label');
  row.className = 'cat-item';
  row.innerHTML = `
    <span class="cat-left">
      <input type="checkbox" checked data-cat="${{catName}}"/>
      <span class="swatch" style="background:${{st.hex}}"></span>
      <span>${{st.short}}</span>
    </span>
    <span class="count-pill">${{cnt}}</span>
  `;
  row.querySelector('input').addEventListener('change', (e) => {{
    if (e.target.checked) activeCats.add(catName);
    else activeCats.delete(catName);
    renderMap();
  }});
  catList.appendChild(row);
}});

// Populate OCR page grid if available
if (PAGES && PAGES.length > 0) {{
  document.getElementById('ocrSection').style.display = 'block';
  document.getElementById('pageCount').textContent = PAGES.length;
  const grid = document.getElementById('pageGrid');
  PAGES.forEach(pg => {{
    const a = document.createElement('a');
    a.className = 'page-link';
    a.href = pg.txt_file;
    a.target = '_blank';
    a.title = `Open OCR text for Page ${{pg.page_index}} (NYPL Capture ${{pg.capture_id}})`;
    a.textContent = `Pg ${{pg.page_index}}`;
    grid.appendChild(a);
  }});
}}

function escapeHtml(s) {{
  return String(s || '').replace(/[&<>"']/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));
}}

function renderMap(fitBounds = false) {{
  markerLayer.clearLayers();
  if (heatLayer) {{
    map.removeLayer(heatLayer);
    heatLayer = null;
  }}
  const q = document.getElementById('searchInput').value.trim().toLowerCase();
  const stFilter = stateSelect.value;
  const showHeat = document.getElementById('heatToggle').checked;

  const bounds = [];
  const heatPts = [];
  let shown = 0;

  POINTS.forEach(p => {{
    const [lat, lon, name, btype, cat, addr, city, state, country, owner, gender, bnotes, enotes, stype] = p;
    if (!activeCats.has(cat)) return;
    const stKey = state ? `${{state}} (${{country || 'USA'}})` : (country || 'Unspecified');
    if (stFilter && stKey !== stFilter) return;
    if (q) {{
      const hay = `${{name}} ${{btype}} ${{addr}} ${{city}} ${{state}} ${{owner}} ${{bnotes}} ${{enotes}}`.toLowerCase();
      if (!hay.includes(q)) return;
    }}

    shown++;
    bounds.push([lat, lon]);
    heatPts.push([lat, lon, 0.8]);

    const st = STYLES[cat] || STYLES["Retail, Services & Other"];
    const marker = L.circleMarker([lat, lon], {{
      radius: 6,
      fillColor: st.hex,
      color: '#ffffff',
      weight: 1.2,
      opacity: 0.9,
      fillOpacity: 0.85
    }});

    let popupHtml = `<div class="popup-title">${{escapeHtml(name)}}</div><div class="popup-meta">`;
    popupHtml += `<div>${{escapeHtml(btype || st.short)}}</div>`;
    popupHtml += `<div>${{escapeHtml([addr, city, state, country].filter(Boolean).join(', '))}}</div>`;
    if (owner && owner.toLowerCase() !== 'unknown') {{
      popupHtml += `<div><b>Owner:</b> ${{escapeHtml(owner)}}${{gender && gender.toLowerCase() !== 'unknown' ? ' (' + escapeHtml(gender) + ')' : ''}}</div>`;
    }}
    if (bnotes) popupHtml += `<div><b>Notes:</b> ${{escapeHtml(bnotes)}}</div>`;
    if (enotes) popupHtml += `<div><b>Archival:</b> ${{escapeHtml(enotes)}}</div>`;
    popupHtml += `<div style="margin-top:6px;"><a href="https://www.google.com/maps/search/?api=1&query=${{encodeURIComponent((addr ? addr + ', ' : '') + city + ' ' + state)}}" target="_blank" style="color:#66bb6a;">Open in Google Maps &nearr;</a></div>`;
    popupHtml += `</div>`;

    marker.bindPopup(popupHtml);
    markerLayer.addLayer(marker);
  }});

  if (showHeat && heatPts.length > 0 && typeof L.heatLayer === 'function') {{
    heatLayer = L.heatLayer(heatPts, {{ radius: 22, blur: 16, maxZoom: 12 }}).addTo(map);
  }}

  if (fitBounds && bounds.length > 0) {{
    map.fitBounds(bounds, {{ padding: [30, 30], maxZoom: 13 }});
  }}

  document.getElementById('visibleCount').textContent = `${{shown.toLocaleString()}} / ${{POINTS.length.toLocaleString()}} shown`;
}}

document.getElementById('searchInput').addEventListener('input', () => renderMap(false));
stateSelect.addEventListener('change', () => renderMap(true));
document.getElementById('heatToggle').addEventListener('change', () => renderMap(false));

const dlModal = document.getElementById('downloadsModal');
document.getElementById('openDownloadsModalBtn').addEventListener('click', () => dlModal.classList.add('open'));
document.getElementById('closeDownloadsModalBtn').addEventListener('click', () => dlModal.classList.remove('open'));
dlModal.addEventListener('click', (e) => {{ if (e.target === dlModal) dlModal.classList.remove('open'); }});
document.querySelectorAll('#dlTabs button[data-dltab]').forEach(btn => {{
  btn.addEventListener('click', () => {{
    const t = btn.dataset.dltab;
    document.querySelectorAll('#dlTabs button[data-dltab]').forEach(b => b.classList.toggle('active', b === btn));
    document.querySelectorAll('#downloadsModal .dl-panel').forEach(p => p.classList.toggle('active', p.dataset.dlpanel === t));
  }});
}});

const faqModal = document.getElementById('faqModal');
document.getElementById('openFaqModalBtn').addEventListener('click', () => faqModal.classList.add('open'));
document.getElementById('closeFaqModalBtn').addEventListener('click', () => faqModal.classList.remove('open'));
faqModal.addEventListener('click', (e) => {{ if (e.target === faqModal) faqModal.classList.remove('open'); }});

renderMap(true);
</script>
</body>
</html>
"""


def build_edition_readme(ed_data: dict, mymaps_files: list[str]) -> str:
    """Builds the README.md for an individual edition directory."""
    ed_dir = ed_data["edition"]
    nypl = ed_data.get("nypl_archival_assets", {})
    cat_lines = [
        f"| {cat} | {cnt:,} |"
        for cat, cnt in ed_data["category_counts"].items()
    ]
    top_states = list(ed_data["state_counts"].items())[:15]
    state_lines = [
        f"| {st} | {cnt:,} |"
        for st, cnt in top_states
    ]
    supp_lines = [f"- `{sf}`" for sf in ed_data.get("supplemental_files", [])] or ["- None"]
    mymaps_lines = [f"- `{mf}`" for mf in mymaps_files]

    pdf_url = nypl.get("pdf_url") or (
        f"https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/{ed_dir}.pdf"
        if nypl.get("pdf_file")
        else None
    )
    if pdf_url:
        pdf_info = (
            f"- [NYPL original PDF ({round(nypl['pdf_bytes']/1048576, 1)} MB)]({pdf_url}) - digitized PDF hosted by NYPL Labs (CC0 1.0)\n"
            f"- `full_text.txt` - concatenated OCR text across all {nypl['txt_count']} pages\n"
            f"- `ocr/` - {nypl['txt_count']} page-level `.txt` and {nypl['hocr_count']} `.hocr` OCR files"
        )
    elif ed_dir == "1966-67":
        pdf_info = (
            "- *Note*: NYPL does not provide 1966-1967 scans because they are still under copyright. We include the non-copyrightable factual directory listings (`listings.*` and `overlay.*`)."
        )
    else:
        pdf_info = (
            f"- *NB*: The {ed_dir} edition is preserved in the [NYPL Digital Collections]({ed_data['nypl_collection_url']}) and all {ed_data['total_records']:,} establishments are included in `listings.*` and `overlay.*`, though its bulk PDF/hOCR files were not included in NYPL's 21-volume `NYPL-publicdomain/greenbooks` release."
        )

    return f"""# {ed_data['title']} - Green Book Atlas ({ed_data['role']})

**TL;DR:** {ed_data['historical_context']} Total geocoded establishments: *{ed_data['total_records']:,}* ([Green Book Atlas](https://greenbookatlas.org) | [NYPL archive]({ed_data['nypl_collection_url']})).

## Files in this directory
- `map.html` - interactive Google Maps / Leaflet web overlay
- `overlay.kml` and `overlay.kmz` - KML/KMZ overlays grouped by category
- `overlay.geojson` - GeoJSON `FeatureCollection`
- `mymaps/` - KML layers split to &le;1,900 pins each for [Google My Maps](https://www.google.com/mymaps):
{chr(10).join('  ' + l for l in mymaps_lines)}
- `listings.csv` and `listings.json` - structured dataset ({ed_data['total_records']:,} records)
{pdf_info}

### Supplemental files
{chr(10).join(supp_lines)}

## Breakdown by category

| Category | Listings |
| :--- | ---: |
{chr(10).join(cat_lines)}

## Top 15 states and regions

| State / region | Listings |
| :--- | ---: |
{chr(10).join(state_lines)}

## Licenses and excluded datasets
- *Original volume*: Victor H. Green & Co. (U.S. public domain for 1937-1963/64; uncopyrightable factual directory listings for 1966-67).
- *Digitized PDF, OCR, and 1947 GeoJSON*: NYPL Schomburg Center & NYPL Labs ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)).
- *Geocoded dataset (`listings.*`, `overlay.*`, `mymaps/*`)*: University of Redlands Center for Spatial Studies (`GreenbookLocations1937_1966`) & Library of Congress ([`loc.gov/item/2016298176/`](https://www.loc.gov/item/2016298176/)) - public educational/research release.
- *Supplemental files (`supplemental/`)*: University of South Carolina Libraries (CC0 1.0); Claudia Engel ([`cengel/GreenBook`](https://github.com/cengel/GreenBook), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for `GreenBook*` files).
- *Excluded datasets*: The 1938 and 1940 versions available on Internet Archive prohibit derivative works (we use NYPL's public-domain scans instead), and NYPL does not provide 1966-1967 scans because they are still under copyright. See [`../LICENSE.md`](../LICENSE.md).
"""


def normalize_key_part(s: str) -> str:
    """Normalizes business name, street address, city, or state for cross-edition deduplication."""
    s = (s or "").lower().strip()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\b(street|st)\b", "st", s)
    s = re.sub(r"\b(avenue|ave)\b", "ave", s)
    s = re.sub(r"\b(road|rd)\b", "rd", s)
    s = re.sub(r"\b(boulevard|blvd)\b", "blvd", s)
    s = re.sub(r"\b(drive|dr)\b", "dr", s)
    s = re.sub(r"\b(north|n)\b", "n", s)
    s = re.sub(r"\b(south|s)\b", "s", s)
    s = re.sub(r"\b(east|e)\b", "e", s)
    s = re.sub(r"\b(west|w)\b", "w", s)
    return re.sub(r"\s+", " ", s).strip()


def deduplicate_across_editions(editions_records: list[tuple[str, list[dict]]]) -> list[list]:
    """Deduplicates establishments across all 24 editions into a single compact table with edition lists."""
    groups: dict[tuple, dict] = {}
    for ed_dir, recs in editions_records:
        for r in recs:
            lat = r["latitude"]
            lon = r["longitude"]
            norm_addr = normalize_key_part(r.get("address", ""))
            key = (
                normalize_key_part(r.get("business_name", "")),
                norm_addr if norm_addr else f"{round(lat, 4)},{round(lon, 4)}",
                normalize_key_part(r.get("city", "")),
                normalize_key_part(r.get("state", "")),
                r.get("category_group", ""),
            )
            if key not in groups:
                groups[key] = {"rec": dict(r), "eds": [ed_dir]}
            else:
                cur = groups[key]["rec"]
                for fld in (
                    "address",
                    "owner_name",
                    "owner_gender",
                    "book_notes",
                    "data_editor_notes",
                    "source_type",
                ):
                    if not cur.get(fld) and r.get(fld):
                        cur[fld] = r[fld]
                cur["latitude"] = lat
                cur["longitude"] = lon
                if ed_dir not in groups[key]["eds"]:
                    groups[key]["eds"].append(ed_dir)

    unique_pts = []
    for g in groups.values():
        r = g["rec"]
        unique_pts.append([
            round(r["latitude"], 5),
            round(r["longitude"], 5),
            r["business_name"],
            r["business_type"],
            r["category_group"],
            r["address"],
            r["city"],
            r["state"],
            r["country"],
            r["owner_name"],
            r["owner_gender"],
            r["book_notes"],
            r["data_editor_notes"],
            r["source_type"],
            g["eds"],
        ])
    return unique_pts


def build_master_index_html(all_editions_meta: list[dict], unique_pts: list[list], total_raw_count: int) -> str:
    """Builds the unified multi-edition interactive Google Maps overlay viewer at greenbook/index.html."""
    meta_json = json.dumps(all_editions_meta, separators=(",", ":"))
    pts_json = json.dumps(unique_pts, separators=(",", ":"))
    styles_json = json.dumps(CATEGORY_STYLES, separators=(",", ":"))
    unique_count = len(unique_pts)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Green Book Atlas (1937-1967)</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet.heat@0.2.0/dist/leaflet-heat.js"></script>
<style>
  :root {{
    --bg: #101517;
    --panel: #182024;
    --border: #2a363b;
    --accent: #2e7d32;
    --accent-light: #81c784;
    --text: #eceff1;
    --muted: #90a4ae;
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: var(--bg); color: var(--text); display: flex; height: 100vh; overflow: hidden; }}
  #sidebar {{ width: 390px; background: var(--panel); border-right: 1px solid var(--border); display: flex; flex-direction: column; z-index: 1000; }}
  .header {{ padding: 12px 16px; background: #12181b; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: baseline; }}
  h1 {{ font-size: 16.5px; margin: 0; }}
  .header-sub {{ font-size: 12px; color: var(--muted); }}
  .controls {{ padding: 12px 16px; overflow-y: auto; flex: 1; }}
  .section-title {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; color: var(--muted); margin: 12px 0 6px 0; }}
  .section-title:first-child {{ margin-top: 0; }}
  .ed-pills {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 5px; margin-bottom: 8px; }}
  .ed-pill {{ background: #101619; border: 1px solid var(--border); color: var(--text); padding: 5px 4px; border-radius: 5px; text-align: center; cursor: pointer; font-size: 12px; font-weight: 600; transition: all 0.15s; }}
  .ed-pill span {{ display: block; font-size: 10px; color: var(--muted); font-weight: 400; margin-top: 1px; }}
  .ed-pill.active {{ background: var(--accent); border-color: #66bb6a; color: #fff; }}
  .ed-pill.active span {{ color: #e8f5e9; }}
  .ed-card {{ background: #12181b; border: 1px solid var(--border); border-radius: 6px; padding: 7px 10px; margin-bottom: 8px; font-size: 12px; color: var(--muted); display: flex; justify-content: space-between; align-items: center; gap: 8px; }}
  .ed-card b {{ color: var(--accent-light); }}
  input[type="text"], select {{ width: 100%; padding: 7px 10px; background: #101619; border: 1px solid var(--border); color: var(--text); border-radius: 6px; font-size: 13px; margin-bottom: 6px; }}
  .cat-item {{ display: flex; align-items: center; justify-content: space-between; padding: 3.5px 0; font-size: 12.5px; cursor: pointer; }}
  .cat-left {{ display: flex; align-items: center; gap: 8px; }}
  .swatch {{ width: 11px; height: 11px; border-radius: 50%; display: inline-block; border: 1px solid rgba(255,255,255,0.4); }}
  .count-pill {{ background: #101619; color: var(--muted); padding: 1px 7px; border-radius: 10px; font-size: 11px; }}
  .btn-group {{ display: flex; flex-wrap: wrap; gap: 5px; margin-top: 6px; }}
  .btn {{ display: inline-block; background: #222e33; color: var(--text); text-decoration: none; padding: 5px 9px; border-radius: 5px; font-size: 12px; border: 1px solid var(--border); cursor: pointer; }}
  .btn:hover {{ background: #2f3e46; }}
  .btn-primary {{ background: var(--accent); border-color: #43a047; color: #fff; }}
  #map {{ flex: 1; height: 100vh; }}
  .stats-bar {{ padding: 8px 16px; background: #101619; border-top: 1px solid var(--border); font-size: 11.5px; color: var(--muted); display: flex; justify-content: space-between; }}
  .leaflet-popup-content-wrapper {{ background: #182024; color: #eceff1; border: 1px solid #2a363b; border-radius: 8px; }}
  .leaflet-popup-tip {{ background: #182024; }}
  .popup-title {{ font-size: 14.5px; font-weight: 700; margin: 0 0 4px 0; color: #81c784; }}
  .popup-meta {{ font-size: 12.5px; line-height: 1.45; }}
  .license-box {{ background: #12181b; border: 1px solid var(--border); border-radius: 6px; padding: 8px 10px; font-size: 11px; color: var(--muted); line-height: 1.4; margin-top: 8px; }}
  .license-box a {{ color: var(--accent-light); text-decoration: none; }}
  .license-box a:hover {{ text-decoration: underline; }}
  .modal-backdrop {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.72); z-index: 3000; align-items: center; justify-content: center; padding: 24px; }}
  .modal-backdrop.open {{ display: flex; }}
  .modal-content {{ background: var(--panel); border: 1px solid var(--border); border-radius: 10px; max-width: 740px; width: 100%; max-height: 85vh; overflow-y: auto; padding: 20px 24px; color: var(--text); box-shadow: 0 16px 48px rgba(0,0,0,0.6); }}
  .modal-content h2 {{ margin: 0 0 10px 0; font-size: 18px; color: var(--accent-light); }}
  .modal-content table {{ width: 100%; border-collapse: collapse; font-size: 12px; margin: 10px 0 14px 0; }}
  .modal-content th, .modal-content td {{ border: 1px solid var(--border); padding: 7px 9px; text-align: left; vertical-align: top; line-height: 1.4; }}
  .modal-content th {{ background: #12181b; color: #b0bec5; font-size: 11px; text-transform: uppercase; }}
  .modal-content a {{ color: var(--accent-light); }}
  .modal-content h3 {{ margin: 14px 0 6px 0; font-size: 14px; color: #fff; }}
  .modal-content ol {{ margin: 6px 0 10px 0; padding-left: 20px; font-size: 13px; line-height: 1.5; }}
  .modal-content li {{ margin-bottom: 6px; }}
  .guide-card {{ background: #12181b; border: 1px solid var(--border); border-radius: 8px; padding: 12px 14px; margin-bottom: 10px; font-size: 13px; line-height: 1.5; }}
  .dl-tabs {{ display: flex; flex-wrap: wrap; gap: 4px; border-bottom: 1px solid var(--border); margin: 12px 0 14px 0; }}
  .dl-tab {{ background: transparent; border: none; border-bottom: 2px solid transparent; color: var(--muted); padding: 8px 12px; font-size: 13px; font-weight: 600; cursor: pointer; text-decoration: none; border-radius: 6px 6px 0 0; transition: all 0.15s; font-family: inherit; }}
  .dl-tab:hover {{ color: var(--text); background: rgba(255,255,255,0.04); }}
  .dl-tab.active {{ color: var(--accent-light); border-bottom-color: var(--accent-light); background: rgba(46, 125, 50, 0.15); }}
  .dl-panel {{ display: none; background: #12181b; border: 1px solid var(--border); border-radius: 8px; padding: 14px 16px; }}
  .dl-panel.active {{ display: block; }}
  .dl-panel h3:first-child {{ margin-top: 0; }}
  .dl-panel .btn-primary {{ color: #fff; }}
  #faqModal .modal-content {{ padding: 26px 32px; font-size: 14px; line-height: 1.65; }}
  #faqModal h3 {{ margin: 24px 0 8px 0; padding-top: 18px; border-top: 1px solid var(--border); font-size: 15.5px; color: #fff; }}
  #faqModal h3:first-of-type {{ margin-top: 16px; padding-top: 0; border-top: none; }}
  #faqModal p {{ margin: 8px 0 12px 0; color: #d8e2e7; line-height: 1.65; }}
  #faqModal ul, #faqModal ol {{ margin: 8px 0 12px 0; padding-left: 22px; color: #d8e2e7; line-height: 1.65; }}
  #faqModal li {{ margin-bottom: 10px; }}
</style>
</head>
<body>
<div id="sidebar">
  <div class="header">
    <h1>Green Book Atlas</h1>
    <span class="header-sub">1937-1967</span>
  </div>
  <div class="controls">
    <div class="section-title">Edition</div>
    <div class="ed-pills" id="editionPills"></div>
    <div class="ed-card" id="editionCard"></div>

    <div class="section-title">Filter</div>
    <input type="text" id="searchInput" placeholder="Search name, owner, street, city..."/>
    <select id="stateSelect"><option value="">All states &amp; countries</option></select>
    <div style="display:flex;gap:14px;margin-bottom:4px;">
      <label style="font-size:12px;cursor:pointer;"><input type="checkbox" id="heatToggle"/> Heatmap</label>
      <label style="font-size:12px;cursor:pointer;"><input type="checkbox" id="autoFitToggle" checked/> Auto-zoom</label>
    </div>

    <div class="section-title">Categories</div>
    <div id="categoryList"></div>

    <div style="display:flex;gap:6px;margin-top:14px;">
      <button class="btn btn-primary" id="openDownloadsModalBtn" type="button" style="flex:1;text-align:center;font-weight:600;">Downloads</button>
      <a class="btn" id="standaloneMapLink" href="1947/map.html" title="Standalone edition map" aria-label="Standalone edition map" style="display:inline-flex;align-items:center;justify-content:center;padding:5px 9px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>
    </div>

    <div class="license-box">
      Data: Victor H. Green &amp; Co. &middot; <a href="https://digitalcollections.nypl.org/collections/the-green-book" target="_blank">NYPL</a> (CC0) &middot; <a href="https://storymaps.arcgis.com/stories/a96fdcea2e9a4f7bb8da1220f76f1ec8" target="_blank">U. Redlands</a> &amp; <a href="https://www.loc.gov/item/2016298176/" target="_blank">LoC</a> &middot; <a href="https://digital.library.sc.edu/collections/the-negro-travelers-green-book-1956/" target="_blank">UofSC</a> (CC0) &middot; <a href="https://github.com/cengel/GreenBook" target="_blank">C. Engel</a> (CC BY-SA 4.0)
      <div style="display:flex;gap:5px;flex-wrap:wrap;margin-top:6px;">
        <button class="btn" id="openFaqModalBtn" type="button" style="font-size:11px;padding:3px 7px;">About / FAQ</button>
        <button class="btn" id="openLicenseModalBtn" type="button" style="font-size:11px;padding:3px 7px;">Licenses &amp; citations</button>
        <a class="btn" href="LICENSE.md" target="_blank" style="font-size:11px;padding:3px 7px;">LICENSE.md &nearr;</a>
        <a class="btn" href="README.md" target="_blank" style="font-size:11px;padding:3px 7px;">README.md &nearr;</a>
      </div>
    </div>
  </div>
  <div class="stats-bar">
    <span id="visibleCount">Loading...</span>
  </div>
</div>
<div id="map"></div>

<div class="modal-backdrop" id="downloadsModal">
  <div class="modal-content">
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <h2>Downloads (<span id="downloadsEditionLabel">1947</span>)</h2>
      <button class="btn" id="closeDownloadsModalBtn" type="button">Close &times;</button>
    </div>
    <div class="dl-tabs" id="dlTabs"></div>
    <div id="dlPanels"></div>
  </div>
</div>

<div class="modal-backdrop" id="faqModal">
  <div class="modal-content">
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <h2>About and frequently-asked questions</h2>
      <button class="btn" id="closeFaqModalBtn" type="button">Close &times;</button>
    </div>
    <h3>What is Green Book Atlas?</h3>
    <p><b>Green Book Atlas</b> (<a href="https://greenbookatlas.org" target="_blank">greenbookatlas.org</a>) contains interactive map overlays, geocoded directory datasets, and page-level OCR transcriptions for all 24 surviving geocoded editions of <i>The Negro Motorist Green Book</i> and <i>Travelers' Green Book</i>. This totals {unique_count:,} unique establishments across {total_raw_count:,} total listings, 1,734 OCR page pairs, and links to NYPL's 21 CC0 PDF volumes.</p>

    <h3>How do I use these overlays with Google Maps?</h3>
    <ol>
      <li>Click <b>Downloads</b> in the sidebar and download the split, Google-compatible KML files for your chosen edition (or <code>ALL</code>).</li>
      <li>Open <a href="https://www.google.com/mymaps" target="_blank">Google My Maps</a>, click <i>Create a new map</i> &rarr; <i>Add layer</i> &rarr; <i>Import</i>, and upload the file(s) from (1).</li>
      <li>Open regular Google Maps (under <i>Saved</i> &rarr; <i>Maps</i>) and select your newly-created map. Enter your trip in <i>Directions</i>, tap any Green Book pin along your route line, and select <i>Add stop</i>.</li>
    </ol>
    <p style="font-size:12px;color:var(--muted);">Note: Google Maps enforces a cap on features per layer, so some editions are split across multiple KML files.</p>

    <h3>Why does the "ALL" tab have {unique_count:,} sites instead of {total_raw_count:,}?</h3>
    <p>The "All" tab is deduplicated.</p>

    <h3>Why are 1936, 1942-1945, and 1965 missing?</h3>
    <p>Those editions either do not survive or were never published:</p>
    <ul>
      <li><b>1936</b>: No copy of the 1936 New York prototype edition is known to survive in any public archive.</li>
      <li><b>1942-1945</b>: Publication was suspended during World War II due to wartime rationing.</li>
      <li><b>1965</b>: The final two issues were published as multi-year editions (1963-64 and 1966-67).</li>
    </ul>

    <h3>Why are the 1966-67 PDF and some Internet Archive scans excluded?</h3>
    <ul>
      <li>The 1938 and 1940 versions available on Internet Archive prohibit derivative works. As such, we use NYPL's public-domain scans instead.</li>
      <li>NYPL does not provide 1966-1967 scans because they are still under copyright. We include the non-copyrightable factual directory listings.</li>
    </ul>

    <h3>Where can I find the raw data and source code?</h3>
    <p>On GitHub at <a href="https://github.com/ffleming/greenbookatlas.org" target="_blank">github.com/ffleming/greenbookatlas.org</a>.</p>
  </div>
</div>

<div class="modal-backdrop" id="licenseModal">
  <div class="modal-content">
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <h2>Licenses, attributions, and excluded datasets</h2>
      <button class="btn" id="closeLicenseModalBtn" type="button">Close &times;</button>
    </div>
    <p style="font-size:13px;color:var(--muted);margin:4px 0 12px 0;"><b>TL;DR:</b> Every file in this repository is cleared for public release under public-domain or open-access terms. Datasets with non-commercial or no-derivatives restrictions are excluded. Full details are in <a href="LICENSE.md" target="_blank">LICENSE.md</a>.</p>
    <table>
      <thead>
        <tr>
          <th>Source</th>
          <th>Files covered</th>
          <th>License</th>
          <th>Attribution / notes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Original historical volumes (1937-1967)</td>
          <td>Directory entries across all 24 editions</td>
          <td>U.S. Public Domain (1937-1963/64); uncopyrightable factual listings (1966-67)</td>
          <td>Victor H. Green &amp; Co. (Victor Hugo Green, Alma Duke Green, Novera C. Dashiell, Langley Waller), Harlem, NY (1936-1967).</td>
        </tr>
        <tr>
          <td>The New York Public Library (Schomburg Center &amp; NYPL Labs)</td>
          <td>1,734 <code>ocr/*.txt</code> &amp; <code>ocr/*.hocr</code> files, <code>full_text.txt</code>, <code>1947/supplemental/nypl_*</code>, and linked NYPL CC0 PDFs</td>
          <td><a href="https://creativecommons.org/publicdomain/zero/1.0/" target="_blank">CC0 1.0 Universal</a></td>
          <td>Schomburg Center for Research in Black Culture, The New York Public Library (<a href="https://github.com/NYPL-publicdomain/greenbooks" target="_blank">NYPL-publicdomain/greenbooks</a> &amp; <a href="https://github.com/NYPL-publicdomain/greenbook-map" target="_blank">greenbook-map</a>, Brian Foo).</td>
        </tr>
        <tr>
          <td>University of Redlands &amp; Library of Congress</td>
          <td>All 24 editions' <code>listings.csv</code>, <code>listings.json</code>, <code>overlay.kml</code>, <code>overlay.kmz</code>, <code>overlay.geojson</code>, <code>mymaps/*.kml</code> ({total_raw_count:,} listings; {unique_count:,} unique sites)</td>
          <td>Public educational &amp; research release (<code>access: "public"</code>, <code>licenseInfo: "None"</code>)</td>
          <td>Center for Spatial Studies, University of Redlands (<i>Mapping the Green Books</i>, <code>GreenbookLocations1937_1966</code>, Lisa Benvenuti et al.); Library of Congress (<a href="https://www.loc.gov/item/2016298176/" target="_blank">loc.gov/item/2016298176/</a>).</td>
        </tr>
        <tr>
          <td>University of South Carolina Libraries</td>
          <td><code>1956/supplemental/uofsc_*</code>, <code>library_sc_edu_*</code></td>
          <td><a href="https://creativecommons.org/publicdomain/zero/1.0/" target="_blank">CC0 1.0 Universal</a></td>
          <td>University of South Carolina Libraries Digital Collections (<a href="https://digital.library.sc.edu/collections/the-negro-travelers-green-book-1956/" target="_blank"><i>The Negro Travelers' Green Book, Spring 1956</i></a>).</td>
        </tr>
        <tr>
          <td>Claudia Engel / Stanford University</td>
          <td>Supplemental tables in 11 editions (<code>1937</code>-<code>1941</code>, <code>1946</code>-<code>1950</code>, <code>1952/supplemental/GreenBook*</code>)</td>
          <td><a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank">CC BY-SA 4.0</a></td>
          <td>Claudia Engel (<a href="https://github.com/cengel/GreenBook" target="_blank">github.com/cengel/GreenBook</a>). Primary <code>listings.*</code> and <code>overlay.*</code> files do not derive from this source.</td>
        </tr>
        <tr>
          <td>Mapping software &amp; basemap tiles</td>
          <td><code>index.html</code>, <code>&lt;edition&gt;/map.html</code></td>
          <td><a href="https://opensource.org/licenses/BSD-2-Clause" target="_blank">BSD 2-Clause</a> (Leaflet &amp; Leaflet.heat); provider terms</td>
          <td>Leaflet &copy; Volodymyr Agafonkin; tiles &copy; Google Maps, &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap contributors</a> (ODbL), &copy; <a href="https://carto.com/attributions" target="_blank">CARTO</a> (CC BY 3.0).</td>
        </tr>
        <tr>
          <td>Excluded datasets</td>
          <td><i>0 files in repository</i></td>
          <td>Excluded</td>
          <td>The 1938 and 1940 versions available on Internet Archive prohibit derivative works. As such, we use NYPL's public-domain scans instead. NYPL does not provide 1966-1967 scans because they are still under copyright. We include the non-copyrightable factual directory listings.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<script>
const META = {meta_json};
const UNIQUE_PTS = {pts_json};
const STYLES = {styles_json};

const mapLang = encodeURIComponent(navigator.language || 'en');
const googleStreets = L.tileLayer(`https://mt1.google.com/vt/lyrs=m&hl=${{mapLang}}&gl=US&x={{x}}&y={{y}}&z={{z}}`, {{
  maxZoom: 20,
  attribution: '&copy; Google Maps | NYPL Schomburg Center | Univ. of Redlands'
}});
const googleTerrain = L.tileLayer(`https://mt1.google.com/vt/lyrs=p&hl=${{mapLang}}&gl=US&x={{x}}&y={{y}}&z={{z}}`, {{
  maxZoom: 20,
  attribution: '&copy; Google Maps Terrain'
}});
const googleHybrid = L.tileLayer(`https://mt1.google.com/vt/lyrs=y&hl=${{mapLang}}&gl=US&x={{x}}&y={{y}}&z={{z}}`, {{
  maxZoom: 20,
  attribution: '&copy; Google Maps Satellite/Hybrid'
}});
const cartoDark = L.tileLayer('https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
  maxZoom: 20,
  attribution: '&copy; OpenStreetMap &copy; CARTO'
}});

const map = L.map('map', {{
  center: [38.5, -92.0],
  zoom: 4,
  layers: [googleStreets],
  preferCanvas: true
}});

L.control.layers({{
  "Google Maps Roadmap": googleStreets,
  "Google Maps Terrain": googleTerrain,
  "Google Maps Satellite Hybrid": googleHybrid,
  "Dark Historical Theme": cartoDark
}}, null, {{ position: 'topright' }}).addTo(map);

const markerLayer = L.layerGroup().addTo(map);
let heatLayer = null;
function getSavedEdition() {{
  const m = document.cookie.match(/(?:^|;\s*)gb_edition=([^;]*)/);
  const val = m ? decodeURIComponent(m[1]) : '';
  return (val === 'ALL' || META.some(x => x.edition === val)) ? val : 'ALL';
}}
let currentEdition = getSavedEdition();
const activeCats = new Set(Object.keys(STYLES));

function escapeHtml(s) {{
  return String(s || '').replace(/[&<>"']/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));
}}

function formatEditions(eds) {{
  if (!eds || !eds.length) return '';
  const runs = [[eds[0], eds[0]]];
  for (let i = 1; i < eds.length; i++) {{
    const e = eds[i];
    const prev = runs[runs.length - 1][1];
    if (!e.includes('-') && !prev.includes('-') && Number(e) === Number(prev) + 1) {{
      runs[runs.length - 1][1] = e;
    }} else {{
      runs.push([e, e]);
    }}
  }}
  return runs.map(r => r[0] === r[1] ? r[0] : `${{r[0]}}-${{r[1]}}`).join(', ');
}}

// Compute per-edition counts from UNIQUE_PTS
const edCounts = {{}};
UNIQUE_PTS.forEach(p => {{
  p[14].forEach(ed => {{
    edCounts[ed] = (edCounts[ed] || 0) + 1;
  }});
}});

const pillsEl = document.getElementById('editionPills');
META.forEach(m => {{
  const btn = document.createElement('div');
  btn.className = 'ed-pill' + (m.edition === currentEdition ? ' active' : '');
  btn.dataset.ed = m.edition;
  const cnt = edCounts[m.edition] || m.total_records;
  btn.innerHTML = `${{m.edition}}<span>${{cnt.toLocaleString()}}</span>`;
  btn.addEventListener('click', () => selectEdition(m.edition));
  pillsEl.appendChild(btn);
}});

const allBtn = document.createElement('div');
allBtn.className = 'ed-pill' + (currentEdition === 'ALL' ? ' active' : '');
allBtn.dataset.ed = 'ALL';
allBtn.innerHTML = `ALL<span>${{UNIQUE_PTS.length.toLocaleString()}}</span>`;
allBtn.addEventListener('click', () => selectEdition('ALL'));
pillsEl.appendChild(allBtn);

function getActivePoints() {{
  if (currentEdition === 'ALL') {{
    return UNIQUE_PTS;
  }}
  return UNIQUE_PTS.filter(p => p[14].includes(currentEdition));
}}

function triggerBlobDownload(filename, content, mimeType) {{
  const blob = new Blob([content], {{ type: mimeType }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  setTimeout(() => {{
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }}, 200);
}}

function buildKmlFromPoints(pts, docName) {{
  let xml = '<?xml version="1.0" encoding="UTF-8"?>\\n<kml xmlns="http://www.opengis.net/kml/2.2">\\n<Document>\\n';
  xml += `<name>${{escapeHtml(docName)}}</name>\\n`;
  Object.entries(STYLES).forEach(([, st]) => {{
    xml += `<Style id="${{st.id}}"><IconStyle><color>${{st.kml_color}}</color><scale>1.0</scale><Icon><href>${{st.icon}}</href></Icon></IconStyle></Style>\\n`;
  }});
  pts.forEach(p => {{
    const [lat, lon, name, btype, cat, addr, city, state, country, owner, gender, bnotes, enotes, , eds] = p;
    const st = STYLES[cat] || STYLES["Retail, Services & Other"];
    const edSpan = formatEditions(eds);
    const loc = [addr, city, state, country].filter(Boolean).join(', ');
    const desc = `${{btype || st.short}} | ${{loc}} | Editions (${{eds.length}}): ${{edSpan}}`;
    xml += `<Placemark><name>${{escapeHtml(name || 'Unnamed')}}</name><styleUrl>#${{st.id}}</styleUrl><description>${{escapeHtml(desc)}}</description><Point><coordinates>${{lon}},${{lat}},0</coordinates></Point></Placemark>\\n`;
  }});
  xml += '</Document>\\n</kml>';
  return xml;
}}

window.downloadUniqueKml = function(partIdx, totalParts) {{
  const maxPerFile = 1900;
  if (typeof partIdx === 'number') {{
    const chunk = UNIQUE_PTS.slice(partIdx * maxPerFile, (partIdx + 1) * maxPerFile);
    const kml = buildKmlFromPoints(chunk, `Green Book Atlas Unique Sites - Part ${{partIdx + 1}} of ${{totalParts}} (${{chunk.length}})`);
    triggerBlobDownload(`greenbook_all_unique_mymaps_part${{partIdx + 1}}_of_${{totalParts}}.kml`, kml, 'application/vnd.google-earth.kml+xml');
  }} else {{
    const kml = buildKmlFromPoints(UNIQUE_PTS, `Green Book Atlas - All 24 Editions (${{UNIQUE_PTS.length}} Unique Sites)`);
    triggerBlobDownload('greenbook_all_unique.kml', kml, 'application/vnd.google-earth.kml+xml');
  }}
}};

window.downloadUniqueGeoJson = function() {{
  const fc = {{
    type: 'FeatureCollection',
    features: UNIQUE_PTS.map((p, idx) => ({{
      type: 'Feature',
      id: idx + 1,
      geometry: {{ type: 'Point', coordinates: [p[1], p[0]] }},
      properties: {{
        name: p[2], business_type: p[3], category_group: p[4],
        address: p[5], city: p[6], state: p[7], country: p[8],
        owner_name: p[9], owner_gender: p[10], book_notes: p[11],
        data_editor_notes: p[12], source_type: p[13],
        editions: p[14], edition_count: p[14].length, edition_span: formatEditions(p[14])
      }}
    }}))
  }};
  triggerBlobDownload('greenbook_all_unique.geojson', JSON.stringify(fc), 'application/geo+json');
}};

window.downloadUniqueCsv = function() {{
  const headers = ['latitude','longitude','business_name','business_type','category_group','address','city','state','country','owner_name','owner_gender','book_notes','data_editor_notes','source_type','edition_count','editions'];
  const csvEsc = v => `"${{String(v ?? '').replace(/"/g, '""')}}"`;
  const rows = [headers.join(',')];
  UNIQUE_PTS.forEach(p => {{
    rows.push([p[0],p[1],csvEsc(p[2]),csvEsc(p[3]),csvEsc(p[4]),csvEsc(p[5]),csvEsc(p[6]),csvEsc(p[7]),csvEsc(p[8]),csvEsc(p[9]),csvEsc(p[10]),csvEsc(p[11]),csvEsc(p[12]),csvEsc(p[13]),p[14].length,csvEsc(p[14].join(';'))].join(','));
  }});
  triggerBlobDownload('greenbook_all_unique.csv', rows.join('\\n'), 'text/csv;charset=utf-8');
}};

window.downloadUniqueJson = function() {{
  const records = UNIQUE_PTS.map((p, idx) => ({{
    id: idx + 1,
    latitude: p[0], longitude: p[1],
    business_name: p[2], business_type: p[3], category_group: p[4],
    address: p[5], city: p[6], state: p[7], country: p[8],
    owner_name: p[9], owner_gender: p[10], book_notes: p[11],
    data_editor_notes: p[12], source_type: p[13],
    edition_count: p[14].length, editions: p[14]
  }}));
  triggerBlobDownload('greenbook_all_unique.json', JSON.stringify(records, null, 2), 'application/json');
}};

let activeDlTab = 'kml';
function bindDlTabs() {{
  document.querySelectorAll('#dlTabs button[data-dltab]').forEach(btn => {{
    btn.addEventListener('click', () => {{
      activeDlTab = btn.dataset.dltab;
      document.querySelectorAll('#dlTabs button[data-dltab]').forEach(b => b.classList.toggle('active', b === btn));
      document.querySelectorAll('#dlPanels .dl-panel').forEach(p => p.classList.toggle('active', p.dataset.dlpanel === activeDlTab));
    }});
  }});
}}

function selectEdition(ed) {{
  currentEdition = ed;
  document.cookie = `gb_edition=${{encodeURIComponent(ed)}}; path=/; max-age=31536000; SameSite=Lax`;
  document.querySelectorAll('.ed-pill').forEach(el => {{
    el.classList.toggle('active', el.dataset.ed === ed);
  }});
  updateEditionCardAndFilters();
  renderMap(document.getElementById('autoFitToggle').checked);
}}

function updateEditionCardAndFilters() {{
  const card = document.getElementById('editionCard');
  const dlTabs = document.getElementById('dlTabs');
  const dlPanels = document.getElementById('dlPanels');
  const dlEdLabel = document.getElementById('downloadsEditionLabel');
  const standaloneLink = document.getElementById('standaloneMapLink');
  const pts = getActivePoints();
  const linkIconSvg = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>';

  if (currentEdition === 'ALL') {{
    card.innerHTML = `<span><b>All 24 editions (1937-1967)</b> &middot; ${{UNIQUE_PTS.length.toLocaleString()}} sites</span>`;
    if (dlEdLabel) dlEdLabel.textContent = 'All 24 editions';
    if (standaloneLink) standaloneLink.style.display = 'none';
    if (!['kml','geojson','csv','json'].includes(activeDlTab)) activeDlTab = 'kml';
    const numParts = Math.ceil(UNIQUE_PTS.length / 1900);
    let partBtns = '';
    for (let i = 0; i < numParts; i++) {{
      partBtns += `<button class="btn btn-primary" type="button" onclick="downloadUniqueKml(${{i}}, ${{numParts}})">Download ALL KML ${{i + 1}} of ${{numParts}}</button>`;
    }}
    dlTabs.innerHTML = `
      <button class="dl-tab ${{activeDlTab === 'kml' ? 'active' : ''}}" type="button" data-dltab="kml">KML</button>
      <button class="dl-tab ${{activeDlTab === 'geojson' ? 'active' : ''}}" type="button" data-dltab="geojson">GeoJSON</button>
      <button class="dl-tab ${{activeDlTab === 'csv' ? 'active' : ''}}" type="button" data-dltab="csv">CSV</button>
      <button class="dl-tab ${{activeDlTab === 'json' ? 'active' : ''}}" type="button" data-dltab="json">JSON</button>
    `;
    dlPanels.innerHTML = `
      <div class="dl-panel ${{activeDlTab === 'kml' ? 'active' : ''}}" data-dlpanel="kml">
        <h3>Download full KML</h3>
        <div class="btn-group">
          <button class="btn btn-primary" type="button" onclick="downloadUniqueKml()">Download full KML</button>
        </div>
        <h3>Download Google Maps split KML</h3>
        <div class="btn-group">${{partBtns}}</div>
      </div>
      <div class="dl-panel ${{activeDlTab === 'geojson' ? 'active' : ''}}" data-dlpanel="geojson">
        <button class="btn btn-primary" type="button" onclick="downloadUniqueGeoJson()">Download GeoJSON</button>
      </div>
      <div class="dl-panel ${{activeDlTab === 'csv' ? 'active' : ''}}" data-dlpanel="csv">
        <button class="btn btn-primary" type="button" onclick="downloadUniqueCsv()">Download CSV</button>
      </div>
      <div class="dl-panel ${{activeDlTab === 'json' ? 'active' : ''}}" data-dlpanel="json">
        <button class="btn btn-primary" type="button" onclick="downloadUniqueJson()">Download JSON</button>
      </div>
    `;
    bindDlTabs();
  }} else {{
    const m = META.find(x => x.edition === currentEdition);
    card.innerHTML = `<span><b>${{escapeHtml(m.edition)}}</b> &middot; ${{pts.length.toLocaleString()}} sites</span><span style="display:inline-flex;align-items:center;gap:8px;"><a href="${{m.edition}}/map.html" title="Standalone ${{m.edition}} map" style="color:var(--accent-light);display:inline-flex;align-items:center;">${{linkIconSvg}}</a><a href="${{escapeHtml(m.nypl_collection_url)}}" target="_blank" style="color:var(--accent-light);text-decoration:none;">NYPL &nearr;</a></span>`;
    if (dlEdLabel) dlEdLabel.textContent = m.edition;
    if (standaloneLink) {{
      standaloneLink.href = `${{m.edition}}/map.html`;
      standaloneLink.title = `Standalone ${{m.edition}} map`;
      standaloneLink.style.display = 'inline-flex';
    }}
    const hasOcr = m.txt_count > 0;
    if (activeDlTab === 'ocr' && !hasOcr) activeDlTab = 'kml';
    const mFiles = m.mymaps_files || [];
    const splitBtns = mFiles.map((mf, idx) => `<a class="btn btn-primary" href="${{m.edition}}/${{mf}}" download>Download ${{m.edition}} KML ${{idx + 1}} of ${{mFiles.length}}</a>`).join('');
    dlTabs.innerHTML = `
      <button class="dl-tab ${{activeDlTab === 'kml' ? 'active' : ''}}" type="button" data-dltab="kml">KML</button>
      <button class="dl-tab ${{activeDlTab === 'kmz' ? 'active' : ''}}" type="button" data-dltab="kmz">KMZ</button>
      <button class="dl-tab ${{activeDlTab === 'geojson' ? 'active' : ''}}" type="button" data-dltab="geojson">GeoJSON</button>
      <button class="dl-tab ${{activeDlTab === 'csv' ? 'active' : ''}}" type="button" data-dltab="csv">CSV</button>
      <button class="dl-tab ${{activeDlTab === 'json' ? 'active' : ''}}" type="button" data-dltab="json">JSON</button>
      ${{hasOcr ? `<button class="dl-tab ${{activeDlTab === 'ocr' ? 'active' : ''}}" type="button" data-dltab="ocr">OCR text</button>` : ''}}
      ${{m.pdf_url ? `<a class="dl-tab" href="${{m.pdf_url}}" target="_blank">PDF (${{(m.pdf_bytes/1048576).toFixed(1)}} MB) &nearr;</a>` : ''}}
    `;
    dlPanels.innerHTML = `
      <div class="dl-panel ${{activeDlTab === 'kml' ? 'active' : ''}}" data-dlpanel="kml">
        <h3>Download full KML</h3>
        <div class="btn-group">
          <a class="btn btn-primary" href="${{m.edition}}/overlay.kml" download="greenbook_${{m.edition}}.kml">Download full KML</a>
        </div>
        <h3>Download Google Maps split KML</h3>
        <div class="btn-group">${{splitBtns}}</div>
      </div>
      <div class="dl-panel ${{activeDlTab === 'kmz' ? 'active' : ''}}" data-dlpanel="kmz">
        <a class="btn btn-primary" href="${{m.edition}}/overlay.kmz" download="greenbook_${{m.edition}}.kmz">Download KMZ</a>
      </div>
      <div class="dl-panel ${{activeDlTab === 'geojson' ? 'active' : ''}}" data-dlpanel="geojson">
        <a class="btn btn-primary" href="${{m.edition}}/overlay.geojson" download="greenbook_${{m.edition}}.geojson">Download GeoJSON</a>
      </div>
      <div class="dl-panel ${{activeDlTab === 'csv' ? 'active' : ''}}" data-dlpanel="csv">
        <a class="btn btn-primary" href="${{m.edition}}/listings.csv" download="greenbook_${{m.edition}}.csv">Download CSV</a>
      </div>
      <div class="dl-panel ${{activeDlTab === 'json' ? 'active' : ''}}" data-dlpanel="json">
        <a class="btn btn-primary" href="${{m.edition}}/listings.json" download="greenbook_${{m.edition}}.json">Download JSON</a>
      </div>
      ${{hasOcr ? `<div class="dl-panel ${{activeDlTab === 'ocr' ? 'active' : ''}}" data-dlpanel="ocr"><a class="btn btn-primary" href="${{m.edition}}/full_text.txt" download="greenbook_${{m.edition}}_ocr.txt">Download OCR text</a></div>` : ''}}
    `;
    bindDlTabs();
  }}

  const stateCounts = {{}};
  const catCounts = {{}};
  pts.forEach(p => {{
    const st = p[7] ? `${{p[7]}} (${{p[8] || 'USA'}})` : (p[8] || 'Unspecified');
    stateCounts[st] = (stateCounts[st] || 0) + 1;
    catCounts[p[4]] = (catCounts[p[4]] || 0) + 1;
  }});

  const stateSelect = document.getElementById('stateSelect');
  const prevState = stateSelect.value;
  stateSelect.innerHTML = '<option value="">All states &amp; countries</option>';
  Object.keys(stateCounts).sort().forEach(st => {{
    const opt = document.createElement('option');
    opt.value = st;
    opt.textContent = `${{st}} (${{stateCounts[st]}})`;
    stateSelect.appendChild(opt);
  }});
  if (stateCounts[prevState]) stateSelect.value = prevState;

  const catList = document.getElementById('categoryList');
  catList.innerHTML = '';
  Object.entries(STYLES).forEach(([catName, st]) => {{
    const cnt = catCounts[catName] || 0;
    const row = document.createElement('label');
    row.className = 'cat-item';
    row.innerHTML = `
      <span class="cat-left">
        <input type="checkbox" ${{activeCats.has(catName) ? 'checked' : ''}} data-cat="${{catName}}"/>
        <span class="swatch" style="background:${{st.hex}}"></span>
        <span>${{st.short}}</span>
      </span>
      <span class="count-pill">${{cnt.toLocaleString()}}</span>
    `;
    row.querySelector('input').addEventListener('change', (e) => {{
      if (e.target.checked) activeCats.add(catName);
      else activeCats.delete(catName);
      renderMap(false);
    }});
    catList.appendChild(row);
  }});
}}

function renderMap(fitBounds = false) {{
  markerLayer.clearLayers();
  if (heatLayer) {{
    map.removeLayer(heatLayer);
    heatLayer = null;
  }}
  const pts = getActivePoints();
  const q = document.getElementById('searchInput').value.trim().toLowerCase();
  const stFilter = document.getElementById('stateSelect').value;
  const showHeat = document.getElementById('heatToggle').checked;

  const bounds = [];
  const heatPts = [];
  let shown = 0;

  pts.forEach(p => {{
    const [lat, lon, name, btype, cat, addr, city, state, country, owner, gender, bnotes, enotes, , eds] = p;
    if (!activeCats.has(cat)) return;
    const stKey = state ? `${{state}} (${{country || 'USA'}})` : (country || 'Unspecified');
    if (stFilter && stKey !== stFilter) return;
    if (q) {{
      const hay = `${{name}} ${{btype}} ${{addr}} ${{city}} ${{state}} ${{owner}} ${{bnotes}} ${{enotes}}`.toLowerCase();
      if (!hay.includes(q)) return;
    }}

    shown++;
    bounds.push([lat, lon]);
    heatPts.push([lat, lon, 0.8]);

    const st = STYLES[cat] || STYLES["Retail, Services & Other"];
    const marker = L.circleMarker([lat, lon], {{
      radius: currentEdition === 'ALL' ? 4.5 : 6,
      fillColor: st.hex,
      color: '#ffffff',
      weight: 1,
      opacity: 0.9,
      fillOpacity: 0.85
    }});

    let popupHtml = `<div class="popup-title">${{escapeHtml(name)}}</div><div class="popup-meta">`;
    popupHtml += `<div>${{escapeHtml(btype || st.short)}}</div>`;
    popupHtml += `<div>${{escapeHtml([addr, city, state, country].filter(Boolean).join(', '))}}</div>`;
    popupHtml += `<div><b>Editions (${{eds.length}}):</b> ${{escapeHtml(formatEditions(eds))}}</div>`;
    if (owner && owner.toLowerCase() !== 'unknown') {{
      popupHtml += `<div><b>Owner:</b> ${{escapeHtml(owner)}}${{gender && gender.toLowerCase() !== 'unknown' ? ' (' + escapeHtml(gender) + ')' : ''}}</div>`;
    }}
    if (bnotes) popupHtml += `<div><b>Notes:</b> ${{escapeHtml(bnotes)}}</div>`;
    if (enotes) popupHtml += `<div><b>Archival:</b> ${{escapeHtml(enotes)}}</div>`;
    popupHtml += `<div style="margin-top:6px;"><a href="https://www.google.com/maps/search/?api=1&query=${{encodeURIComponent((addr ? addr + ', ' : '') + city + ' ' + state)}}" target="_blank" style="color:#81c784;">Open in Google Maps &nearr;</a></div>`;
    popupHtml += `</div>`;

    marker.bindPopup(popupHtml);
    markerLayer.addLayer(marker);
  }});

  if (showHeat && heatPts.length > 0 && typeof L.heatLayer === 'function') {{
    heatLayer = L.heatLayer(heatPts, {{ radius: 22, blur: 16, maxZoom: 12 }}).addTo(map);
  }}

  if (fitBounds && bounds.length > 0) {{
    map.fitBounds(bounds, {{ padding: [30, 30], maxZoom: 13 }});
  }}

  document.getElementById('visibleCount').textContent = `${{shown.toLocaleString()}} / ${{pts.length.toLocaleString()}} shown (${{currentEdition}})`;
}}

document.getElementById('searchInput').addEventListener('input', () => renderMap(false));
document.getElementById('stateSelect').addEventListener('change', () => renderMap(true));
document.getElementById('heatToggle').addEventListener('change', () => renderMap(false));

const licModal = document.getElementById('licenseModal');
document.getElementById('openLicenseModalBtn').addEventListener('click', () => licModal.classList.add('open'));
document.getElementById('closeLicenseModalBtn').addEventListener('click', () => licModal.classList.remove('open'));
licModal.addEventListener('click', (e) => {{ if (e.target === licModal) licModal.classList.remove('open'); }});

const dlModal = document.getElementById('downloadsModal');
document.getElementById('openDownloadsModalBtn').addEventListener('click', () => dlModal.classList.add('open'));
document.getElementById('closeDownloadsModalBtn').addEventListener('click', () => dlModal.classList.remove('open'));
dlModal.addEventListener('click', (e) => {{ if (e.target === dlModal) dlModal.classList.remove('open'); }});

const faqModal = document.getElementById('faqModal');
document.getElementById('openFaqModalBtn').addEventListener('click', () => faqModal.classList.add('open'));
document.getElementById('closeFaqModalBtn').addEventListener('click', () => faqModal.classList.remove('open'));
faqModal.addEventListener('click', (e) => {{ if (e.target === faqModal) faqModal.classList.remove('open'); }});

updateEditionCardAndFilters();
renderMap(true);
</script>
</body>
</html>
"""


def main():
    if os.path.exists(OVERLAYS_DIR):
        shutil.rmtree(OVERLAYS_DIR)
    all_editions_meta = []
    editions_records = []
    total_raw_count = 0

    for ed_dir in EDITION_DIRS:
        ed_path = os.path.join(BASE_DIR, ed_dir)
        listings_path = os.path.join(ed_path, "listings.json")
        with open(listings_path, "r", encoding="utf-8") as f:
            ed_data = json.load(f)

        recs = valid_records(ed_data["records"])
        total_raw_count += len(recs)
        editions_records.append((ed_dir, recs))
        print(f"[*] Building overlays for {ed_dir} ({len(recs)} valid geocoded points)...")

        # 1. GeoJSON
        geojson_obj = build_geojson(ed_data, recs)
        geojson_path = os.path.join(ed_path, "overlay.geojson")
        with open(geojson_path, "w", encoding="utf-8") as gf:
            json.dump(geojson_obj, gf, indent=2)

        # 2. Full KML
        kml_str = build_kml_document(
            ed_data["title"],
            ed_data["historical_context"],
            recs,
            ed_dir,
            group_by_category=True,
        )
        kml_path = os.path.join(ed_path, "overlay.kml")
        with open(kml_path, "w", encoding="utf-8") as kf:
            kf.write(kml_str)

        # 3. Compressed KMZ
        kmz_path = os.path.join(ed_path, "overlay.kmz")
        with zipfile.ZipFile(kmz_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("doc.kml", kml_str.encode("utf-8"))

        # 4. Google My Maps <=2,000-feature split KMLs
        mymaps_files = write_mymaps_splits(ed_path, ed_data, recs)

        # 5. Standalone interactive HTML map
        map_html = build_edition_map_html(ed_data, recs, mymaps_files)
        with open(os.path.join(ed_path, "map.html"), "w", encoding="utf-8") as mf:
            mf.write(map_html)

        # 6. Edition README.md
        readme_md = build_edition_readme(ed_data, mymaps_files)
        with open(os.path.join(ed_path, "README.md"), "w", encoding="utf-8") as rf:
            rf.write(readme_md)

        nypl = ed_data.get("nypl_archival_assets", {})
        pdf_url = nypl.get("pdf_url") or (
            f"https://raw.githubusercontent.com/NYPL-publicdomain/greenbooks/master/{ed_dir}.pdf"
            if nypl.get("pdf_file")
            else None
        )
        local_pdf = os.path.join(ed_path, f"{ed_dir}.pdf")
        if os.path.exists(local_pdf):
            os.remove(local_pdf)
        all_editions_meta.append({
            "edition": ed_dir,
            "title": ed_data["title"],
            "role": ed_data["role"],
            "historical_context": ed_data["historical_context"],
            "nypl_collection_url": ed_data["nypl_collection_url"],
            "total_records": ed_data["total_records"],
            "valid_coordinates_count": len(recs),
            "pdf_url": pdf_url,
            "pdf_bytes": nypl.get("pdf_bytes", 0),
            "txt_count": nypl.get("txt_count", 0),
            "hocr_count": nypl.get("hocr_count", 0),
            "mymaps_files": mymaps_files,
        })

    unique_pts = deduplicate_across_editions(editions_records)
    print(f"[*] Deduplicated {total_raw_count} raw records -> {len(unique_pts)} unique sites across 24 editions.")

    # Build unified multi-edition index.html
    master_html = build_master_index_html(all_editions_meta, unique_pts, total_raw_count)
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as mhf:
        mhf.write(master_html)

    print("[+] Successfully generated all KML, KMZ, My Maps splits, GeoJSON, HTML maps, and READMEs.")


if __name__ == "__main__":
    main()
