import json
import random


item_names = [
    "Medicine", "Food", "Water", "Ammunition", "Bandage", 
    "Map", "Flashlight", "Knife", "Radio", "Backpack",
    "Compass", "Rope", "Binoculars", "Goggles", "Gloves",
    "Battery", "First Aid Kit", "Tent", "Sleeping Bag", "Matches",
    "Pocket Knife", "Canteen", "Whistle", "Sunglasses", "Sunscreen",
    "Bug Spray", "Notebook", "Pencil", "Compass", "Fishing Rod",
    "Candle", "Lighter", "Flare Gun", "Blanket", "Hatchet",
    "Multitool", "Firestarter", "Tarp", "Solar Charger", "Duct Tape",
    "Paracord", "Insect Repellent", "Hand Warmers", "Signal Mirror",
    "Water Purification Tablets", "Emergency Whistle", "Sewing Kit"
]

# Function to generate a random item
def generate_item():
    item_name = random.choice(item_names)  # Random item name from the list
    item_type = random.choice(["health", "food", "money", "weapon", "map"])  # Random item type
    item_effect = random.randint(1, 10)  # Random effect value
    item_passive_effect = 0  # Passive effect set to 0 by default
    drop_at_start_of_next_day = random.choice([True, False])  # Random drop_at_start_of_next_day value

    return {
        "name": item_name,
        "type": item_type,
        "effect": item_effect,
        "passive_effect": item_passive_effect,
        "drop_at_start_of_next_day": drop_at_start_of_next_day
    }

# Generate 50 items
items = [generate_item() for _ in range(50)]

# Save items to a JSON file
file_path = "items.json"
with open(file_path, "w") as json_file:
    json.dump({"items": items}, json_file, indent=4)

print(f"Items saved to {file_path}")
