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



if __name__ == '__main__':

    pass