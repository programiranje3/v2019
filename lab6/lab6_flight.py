# Modify the Flight class from Lab5 as follows:
#
# In addition to the flight_num, departure, and passengers attributes,
# the class should also have the following attributes:
# - origin - the location the flight departs from
# - destination - the destination of the flight
# - operated_by - the company that operates the flight
#
# The following methods of the Flight class need to be revised:
# - the constructor (__init__()) - it should receive 6 input parameters, one for
#   each attribute, but only the parameters for the flight number and the departure
#   have to be specified; the parameters for the origin, the destination, and
#   the operator have default value "unknown", while the default for passengers is None.
#
# - the method that returns a string representation of the given Flight object (__str__())
#   so that it describes the flight with the extended set of attributes
#
# Finally, the following new methods should be added:
# - get and set methods (using appropriate decorators) for the following attributes:
#   - flight_num - make it a private attribute and assure that the flight number consist of
#     two letters followed by 3-4 digits
#   - passengers - make it a private attribute and assure that only objects of the type Passenger
#     can be added to the passengers list; if None is passed to the setter, create an empty
#     passengers list
#
# - the class method from_Frankfurt_by_Lufthansa() for creating flights that fly from Frankfurt and
#   are operated by Lufthansa (alternative constructor); the method receives flight number and
#   the scheduled departure date and time
#
# - the class method to_Belgrade_by_AirSerbia() for creating flights that fly to Belgrade and
#   are operated by AirSerbia (alternative constructor); the method receives flight number and
#   the scheduled departure date and time
#
# - a generator method that generates a sequence of passengers who have not yet checked in
#
# - a generator method that generates a sequence of candidate passengers for an upgrade to
#   the business class; those are the passengers of the economy class whose air miles
#   exceed the given threshold (input parameter) and who have checked in for the flight;
#   the generated sequence should consider the passengers air miles, so that those with more
#   air miles are first offered the upgrade option

from datetime import datetime
from lab6.lab6_passengers import Passenger, EconomyPassenger, BusinessPassenger

