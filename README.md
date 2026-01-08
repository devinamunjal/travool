# travool — Travel Recommendations from the Command Line

travool is a Python-based command-line tool that recommends travel destinations based on budget, visa requirements, and personal preferences. I built it to practice working with real data, SQL, and CLI design — and to create something I’d actually use.

Instead of interactive prompts, travool is fully flag-driven, making it easy to query, filter, and extend.

What travool does

Filters destinations by:

Daily cost

Visa-free access

Traveler rating

Queries a real SQLite database built from CSV data

Displays results in clean, readable tables directly in the terminal

Designed to be simple, predictable, and easy to modify

How it works

The data flow looks like this:

CSV → pandas → SQLite → SQL queries → pandas → terminal output


Each step is intentionally kept simple and debuggable.

## Project Structure
.
├── travel_data.csv          # Raw destination data
├── load_travel_data.py      # Loads and cleans data into SQLite
├── travel.db                # SQLite database
├── travel_final_cli.py      # CLI entry point (argparse-based)

Example Usage
python travel_final_cli.py --max-cost 100 --visa-free yes --min-rating 4.5


Example output:

Matching Results:
╒══════════════╤══════════════╤═════════════╤══════════╕
│ Country      │ CostPerDay   │ VisaFree    │ Rating   │
╘══════════════╧══════════════╧═════════════╧══════════╛
│ Portugal     │ 75           │ Yes         │ 4.8      │
│ Thailand     │ 65           │ Yes         │ 4.7      │

## What I added & improved over time

This project evolved as I worked on it. Along the way, I:

Refactored the CLI to rely fully on argparse

Improved SQL querying using parameterized queries

Made filtering logic more flexible and readable

Cleaned up data loading and validation

Improved output formatting using tabulate

Reorganized code for clarity and maintainability

Things I struggled with (and learned)

Moving from interactive input to a proper CLI

Building dynamic SQL queries safely

Designing flags that feel intuitive to use

Debugging data issues between CSV, SQLite, and Python

Formatting terminal output so it’s actually readable

## Why I built this

I wanted a project that felt practical, not academic.

## Travool helped me:

Get more confident with SQL and databases

Practice writing non-trivial Python scripts

Learn how to design a clean CLI interface

Work through real debugging instead of tutorials

## Possible next steps

Add CSV export support

Add preset queries (cheapest, highest rated)

Build a lightweight GUI version

Expand the dataset

## Final Thoughts

This project isn’t meant to be flashy — it’s meant to be solid. I can explain every line of it, extend it confidently, and defend the design choices I mad
