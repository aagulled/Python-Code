import csv
import random
from faker import Faker  # Import from faker library

# Define the column headers
columns = ['order_id', 'customer_id', 'order_date', 'shipping_address', 'shipping_city', 'shipping_state', 'shipping_zip_code', 'shipping_country', 'order_status']

# Create a Faker instance
fake = Faker()

# Generate sample data
data = []
for i in range(4000000, 4000000 + 100):  # Adjust the number of records as needed
    order_id = i
    customer_id = random.randint(1000000, 1000099)  # Adjust the customer ID range
    order_date = fake.date_between(datetime.date(2021, 12, 27), datetime.date(2022, 4, 15))


    shipping_address = fake.address()
    shipping_city = fake.city()
    shipping_state = fake.state()
    shipping_zip_code = fake.postcode()
    shipping_country = fake.country()
    order_status = random.choice(["Pending", "Shipped", "Delivered"])
    data.append([order_id, customer_id, order_date, shipping_address, shipping_city, shipping_state, shipping_zip_code, shipping_country, order_status])

# Write the data to a CSV file
with open('order.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(columns)
    writer.writerows(data)

print("Orders CSV file generated successfully.")