class Carrito:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart
    #append()
    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{product} agregado exitosamente")
    #remove
    def remove_from_cart(self):
        doomed_input = input("Coloque el producto que quiere eliminar")
        for item in self.cart:
            if doomed_input.lower() == item.lower():
                print(f"{item} a sido eliminado exitosamente")
                self.cart.remove(item)
    #extend()
    def import_from_liked(self, followed_import):
        self.cart.extend(followed_import)
        print(f"Ahora el carrito contiene: {self.cart}")

class Favoritos:
    def __init__(self, user, followed):
        self.user = user
        self.followed = followed
    #sort
    def positive_sort(self):
        print(f"Su lista de favoritos a sido ordenada de manera ascendente:{self.followed.sort()}")
    #reverse()
    def negative_sort(self):
        print(f"Su lista de favoritos a sido ordenada de manera descendente:{self.followed.reverse()}")
    #clear()
    def doom_nuke(self):
        print("Su lista de favoritos será purgada...")
        self.followed.clear()

temp_kart = []
fav_list = []
#Objetos:
user_cart = Carrito("Usuario_1", [])
user_followed = Favoritos("Usuario_1", [])
# Programa
key = True
while key:
    try:
        print("----------Menú-----------")
        ops = input("1.Agregar al carrito\n"
                    "2.Agregar a favoritos\n"
                    "3.Eliminar del carrito\n"
                    "4.Ordenar favoritos.\n"
                    "Opción: ")
        match ops:
            case "1":
                max_count = int(input("Cuántos productos desea agregar al carrito: "))
                for temp_product in range(max_count):
                    product_x = input("Coloque el producto: ")
                    user_cart.add_to_cart(product_x)
                print(user_cart.cart)
            case "2":
                max_count = int(input("Cuántos productos desea agregar a favoritos: "))
                for temp_product in range(max_count):
                    followed_x = input("Coloque el producto: ")
                    user_followed.followed.append(followed_x)
                print(user_followed.followed)
                #Merge lists
                merge_ops = input("Desea agregar esto al carrito Y/N: ")
                if merge_ops.lower() == "y":
                    user_cart.import_from_liked(user_followed.followed)
                elif merge_ops.lower() == "n":
                    print("Regresando al programa")
                else:
                    print("Eso no es un valor aceptado, regresando a menú...")

            case "3":
                pass
            case "4":
                key = False
                print("Gracias por usar el programa")
    except ValueError:
        print("Eso no es un número, pe")
    except Exception as e:
        print(f"Error inesperado: {e}")