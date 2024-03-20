from typing import Union

from inventory_report.product import Product


class Inventory:
    @property
    def data(self) -> list[Product]:
        return self.__data.copy()

    def __init__(self, data: Union[list[Product], None] = None) -> None:
        self.__data = data or []

    def add_data(self, data: list[Product]) -> None:
        self.__data.extend(data)
