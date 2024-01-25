class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity > len(self.items):
            self.items.append(item)
        return f'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        total = self.get_capacity()
        left_capacity = total - len(self.items)
        return f'Items: {", ".join(self.items)}.\nCapacity left: {left_capacity}'


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)