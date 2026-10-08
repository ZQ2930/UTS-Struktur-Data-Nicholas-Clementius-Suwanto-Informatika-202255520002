# CAR SELLING INVENTORY SYSTEM

cars = []

def evaluatePrice(year, mileage, condition, originalPrice):
    price = originalPrice
    age = 2026 - year
    price -= age * 15000000
    price -= (mileage // 10000) * 5000000
    if condition == "Excellent":
        price += 20000000
    elif condition == "Good":
        price += 10000000
    elif condition == "Fair":
        price -= 10000000
    elif condition == "Poor":
        price -= 20000000
    return price

def addCar():
    print("\n===== ADD CAR =====")
    carID = input("Enter Car ID: ")
    brand = input("Enter Brand: ")
    model = input("Enter Model: ")
    year = int(input("Enter Year: "))
    mileage = int(input("Enter Mileage (km): "))
    originalPrice = int(input("Enter the original price of the car: "))
    
    print("\nCondition:")
    print("1. Excellent")
    print("2. Good")
    print("3. Fair")
    print("4. Poor")

    conditionChoice = input("Choose condition: ")
    
    if conditionChoice == "1":
        condition = "Excellent"
    elif conditionChoice == "2":
        condition = "Good"
    elif conditionChoice == "3":
        condition = "Fair"
    elif conditionChoice == "4":
        condition = "Poor"
    else:
        print("Invalid condition.")
        return

    price = evaluatePrice(year, mileage, condition, originalPrice)
    car = [carID, brand, model, year, mileage, condition, price]
    cars.append(car)
    print("\nCar added successfully!")
    print("Estimated Price: Rp", price)

def sellCar():
    print("\n===== SELL CAR =====")
    searchID = input("Enter Car ID: ")

    for car in cars:
        if searchID.lower() == car[0].lower():

            print("\n===== CAR FOUND =====")
            print("ID        :", car[0])
            print("Brand     :", car[1])
            print("Model     :", car[2])
            print("Year      :", car[3])
            print("Mileage   :", car[4], "km")
            print("Condition :", car[5])
            print("Price     : Rp", car[6])

            confirm = input("\nSell this car? (y/n): ")

            if confirm.lower() == "y":
                cars.remove(car)
                print("\nCar sold successfully!")
            else:
                print("\nSale cancelled.")
            return

    print("\nCar not found.")

def displayCars(cars, index=0):
    if index == len(cars):
        return
    car = cars[index]
    print("---------------------------------------------")
    print("ID        :", car[0])
    print("Brand     :", car[1])
    print("Model     :", car[2])
    print("Year      :", car[3])
    print("Mileage   :", car[4], "km")
    print("Condition :", car[5])
    print("Price     : Rp", car[6])
    displayCars(cars, index + 1)

def sortByPrice(cars):
    if len(cars) <= 1:
        return cars
    
    pivot = cars[-1]
    smaller = []
    larger = []

    for car in cars[:-1]:
        if car[6] < pivot[6]:
            smaller.append(car)
        else:
            larger.append(car)

    return sortByPrice(smaller) + [pivot] + sortByPrice(larger)

def searchByModel(cars, target):
    found = []

    for car in cars:
        if (target.lower() in car[1].lower() or target.lower() in car[2].lower()):
            found.append(car)

    return found

def sortByModel(cars):
    if len(cars) <= 1:
        return cars
    
    pivot = cars[-1]
    smaller = []
    larger = []

    for car in cars[:-1]:
        if car[2].lower() < pivot[2].lower():
            smaller.append(car)
        else:
            larger.append(car)
    return sortByModel(smaller) + [pivot] + sortByModel(larger)


while True:
    print("\n===================================")
    print("       CAR SELLING INVENTORY")
    print("===================================")
    print("1. Add Car")
    print("2. Display Cars")
    print("3. Sort Cars by Price")
    print("4. Search Car by Make or Model")
    print("5. Sell Car")
    print("6. Exit")

    choice = input("\nChoose: ")

    if choice == "1":
        addCar()
    elif choice == "2":
        if len(cars) == 0:
            print("\nNo cars in inventory.")
        else:
            print("\n===== CAR INVENTORY =====")
            displayCars(cars)
    elif choice == "3":
        if len(cars) == 0:
            print("\nNo cars in inventory.")
        else:
            cars = sortByPrice(cars)
            print("\n===== CARS SORTED BY PRICE =====")
            displayCars(cars)
    elif choice == "4":
        if len(cars) == 0:
            print("\nNo cars in inventory.")
        else:
            target = input("\nEnter Car Make or Model: ")
            results = searchByModel(cars, target)
            if len(results) > 0:
                print("\n===== CARS FOUND =====")
                for car in results:
                    print("---------------------------------------------")
                    print("ID        :", car[0])
                    print("Brand     :", car[1])
                    print("Model     :", car[2])
                    print("Year      :", car[3])
                    print("Mileage   :", car[4], "km")
                    print("Condition :", car[5])
                    print("Price     : Rp", car[6])
            else:
                print("\nCar not found.")

    elif choice == "5":
        if len(cars) == 0:
            print("\nNo cars in inventory.")
        else:
            sellCar()

    elif choice == "6":
        print("\nThank you for using the system!")
        break
    else:
        print("\nInvalid choice.")