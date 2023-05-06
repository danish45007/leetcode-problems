from abc import ABC, abstractclassmethod
from vending_machine import VendingMachine
from product import Product
from coin import Coin

class State(ABC):
    @abstractclassmethod
    def click_on_insert_coin_button(self, vending_machine: VendingMachine):
        pass
    @abstractclassmethod
    def click_on_start_product_select_button(self, vending_machine: VendingMachine):
        pass
    @abstractclassmethod
    def insert_coin(self, vending_machine: VendingMachine,  coin: Coin):
        pass
    @abstractclassmethod
    def choose_product(self, vending_machine: VendingMachine, code_number: int):
        pass
    @abstractclassmethod
    def get_change(self, return_change_money: int):
        pass
    @abstractclassmethod
    def dispense_product(self, vending_machine: VendingMachine, code_number: int):
        pass
    @abstractclassmethod
    def refund_full_money(self, vending_machine: VendingMachine):
        pass
    @abstractclassmethod
    def update_inventory(self, vending_machine: VendingMachine, product: Product, code_number: int):
        pass
    