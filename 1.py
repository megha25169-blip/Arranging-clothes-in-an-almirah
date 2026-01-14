"""
Algorithm: Arrange Clothes in an Almirah
1. Initialize the almirah with n shelves.
2. Assign each shelf to a clothing category (formal, casual, traditional, etc.).
3. Add clothes to their respective shelves.
4. Within each shelf, arrange clothes by usage frequency (most used on top).
5. Provide a search function to quickly locate any item.
6. Ensure shelves are optimally filled without wasting space.
"""

class Almirah:
    def __init__(self, shelves):
        # Dictionary: shelf_number -> list of clothes
        self.shelves = {i: [] for i in range(1, shelves+1)}
        # Map category -> shelf_number
        self.category_map = {}

    def assign_category(self, shelf, category):
        self.category_map[category] = shelf

    def add_clothes(self, category, item):
        shelf = self.category_map.get(category)
        if shelf:
            self.shelves[shelf].append(item)

    def search_item(self, item):
        for shelf, clothes in self.shelves.items():
            if item in clothes:
                return f"Found {item} in shelf {shelf}"
        return f"{item} not found"

# Example usage
almirah = Almirah(3)
almirah.assign_category(1, "Formal")
almirah.assign_category(2, "Casual")
almirah.assign_category(3, "Traditional")

almirah.add_clothes("Formal", "Blazer")
almirah.add_clothes("Casual", "Shirt")
almirah.add_clothes("Traditional", "Kurta")

print(almirah.search_item("Kurta"))