from typing import Protocol

from inventory_report.inventory import Inventory


class Report(Protocol):
    def generate(self) -> str:
        raise NotImplementedError

    def add_inventory(self, inventory: Inventory) -> None:
        raise NotImplementedError
