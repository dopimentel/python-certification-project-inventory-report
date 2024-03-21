from inventory_report.importers import JsonImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        report = super().generate()
        report += "Stocked products by company:\n"
        for company, count in self._company_inventory_count.items():
            report += f"- {company}: {count}\n"
        return report


if __name__ == "__main__":
    list_products = JsonImporter(
        "inventory_report/data/inventory.json"
    ).import_data()
    inventory = Inventory(list_products)
    report = CompleteReport()
    report.add_inventory(inventory)
    print(report.generate())
