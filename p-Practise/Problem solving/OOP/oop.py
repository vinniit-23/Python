# Object Oriented Proframming in Python
class Car:
    total_obj_created = 0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        print("This is constructor in python. ")
        print(f"this {brand} and its model is {model}")
        Car.total_obj_created += 1
    def full_name(self):
        return "car brand name "+self.__brand + " car model name "+ self.__model
    def get_brand(self):
        print("This is getter method of car class which return brand ")
        return self.__brand + " brand name"
    
    def get_model(self):
        print("This is getter method of car class which return model ")
        return self.__model + " model name"
    def fuel_type(self):
        return " normal car runs on petrol and diesel"
    @staticmethod
    def general_info_of_car():
        return f"this is general information of cars"
    @property
    def model_brand(self):
        return self.__model + " "+self.__brand
    

class Battery:
    def __init__(self):
        print( "the battery capacity is 80 to 90kwh" )
    

class Engine:
    def __init__(self):
        print ( "Engine have 150 horsepower"  ) 
    
    
    
class ElectricCar(Car,Engine,Battery):
    def __init__(self, brand, model):
        Car.__init__(self, brand, model)
        Engine.__init__(self)
        Battery.__init__(self)   
        
    battery_size = "85kwh"
    def fuel_type(self):
        return "electric car runs on electric current, they need to recharge their batterys"
        



        

my_car = Car("bmw","M5")
print("car details",my_car.full_name())
print(my_car.get_brand(),my_car.get_model())
print(my_car.fuel_type())
print(my_car.model_brand)
print(isinstance(my_car,Car))

electric_car = ElectricCar("tesla","s1")
print("car name ",electric_car.get_brand(),"model name",electric_car.get_model(),"battery size", electric_car.battery_size)
print(electric_car.fuel_type())
print(isinstance(electric_car,Car))
print(isinstance(electric_car,ElectricCar))

print(Car.total_obj_created)
print(Car.general_info_of_car())