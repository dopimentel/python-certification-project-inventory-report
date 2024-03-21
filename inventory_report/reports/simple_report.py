from datetime import datetime, timedelta
from typing import List


class SimpleReport:
    def __init__(self):
        self.inventories = []

    def add_inventory(self, inventory):
        """
        Adiciona um estoque à lista de estoques.
        """
        self.inventories.append(inventory)

    def generate(self):
        """
        Gera o relatório conforme as especificações.
        """
        # Encontrar a data de fabricação mais antiga
        oldest_manufacturing_date = self.find_oldest_manufacturing_date()

        # Encontrar a data de validade mais próxima
        closest_expiration_date = self.find_closest_expiration_date()

        # Encontrar a empresa com o maior estoque
        company_with_largest_inventory = self.find_company_with_largest_inventory()

        # Formatar o relatório
        report = (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: {company_with_largest_inventory}"
        )

        return report

    def find_oldest_manufacturing_date(self):
        """
        Encontra a data de fabricação mais antiga entre todos os estoques.
        """
        if not self.inventories:
            return None

        oldest_date = datetime.now()
        for inventory in self.inventories:
            for product in inventory.products:
                if product.manufacturing_date < oldest_date:
                    oldest_date = product.manufacturing_date

        return oldest_date.strftime('%Y-%m-%d')

    def find_closest_expiration_date(self):
        """
        Encontra a data de validade mais próxima entre todos os estoques.
        """
        if not self.inventories:
            return None

        today = datetime.now()
        closest_date = None
        for inventory in self.inventories:
            for product in inventory.products:
                if product.expiration_date > today:
                    if closest_date is None or product.expiration_date < closest_date:
                        closest_date = product.expiration_date

        return closest_date.strftime('%Y-%m-%d') if closest_date else None

    def find_company_with_largest_inventory(self):
        """
        Encontra a empresa com o maior estoque.
        """
        if not self.inventories:
            return None

        company_inventory = {}
        for inventory in self.inventories:
            if inventory.company_name in company_inventory:
                company_inventory[inventory.company_name] += len(inventory.products)
            else:
                company_inventory[inventory.company_name] = len(inventory.products)

        max_inventory_company = max(company_inventory, key=company_inventory.get)
        return max_inventory_company
