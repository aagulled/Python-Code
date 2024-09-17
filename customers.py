{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19b32d64-c31b-4d4c-a7cc-30f474efccf9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import random\n",
    "import faker\n",
    "\n",
    "# Create a Faker instance for generating fake data\n",
    "fake = faker.Faker()\n",
    "\n",
    "# Define the column headers\n",
    "columns = ['customer_id', 'first_name', 'last_name', 'email', 'address', 'city', 'state', 'zip_code', 'country']\n",
    "\n",
    "# Generate sample data\n",
    "data = []\n",
    "for i in range(1000000, 1000000 + 100):  # Adjust the number of records as needed\n",
    "    customer_id = i\n",
    "    first_name = fake.first_name()\n",
    "    last_name = fake.last_name()\n",
    "    email = fake.email()\n",
    "    address = fake.address()\n",
    "    city = fake.city()\n",
    "    state = fake.state()\n",
    "    zip_code = fake.postcode()\n",
    "    country = fake.country()\n",
    "    data.append([customer_id, first_name, last_name, email, address, city, state, zip_code, country])\n",
    "\n",
    "# Write the data to a CSV file\n",
    "with open('customers.csv', 'w', newline='') as csvfile:\n",
    "    writer = csv.writer(csvfile)\n",
    "    writer.writerow(columns)\n",
    "    writer.writerows(data)\n",
    "\n",
    "print(\"Customers CSV file generated successfully.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
