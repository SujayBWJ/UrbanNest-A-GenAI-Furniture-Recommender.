# Data Dictionary

## 1. products.csv

| Column Name | Data Type | Description |
|------------|----------|-------------|
| product_id | string | Unique identifier for each product (e.g., P0001) |
| name | string | Generated product name combining style, material, and category |
| category | string | Type of furniture (Sofa, Chair, Table, Bed, Wardrobe) |
| material | string | Material used (Wood, Metal, Glass, Fabric, Leather) |
| color | string | Product color (Black, White, Grey, Brown, Beige, Blue) |
| style | string | Design style (Modern, Contemporary, Vintage, Minimalist, Industrial) |
| price | integer | Price of the product in INR |
| rating | float | Customer rating (range: 3.0 – 5.0) |

---

## 2. user_behavior.csv

| Column Name | Data Type | Description |
|------------|----------|-------------|
| user_id | string | Unique identifier for each user (e.g., U0001) |
| product_id | string | Product identifier referencing products.csv |
| timestamp | datetime | Time of user interaction (within last 1 year) |
| event_type | string | Type of interaction: view, cart, wishlist, purchase |

---

## 3. products_clean.parquet

| Column Name | Data Type | Description |
|------------|----------|-------------|
| product_id | string | Unique product identifier |
| name | string | Product name |
| category | string | Furniture category |
| material | string | Product material |
| color | string | Product color |
| style | string | Product style |
| price | integer | Product price |
| rating | float | Product rating |

Note: This dataset is cleaned (duplicates removed, consistent formatting).

---

## 4. user_features.parquet

| Column Name | Data Type | Description |
|------------|----------|-------------|
| user_id | string | Unique user identifier |
| Recency | integer | Number of days since the user's last purchase |
| Frequency | integer | Total number of purchases made by the user |
| Monetary | integer | Total amount spent by the user |

---

## Notes

- All IDs are uniquely generated and consistent across datasets  
- No missing values in critical fields  
- product_id acts as a foreign key linking user_behavior to products  
- Data is synthetically generated but follows realistic constraints  