class Flight:

    departure_format = "%Y-%m-%d %H:%M"

    def __init__(self, flight_num, departure, origin='unknown',
                 destination='unknown', operated_by='unknown', passengers=None):
        self.flight_num = flight_num
        self.departure = departure
        self.origin = origin
        self.destination = destination
        self.operated_by = operated_by
        self.passengers = passengers

        self.passenger_iter_index = 0


    @property
    def departure(self):
        return self.__departure if self.__departure else 'unknown'


    @departure.setter
    def departure(self, departure):
        if isinstance(departure, datetime) and departure > datetime.today():
            self.__departure = departure
        elif isinstance(departure, str):
            departure = datetime.strptime(departure, self.departure_format)
            self.__departure = departure if departure > datetime.today() else None


    @property
    def flight_num(self):
        return self.__flight_num if self.__flight_num else 'unknown'


    @flight_num.setter
    def flight_num(self, fnumber):
        if self.flight_number_valid(fnumber):
            self.__flight_num = fnumber
        else:
            print("ERROR - flight number could not be set")
            self.__flight_num = None


    @staticmethod
    def flight_number_valid(flight_number):
        return type(flight_number == str) and \
               5 <= len(flight_number) <= 6 and \
               all([ch.isalpha() for ch in flight_number[:2]]) and \
               all([ch.isdigit() for ch in flight_number[2:]])


    @property
    def passengers(self):
        return self.__passengers


    @passengers.setter
    def passengers(self, passenger_list):
        self.__passengers = list()
        if passenger_list:
            for passenger in passenger_list:
                self.add_passenger(passenger)


    def add_passenger(self, passenger):
        if isinstance(passenger, Passenger) and (passenger not in self.passengers):
            self.passengers.append(passenger)
        else:
            print('ERROR - passenger could not be added')


    def __iter__(self):
        return self


    def __next__(self):
        if self.passenger_iter_index == len(self.passengers):
            raise StopIteration
        current_passenger = self.passengers[self.passenger_iter_index]
        self.passenger_iter_index += 1
        return current_passenger


    def __str__(self):
        flight_str = f"Flight {self.flight_num}:"
        flight_str +=f"\nscheduled departure: {self.format_departure()}."
        if self.is_known(self.origin):
            flight_str += f"\ndeparting from: {self.origin}"
        if self.is_known(self.destination):
            flight_str += f"\nflying to: {self.destination}"
        if self.is_known(self.operated_by):
            flight_str += f"\nflight operated by: {self.operated_by}"
        if len(self.passengers) == 0:
            flight_str += "\nNo checked-in passengers"
        else:
            flight_str += "\nPassengers:\n" + "\n".join([str(passenger) for passenger in self.passengers])
        return flight_str


    @staticmethod
    def is_known(value):
        return value != 'unknown'


    def format_departure(self):
        if self.is_known(self.departure):
            return datetime.strftime(self.departure, self.departure_format)
        else:
            return 'unknown'


    @classmethod
    def from_Frankfurt_by_Lufthansa(cls, flight_num, departure):
        return cls(flight_num, departure, origin='Frankfurt', operated_by='Lufthansa')


    @classmethod
    def to_Belgrade_by_AirSerbia(cls, flight_num, departure):
        return cls(flight_num, departure, destination='Belgrade', operated_by='AirSerbia')


    def not_checked_in_passengers(self):
        not_checked_counter = 0
        for passenger in self.passengers:
            if not passenger.checked_in:
                yield passenger
                not_checked_counter += 1
        print(not_checked_counter)


    def candidates_for_upgrade(self, min_air_miles):
        # candidates = []
        # for passenger in self.passengers:
        #     if isinstance(passenger, EconomyPassenger) and passenger.candidate_for_upgrade(min_air_miles):
        #         candidates.append(passenger)
        #
        # for candidate in sorted(candidates, key=lambda c: c.air_miles, reverse=True):
        #     yield candidate

        for passenger in sorted(self.passengers, key=lambda p: p.air_miles, reverse=True):
            if isinstance(passenger, EconomyPassenger) and passenger.candidate_for_upgrade(min_air_miles):
                yield passenger



if __name__ == '__main__':

    # lh1411 = Flight('LH1411', '2019-11-09 6:50', origin='Belgrade', destination='Frankfurt')
    # print(lh1411)
    # print()

    lh992 = Flight.from_Frankfurt_by_Lufthansa('LH992', '2018-11-09 12:20')
    lh992.destination = "Amsterdam"
    # print(lh992)
    # print()

    bob = BusinessPassenger("Bob Smith", "123456", air_miles=1000, checked_in=True)
    john = EconomyPassenger("John Smith", "987654", checked_in=False)
    bill = EconomyPassenger("Billy Stone", "917253", air_miles=5000, checked_in=True)
    dona = EconomyPassenger("Dona Stone", "917251", air_miles=2500, checked_in=False)
    kate = EconomyPassenger("Kate Fox", "114252", air_miles=3500, checked_in=True)

    for p in [bob, john, bill, dona, kate]:
        lh992.add_passenger(p)

    # print(f"After adding passengers to flight {lh992.flight_num}:\n")
    # print(lh992)
    #
    print("Last call to passengers who have not yet checked in!")
    for passenger in lh992.not_checked_in_passengers():
        print(passenger)

    # print("Passengers offered an upgrade opportunity:")
    # for ind, passenger in enumerate(lh992.candidates_for_upgrade(2000)):
    #     print(f"{ind+1}. {passenger}")


    print()
    print("Candidates for upgrade to business class")
    g = lh992.candidates_for_upgrade(min_air_miles=1000)
    try:
        while True:
            print(next(g))
    except StopIteration:
        print("--- end of candidates list ---")