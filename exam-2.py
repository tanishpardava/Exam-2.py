# Inventory List Analyzer - Store Stock Tracker

items = []
categories = []
quantities = []

print("Welcome to Inventory List Analyzer!")

while True:
    name = input("\nEnter item name: ").strip().title()
    category = input("Enter category: ").strip().lower()

    quantity = int(input("Enter quantity: "))

    items.append(name)
    categories.append(category)
    quantities.append(quantity)

    choice = input("\nDo you want to add more items? (y/n): ").lower()

    if choice != "y":
        break


# Inventory Summary
print("\n========== INVENTORY SUMMARY ==========")

# Total Different Items
total_items = len(items)
print("Total Different Items:", total_items)

# Total Quantity
total_quantity = sum(quantities)
print("Total Quantity in Stock:", total_quantity)

# Average Quantity
average = total_quantity / total_items
print("Average Quantity per Item:", round(average, 2))

# Most Stocked Item
max_quantity = max(quantities)
max_index = quantities.index(max_quantity)

print("Most Stocked Item:", items[max_index])
print("Quantity:", max_quantity)

# Least Stocked Item
min_quantity = min(quantities)
min_index = quantities.index(min_quantity)

print("Least Stocked Item:", items[min_index])
print("Quantity:", min_quantity)


# Unique Categories
unique_categories = set(categories)

print("\nUnique Categories in Inventory:")
for category in sorted(unique_categories):
    print("-", category)


# Sort Items by Quantity
print("\nItems Sorted by Quantity (High to Low):")

sorted_items = sorted(
    zip(items, categories, quantities),
    key=lambda x: x[2],
    reverse=True
)

for name, category, quantity in sorted_items:
    print(name, "-", quantity, "units")


# Categories in Alphabetical Order
print("\nCategories in Alphabetical Order:")

for category in sorted(unique_categories):
    print("-", category)


print("\n========== END OF REPORT ==========")