from product import product_details


def test_product_details():
    expected_output = (
        "Product ID: 101\n"
        "Product Name: Laptop\n"
        "Quantity: 5\n"
        "Price: Rs. 45000.00"
    )

    assert product_details(101, "Laptop", 5, 45000) == expected_output


def test_another_product():
    expected_output = (
        "Product ID: 102\n"
        "Product Name: Mouse\n"
        "Quantity: 10\n"
        "Price: Rs. 500.00"
    )

    assert product_details(102, "Mouse", 10, 500) == expected_output