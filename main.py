from functions import *

while True:
    try:
        print("=" * 30)
        print("     MINI PRODUCT SYSTEM")
        print("=" * 30)
        
        print("""
            
            1. Show all products
            2. Sort by price ascending
            3. Sort by price descending
            4. Search product by name
            5. Search product by ID
            6. Find cheapest product
            7. Find most expensive product

            0. Exit
            """)
        
        print("=" * 30)


        choice = int(input("Enter your choice: "))

        if choice == 1:
            showProducts()

        elif choice == 2:
            sortByPriceAsc()

        elif choice == 3:
            sortByPriceDesc()

        elif choice == 4:
            searchByName()

        elif choice == 5:
            searchById()

        elif choice == 6:
            getCheapestProduct()

        elif choice == 7:
            getExpensiveProduct()

        elif choice == 0:
            print("Program exited!")
            break

        else:
            print("Invalid choice!")

    except ValueError as error:
        print(f"Error: {error}")