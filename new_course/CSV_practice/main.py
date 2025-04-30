"""
In this project, you will read a CSV file, process the data, and produce a result using Python. In this exercise, you will calculate the price of products and save the information. You will also create a new CSV file that contains this processed data.

Project Details:

Inputs:
A CSV file that contains the product names, prices, and quantities available.
Outputs:

Calculate the total price of the products by multiplying the price by the quantity and saving the result in a new CSV file.
Create a new CSV file with four columns: product name, price, quantity, and total price.
Project Steps:

Read data from the CSV file.
Calculate the total price of the products.
Save the processed data in a new CSV file.
"""
import csv


with open("products.csv", mode='r', newline='') as f_in:
    reader = csv.DictReader(f_in)
    rows = list(reader)


for row in rows:
    price = int(row['Price'])
    quantity = int(row['Quantity'])
    # calculate total price for each product
    row['Total_price'] = price * quantity  


# add new header to exiting headers
fieldnames = list(rows[0].keys() + ['Total_price'] if 'Total_price' not in rows[0] else list(rows[0].keys()))


with open("output.csv", mode='w', newline='') as f_out:
    writer = csv.DictWriter(f_out, fieldnames=fieldnames)
    writer.writeheader()    # write header automaticly
    writer.writerows(rows)
