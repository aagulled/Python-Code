{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0be51a10-6496-4067-b716-310957024652",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import random\n",
    "\n",
    "# Define the column headers\n",
    "columns = ['product_id', 'product_name', 'description', 'price', 'image', 'category_id']\n",
    "\n",
    "# Generate sample data\n",
    "data = []\n",
    "for i in range(2000000, 2000000 + 100):  # Adjust the number of records as needed\n",
    "    product_id = i\n",
    "    product_name = fake.word()\n",
    "    description = fake.text()\n",
    "    price = random.uniform(10, 100)\n",
    "    image = \"product_\" + str(i) + \".jpg\"  # Replace with actual image filenames\n",
    "    category_id = random.randint(3000, 3010)  # Adjust the category ID range\n",
    "    data.append([product_id, product_name, description, price, image, category_id])\n",
    "\n",
    "# Write the data to a CSV file\n",
    "with open('products.csv', 'w', newline='') as csvfile:\n",
    "    writer = csv.writer(csvfile)\n",
    "    writer.writerow(columns)\n",
    "    writer.writerows(data)\n",
    "\n",
    "print(\"Products CSV file generated successfully.\")"
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
