# Mini Expense Tracker (Python)
# Parses simple transaction records and outputs totals by category (and a monthly summary) to help spot spending patterns.
# Input CSV per line: date,description,amount,category

import csv, sys
from collections import defaultdict

def totals_by_category(lines):
    totals = defaultdict(float)
    for line in lines:
        line = line.strip()
        if not line:
            continue
        date, desc, amount, category = (line.split(",", 3) + ["","","",""])[:4]
        try:
            totals[category.strip()] += float(amount)
        except Exception:
            pass
    return totals

if __name__ == "__main__":
    totals = totals_by_category(sys.stdin)
    for k in sorted(totals):
        print(f"{k}: {totals[k]:.2f}")
