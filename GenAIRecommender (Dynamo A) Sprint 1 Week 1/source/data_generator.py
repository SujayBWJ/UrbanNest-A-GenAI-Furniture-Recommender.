from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()

# -----------------------------
# CONFIG
# -----------------------------
NUM_PRODUCTS = 500
NUM_USERS = 2000
NUM_EVENTS = 15000

categories = ["Sofa", "Chair", "Table", "Bed", "Wardrobe"]
materials = ["Wood", "Metal", "Glass", "Fabric", "Leather"]
colors = ["Black", "White", "Grey", "Brown", "Beige", "Blue"]
styles = ["Modern", "Contemporary", "Vintage", "Minimalist", "Industrial"]

price_ranges = {
    "Sofa": (20000, 80000),
    "Chair": (2000, 10000),
    "Table": (5000, 25000),
    "Bed": (15000, 60000),
    "Wardrobe": (10000, 50000)
}

event_types = ["view", "cart", "wishlist", "purchase"]

# -----------------------------
# 1. PRODUCT DATA
# -----------------------------
products = []

for i in range(NUM_PRODUCTS):
    category = random.choice(categories)
    material = random.choice(materials)
    color = random.choice(colors)
    style = random.choice(styles)

    price = random.randint(*price_ranges[category])
    rating = round(random.uniform(3.0, 5.0), 1)

    name = f"{style} {material} {category}"

    products.append({
        "product_id": f"P{i+1:04}",
        "name": name,
        "category": category,
        "material": material,
        "color": color,
        "style": style,
        "price": price,
        "rating": rating
    })

products_df = pd.DataFrame(products)

# -----------------------------
# 2. USER IDS
# -----------------------------
users = [f"U{i+1:04}" for i in range(NUM_USERS)]

# -----------------------------
# 3. USER BEHAVIOR DATA
# -----------------------------
behavior = []

for _ in range(NUM_EVENTS):
    user = random.choice(users)
    product = random.choice(products_df["product_id"].values)

    days_ago = random.randint(0, 365)
    timestamp = datetime.now() - timedelta(days=days_ago)

    event = random.choices(
        event_types,
        weights=[0.6, 0.2, 0.1, 0.1]
    )[0]

    behavior.append({
        "user_id": user,
        "product_id": product,
        "timestamp": timestamp,
        "event_type": event
    })

behavior_df = pd.DataFrame(behavior)

# -----------------------------
# 4. ENSURE ≥1 PURCHASE PER USER
# -----------------------------
extra_rows = []

for user in users:
    product = random.choice(products_df["product_id"].values)
    timestamp = datetime.now() - timedelta(days=random.randint(0, 365))

    extra_rows.append({
        "user_id": user,
        "product_id": product,
        "timestamp": timestamp,
        "event_type": "purchase"
    })

behavior_df = pd.concat([behavior_df, pd.DataFrame(extra_rows)], ignore_index=True)

# -----------------------------
# SAVE
# -----------------------------
products_df.to_csv("products.csv", index=False)
behavior_df.to_csv("user_behavior.csv", index=False)

print("Generated: products.csv, user_behavior.csv")