from typing import Protocol


class Report(Protocol):
    def generate(self) -> str:
        raise NotImplementedError

    def add_inventory(self, inventory) -> None:
        raise NotImplementedError
