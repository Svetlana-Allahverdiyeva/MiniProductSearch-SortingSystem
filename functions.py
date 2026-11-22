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

        n = len(products)

# Bubble Sort - ascending order

        for i in range(n - 1):
            for j in range(n - i - 1):
                if products[j]["price"] > products[j + 1]["price"]:
                    products[j], products[j + 1] = products[j + 1], products[j]

        for product in products:
            print(f"""
            ID: {product['id']}
            Name: {product['name']}
            Price: {product['price']} AZN
            """)

    except (KeyError, TypeError, ValueError) as error:
        print(f"Error: {error}")   

# Azalan sira ile...

def sortByPriceDesc():
    try:
        products = loadProducts()

        if not products:
            print("No products available!")
            return

        n = len(products)

# Bubble Sort - descending order

        for i in range(n - 1):
            for j in range(n - i - 1):
                if products[j]["price"] < products[j + 1]["price"]:
                    products[j], products[j + 1] = products[j + 1], products[j]

        for product in products:
            print(f"""
            ID: {product['id']}
            Name: {product['name']}
            Price: {product['price']} AZN
            """)

    except (KeyError, TypeError, ValueError) as error:
        print(f"Error: {error}")    

def searchByName():
    try:
        products = loadProducts()

        if not products:
            print("No products available!")
            return

        productName = input("Enter product name: ").lower()

        for product in products:
            if product["name"].lower() == productName:
                print(f"""
                Product Found!

                ID: {product['id']}
                Name: {product['name']}
                Price: {product['price']} AZN
                """)
                return

        print("Product not found!")

    except (KeyError, TypeError, ValueError) as error:
        print(f"Error: {error}")


def searchById():
    try:
        products = loadProducts()

        if not products:
            print("No products available!")
            return

        productId = int(input("Enter product ID: "))

# Binary Search requires sorted data

        products.sort(key=lambda product: product["id"])

        left = 0
        right = len(products) - 1

        while left <= right:
            mid = (left + right) // 2

            if products[mid]["id"] == productId:
                print(f"""
                Product Found!

                ID: {products[mid]['id']}
                Name: {products[mid]['name']}
                Price: {products[mid]['price']} AZN
                """)
                return

            elif products[mid]["id"] < productId:
                left = mid + 1

            else:
                right = mid - 1

        print("Product not found!")

    except (ValueError, KeyError, TypeError) as error:
        print(f"Error: {error}")

# En ucuz...
def getCheapestProduct():
    try:
        products = loadProducts()

        if not products:
            print("No products available!")
            return

        cheapestProduct = min(products, key=lambda product: product["price"])

        print(f"""
        Cheapest Product:
        ID: {cheapestProduct['id']}
        Name: {cheapestProduct['name']}
        Price: {cheapestProduct['price']} AZN
        """)

    except (KeyError, TypeError, ValueError) as error:
        print(f"Error: {error}")

# En bahali...
def getExpensiveProduct():
    try:
        products = loadProducts()

        if not products:
            print("No products available!")
            return

        expensiveProduct = max(products, key=lambda product: product["price"])

        print(f"""
        Most Expensive Product:
        ID: {expensiveProduct['id']}
        Name: {expensiveProduct['name']}
        Price: {expensiveProduct['price']} AZN
        """)

    except (KeyError, TypeError, ValueError) as error:
        print(f"Error: {error}")