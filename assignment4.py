
#Menu
# 1. Add a city
# 2. Add a driver: Name, route
# 3. Add a city to the driver:
   # 0. to add the city at the beginning of the route
   # -1 to add the city at the end
   # you add it at this index
# 4. Remove the city from a driver's route
# 5. to check availability

class Driver:
    def __init__(self, name, route):
        self.name = name
        self.route = route

cities = []
drivers = []

def add_city():
    new_city = input("Enter the name of the city: ")
    if new_city.strip():
        if new_city not in cities:
            cities.append(new_city)
            print("City ",new_city,"added.")
        else:
            print("City ",new_city,"already exists.")
    else:
        print("Error: City name cannot be empty.")

def add_driver():
    driver_name = input("Enter driver name: ")
    if driver_name.strip():
        driver_route = input("Enter driver route (comma-separated cities): ").split(',')
        new_driver = Driver(name=driver_name, route=driver_route)
        drivers.append(new_driver)
        print("Driver ",driver_name,"added with route: {', '.join(driver_route)}")
    else:
        print("Error: Driver name cannot be empty.")


def add_city_to_driver_route():
    driver_name = input("Enter the name of the driver: ")
    city_name = input("Enter the name of the city to add to the driver's route: ")

    driver = next((d for d in drivers if d.name == driver_name), None)
    if driver:
        if city_name in cities:
            driver.route.append(city_name)
            print(city_name,"added to ",driver_name,"s route.")
        else:
            print("Error: ",city_name," is not a valid city.")
    else:
        print("Error: Driver ",driver_name," not found.")

def remove_city_from_driver_route():
    driver_name = input("Enter the name of the driver: ")
    city_name = input("Enter the name of the city to remove from the driver's route: ")

    driver = next((d for d in drivers if d.name == driver_name), None)
    if driver:
        normalized_city_name = city_name.strip().lower()
        if any(c.strip().lower() == normalized_city_name for c in driver.route):
            driver.route = [c for c in driver.route if c.strip().lower() != normalized_city_name]
            print(city_name, "removed from", driver_name,"'s route.")
        else:
            print("Error:",city_name,"is not in",driver_name,"'s route.")
    else:
        print("Error: Driver",driver_name,"not found.")

def check_deliverability():
    destination = input("Enter the destination city for the package: ")
    
    eligible_drivers = [driver.name for driver in drivers if destination in driver.route]

    if eligible_drivers:
        print("The package can be delivered by the following drivers:", ', '.join(eligible_drivers))
    else:
        print("No available driver for the specified destination.")
        
while True:
    print("Options:")
    print("1. Add a city")
    print("2. Add a driver")
    print("3. Add a city to a driver's route")
    print("4. Remove a city from a driver's route")
    print("5. Check deliverability of a package")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_city()
    elif choice == '2':
        add_driver()
    elif choice == '3':
        add_city_to_driver_route()
    elif choice == '4':
        remove_city_from_driver_route()
    elif choice == '5':
        check_deliverability()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a numSber between 1 and 6.")
