from collections import defaultdict
from datetime import datetime

from inventory_report.importers import JsonImporter
from inventory_report.inventory import Inventory


class SimpleReport:
    def __init__(self):
        self.stocks = []

    def add_inventory(self, inventory: Inventory):
        if isinstance(inventory, Inventory):
            self.stocks.append(inventory)

    def find_company_with_largest_inventory(self):
        # Dicionário para armazenar o número de produtos por empresa
        company_inventory_count = defaultdict(int)

        # Iterar sobre cada inventário
        for inventory in self.stocks:
            # Iterar sobre cada produto no inventário
            for product in inventory.data:
                # Incrementar o contador de inventário para
                # a empresa do produto atual
                company_inventory_count[product.company_name] += 1

        # Encontrar a empresa com o maior estoque
        company_with_largest_inventory = max(
            company_inventory_count,
            key=lambda k: int(company_inventory_count[k])
        )

        # Retorna o nome da empresa com o
        # maior estoque e a contagem de inventário
        return (
            company_with_largest_inventory,
            company_inventory_count[company_with_largest_inventory],
        )

    def generate(self):
        oldest_manufacturing_date = min(
            [
                product.manufacturing_date
                for inventory in self.stocks
                for product in inventory.data
            ]
        )
        closest_expiration_date = min(
            [
                product.expiration_date
                for inventory in self.stocks
                for product in inventory.data
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
        report += f"{company_with_largest_inventory}"

        return report


if __name__ == "__main__":
    list_products = JsonImporter(
        "inventory_report/data/inventory.json"
    ).import_data()
    inventory = Inventory(list_products)
    report = SimpleReport()
    report.add_inventory(inventory)
    print(report.generate())
