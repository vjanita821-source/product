def product_details(product_id, name, quantity, price):
    return (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: Rs. {price:.2f}"
    )


# Example
print(product_details(101, "Laptop", 5, 45000))