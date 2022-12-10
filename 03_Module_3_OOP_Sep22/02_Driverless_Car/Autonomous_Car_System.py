# Importing abstract base class to prevent creating and instance from parent class
from abc import ABC, abstractmethod
# Importing exit to end the process when selecting exit
from sys import exit
# Importing date time stamp to print with log
from datetime import datetime


# -----------------------------------------------------------------------------------------------------
# Section 1: Creating The main base classes (super class) for future implementations.
class MainControlUnit(ABC):
    """Control unit stores all the critical information and manages the car."""

    def __init__(self, def_driver, curnt_driver=None, drivers_dp=None, drivers=None, car_state=False, obstacles=None,
                 car_log=None):
        self._def_driver = def_driver
        self._curnt_driver = None
        self.drivers_dp = []
        self._drivers = {def_driver.username}
        self._car_state = car_state
        self._obstacles = []
        self._car_log = []
        self.drivers_dp.append(def_driver)

    # Driver database abstract methods -----------------------------------------
    @abstractmethod
    def check_driver(self, user):
        raise NotImplementedError

    @abstractmethod
    def insert_driver(self):
        raise NotImplementedError

    @abstractmethod
    def view_drivers(self):
        raise NotImplementedError

    @abstractmethod
    def remove_driver(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def drivers(self):
        raise NotImplementedError

    @drivers.setter
    @abstractmethod
    def drivers(self, value):
        raise NotImplementedError

    # Car Control Methods -----------------------------------------
    @abstractmethod
    def car_ignition(self):
        raise NotImplementedError

    @abstractmethod
    def accelerate(self):
        raise NotImplementedError

    @abstractmethod
    def decelerate(self):
        raise NotImplementedError

    @abstractmethod
    def change_lane(self):
        raise NotImplementedError

    @abstractmethod
    def change_direction(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def car_state(self):
        raise NotImplementedError

    @car_state.setter
    @abstractmethod
    def car_state(self):
        raise NotImplementedError

    # Object detection Methods -----------------------------------------
    @property
    @abstractmethod
    def curnt_driver(self):
        raise NotImplementedError

    @curnt_driver.setter
    @abstractmethod
    def curnt_driver(self, value):
        raise NotImplementedError

    @abstractmethod
    def check_sign(self):
        raise NotImplementedError

    @abstractmethod
    def check_car(self):
        raise NotImplementedError

    @abstractmethod
    def check_obj(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def obstacles(self):
        raise NotImplementedError

    @abstractmethod
    def add_obstacles(self):
        raise NotImplementedError

    @abstractmethod
    def list_obstacles(self):
        raise NotImplementedError

    @abstractmethod
    def update_carlog(self):
        raise NotImplementedError

    @abstractmethod
    def view_carlog(self):
        raise NotImplementedError


# Driver info Base Class -----------------------------------------
class DriverInfo(ABC):
    """Base class for driver info"""

    def __init__(self, name, age, username):
        self._name = name
        self._age = age
        self._username = username

    @abstractmethod
    def turn_on(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self):
        return self._name

    @property
    @abstractmethod
    def age(self):
        return self._age

    @property
    @abstractmethod
    def username(self):
        raise NotImplementedError


# V2V Base Class -----------------------------------------
class V2v(ABC):
    """Vehicle to Vehicle communication"""

    def __init__(self, car_type=None, cars=None):
        car_type = {}
        cars = []

    @abstractmethod
    def get_data(self):
        raise NotImplementedError

    @abstractmethod
    def update_db(self):
        raise NotImplementedError

    @abstractmethod
    def view_cars(self):
        raise NotImplementedError

    @abstractmethod
    def send_data(self, ):
        raise NotImplementedError


# Car info Base Class -----------------------------------------
class CarInfo(ABC):
    """The abstract class which provides an interface for the car and the vehicles in the system."""

    def __init__(self, car_type, direction, lane, speed=0):
        self._car_type = car_type
        self._direction = direction
        self._speed = speed
        self._lane = lane

    @property
    @abstractmethod
    def car_type(self):
        raise NotImplementedError

    @car_type.setter
    @abstractmethod
    def car_type(self, value):
        raise NotImplementedError

    @property
    @abstractmethod
    def direction(self):
        raise NotImplementedError

    @direction.setter
    @abstractmethod
    def direction(self, value):
        raise NotImplementedError

    @property
    @abstractmethod
    def lane(self):
        raise NotImplementedError

    @lane.setter
    @abstractmethod
    def lane(self, value):
        raise NotImplementedError

    @property
    @abstractmethod
    def speed(self):
        raise NotImplementedError

    @speed.setter
    @abstractmethod
    def speed(self, value):
        raise NotImplementedError


# objects, signs and sensor systems Base class -----------------------------------------
class Sensors(ABC):
    """base class from senor information"""

    def __init__(self, obj_types, obstacle=None):
        self._obj_types = obj_types
        self._obstacle = obstacle

    @abstractmethod
    def detect(self):
        raise NotImplementedError

    @abstractmethod
    def send_data(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def obstacle(self):
        raise NotImplementedError


class Obstacles(ABC):
    """Base class for obstacle types and position"""

    def __init__(self, obj_type, lane):
        self._obj_type = obj_type
        self._lane = lane

    @property
    @abstractmethod
    def obj_type(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def lane(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def timestamp(self):
        raise NotImplementedError


class Tsrs(ABC):
    """base class for sign data"""

    def __init__(self, sign_data):
        self._sign_data = sign_data

    @abstractmethod
    def check_sign(self):
        raise NotImplementedError

    @abstractmethod
    def check_db(self):
        raise NotImplementedError

    @abstractmethod
    def send_data(self):
        raise NotImplementedError


class SignType(ABC):
    """Base class for Sign Type."""

    def __init__(self, sign_type):
        self._sign_type = sign_type

    @property
    @abstractmethod
    def sign_type(self):
        raise NotImplementedError

    @sign_type.setter
    @abstractmethod
    def sign_type(self, value):
        raise NotImplementedError

    @property
    @abstractmethod
    def sign_descrip(self):
        raise NotImplementedError

    @sign_descrip.setter
    @abstractmethod
    def sign_descrip(self, value):
        raise NotImplementedError


class SignDb(ABC):
    """base class for signs database"""

    def __init__(self, signs):
        self.signs = signs

    @abstractmethod
    def check_sign(self):
        raise NotImplementedError


# -----------------------------------------------------------------------------------------------------
# Section 2: Creating  Classes

# Creating classes for car information ----------
class CarInfo2(CarInfo):
    """super class containing car data and position"""

    def __init__(self, car_type, direction, lane, speed=0):
        self._type = car_type
        self._speed = speed
        self._direction = direction
        self._lane = lane

    @property
    def car_type(self):
        return self._type

    @car_type.setter
    def car_type(self, value):
        self._type = value

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    @property
    def lane(self):
        return self._lane

    @lane.setter
    def lane(self, value):
        self._lane = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value


class Car(CarInfo2):
    """a subclass for carinfo2 to print the current state of the car"""

    def print_state(self):
        print(f"car type: {self.car_type}")
        print(f"speed: {self.speed}")
        print(f"Direction: {self.direction}")
        print(f"Lane: {self.lane}")


# Creating control unit class -------------------------------------------
# Creating data structure in class attribute
class ControlUnit(MainControlUnit):
    """The main control unit class that manages the car and the information"""

    def __init__(self, def_driver, drivers_dp=None, drivers=None, obstacles=None, car_state=False, car_log=None,
                 curnt_driver=None):
        self._def_driver = def_driver
        self._driver_db = []
        self._drivers = {def_driver.username}
        self._obstacles = []
        self._car_state = car_state
        self._car_log = []
        self._curnt_driver = None
        self._driver_db.append(def_driver)

    def view_drivers(self):
        print("CURRENT REGISTERED DRIVERS")
        print("{:<40} {:<28} {:<40}".format('NAME', 'AGE', 'USERNAME'))
        for user in self._driver_db:
            print("{:<40} {:<28} {:<40}".format(user.name, user.age, user.username))
        print("\n", 102 * "=", "\n")

    def remove_driver(self):
        """Deletes driver from driver list"""
        del_user = input("\nEnter the Driver Username to delete")
        if del_user == self._curnt_driver:
            print(
                "\nThis is an active driver, change username to remove driver \n")
            self.update_carlog(f"Attempt to remove '{del_user}'. is rejected.")

        elif del_user == self._def_driver.username:
            print("\nThis is the Default system Driver, Can not remove driver \n")
            self.update_carlog(f"Attempt to remove '{del_user}'. is rejected.")

        else:
            if del_user in self._drivers:
                self._drivers.remove(del_user)
                for user in self._driver_db:
                    if del_user == user.username:
                        self._driver_db.remove(user)
                print("\nDriver Removed!\n")
                self.update_carlog(f"Driver'{del_user}' Is removed from the system")

            else:
                print("\nDriver not in database")
                self.update_carlog("Attempt to remove failed, Driver does not exist.")

# adds Driver info to database and checks if it exists in the database.
    def insert_driver(self):
        """inserts new driver to the list"""
        new_name = (input("Enter driver's name: "))
        new_age = (input("Enter driver's age: "))
        new_username = (input("Enter new username:  "))
        self._driver_db.append(Driver(new_name, new_age, new_username))

        # Adding username to the user list
        if new_username in self._drivers:
            print("\nDriver is already registered")
            self.update_carlog("Attempt to add an existing username")
        else:
            self._drivers.add(new_username)
            print("\nUsername created!")
            self.update_carlog(f"Driver '{new_username}' is added.")

    def check_driver(self, login):
        """ Checks if there if the driver is added to the database and prevents duplicate usernames.)"""
        if login in control_unit.drivers:
            print("You are now logged in \n")
            self.update_carlog(f"Driver '{login}' is now authorized to use the system.")
            self.currnt_driver = login
            inter_menu()
        else:
            print("Driver is not in database, authorization denied\n")
            self.update_carlog("failed attempt to login")
            exit()

    def car_ignition(self, vehicle):
        """Changes car state to true"""
        if self.car_state:
            print("\nCar is already on!\n")

        else:
            self.car_state = True
            vehicle.speed = 30
            print("\nCar started, car is moving at 30 km/h\n")
            self.update_carlog("Car is on and moving at speed of 30 km/h")
        car_drive()

    def accelerate(self, car):
        """Accelerates the car by 20 km/h"""
        if not self.car_state:
            print("\nCar is Off, Please turn the car 'on'\n")
            self.update_carlog("Driver attempted to accelerate the car while off, command rejected!")
        else:
            car.speed += 20
            print(f"\nCar now is moving at {car.speed} km/h.\n")
            self.update_carlog(f"Car is accelerated to {car.speed} km/h.")

    def decelerate(self, car):
        """decelerates the car by 20km/h"""
        if not self.car_state:
            print("\nCar is off, Please turn the car 'on'\n")
            self.update_carlog("Driver attempted to reduce speed, command rejected!")
        else:
            if car.speed == 0:
                print(f"\ncar speed is already {car.speed}, can't reduce speed.\n")
                self.update_carlog("Driver attempted to decelerate the car while still, command rejected!")
            else:
                car.speed -= 20
                print(f"\nspeed reduced to {car.speed} km/h.\n")
                self.update_carlog(f"The car decelerated to {car.speed} km/h.")

    def change_direction(self):
        """A class to change car direction from (N)north to (S)south, or (S)south to (N)north"""
        if not self.car_state:
            print("\nCar is off, Please turn the car 'on'\n")
            self.update_carlog("Driver attempted to change direction of the car while off, command rejected!")
        else:
            if car.direction == "N":
                car.direction = "S"
                print(f"\ncar direction is now {car.direction}\n")
                self.update_carlog(f"car direction is now: {car.direction}.")

            else:
                car.direction = "N"
                print(f"\ncar direction is now: {car.direction}\n")
                self.update_carlog(f"car direction changed to: {car.direction}.")

# Checks car state and changes lanes
    def change_lane(self):
        """changes the car between 2 lanes."""
        if not self.car_state:
            print("\nCar is off, Please turn the car 'on'\n")
            self.update_carlog("Driver attempted to change lane of the car while off, command rejected!")
        else:
            if car.lane == 1:
                try:
                    new_lane = int(input("""\nEnter lane 2 by typing 2, Or 0 for the drive menu.
    Select option 0 or 2: """))
                    if new_lane == 2:
                        car.lane = 2
                        print(f"\nLane changed to 2 {car.lane}.\n")
                        self.update_carlog(f"Car lane changed to  {car.lane}.")

                    elif new_lane == 0:
                        car_drive()
                    else:
                        print("\n Wrong input, Select options 1 to 2")
                        self.change_lane()
                except ValueError:
                    print("\nWrong input")
            elif car.lane == 2:
                try:
                    new_lane = int(input(f"""\nCar is in lane {car.lane}. Enter lane 1 by typing 1, Or 0 for the drive
                     menu!
    Select option 0 or 1: """))
                    if new_lane == 1:
                        car.lane = 1
                        print(f"\nCar lane changed to {car.lane}.\n")
                        self.update_carlog(f"car lane change to: {car.lane}.")

                    elif new_lane == 0:
                        car_drive()
                    else:
                        print("\nWrong input")
                        self.change_lane()
                except ValueError:
                    print("\nWrong input!")

    def stop(self, vehicle):
        """stops the car and changes car state to false"""
        if not self._car_state:
            print("\nCar is not on, Cannot stop car\n")
            self.update_carlog("Driver attempted to stop car, command rejected!")
        else:
            if vehicle.speed == 0:
                print("\nCar already stopped\n")
                self.update_carlog("Driver stopped the car while already stopped")

            else:
                vehicle.speed = 0
                print("\nCar is stopped\n")
                self.update_carlog("car stopped")

# Checks sign data and commands the car depending on sign code inserted by user
    def check_sign(self, sign):
        """Checks traffic sign and commands the car"""

        code = sign.car_type
        desc = sign.sign_descrip

        if code == 1:
            if car.speed <= 30:
                print(f"\nCurrent speed is already {car.speed}\n")
                self.update_carlog(f"{desc} 30 km/h sign detected no action needed.")
            else:
                car.speed = 30
                print("\nCar speed set to 30 km/h\n")
                self.update_carlog(f"{desc} sign detected, speed reduced ")
        elif code == 2:
            if car.speed <= 110:
                print(f"\nCurrent speed is already {car.speed}.\n")
                self.update_carlog(f"{desc} sign detected. Car's speed is already {car.speed}.")
            else:
                car.speed = 110
                print("\nCar speed is set to 110 km/h\n")
                self.update_carlog(f"{desc} sign detected. Car's speed is set to {car.speed}.")
        elif code == 3:
            if car.speed == 0:
                print("\nCar is already stopped\n")
                self.update_carlog(f"{desc} sign detected. car already stopped")
            else:
                car.speed = 0
                print("\ncar is stopped\n")
                self.update_carlog(f"{desc} sign detected. car stopped")
        elif code == 4:
            if car.speed == 0:
                print("\ncar is already stopped\n")
                self.update_carlog(f"{desc} sign detected. Car is already stopped.")
            else:
                car.speed = 0
                print(
                    f"\nPedestrian crossing, car stopped {car.speed}.\n")
                self.update_carlog(f"{desc} sign detected. car stopped {car.speed}.")
        elif code == 5:
            if car.speed <= 30:
                print(f"\nCurrent speeds is already {car.speed}\n")
                self.update_carlog(f"{desc} sign detected. car speed is already {car.speed}.")
            else:
                car.speed = 30
                print(f"\nTurn sign detected car speed is set to {car.speed}\n")
                self.update_carlog(f"{desc} sign detected. Car's speed is set to {car.speed}.")

# A function that checks if other cars are in the same lane of the cars and changes lanes accordingly
    def check_car(self, veh):
        """Checks other cars and commands the car"""
        if veh.direction != car.direction:
            if veh.lane == car.lane:
                if car.lane == 1:
                    car.lane = 2
                    print("\ncar lane changed to 2\n")
                    self.update_carlog(
                        f"Car detected at Lane {veh.lane} and Direction: {veh.direction}. car lane changed to {car.lane}")
                elif car.lane == 2:
                    if car.speed < 110:  # If the velocity is less than 80, car changes its lane to the slowest one.
                        car.lane = 1
                        print("\ncar lane changed to 1\n")
                        self.update_carlog(
                            f"Car detected at Lane {veh.lane} and Direction: {veh.direction}. car lane changed to {car.lane}")
                    else:
                        car.lane = 1
                        print("\nCar is already in lane 1\n")
                        self.update_carlog(
                            f"Car detected at Lane {veh.lane} and Direction: {veh.direction}. car is already in lane {car.lane}")
                else:
                    car.lane = 2
                    print("\nThe car changed its lane from 3 to 2.\n")
                    self.update_carlog(
                        f"Car detected at Lane {veh.lane} and Direction: {veh.direction}. car lane changed to {car.lane}")
            else:
                print("\nCar is in anothor lane\n")
                self.update_carlog(
                    f"Car detected at Lane {veh.lane} and Direction: {veh.direction}. car lane changed to {car.lane}")
        else:
            if veh.lane == car.lane:
                if veh.speed <= car.speed:
                    print(
                        "\nOther car is slow, no action needed\n")  # It is on the same lane, but slower than our car.
                    self.update_carlog(
                        f"Car detected at Lane {veh.lane} and Direction: {veh.direction}. no action needed")
                else:
                    if car.lane == 1:
                        print(
                            "\nCar on different lane, no action needed\n")
                        self.update_carlog(
                            f"Car detected at Lane {veh.lane} and Direction: {veh.direction}. no action needed")
                    elif car.lane == 2:
                        car.lane = 1
                        print(f"\nCar Lane changed to {veh.direction}\n")
                        self.update_carlog(
                            f"Car detected at Lane {veh.lane} and Direction: {veh.direction}. Car lane changed to {car.lane}")
                    else:
                        car.lane = 2
                        print("\nCar lane not changed\n")
                        self.update_carlog(
                            f"Car detected at Lane {veh.lane} and Direction: {veh.direction}. no action needed")
            else:
                print("\nCar in another lane, no action needed\n")
                self.update_carlog(
                    f"Car detected at Lane {veh.lane} and Direction: {veh.direction}. no action needed")

    def check_obj(self, obstacle):
        """Checks detected objects detected and commands the car"""
        self.add_obstacles(obstacle)  # Adds the obstacle to the obstacle list
        if car.lane == obstacle.lane:
            if car.lane == 1:
                car.lane = 2
                print("\nCar lane changed to 2\n")
                self.update_carlog(
                    f"Object detected {obstacle.car_type} on lane {obstacle.lane}, lane changed to 2")
            else:
                car.lane = 1
                print("\nCar lane changed to 1\n")
                self.update_carlog(
                    f"Object detected {obstacle.car_type} on lane {obstacle.lane}, lane changed to 1")
        else:
            print(f"\nCurrent lane is {car.lane}, object lane is {obstacle.lane}. No action needed\n")
            self.update_carlog(
                f"Object detected {obstacle.car_type} on lane {obstacle.lane}, no action needed")

    @property
    def car_state(self):
        return self._car_state

    @car_state.setter
    def car_state(self, value):
        self._car_state = value

    @property
    def drivers(self):
        return self._drivers

    @property
    def obstacles(self):
        return self._obstacles

    @property
    def curnt_driver(self):
        return self._curnt_driver

    @curnt_driver.setter
    def curnt_driver(self, value):
        self._curnt_driver = value

    def add_obstacles(self, obstacle):
        self._obstacles.append(obstacle)

    def list_obstacles(self):
        """Views obstacles detected by sensors"""
        print("\n", "obstacles detected", "\n")
        print("{:<30} {:<18} {:<30}".format('DETECTED OBSTACLE', 'LANE', 'DATE AND TIME'))
        for obstacle in self._obstacles:
            print("{:<30} {:<18} {:<30}".format(obstacle.car_type, obstacle.lane, obstacle.timestamp))
        print("\n", 78 * "=", "\n")

    def update_carlog(self, text):
        """Updates the car log."""
        # Calculating timestamp
        time_now = datetime.now()
        timestamp = time_now.strftime("%d/%m/%Y %H:%M:%S")
        self._car_log.append([text, timestamp])  # Adding the message with timestamp

    def view_carlog(self):
        """A class to view the car log that contains the recent driver input"""
        print("\n", "Car log updates:""\n")
        print("{:<84} {:<25}".format('Record', 'Time Stamp'))
        while len(self._car_log) > 0:
            temp = self._car_log.pop()
            print("{:<84} {:<25}".format(temp[0], temp[1]))
        print("\n", "----- THE END OF CAR LOG -----", "\n")


# A class to store Driver info, Only getters are added to view the information
class Driver(DriverInfo):
    """Class for driver information"""

    def __init__(self, name, age, username):
        self._name = name
        self._surname = age
        self._username = username

    def turn_on(self):
        control_unit.car_ignition(car)

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._surname

    @property
    def username(self):
        return self._username


# Creating Classes for object detection  -------------------------------------------
# A class to insert objects or obstacles and lane position
class Sensor(Sensors):
    """a class to detect/insert object type and sends it to control unit"""

    def __init__(self, obj_types=None, obstacle=None):
        self._obj_types = {1: 'Unkown Object', 2: 'Traffic cone', 3: 'Pedestrian', 4: 'cat', 5: 'speed pump'}
        self._obstacle = []

    def detect(self):
        """Detects Object Sign."""
        type_code = int(input("""\nPlease select an obstacle to place on the road:
1. Unknown Object
2. Traffic object
3. Pedestrian
4. cat
5. Speed pump
Select options 1 to 5: """))
        lane = int(input("""\nSelect Lane to place object: """))

# Object inserted by driver is defined, timestamp is calculated and sent to control unit
        for x in self._obj_types.keys():
            if type_code == x:
                obj_type = self._obj_types.get(x)
        time_now = datetime.now()
        timestamp = time_now.strftime("%d/%m/%Y %H:%M:%S")
        obj = Obstacle(obj_type, lane, timestamp)
        self._obstacle = obj
        self.send_data(obj)

    def send_data(self, obj):
        """Sends the data to the control unit"""
        control_unit.check_obj(obj)

    @property
    def obstacle(self):
        return self._obstacle


# A class for sharing obstacle data and position with control unit using getters and setters
class Obstacle(Obstacles):
    """Class for storing obstacle types and position"""

    def __init__(self, obj_type, lane, timestamp):
        self._type = obj_type
        self._lane = lane
        self._timestamp = timestamp

    @property
    def obj_type(self):
        return self._type

    @property
    def lane(self):
        return self._lane

    @property
    def timestamp(self):
        return self._timestamp


# A class to insert a car type --> Speed --> Lane --> then sends data to control unit
class V2VC(V2v):
    """V2V Communication, Inserting other cars and sends information to the control unit"""

    def __init__(self, car_type=None, cars=None):
        self._car_type = {1: 'Sedan', 2: 'SUV', 3: 'Motorbike', 4: 'Truck'}
        self._cars = []

    def get_data(self):
        """Inserts and detects nearby cars"""
        while True:
            try:
                type_code = int(input("""\nSelect car type instance:
1. Sedan
2. SUV
3. Motorbike
4. Truck


Insert: """))
                if type_code < 1 or type_code > 4:
                    print("\nWrong input.\n")
                    continue
            except ValueError:
                print("\nEnter a number.\n")
                continue
            else:
                break

        while True:
            try:
                speed = int(input("""\n Insert Car Speed (MAX 200 km/h): """))
                if speed > 200:
                    print("\n Exceeding speed, input speed should be lower than 200 km/h\n")
                    continue
                elif speed < 0:
                    print("\nSpeed can not be lower that 0, try again\n")
                    continue
            except ValueError:
                print("\nEnter a number\n")
                continue
            else:
                break

        while True:
            try:
                direction = input("""\n Enter current car direction: """)
                direction = direction.upper()
                if direction != "N" and direction != "S":
                    print("\n Wrong Input, Enter (N) north or (S) south.\n")
                    continue
            except ValueError:
                print("\nWrong Input, Enter (N) north or (S) south.\n")
                continue
            else:
                break

        while True:
            try:
                lane = int(input("""\n Select Current car lane
Enter options 1 or 2: """))
                if lane not in [1, 2]:
                    print("\nEnter options 1 or 2\n")
                    continue
            except ValueError:
                print("\nWrong Input\n")
                continue
            else:
                break

        for x in self._car_type.keys():
            if type_code == x:
                car_type = self._car_type.get(x)

        vehicle = CarInfo2(car_type, direction, lane, speed)

        self.update_db(vehicle)
        self.send_data(vehicle)

    def update_db(self, veh):
        """sends cars information to control unit """
        self._cars.append(veh)

    def view_cars(self):
        """prints detected cars"""
        print("\n", "Detected Cars", "\n")
        print("{:<33} {:<15} {:<15} {:<15}".format('Detected cars', 'lane', 'direction', 'speed'))
        for vehicle in self._cars:
            print(
                "{:<33} {:<15} {:<15} {:<15}".format(vehicle.car_type, vehicle.lane, vehicle.direction, vehicle.speed))

    def send_data(self, veh):
        control_unit.check_car(veh)


# Creating classes for sign db and TSRS -------------------------------------------
# Class will insert traffic signs using the sign codes stored in the sign database.
class TsrsType(Tsrs):
    """Class for detecting traffic sign type, placing it and sending the data to the control unit """

    def __init__(self, sign_number=None):
        self._sign_code = sign_number

    def check_sign(self):
        while True:
            try:
                self._sign_code = int(input("""\nInsert Sign type:
 1. Speed Limit (30 km/h)
 2. Speed Limit (110 km/h)
 3. Stop
 4. Pedestrian Cross Road
 5. Turn A head Reduce speed (30 km/h)
     """))
                if self._sign_code < 1 or self._sign_code > 5:
                    print("Wrong Input, Select from options above")
            except ValueError:
                print("input a number")
            else:
                return self.sign_code

    def check_db(self, code):
        """sends and receives traffic sign information."""
        return sign_db.check_sign(code)

    def send_data(self, sign_code, sign_desc):
        """A function to send traffic sign description to control unit"""
        traffic_sign = SignTypeDb(sign_code, sign_desc)
        control_unit.check_sign(traffic_sign)

    @property
    def sign_code(self):
        return self._sign_code


# A class for send and retrieve sign information using getters and setters.
class SignTypeDb(SignType):
    """A class to store sign type and retrieves it """

    def __init__(self, sign_type=None, sign_descrip=None):
        self._sign_type = sign_type
        self._descrip = sign_descrip

    @property
    def sign_type(self):
        return self._sign_type

    @sign_type.setter
    def sign_type(self, value):
        self._sign_type = value

    @property
    def sign_descrip(self):
        return self._descrip

    @sign_descrip.setter
    def sign_descrip(self, value):
        self._descrip = value


# Class for storing sign database in a dictionary with a function to send sign information to TSRS.
class SignsDb2(SignDb):
    """Traffic signs database."""

    def __init__(self, t_signs=None):
        self._t_signs = {1: 'Speed Limit (30 km/h)', 2: 'Speed Limit (100 km/H)', 3: 'Stop', 4: 'pedestrian crossing',
                         5: 'Turn A head Reduce speed (30 km/h)'}

    def check_sign(self, t_code):
        """Checks sign type and sends description"""
        return self._t_signs.get(t_code)


# Creating objects -------------------------------------------
# Creating permanent objects, passing the default driver and setting a default car position
defualt_driver = Driver('Alex', '28', 'defaultd')
control_unit = ControlUnit(defualt_driver)
sign_db = SignsDb2()
sign_recog = TsrsType()
v2v = V2VC()
car = Car('Car', 'N', 1)
sensors = Sensor()


# -----------------------------------------------------------------------------------------------------
# Section 3: Creating  functions for user interaction


# checks username to access car system (landing page)
def login():
    """step 1 driver log in"""
    print("Welcome to the autonomous car system")
    print("""
        Please enter your username
        """)
    print("")
    username = input("Username : ")
    control_unit.check_driver(username)


# Interface menu for car operations and information
def inter_menu():
    """Step 2 car interaction menu"""
    while True:
        print(30 * "", "SMART CAR INFORMATION AND INTERACTION SYSTEM (SCIIS)")
        print("""
        1. Car Info
        2. Car Drive
        3. Car Settings
        4. Change Driver
        5. Exit
        """)
        try:
            choice = int(input("Please select your option 1 - 5: "))
            if choice == 1:
                inf_menu()
            elif choice == 2:
                car_drive()
            elif choice == 3:
                car_settings()
            elif choice == 4:
                login()
            elif choice == 5:
                print("System Off, Goodbye!")
                exit()
            else:
                print("Wrong input")

        except ValueError:
            print("Wrong input")


# Interface menu for car information
def inf_menu():
    """information menu for viewing car information"""
    while True:
        print("""
        INFORMATION MENU

        1. Car Status
        2. View Car Log
        3. View user list
        4. view object list 
        5. view detected cars list 
        6. Main menu
        7. Exit
            """)
        try:
            choice = int(input("Please select an option: "))
            if choice == 1:
                print("")
                car.print_state()
                print("")

            elif choice == 2:
                control_unit.view_carlog()
            elif choice == 3:
                control_unit.view_drivers()
            elif choice == 4:
                control_unit.list_obstacles()
            elif choice == 5:
                v2v.view_cars()
            elif choice == 6:
                inter_menu()
            elif choice == 7:
                print("System Off, Goodbye!")
                exit()
            else:
                print("Wrong input")

        except ValueError:
            print("Wrong input, Select options from 1 - 7")


# Interface menu for car controls
def car_drive():
    """car controls function"""
    while True:
        print("""
        Drive Menu 
        
        1. Start the car
        2. Accelerate
        3. Decelerate 
        4. Change direction (U-turn)
        5. Change lane
        6. Stop the car
        7. Main Menu
        8. Exit
            """)

        try:
            choice = int(input("Please select an option: "))
            if choice == 1:
                defualt_driver.turn_on()
            elif choice == 2:
                control_unit.accelerate(car)
            elif choice == 3:
                control_unit.decelerate(car)
            elif choice == 4:  # U-turn
                control_unit.change_direction()
            elif choice == 5:
                control_unit.change_lane()
            elif choice == 6:
                control_unit.stop(car)
            elif choice == 7:
                inter_menu()
            elif choice == 8:
                print("System Off, Goodbye!")
                exit()
            else:
                print("Wrong input")
        except ValueError:
            print("Wrong input")


# Interface menu for inserting objects and drivers
def car_settings():
    """Function for modifying users, adding obstacles and traffic signs"""
    while True:
        print("""
        Settings menu

        1. Insert Obstacle
        2. Insert Traffic Sign 
        3. Insert Car
        4. Insert New Driver
        5. Remove Existing Driver
        6. Main Menu
        7. Exit 
            """)

        try:
            choice = int(input("Please select an option: "))
            if choice == 1:
                sensors.detect()
            elif choice == 2:
                code = sign_recog.check_sign()
                description = sign_recog.check_db(code)
                sign_recog.send_data(code, description)
            elif choice == 3:
                v2v.get_data()
            elif choice == 4:
                control_unit.insert_driver()
            elif choice == 5:
                control_unit.remove_driver()
            elif choice == 6:
                inter_menu()
            elif choice == 7:
                print("System Off, Goodbye!")
                exit()
            else:
                print("Wrong input")
        except ValueError:
            print("Wrong input")


login()
# -----------------------------------------------------------------------------------------------------
