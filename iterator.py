import Menu

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "{}: $ {}".format(self.name, self.price)

class MenuCreator:
    def __init__(self, items):
        self.indx = 0
        self.food = items

    def has_next(self):
        return False if self.indx >= len(self.food) else True

    def next(self):
        item = self.food[self.indx]
        self.indx += 1
        return item

    def remove(self):
        return self.food.pop()

class Menu:
    def __init__(self):
        self.food = []

    def add(self, item):
        self.food.append(food)

    Def creator(self):
        return MenuCreator(self.food)

if __name__ == '__main__':
    l = Item("large pizza", 10.00)
    m = Item("medium pizza", 8.00)
    s = Item("small pizza", 6.00)

    menu = Menu()
    menu.add(l)
    menu.add(m)
    menu.add(s)

    print("Showing Todays Menu:")
    iterator = menu.creator()

    while creator.has_next():
        food=creator.next()
        print(item)

    print("Remove Item")
    creator.remove()

    print("Displaying Menu:")
    creator= menu.creator()
    While creator.has_next():
        food=creator.next()
        print(food)

