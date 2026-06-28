import csv
from pathlib import Path


input_file = Path("data/raw/orders.csv")

with input_file.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for order in reader:
        print(order)