class Airplane:
    def __init__(self, make, model, year, max_speed, odometer, is_flying):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__max_speed = max_speed 
        self.__odometer = odometer
        self.__is_flying = is_flying
    

    def get_charactesristics(self):
        print(f'{self.__make} {self.__model}. Year: {self.__year}, Maximum speed: {self.__max_speed} km/h ')
    
    def take_off(self):
        self.__is_flying = 'True'
        print(f'Aiplane is flying: {self.__is_flying}')

    def fly(self):
        print(f'Distance: {self.__odometer} km')
    
    def land(self):
        self.__is_flying = 'False'
        print(f'Aiplane is flying: {self.__is_flying}')
       

airplane = Airplane('Airbus', 'GT-200', '2006', '600', '4000', 'False')
airplane.take_off()
airplane.land()
airplane.fly()
airplane.get_charactesristics()

    

     

