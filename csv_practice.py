# Python makes it easier to repeat an ETL process because the same code can
# read, transform, and write data every time it runs. Excel is useful for
# quickly viewing data and making manual changes, but Python automates larger or repeated tasks.
#
# A store could use an append-mode log to record each daily sales report that runs.
# Append mode keeps the previous records instead of replacing them, which creates
# a history that can be reviewed later.

import csv
from datetime import datetime

total_revenue = 0

with open("data/sales.csv", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(header)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Overall revenue: ${total_revenue:.2f}")

# Exercise 5
original_count = 0
written_count = 0

with open("data/sales.csv", newline="") as input_file, open(
    "data/cleaned.csv", "w", newline=""
) as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        original_count += 1
        if total > 100:
            written_count += 1
            writer.writerow([product, price, quantity, total])

print(f"Original rows: {original_count}")
print(f"Written rows: {written_count}")

# Exercise 6
dict_total_revenue = 0
with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
            product = row["product"]
            price = float(row["price"])
            quantity = int(row["quantity"])
            total = price * quantity
            dict_total_revenue += total
print(f"Dictionary total revenue: ${dict_total_revenue:.2f}")

# csv.reader is useful when column positions stay consistent.
# csv.DictReader is easier to read when using column names.

# Exercise 7
product_totals = {}
with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        product_totals[product] = product_totals.get(product, 0) + total

for product in sorted(product_totals):
        print(f"{product}: ${product_totals[product]:.2f}")

# Exercise 8
with open("data/run_log.txt", "a") as log_file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"{timestamp} - Total revenue: ${total_revenue:.2f}\n")