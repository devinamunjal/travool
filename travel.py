
import argparse
import sqlite3
import pandas as pd
from tabulate import tabulate

def main():
    # --- Parse CLI args ---
    parser = argparse.ArgumentParser(description="Filter travel destinations using clean CLI arguments")
    parser.add_argument("--max-cost", type=int, help="Max cost per day (e.g. 100)")
    parser.add_argument("--visa-free", choices=["yes", "no"], help="Visa-free only? (yes/no)")
    parser.add_argument("--min-rating", type=float, help="Minimum destination rating (e.g. 4.5)")
    args = parser.parse_args()

    # --- Build query and params ---
    query = "SELECT * FROM travel WHERE 1=1"
    params = []

    if args.max_cost is not None:
        query += " AND CostPerDay <= ?"
        params.append(args.max_cost)

    if args.visa_free is not None:
        query += " AND LOWER(VisaFree) = ?"
        params.append(args.visa_free.lower())

    if args.min_rating is not None:
        query += " AND Rating >= ?"
        params.append(args.min_rating)

    # --- Show query and params ---
    print("\n🔍 Running query with filters:")
    print("  Max Cost:", args.max_cost)
    print("  Visa Free:", args.visa_free)
    print("  Min Rating:", args.min_rating)

    try:
        # --- Execute query ---
        conn = sqlite3.connect("travel.db")
        df = pd.read_sql_query(query, conn, params=tuple(params))
        conn.close()

        print("\n📊 Matching Results:")
        if df.empty:
            print("❌ No results found.")
        else:
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
    except Exception as e:
        print("❌ Error executing query:", e)

if __name__ == "__main__":
    main()
