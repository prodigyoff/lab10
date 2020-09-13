class Car:
    wheels_amount = 4

    def __init__(self, engine_power=None, car_brand=None, max_speed=None, fuel_tank_size=None,
                 width_in_meters=None, length_in_meters=None):
        self.engine_power = engine_power
        self.car_brand = car_brand
        self.max_speed = max_speed
        self.fuel_tank_size = fuel_tank_size
        self.width_in_meters = width_in_meters
        self.length_in_meters = length_in_meters

    @staticmethod
    def get_wheels_amount():
        return Car.wheels_amount

    def __str__(self):
        return "Car engine power is " + str(self.engine_power) + " horsepower" + "\n" + \
               "Car brand is " + str(self.car_brand) + "\n" + \
               "Car max speed is " + str(self.max_speed) + " mph" + "\n" + \
               "Car fuel tank size is " + str(self.fuel_tank_size) + " litres" + "\n" + \
               "Car width is " + str(self.width_in_meters) + " meters" + "\n" + \
               "Car length is " + str(self.length_in_meters) + " meters" + "\n"

    def __del__(self):
        pass

    @staticmethod
    def main():
        car_1 = Car(450)
        car_2 = Car(500, "Dota", 160, 35, 4)
        car_3 = Car(600, "Dota", 160, 35, 4, 1.5)
        cars = [car_1, car_2, car_3]
        for e in cars:
            print(e)
        print(Car.get_wheels_amount())


if __name__ == '__main__':
    Car.main()
