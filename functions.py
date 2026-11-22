import json

def loadProducts():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            products = json.load(file)
            
        return products
    
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        return []

def showProducts():
    try:
        products = loadProducts()

        if not products:
            print("No products available!")
            return

        for product in products:

            print(f"""
            ID: {product['id']}
            Name: {product['name']}
            Price: {product['price']} AZN
            """)

    except (KeyError, TypeError) as error:
        print(f"Error: {error}")

# Artan sira ile...

def sortByPriceAsc():
    try:
        products = loadProducts()
        
        if not products:
            print("No products available!")
            return
        
        sortByPriceAsc = sorted(products, key=lambda product: product["price"])

        for product in sortByPriceAsc:

            print(f"""
            ID: {product['id']}
            Name: {product['name']}
            Price: {product['price']} AZN
            """)

    except (KeyError, TypeError) as error:
        print(f"Error: {error}")

# Azalan sira ile...

def sortByPriceDesc():
    try:
        products = loadProducts()

        if not products:
            print("No products available!")
            return

        sortedProductsDesc = sorted(products, key=lambda product: product["price"], reverse=True)

        for product in sortedProductsDesc:

            print(f"""
            ID: {product['id']}
            Name: {product['name']}
            Price: {product['price']} AZN
            """)

    except (KeyError, TypeError) as error:
        print(f"Error: {error}")

def searchByName():
    try:
        products = loadProducts()
        
        if not products:
            print("No products available!")
            return

        searchName = input("Enter product name: ").lower()

        foundProducts = []

        for product in products:
            if searchName in product["name"].lower():
                foundProducts.append(product)

        if foundProducts:
            for product in foundProducts:

                print(f"""
                ID: {product['id']}
                Name: {product['name']}
                Price: {product['price']} AZN
                """) 

        else:
            print("Product not found!")
    
    except (KeyError, TypeError, ValueError) as error:
        print(f"Error: {error}")   