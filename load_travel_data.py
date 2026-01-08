import sqlite3
import csv

# Connect to SQLite
conn = sqlite3.connect('travel.db')
cursor = conn.cursor()

# Drop old table if exists (for re-runs)
cursor.execute("DROP TABLE IF EXISTS travel")

# Create table
cursor.execute('''
    CREATE TABLE travel (
        Country TEXT,
        CostPerDay INTEGER,
        VisaFree TEXT,
        Rating REAL,
        BestMonth TEXT
    )
''')

# Load CSV
with open('travel_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [(row['Country'], int(row['CostPerDay']), row['VisaFree'], float(row['Rating']), row['BestMonth']) for row in reader]

cursor.executemany("INSERT INTO travel VALUES (?, ?, ?, ?, ?);", data)
conn.commit()

print("Data loaded successfully!")

# print("\nBudget countries under $70/day:")
# for row in cursor.execute("SELECT Country, CostPerDay FROM travel WHERE CostPerDay < 70;"):
#     print(row)

# print("\nVisa-free countries rated 4.6+:")
# for row in cursor.execute("SELECT Country FROM travel WHERE VisaFree = 'Yes' AND Rating >= 4.6;"):
#     print(row)

print("\nTop 3 cheapest visa free countries (by cost/day):")
for row in cursor.execute("""
    SELECT Country, CostPerDay
    FROM travel
    WHERE VisaFree = 'Yes'
    ORDER BY CostPerDay ASC
    LIMIT 3;
"""):
    print(row)

print("\nTop 3 highest rated destinations:")
for row in cursor.execute("""
    SELECT Country, Rating
    FROM travel
    ORDER BY Rating DESC
    LIMIT 3;
"""):
    print(row)


conn.close()
