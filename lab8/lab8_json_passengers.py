# The starting point for this task is the module lab6_passengers, that is,
# the Passenger class and its subclasses BusinessPassenger and EconomyPassenger.
# Your task is to create functions for
# - serialising (writing) objects of the class Passenger and its subclasses
#   into a .json file
# - deserializing (reconstructing) objects of the class Passenger and its subclasses
#   from a .json file (created using the previous function)


from lab6.lab6_passengers import Passenger, EconomyPassenger, BusinessPassenger
import json
from sys import stderr
from pathlib import Path

known_classes = {
    Passenger.__name__ : Passenger,
    EconomyPassenger.__name__ : EconomyPassenger,
    BusinessPassenger.__name__ : BusinessPassenger
}


def serialise_to_json(obj):

    obj_type = type(obj)

    if obj_type in known_classes.values():
        obj_dict = {'__objclass__' : obj_type.__name__}
        obj_dict.update(vars(obj))
        return obj_dict

    raise TypeError(f"ERROR! Cannot serialise objects of type {obj_type.__name__}!\n"
                    f"Only objects of the following types: " + ", ".join(known_classes.keys()))



def deserialise_from_json(json_obj):

    try:
        obj_cls = json_obj['__objclass__']
    except KeyError as key_err:
        stderr.write("ERROR! No information about the object's class -> cannot proceed")
        stderr.write(str(key_err))
        return json_obj

    if obj_cls in known_classes.keys():
        cls = known_classes[obj_cls]
        obj = cls.__new__(cls)
        for key, val in json_obj.items():
            if key == '__objclass__': continue
            setattr(obj, key, val)
        return obj

    stderr.write(f"ERROR! Cannot desirialise objects of type {obj_cls}!")
    return json_obj


class PassengerEncoder(json.JSONEncoder):

    def default(self, o):

        if isinstance(o, tuple(known_classes.values())):
            json_obj = {'__objclass__' : o.__class__.__name__}
            json_obj.update(vars(o))
            return json_obj

        stderr.write(f"ERROR! Cannot serialise objects of type {o.__class__.__name__}")
        return super().default(self, o)



if __name__ == '__main__':

    bob = BusinessPassenger("Bob Smith", "123456", air_miles=1000, checked_in=True)
    # print(bob)
    # print()

    john = EconomyPassenger("John Smith", "987654", checked_in=False)
    # print(john)
    # print()

    bill = EconomyPassenger("Billy Stone", "917253", air_miles=5000, checked_in=True)
    # print(bill)
    # print()

    dona = EconomyPassenger("Dona Stone", "917253", air_miles=2500, checked_in=True)
    # print(dona)
    # print()

    passengers = [bob, john, bill, dona]
    # for p in passengers:
    #     print(p)
    #     print(p.__dict__)
    #     print()

    results_dir = Path.cwd() / 'results'
    if not results_dir.exists():
        results_dir.mkdir()
    passengers_file = results_dir / 'passengers.json'

    with open(passengers_file, 'w') as fjson:
        # json.dump(passengers, fjson, default=serialise_to_json, indent=4)
        json.dump(passengers, fjson, cls=PassengerEncoder, indent=4)

    print(f"\nPrinting passengers read from the json file: '{passengers_file}'")

    with open(passengers_file, 'r') as fjson:
        passengers_copy = json.load(fjson, object_hook=deserialise_from_json)

    for p in passengers_copy:
        print(p.__dict__)
        print()
        print(p)

