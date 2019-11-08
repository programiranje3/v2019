#
# Create the FlightService enumeration that defines the following items (services):
# snack, free e-journal, priority boarding, selection of food and drinks,
# free onboard wifi, and an item for cases when services are not specified.
#

from enum import Enum

class FlightService(Enum):

    SNACK = "snack"
    FREE_JOURNAL = "free e-journal"
    PRIORITY_BOARDING = "priority boarding"
    FOOD_AND_DRINKS = "selection oF food and drinks"
    FREE_WIFI = "free onboard wifi"
    UNSPECIFIED = "services not specified"


# Modify the Passenger class from Lab5 as follows:
#
# In addition to the name and passport attributes, the class should also have
# the following attributes:
# - air_miles - the number of miles the passenger has made with the given air company;
#   zero if not specified
# - checked_in - a boolean indicator variable, true if the passenger has checked in;
#   False if not specified
# - services - a class attribute defining the list of services available to all
#   passengers of a particular class (category); available services for various categories
#   of passengers should be defined as elements of the FlightService enumeration.
#   For this class, services are unspecified (FlightService.UNSPECIFIED), as they depend on
#   the passenger class and will be defined in the subclasses.
# Note that the attribute is_business (from Lab 5 version of the Passenger class) is dropped,
# as the flight class will be handled through (Python) class hierarchy.
#
#
# The following methods of the Passenger class need to be revised:
# - constructor (__init__()) - it should receive 4 input parameters, one for
#   each attribute, but only the parameters for the passenger's name and passport
#   have to be specified; the parameter for air_miles has zero as its default value,
#   while False is the default value for checked_in
# - a method that returns a string representation of a given Passenger object (__str__())
#   so that it describes a passenger with the extended set of attributes
#
# Finally, the following new method should be added:
# - a method (available_services()) that returns a list of strings describing services
#   available to the passengers (a class method); this list is created based on the
#   services attribute.
#


class Passenger:

    services = [FlightService.UNSPECIFIED]

    def __init__(self, name, passport, air_miles=0, checked_in=False):
        self.name = name
        self.passport = passport
        self.air_miles = air_miles
        self.checked_in = checked_in


    @property
    def passport(self):
        return self.__passport if self.__passport else 'unknown'

    @passport.setter
    def passport(self, passport_num):
        if isinstance(passport_num, str) and len(passport_num) == 6 and all([ch.isdigit() for ch in passport_num]):
            self.__passport = passport_num
        elif isinstance(passport_num, int) and len(str(passport_num)) == 6:
            self.__passport = str(passport_num)
        else:
            print("Error! Incorrect passport number! Passport set to None")
            self.__passport = None


    def __str__(self):
        passenger_str = f"{self.name}, passport number: {self.passport}, "
        passenger_str += f"current air miles: {self.air_miles}, "
        passenger_str += "checked-in." if self.checked_in else "NOT checked-in yet."
        return passenger_str


    def __eq__(self, other):
        return isinstance(other, Passenger) and other.passport == self.passport


    @classmethod
    def available_services(cls):
        return [service.value for service in cls.services]



# Create the EconomyPassenger class that extends the Passenger class and has:
# - method candidate_for_upgrade that check if the passenger is a candidate for an upgrade
#   and returns an appropriate boolean value; a passenger is a candidate for upgrade if their
#   current air miles exceed the given threshold (input parameter) and the passenger
#   has checked in
# - changed value for the services class attribute, which includes the following elements of
#   the FlightServices enum: snack, free e-journal
# - overridden __str__ method so that it first prints "Economy class passenger" and then
#   the available information about the passenger

class EconomyPassenger(Passenger):

    services = [FlightService.SNACK, FlightService.FREE_JOURNAL]

    def candidate_for_upgrade(self, threshold):
        return self.checked_in and self.air_miles > threshold

    def __str__(self):
        return "Economy class passenger " + super().__str__()


# Create class BusinessPassenger that extends the Passenger class and has:
# - changed value for the services class attribute, so that it includes:
#   priority boarding, selection of food and drinks, and free onboard wifi
# - overridden __str__ method so that it first prints "Business class passenger" and then
#   the available information about the passengers

class BusinessPassenger(Passenger):

    services = [FlightService.PRIORITY_BOARDING, FlightService.FOOD_AND_DRINKS, FlightService.FREE_WIFI]

    def __str__(self):
        return "Business class passenger " + super().__str__()



if __name__ == '__main__':

    jim = EconomyPassenger("Jim Jonas", '123456', air_miles=1000)
    # jim.flight_services = FlightService.FREE_WIFI
    print(jim)
    print(jim.__dict__)
    print(jim.available_services())
    print()

    bob = EconomyPassenger("Bob Jones", '987654')
    print(bob)
    print(bob.__dict__)
    print(bob.available_services())
    print()

    mike = BusinessPassenger("Mike Stone", '234567', air_miles=2000)
    print(mike)
    print(mike.__dict__)
    print(",".join([str(s) for s in mike.available_services()]))