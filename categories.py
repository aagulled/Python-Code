{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0acaea0f-a34a-429d-b45b-ebccfbed382c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "\n",
    "# Define the column headers\n",
    "columns = ['category_id', 'category_name']\n",
    "\n",
    "# Generate sample data\n",
    "data = [\n",
    "    [3000, \"Electronics\"],\n",
    "    [3001, \"Clothing\"],\n",
    "    [3002, \"Books\"],\n",
    "    # Add more categories as needed\n",
    "]\n",
    "\n",
    "# Write the data to a CSV file\n",
    "with open('categories.csv', 'w', newline='') as csvfile:\n",
    "    writer = csv.writer(csvfile)\n",
    "    writer.writerow(columns)\n",
    "    writer.writerows(data)\n",
    "\n",
    "print(\"Categories CSV file generated successfully.\")"
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
