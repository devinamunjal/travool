import argparse
import sqlite3
import pandas as pd
from tabulate import tabulate

def main():
    # --- Parse CLI args ---
    parser = argparse.ArgumentParser(
        description="Filter travel destinations using clean CLI arguments"
    )
    parser.add_argument("--max-cost", type=int, help="Max cost per day (e.g. 100)")
    parser.add_argument("--visa-free", choices=["yes", "no"], help="Visa-free only? (yes/no)")
    parser.add_argument("--min-rating", type=float, help="Minimum destination rating (e.g. 4.5)")
    parser.add_argument(
        "--optimize-for",
        choices=["value", "rating", "budget"],
        help="Optimization focus: value (default), rating, or budget"
    )
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
    print("\nbRunning query with filters:")
    print("  Max Cost:", args.max_cost)
    print("  Visa Free:", args.visa_free)
    print("  Min Rating:", args.min_rating)
    print("  Optimize For:", args.optimize_for or "value (default)")

    try:
        # --- Execute query ---
        conn = sqlite3.connect("travel.db")
        df = pd.read_sql_query(query, conn, params=tuple(params))
        conn.close()

        if df.empty:
            print("\m Matching Results:")
            print("No results found.")
            return

        # --- Scoring logic: normalize + weight ---
        cost_max = df["CostPerDay"].max()
        cost_min = df["CostPerDay"].min()
        rating_max = df["Rating"].max()
        rating_min = df["Rating"].min()

        # Avoid division by zero
        df["NormCost"] = (cost_max - df["CostPerDay"]) / max(1, (cost_max - cost_min))
        df["NormRating"] = (df["Rating"] - rating_min) / max(1, (rating_max - rating_min))
        df["VisaBoost"] = df["VisaFree"].str.lower().eq("yes").astype(int)

        # Default weights: "value"
        w_cost, w_rating, w_visa = 0.4, 0.4, 0.2
  
        if args.optimize_for == "rating":
            w_cost, w_rating, w_visa = 0.2, 0.6, 0.2
        elif args.optimize_for == "budget":
            w_cost, w_rating, w_visa = 0.6, 0.25, 0.15

        df["Score"] = (
            w_cost * df["NormCost"]
            + w_rating * df["NormRating"]
            + w_visa * df["VisaBoost"]
        )

        df = df.sort_values("Score", ascending=False)

        # --- Summary stats ---
        avg_cost = df["CostPerDay"].mean()
        avg_rating = df["Rating"].mean()

        print(f"\n📈 Summary for {len(df)} matching destinations:")
        print(f"  • Avg cost per day: ${avg_cost:.0f}")
        print(f"  • Avg rating: {avg_rating:.2f}")

        # --- Display clean results ---
        print("\n Matching Results:")
        display_cols = ["Country", "CostPerDay", "VisaFree", "Rating", "BestMonth", "Score"]
        print(tabulate(df[display_cols], headers="keys", tablefmt="fancy_grid", showindex=False))

    except Exception as e:
        print("❌ Error executing query:", e)

if __name__ == "__main__":
    main()
