# The starting point for this task is the module lab6_flight, that is, the Flight class.
# Note that one attribute of this class is a list of flight passengers, that is, a list
# of objects of the class Passenger and/or its subclasses BusinessPassenger and
# EconomyPassenger defined in the module lab6_passengers.
# In addition, one attribute (departure) is of the datetime.datetime type.
# Your task is to create functions for
# - serialising (writing) objects of the class Flight into a .json file
# - deserializing (reconstructing) objects of the class Flight from a
#   .json file (created using the previous function)


from lab6.lab6_flight import Flight
from lab6.lab6_passengers import EconomyPassenger, BusinessPassenger, Passenger
import json
from pathlib import Path
from sys import stderr


known_classes = {
    Passenger.__name__ : Passenger,
    EconomyPassenger.__name__ : EconomyPassenger,
    BusinessPassenger.__name__ : BusinessPassenger,
    Flight.__name__ : Flight
}


def get_results_dir():
    results_dir = Path.cwd() / "results"
    if not results_dir.exists(): results_dir.mkdir()
    return results_dir


def serialise_to_json(obj):

    obj_type = type(obj)

    if obj_type in known_classes.values():
        obj_dict = {'__objclass__': obj_type.__name__}
        obj_dict.update(vars(obj))

        if isinstance(obj, Flight):
            # representing departure (datetime) object as string by
            # calling the function from the flight class that does the formatting
            obj_dict['_Flight__departure'] = obj.format_departure()

        return obj_dict

    raise TypeError(f"ERROR! Cannot serialise objects of type {obj_type.__name__}!\n"
                    f"Only objects of the following types: " + ", ".join(known_classes.keys()))


def deserialise_from_json(json_obj):

    try:
        obj_type = json_obj['__objclass__']
    except KeyError as key_err:
        stderr.write(f"ERROR! Cannot retrieve object type -> not able to proceed!")
        return json_obj

    if obj_type in known_classes.keys():
        obj_cls = known_classes[obj_type]
        obj = obj_cls.__new__(obj_cls)
        for key, val in json_obj.items():
            if key != '__objclass__':
                setattr(obj, key, val)

        if obj_type == Flight.__name__:
            # calling setter for the departure attribute and
            # passing it the value associated with the '_Flight__departure' key
            obj.departure = json_obj['_Flight__departure']

        return obj

    stderr.write(f"ERROR! Received object of type {obj_type}, "
                 f"but can only process objects of the following types: " + ", ".join(known_classes.keys()))
    return json_obj


if __name__ == '__main__':

    lh992 = Flight.from_Frankfurt_by_Lufthansa('LH992', '2019-12-03 12:20')
    lh992.destination = "Amsterdam"
    # print(lh992)
    # print()

    bob = BusinessPassenger("Bob Smith", "123456", air_miles=1000, checked_in=True)
    john = EconomyPassenger("John Smith", "987654", checked_in=False)
    bill = EconomyPassenger("Billy Stone", "917253", air_miles=5000, checked_in=True)
    dona = EconomyPassenger("Dona Stone", "917254", air_miles=2500, checked_in=True)
    kate = EconomyPassenger("Kate Fox", "114252", air_miles=3500, checked_in=True)

    for p in (bob, john, bill, dona, kate):
        lh992.add_passenger(p)

    # print(lh992.__dict__)

    lh992_file = get_results_dir() / 'flight_lh992.json'

    with open(lh992_file, 'w') as fjson:
        json.dump(lh992, fjson, indent=4, default=serialise_to_json)

    print(f"\nContent read from json file '{lh992_file.absolute()}':")
    with open(lh992_file, 'r') as fjson:
        flight_copy = json.load(fjson, object_hook=deserialise_from_json)
        print(flight_copy)