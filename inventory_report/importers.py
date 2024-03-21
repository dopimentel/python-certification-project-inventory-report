import json
from abc import ABC, abstractmethod
from typing import Dict, Type

from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        raise NotImplementedError


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, "r") as file:
            data = json.load(file)
        return [
            Product(
                product["id"],
                product["product_name"],
                product["company_name"],
                product["manufacturing_date"],
                product["expiration_date"],
                product["serial_number"],
                product["storage_instructions"],
            )
            for product in data
        ]


class CsvImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, "r") as file:
            data = file.readlines()
        data = data[1:]
        return [
            Product(
                product[0],
                product[1],
                product[2],
                product[3],
                product[4],
                product[5],
                product[6],
            )
            for product in map(lambda x: x.strip().split(","), data)
        ]


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

if __name__ == "__main__":
    imp = JsonImporter("inventory_report/data/inventory.json")
    products = imp.import_data()
    for product in products:
        print(product)

    imp_csv = CsvImporter("inventory_report/data/inventory.csv")
    products_csv = imp_csv.import_data()
    for product in products_csv:
        print(product)
