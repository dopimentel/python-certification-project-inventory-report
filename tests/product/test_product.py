from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        "123",
        "product_name",
        "company_name",
        "01-01-2021",
        "01-01-2022",
        "serial_number",
        "storage_instructions",
    )
    assert product.id == "123"
    assert product.product_name == "product_name"
    assert product.company_name == "company_name"
    assert product.manufacturing_date == "01-01-2021"
    assert product.expiration_date == "01-01-2022"
    assert product.serial_number == "serial_number"
    assert product.storage_instructions == "storage_instructions"
