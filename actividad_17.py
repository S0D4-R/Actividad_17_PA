main_kart = []
fav_list = []
class Carrito:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart
    #append()
    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{product} agregado exitosamente: {self.cart}")
    #remove
    def remove_from_cart(self):
        pass
    #extend()
    def import_from_liked(self):
        pass

class Favoritos:
    def __init__(self, user, followed):
        self.user = user
        self.followed = followed
    #sort
    def positive_sort(self):
        pass
    #reverse()
    def negative_sort(self):
        pass
    #clear()
    def doom_nuke(self):
        pass