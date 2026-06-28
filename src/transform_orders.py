import csv
from pathlib import Path


input_file = Path("data/raw/orders.csv")
output_file = Path("data/processed/orders_processed.csv")

output_columns = [
    "order_id",
    "customer_name",
    "city",
    "order_value",
    "order_category",
]

with input_file.open(mode="r", encoding="utf-8", newline="") as input_csv:
    reader = csv.DictReader(input_csv)

    with output_file.open(mode="w", encoding="utf-8", newline="") as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=output_columns)

        writer.writeheader()

        for order in reader:
            order_value = float(order["order_value"])

            if order_value > 100:
                order_category = "high_value"
            else:
                order_category = "standard"

            transformed_order = {
                "order_id": order["order_id"],
                "customer_name": order["customer_name"],
                "city": order["city"],
                "order_value": order_value,
                "order_category": order_category,
            }

            writer.writerow(transformed_order)