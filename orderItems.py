{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "638fcc53-0499-47db-b494-fe12b78f2fb3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Order Items CSV file generated successfully.\n"
     ]
    }
   ],
   "source": [
    "   import csv\n",
    "import random\n",
    "\n",
    "# Define the column headers\n",
    "columns = ['order_item_id', 'order_id', 'product_id', 'quantity', 'price']\n",
    "\n",
    "# Generate sample data\n",
    "data = []\n",
    "for i in range(5000000, 5000000 + 100):  # Adjust the number of records as needed\n",
    "    order_item_id = i\n",
    "    order_id = random.randint(4000000, 4000099)  # Adjust the order ID range\n",
    "    product_id = random.randint(2000000, 2000099)  # Adjust the product ID range\n",
    "    quantity = random.randint(1, 5)\n",
    "    price = random.uniform(10, 100)\n",
    "    data.append([order_item_id, order_id, product_id, quantity, price])\n",
    "\n",
    "# Write the data to a CSV file\n",
    "with open('order_items.csv', 'w', newline='') as csvfile:\n",
    "    writer = csv.writer(csvfile)\n",
    "    writer.writerow(columns)\n",
    "    writer.writerows(data)\n",
    "\n",
    "print(\"Order Items CSV file generated successfully.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80314062-05aa-43cd-b850-2928fba9ce88",
   "metadata": {},
   "outputs": [],
   "source": []
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
