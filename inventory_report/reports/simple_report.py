from collections import defaultdict
from datetime import datetime

from inventory_report.importers import JsonImporter
from inventory_report.inventory import Inventory


class SimpleReport:
    """
    Class responsible for generating a simple report
    with information about the inventory.

    Attributes:
    stocks (list): List of products in the inventory.
    _company_inventory_count (defaultdict): Dictionary storing the number
    of products per company.

    Methods:
    add_inventory(inventory): Adds an inventory to the inventory.
    find_company_with_largest_inventory(): Finds the company with
    the largest inventory.
    generate(): Generates the report with inventory information.
    """

    def __init__(self):
        self.stocks = []
        self._company_inventory_count = defaultdict(int)

    def add_inventory(self, inventory: Inventory):
        """
        Adds an inventory to the inventory.

        Parameters:
        inventory (Inventory): Inventory object containing the
        products to be added to the inventory.
        """
        if isinstance(inventory, Inventory):
            self.stocks.extend(inventory.data)

    def find_company_with_largest_inventory(self):
        """
        Finds the company with the largest inventory.

        Returns:
        tuple: A tuple containing the name of the company with the largest
        inventory and the inventory count.
        """
        company_inventory_count = defaultdict(int)

        for product in self.stocks:
            company_inventory_count[product.company_name] += 1

        self._company_inventory_count = company_inventory_count

        company_with_largest_inventory = max(
            company_inventory_count,
            key=lambda k: int(company_inventory_count[k]),
        )

        return (
            company_with_largest_inventory,
            company_inventory_count[company_with_largest_inventory],
        )

    def generate(self):
        """
        Generates the report with inventory information.

        Returns:
        str: The generated report.
        """
        oldest_manufacturing_date = min(
            [product.manufacturing_date for product in self.stocks]
        )
        closest_expiration_date = min(
            [
                product.expiration_date
                for product in self.stocks
                if datetime.strptime(product.expiration_date, "%Y-%m-%d")
                > datetime.now()
            ]
        )
        company_with_largest_inventory = (
            self.find_company_with_largest_inventory()[0]
        )
        report = f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
        report += f"Closest expiration date: {closest_expiration_date}\n"
        report += "Company with the largest inventory: "
        report += f"{company_with_largest_inventory}\n"

        return report


if __name__ == "__main__":
    list_products = JsonImporter(
        "inventory_report/data/inventory.json"
    ).import_data()
    inventory = Inventory(list_products)
    report = SimpleReport()
    report.add_inventory(inventory)
    print(report.generate())
