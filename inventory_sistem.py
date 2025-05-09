# The list is created with its corresponding dictionary during the initial inventory.

stock = [
    {"name":"cuaderno", "price":3500, "quantity":10},
    {"name":"lapiz", "price":800, "quantity":20},
    {"name":"borrador","price":400, "quantity":50}
]

# The function to add products is created, validating that price and quantity are numbers.
def add_product():
    price1 = True
    name = str( input("Ingresa el nombre del producto que deseas añadir al inventario:\n").strip().lower())
    while price1:
         try:
             price = float(input("Ingresa el valor unitario del producto:\n"))
             quantity = int(input("Ingresa la cantidad del producto:\n"))
             product = {"name": name, "price": price, "quantity": quantity}
             stock.append(product)
             print(f"El producto {name} se agregó exitosamente.")
             price1= False
         except ValueError:
             print("El precio y la cantidad deben ser números.")    

# The function is created to query products, validates that the product is registered and can return the information.
def consult_product():
    consult = input("¿Cuál producto deseas consultar?\n").strip().lower()
    found = False
    for product in stock:
        if product["name"].strip().lower() == consult:
            print(f"Nombre: {product['name']}\nPrecio: {product['price']}\nCantidad: {product['quantity']}")
            found = True
            break
    if not found:
        print(f"El producto {consult} no se encuentra registrado.")  
        
# Function is created to update product price. Validates that the product to update is registered and that the price is a number.
def update_price():
    update = input("¿A cuál producto deseas actualizarle el precio?\n").strip().lower()
    found_1 = False
    for product in stock:
        if product["name"].strip().lower() == update:
                 try:
                     change = float(input("Ingrese el precio actualizado:\n"))
                     product["price"] = change
                     print(f"Precio actualizado exitosamente:\nProducto:{product['name']}\nPrecio:${product['price']}")
                     found_1 = True
                     break
                 except ValueError:    
                     print("El precio debe ser un número.")    
                     return
    if not found_1:
        print(f"Producto {update} no encontrado.")
        
# A function is created to delete a product, validating that the product is registered. It also adds a confirmation so that the user can be sure to delete the product.
def delete_product():
    delete = input("¿Qué producto deseas eliminar?\n").strip().lower()
    if not delete:
        print("No se ingresó ningún producto.\n")
        return
    found_2 = False  
    for product in stock:    
        if product["name"].strip().lower() == delete:
            safety = input(f"¿Estás seguro que deseas eliminar {delete} del inventario? (si/no)\n").strip().lower()
            if safety == "si":
                stock.remove(product)
                print(f"El producto {delete} fue eliminado exitosamente.\n")
            else:
                print("Proceso Cancelado.\n")
            found_2 = True
            break  
    if not found_2:
        print(f"Producto {delete} no encontrado.\n")

    
# The function is created to calculate the total value of the inventory, validating that the inventory does have items recorded.    
def total_stock():
    if not stock:
        print("El inventario está vacío.\n")
        return
    total = sum(map(lambda p: p["price"] * p["quantity"], stock))
    print(f"Valor total del inventario: ${total}")
    
# Function is created to display all current inventory.  
def look_list():
    for product in stock:
        print(f"Nombre: {product['name']} - Precio: {product['price']} - Cantidad: {product['quantity']}\n")
    
# Function to exit the program is created      
def exit_program():
    print("¡Gracias por usar nuestros servicios!")
    print("¡Adiós!")
    

# Welcome to the program is printed
def main_menu():
    print("¡Bienvenido a ARCA DE PAPEL- Navega en la inspiración!")
    print("   ***********Programa de inventarios***********\n")

# Loop is added so that the menu repeats as long as the user wants to continue working on the inventory.
main = 0
while main != 7:

    print("***********MENÚ***********")
    print("1. Agregar un nuevo producto.")
    print("2. Consultar producto.")
    print("3. Actualizar precio de producto.")
    print("4. Eliminar producto.")
    print("5. Consultar valor total de inventario.")
    print("6. Ver listado inventario.")
    print("7. Salir.")

    try:
        option = int(input("Por favor seleccione una opción:\n"))

        if option == 1:
            add_product()
        elif option == 2:
            consult_product()
        elif option == 3:
            update_price()
        elif option == 4:
            delete_product()
        elif option == 5:
            total_stock()
        elif option == 6:
            look_list()
        elif option == 7:
            exit_program()    
            break
        else:
            print("Opción no válida, por favor elige un número entre 1 y 7.\n")
    except ValueError:
        print("Por favor ingresa un número válido.\n")
        



