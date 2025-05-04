import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create the sales table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

# Insert some sample data
data = [
    ('Laptop', 2, 1200.00),
    ('Mouse', 5, 25.00),
    ('Keyboard', 3, 75.00),
    ('Monitor', 1, 300.00),
    ('Webcam', 4, 50.00)
]
cursor.executemany("INSERT INTO sales VALUES (?, ?, ?)", data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("SQLite database 'sales_data.db' and table 'sales' created successfully with sample data.")




import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('sales_data.db')

# SQL query to get total quantity sold and total revenue per product
query = """
SELECT product, SUM(quantity) AS total_quantity, SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
"""

# Load the SQL query results into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Print the DataFrame (results of the SQL query)
print("Sales Information:")
print(df)
print("\n")

# Basic print statements for total quantity and total revenue (optional - can be derived from the DataFrame)
total_quantity_sold = df['total_quantity'].sum()
total_revenue = df['total_revenue'].sum()

print(f"Total Quantity Sold across all products: {total_quantity_sold}")
print(f"Total Revenue across all products: ${total_revenue:.2f}")
print("\n")

# Create a simple bar chart
plt.figure(figsize=(8, 6))
plt.bar(df['product'], df['total_revenue'], color='skyblue')
plt.xlabel("Product")
plt.ylabel("Total Revenue ($)")
plt.title("Total Revenue per Product")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Display the chart
plt.show()

# Save the chart if needed
# plt.savefig('sales_chart.png')
