from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        "123",
        "product_name",
        "company_name",
        "01-01-2021",
        "01-01-2022",
        "serial_number",
        "storage_instructions",
    )
    assert str(product) == (
        "The product 123 - product_name with serial number serial_number "
        "manufactured on 01-01-2021 by the company company_name "
        "valid until 01-01-2022 must be stored according to the following "
        "instructions: storage_instructions."
    )
