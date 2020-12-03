
class Vehicle:
    
    def __init__(self, make, model, color, fuelType, options):
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getfuelType(self):
        return self.fuelType

    def display_info(self):
       print(f'\nYou have a {self.color}, {self.make} {self.model} that runs off of {self.fuelType} and has {self.options}')



class Car(Vehicle):

    car_Amount = 0

    def __init__(self, make, model, color, fuelType, options, engineSize, numDoors):
        super().__init__(make, model, color, fuelType, options)
        self.engineSize = engineSize
        self.numDoors = numDoors

        Car.car_Amount += 1

    def getEngineSize(self):
        return self.engineSize

    def getNumDoors(self):
        return self.numDoors

    def display_info(self):
        super().display_info()
        print(f'Engine size: {self.getEngineSize()}, Number of doors: {self.getNumDoors()}')



class Truck(Vehicle):

    truck_Amount = 0

    def __init__(self, make, model, color, fuelType, options, cabStyle, bedLength):
        super().__init__(make, model, color, fuelType, options)
        self.cabStyle = cabStyle
        self.bedLength = bedLength

        Truck.truck_Amount += 1

    def getCabStyle(self):
        return self.cabStyle

    def getBedLength(self):
        return self.bedLength

    def display_info(self):
        super().display_info()
        print(f'Cab style: {self.getCabStyle()}, Bed length: {self.getBedLength()}')


def selectOptions():
    options_selected = []
    options_avaialable = ['power windows', 'power locks', 'power mirrors', 'dual climate control', 'memory seats', 'cruise control', 'bluetooth', 'remote start']

    while (True):
        for options in options_avaialable:
            print(f'{options}')
        option_chosen = input("Please choose an option to add or enter QUIT: ").upper()
        if (option_chosen.upper() == "QUIT"):
            break
        else:
            options_selected.append(option_chosen)
    
    return options_selected


def getCarInput():
    carDetails = {}
    carDetails["make"] = input("What is the make? ").upper()  
    carDetails["model"] = input("What is the model? ").upper()
    carDetails["color"] = input("What is the color? ").upper()
    carDetails["fuelType"] = input("What is the fuel type? ").upper()
    carDetails["options"] = selectOptions()
    carDetails["engineSize"] = input("What is the engine size? ").upper()
    carDetails["numDoors"] = input("How many doors? ").upper()
    return carDetails

def getTruckInput():
    truckDetails = {}
    truckDetails["make"] = input("What is the make? ").upper()  
    truckDetails["model"] = input("What is the model? ").upper()
    truckDetails["color"] = input("What is the color? ").upper()
    truckDetails["fuelType"] = input("What is the fuel type? ").upper()
    truckDetails["options"] = selectOptions()
    truckDetails["cabStyle"] = input("What is the cab style? ").upper()
    truckDetails["bedLength"] = input("What is the bed length? ").upper()
    return truckDetails

    
print("--------WELCOME TO VIRTUAL GARAGE---------")

def main():

    garage = []

    while True:
        add_Garage = input("(Y/N) Would you like to add a vehicle: ").lower()
        while add_Garage == 'y':
            what_Kind = input("(C/P) car or pickup: ").lower()
            if what_Kind == "c":
                carDetails = getCarInput()
                car = Car(carDetails["make"],
                carDetails["model"],
                carDetails["color"],
                carDetails["fuelType"],
                carDetails["options"],
                carDetails["engineSize"],
                carDetails["numDoors"])
                garage.append(car)
                break
            if what_Kind == "p":
                truckDetails = getTruckInput()
                truck = Truck(truckDetails["make"],
                truckDetails["model"],
                truckDetails["color"],
                truckDetails["fuelType"],
                truckDetails["options"],
                truckDetails["cabStyle"],
                truckDetails["bedLength"])
                garage.append(truck)
                break
            else:
                continue
        if add_Garage == 'n':
            print("Please ensure you have at least one car and one pickup.")
            print("Car amount: ", Car.car_Amount)
            print("Pickup amount: ", Truck.truck_Amount)
            if Car.car_Amount < 1 and Truck.truck_Amount < 1:
                print("You require more vehicles.")
                continue
            if Car.car_Amount >= 1 and Truck.truck_Amount >= 1:
                break
        if add_Garage != 'y' or 'n':
            continue

    for car in garage:
        car.display_info()

    print("---------THANK YOU FOR USING VIRTUAL GARAGE---------")
    

main()