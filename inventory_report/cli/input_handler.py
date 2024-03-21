from typing import List

from inventory_report.importers import CsvImporter, JsonImporter
from inventory_report.inventory import Inventory
from inventory_report.reports import REPORTS


def process_report_request(file_paths: List[str], report_type: str) -> str:
    """
    Process the report given a list of file paths and a report type,
    and returns the result.
    """
    if report_type in REPORTS:
        report = REPORTS[report_type]()
        for file in file_paths:
            if file.endswith(".csv"):
                list_products = CsvImporter(file).import_data()
                inventory = Inventory(list_products)
                report.add_inventory(inventory)
            if file.endswith(".json"):
                list_products = JsonImporter(file).import_data()
                inventory = Inventory(list_products)
                report.add_inventory(inventory)
        return report.generate()

    raise ValueError("Report type is invalid.")
