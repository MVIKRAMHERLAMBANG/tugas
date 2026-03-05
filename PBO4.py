class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        if not isinstance(doors, int):
            raise ValueError("Doors must be an integer")
        self.doors = doors

    def honk(self):
        print("Beep! Beep!")

class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def load(self, weight):
        try:
            if weight > self.load_capacity:
                print(f"Overload! {weight}kg exceeds {self.load_capacity}kg capacity.")
            else:
                print(f"Loaded {weight} kg successfully.")
        except TypeError:
            print("Error: Weight must be a number.")

def main():
    try:
        my_car = Car("Toyota", "Corolla", 4)
        my_truck = Truck("Ford", "F-150", 1000)
        
        my_car.drive()
        my_car.honk()
        my_truck.drive()
        my_truck.load(1200)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()