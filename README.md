# 🌍 travool: Travel Recommendations from the Command Line

**travool** is a pure Python CLI tool that provides personalized travel destination recommendations based on your budget, visa requirements, and travel preferences. Results are formatted in a clean, professional table directly in your terminal.

---

## ✨ Features

- Filter destinations by:
  - Maximum daily cost
  - Visa-free access
  - Minimum traveler rating
- Outputs clean, tabulated results using `tabulate`
- Built on a real SQLite database from CSV data
- Fully CLI-driven, with no interactive prompts

---

## ⚙️ Installation

1. Clone this repo or download the files

2. Install dependencies:

```bash
pip install pandas tabulate
```

3. Load the data into the database:

```bash
python load_travel_data.py
```

4. Run the CLI app:

```bash
python travel_final_cli.py --max-cost 100 --visa-free yes --min-rating 4.5
```

---

## ⚖️ Example Usage

```bash
python travel_final_cli.py --max-cost 75 --visa-free yes --min-rating 4.6
```

Output:

```
🔍 Running query with filters:
  Max Cost: 75
  Visa Free: yes
  Min Rating: 4.6

📊 Matching Results:
╒══════════════╤══════════════╤═════════════╤══════════╕
│ Country      │ CostPerDay   │ VisaFree    │ Rating   │
╘══════════════╧══════════════╧═════════════╧══════════╛
│ Portugal     │ 75           │ Yes         │ 4.8      │
│ Thailand     │ 65           │ Yes         │ 4.7      │
```

---

## 📚 Project Structure

```
.
├── travel_data.csv         # Raw destination data
├── load_travel_data.py     # Loads CSV into SQLite DB
├── travel.db               # SQLite database file
├── travel_final_cli.py     # CLI app for querying destinations
```

---

## ⚠️ Things I Struggled With (and Solved)

| Problem                                           | What I Learned                                                                          |
| ------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Converting from interactive `input()` to full CLI | Use `argparse` and skip prompts for missing args                                        |
| Argument errors                                   | You must pass flags like `--visa-free yes` or it will throw a "too few arguments" error |
| Dynamic SQL                                       | Use `WHERE 1=1` as a base, then add conditions                                          |
| SQLite insertion                                  | `executemany()` is used to insert multiple rows efficiently                             |
| Display formatting                                | `tabulate` makes CLI tables much easier to read                                         |

These are all things I now fully understand and could explain in an interview or modify later.

---

## 🚀 Future Enhancements

- Add `--best-month` filter
- Export results to CSV with `--export`
- Add "Top 5 Cheapest" and "Top 5 Highest Rated" quick commands
- Streamlit version for GUI users

---

## ✨ Why I Built This

I wanted to deepen my knowledge of SQL, Python, and real-world data processing. Instead of just tutorials, I built **travool** from scratch — it solidified my understanding and became a tool I would genuinely use myself.

- CLI tools with `argparse`
- Dynamic SQL filtering
- CSV ⇒ pandas ⇒ SQLite ⇒ pandas ⇒ terminal
- Clean, production-quality formatting

I now feel confident reading, writing, and debugging projects like this on my own.

---

## 😎 Final Thoughts

**travool** isn’t just a travel tool, it’s a showcase of practical Python and SQL skills. It’s simple, flexible, and easy to build on. Whether you want to add more data, filters, or even a GUI, you’re starting from a solid foundation.

---


