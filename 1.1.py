"""
Algorithm: Arranging Clothes in an Almirah

1. Start the program.
2. Create an almirah with n shelves.
3. Define categories of clothes such as:
   - Formal
   - Casual
   - Traditional
4. Assign each category to a separate shelf.
5. For each clothing item:
   a. Identify its category.
   b. Place the item in the corresponding shelf.
6. Arrange clothes in each shelf so that:
   - Frequently used clothes are placed in front or on top.
7. Ensure shelves are not overcrowded and space is used properly.
8. When searching for a cloth:
   a. Ask the user for the category and item name.
   b. Go to the assigned shelf.
   c. Search for the item in that shelf.
   d. If found, display the shelf number.
   e. If not found, display "Item not found".
9. Display the final arrangement of clothes.
10. End the program.
"""

# Simple demonstration code (optional)

almirah = {
    "Formal": ["Blazer", "Shirt"],
    "Casual": ["T-Shirt", "Jeans"],
    "Traditional": ["Kurta"]
}

print("Clothes in Almirah:")
for category, items in almirah.items():
    print(category, ":", items)

search_item = "Kurta"
found = False

for category, items in almirah.items():
    if search_item in items:
        print(search_item, "found in", category, "shelf")
        found = True

if not found:
    print("Item not found")
