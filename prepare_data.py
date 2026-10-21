"""Prepare locally obtained retail CSVs for retail_eda_cleaned.ipynb.

Usage: python prepare_data.py --input path/to/raw_csv_folder
Input files: events.csv, products.csv, countries.csv
No original input files are modified.
"""
from pathlib import Path
import argparse
import pandas as pd


def normalize_headers(frame):
    frame = frame.copy()
    frame.columns = [str(c).strip().lower().replace(" ", "_").replace("-", "_") for c in frame.columns]
    return frame


def text_codes(series):
    return series.astype("string").str.strip().str.upper().replace({"": pd.NA, "#N/A": pd.NA, "UNKNOWN": pd.NA})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Directory containing original CSVs")
    parser.add_argument("--output", type=Path, default=Path("data_clean"))
    args = parser.parse_args()
    frames = {name: normalize_headers(pd.read_csv(args.input / (name + ".csv"))) for name in ("countries", "events", "products")}
    countries, events, products = (frames[k] for k in ("countries", "events", "products"))
    countries = countries.rename(columns={"alpha_3": "country_code"})
    products = products.rename(columns={"id": "product_id"})
    for key in ("name", "alpha_2", "country_code", "region", "sub_region"):
        if key in countries:
            countries[key] = text_codes(countries[key])
    events["country_code"] = text_codes(events["country_code"])
    events["sales_channel"] = text_codes(events["sales_channel"])
    events["order_priority"] = text_codes(events["order_priority"])
    for column in ("order_date", "ship_date"):
        events[column] = pd.to_datetime(events[column], errors="raise").dt.strftime("%Y-%m-%d")
    for column in ("units_sold", "unit_price", "unit_cost"):
        events[column] = pd.to_numeric(events[column], errors="coerce")
    products["item_type"] = products["item_type"].astype("string").str.strip()
    if countries.country_code.dropna().duplicated().any() or products.product_id.dropna().duplicated().any():
        raise ValueError("Duplicate country or product lookup keys")
    if events.order_id.duplicated().any():
        raise ValueError("Duplicate order IDs")
    if not set(events.sales_channel.dropna()) <= {"ONLINE", "OFFLINE"}:
        raise ValueError("Unrecognized sales channel values")
    args.output.mkdir(parents=True, exist_ok=True)
    for name, frame in (("countries", countries), ("events", events), ("products", products)):
        frame.to_csv(args.output / (name + ".csv"), index=False)
        print(f"{name}: {len(frame)} rows")
    print(f"Missing quantities: {events.units_sold.isna().sum()}; missing country codes: {events.country_code.isna().sum()}")
    print(f"Prepared inputs in {args.output.resolve()}")


if __name__ == "__main__":
    main()
