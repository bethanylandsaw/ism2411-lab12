import csv

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