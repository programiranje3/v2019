# Create the Passenger class with the following attributes:
# - name - the passenger's name and surname
# - passport - the passenger's passport number
# - is_business - a boolean indicator variable (true if the passenger is in the business class)
#
# The Passenger class should have the following methods:
# - a constructor (__init__()) that receives three input parameters corresponding to the
#   three attributes and are used to initialise the attributes
# - get and set methods for the passport attribute (using appropriate decorators);
#   designate this attribute as private and assure that it is a string of length 6,
#   consisting of digits only
# - a method that returns a string representation of a Passenger object (__str__())
# - a method that checks for equality of the given Passenger object and another object
#   that is passed to the method as its input parameter (__eq__()); two passengers are
#   considered the same if they have the same passport number

class Passenger:

    def __init__(self, name, passport, is_business):
        self.name = name
        self.passport = passport
        self.is_business = is_business

    @property
    def passport(self):
        return self.__passport if self.__passport else "unknown"

    @passport.setter
    def passport(self, pass_value):
        if isinstance(pass_value, str) and len(pass_value) == 6 and all([ch.isdigit() for ch in pass_value]):
            self.__passport = pass_value
        elif isinstance(pass_value, int) and (100000 <= pass_value <= 999999):
            self.__passport = str(pass_value)
        else:
            print("ERROR - wrong value for passport!")
            self.__passport = None


    def __str__(self):
        passenger_str = f"{self.name}, with passport number: {self.passport}"
        passenger_str += ", bussiness class." if self.is_business else ", economy class."
        return passenger_str


    def __eq__(self, other):
        return (type(other) == Passenger) and (self.passport == other.passport)



# Create the Flight class with the following attributes:
# - flight_num - flight number
# - departure - the date and time of the departure
# - passengers - list of passengers, that is, instances of the Passenger class
#
# - class attribute departure_format representing the expected format for
#   the departure date and time; its value should be "%Y-%m-%d %H:%M"
#
# The Flight class should have the following methods:
# - a constructor (__init__()) that receives the flight number and departure date and time
#   as its input parameters and uses them to initialise the flight_num and departure attributes,
#   respectively; it also initialises the passengers attribute to an empty list
# - get and set methods for the departure attribute (using appropriate decorators);
#   make this attribute private and assure that it is a datetime object and refers to
#   a moment in the future
# - a method for adding a passenger to the passengers list; the method adds the new
#   passenger only if the input parameter is really of the Passenger type and if the
#   passenger is not already in the list
# - a method that returns a string representation of the given Flight object (__str__())
# - methods for turning the given Flight object into an iterator (__iter__(), __next__())
#   over the flight passengers (ie. elements of the passengers list)

from datetime import datetime

class Flight:

    departure_format = "%Y-%m-%d %H:%M"

    def __init__(self, flight_num, departure):
        self.flight_num = flight_num
        self.departure = departure
        self.passengers = list()

        self.current_passenger = 0

    @property
    def departure(self):
        return self.__departure if self.__departure else "unknown"

    @departure.setter
    def departure(self, depart_value):
        if isinstance(depart_value, datetime) and depart_value > datetime.now():
            self.__departure = depart_value
        elif isinstance(depart_value, str):
            departure_parsed = datetime.strptime(depart_value, Flight.departure_format)
            if departure_parsed > datetime.now():
                self.__departure = departure_parsed
            else:
                self.__departure = None
        else:
            print("ERROR - improper value for flight departure")
            self.__departure = None

    def add_passenger(self, passenger):
        if isinstance(passenger, Passenger) and (not passenger in self.passengers):
            self.passengers.append(passenger)
        else:
            print("ERROR - passenger could not be added!")

    def __str__(self):
        flight_str = f"Flight {self.flight_num}, scheduled for departure: {self.format_departure(self.departure)}"
        if len(self.passengers) > 0:
            flight_str += "\nPassengers:\n" + "\n".join([str(passenger) for passenger in self.passengers])
        else:
            flight_str += "\nNo passengers yet"
        return flight_str


    @staticmethod
    def format_departure(departure_dt):
        if departure_dt != 'unknown':
            return  datetime.strftime(departure_dt, Flight.departure_format)
        return departure_dt


    def __iter__(self):
        return self


    def __next__(self):
        if self.current_passenger < len(self.passengers):
            next_passenger = self.passengers[self.current_passenger]
            self.current_passenger += 1
            return next_passenger
        else:
            raise StopIteration


if __name__ == '__main__':

    john = Passenger("John Smith", "123456", True)
    jane = Passenger("Jane Smith", "123489", True)
    bob = Passenger("Bob Smith", 987654, False)

    # print(john)
    # print(jane)
    # print(bob)
    #
    # print(f"john == jane: {john == jane}")
    # print(f"john == bob: {john == bob}")

    # "%Y-%m-%d %H:%M"
    lh14567 = Flight('lh14567', '2019-11-11 12:45')
    lh5678 = Flight('lh5678', '2019-11-04 13:00')

    lh14567.add_passenger(john)
    lh14567.add_passenger(jane)
    lh14567.add_passenger(bob)

    # print(lh14567)
    # print()
    # print(lh5678)

    for p in lh14567:
        print(str(p))