from sys import stderr
import pickle
import csv
from pathlib import Path


def get_data_dir():
    data_dir = Path.cwd() / 'data'
    if not data_dir.exists(): data_dir.mkdir()
    return data_dir

def get_results_dir():
    results_dir = Path('results')  # this is the same as results_dir = Path.cwd() / 'results'
    results_dir.mkdir(exist_ok=True) # alternative for checking if the directory exists
    return results_dir


#
# Task 1
#
# Write a function that reads in the content of the given text file, sorts it,
# and writes the (sorted) content to new textual files.
# Assume that the content of the given file consists of file names, some
# of which have an extension ('hello.txt'), others do not ('results').
# Each file name is given in a separate line.
# Sorting should be case insensitive and done in the ascending alphabetical
# order, as follows:
# - for files with extension: first based on the extension and then based
#   on the file name,
# - for files without extension, based on the file name.
# After sorting, file names with extension should be writen in one textual
# document (e.g., "task1_files_with_extension.txt") and file names without
# an extension in another text file (e.g. "task1_files_no_extension.txt")
# Include appropriate try except blocks to prevent program from crushing
# in case of a non existing file, or a problem ocurring while reading
# from / writing to a file.

# Use the file 'data/sample_file_names.txt'

def read_sort_write(data_src):

    def extension_sort(file_name):
        name, ext = file_name.rsplit(".", maxsplit=1)
        return ext.lower(), name.lower()

    with_extension = []
    no_extension = []

    try:
        with open(data_src, 'r') as fr:
            lines = fr.readlines()
            # print(lines)
            for line in lines:
                if line.count('.') > 0:
                    with_extension.append(line.rstrip())
                else:
                    no_extension.append(line.rstrip())
    except FileNotFoundError:
        stderr.write(f"ERROR: file '{data_src}' does not exist")
    except OSError as err:
        stderr.write(f"ERROR: {err}")

    else:
        no_extension.sort(key=lambda file_name: file_name.lower())
        with_extension.sort(key=extension_sort)

        save_to_file(no_extension, get_results_dir() / 'task1_files_no_extension.txt')
        save_to_file(with_extension, get_results_dir() / 'task1_files_with_extension.txt')


def save_to_file(iter_data, file_path):
    try:
        with open(file_path, 'w') as fw:
            for data_item in iter_data:
                fw.write(data_item)
                fw.write('\n')
    except OSError as err:
        stderr.write(f"ERROR while writing to file {file_path.name}:\n{err}")



#
# Task 2
#
# The file cities_and_times.txt contains city names and time data.
# More precisely, each line contains the name of the city, followed by
# abbreviated weekday (e.g. "Sun"), and the time in the form hh:mm.
# Read in the file and create an alphabetically ordered list of the form:
# [('Amsterdam', 'Sun', datetime.time(8, 52)),
# ('Anchorage', 'Sat', datetime.time(23, 52)), ...].
# Note that the hour and minute data are used to create an object of
# the type datetime.time.
# Having created this list,
# - serialise it in a file, as a list object (using the pickle module)
# - write its content into a csv file, in the format:
#   city_name; weekday; time
#   where time is represented in the format '$H:%M:%S'
# Include appropriate try except blocks to prevent program from crushing
# in the case of a non existing file, or a problem while reading from /
# writing to a file, or transforming data values.
#
# Note: for a list of things that can be pickled, see this page:
# https://docs.python.org/3/library/pickle.html#pickle-picklable

from datetime import time

def read_write_cities_data(data_src):

    def csv_write():
        try:
            with open(get_results_dir() / 'task2_cities_data.csv', 'w') as fcsv:
                csv_writer = csv.writer(fcsv, delimiter=';')
                csv_writer.writerow(('city_name', 'weekday', 'time'))
                for city, wday, dt_time in cities_data:
                    time_str = time.strftime(dt_time, '%H:%M:%S')
                    csv_writer.writerow((city, wday, time_str))
        except csv.Error as err:
            stderr.write(f"ERROR while writing to csv file: {err}")


    cities_data = []

    try:
        with open(data_src, 'r') as rf:
            lines = rf.readlines()
            # print(lines[:10])
            for line in lines:
                city, weekday, time_data = line.rstrip().rsplit(maxsplit=2)
                hour, min = time_data.split(':')
                try:
                    dt_time = time(int(hour), int(min))
                    cities_data.append((city, weekday, dt_time))
                except ValueError as val_err:
                    stderr.write(f"ERROR: {val_err}")

    except FileNotFoundError:
        stderr.write(f"ERROR: file {data_src} does not exist!")
    except OSError as err:
        stderr.write(f"ERROR: {err}")

    else:
        cities_data.sort()
        serialise_to_file(cities_data, get_results_dir() / "task2_cities_data.pkl")
        csv_write()



def serialise_to_file(data, file_path):
    try:
        with open(file_path, 'wb') as fw:
            pickle.dump(data, fw)
    except pickle.PicklingError as err:
        stderr.write(f"ERROR when serializing the data: {err}")
    except OSError as err:
        stderr.write(f"ERROR while writing to the file {file_path}:\n{err}")


#
# Task 3
#
# You are given a text file that lists full file paths for a bunch of images
# (one image file path per line). Write a function that reads in the content
# of this text file and does the following:
# - counts the number of images in each category, and stores the computed
#   counts in a csv file in the format: category_name, image_count
# - creates and stores (in a file) a dictionary with the image category as
#   the key and a list of image names in the corresponding category as value;
#   for storage use 1) pickle and 2) shelve.
#
#
# Note: for a nice quick introduction to the shelve module, see: https://pymotw.com/3/shelve/

from collections import defaultdict, Counter
import shelve

def process_image_files(data_src):

    def write_to_csv():
        try:
            with open(get_results_dir() / 'task3_category_counts.csv', 'w') as fcsv:
                csv_writer = csv.writer(fcsv)
                csv_writer.writerow(('category', 'freq'))
                for item in cat_counts.items():
                    csv_writer.writerow(item)
        except csv.Error as err:
            stderr.write(f"ERROR while writing to csv file:\n{err}")

    def add_to_shelve():
        try:
            # Note: shelve.open function does not support pathlib.Path, so, we have to
            # transform the Path object to its string representation
            with shelve.open(str(get_results_dir() / 'task3_img_shelve'), 'c') as fs:
                for cat, img_list in img_dict.items():
                    fs[cat] = img_list
        except Exception as err:
            stderr.write(f"ERROR when writing to shelve:\n{err}")


    categories = []
    img_dict = defaultdict(list)

    try:
        with open(data_src, 'r') as fr:
            lines = [line.rstrip() for line in fr.readlines()]
            # print(lines[:10])
            for line in lines:
                try:
                    sth, category, img_file = line.rsplit('/', maxsplit=2)
                    categories.append(category)
                    img_dict[category].append(img_file)
                except ValueError as val_err:
                    stderr.write(f"ERROR: {val_err}")
    except FileNotFoundError:
        stderr.write(f"ERROR: file '{data_src}' does not exist")
    except OSError as err:
        stderr.write(f"ERROR: {err}")

    else:
        cat_counts = Counter(categories)
        write_to_csv()

        serialise_to_file(img_dict, get_results_dir() / 'task3_image_dictionary.pkl')
        add_to_shelve()



#
# Task 4
#
# Write a function that receives two text files with lists of numbers (integers) in
# them (one number per line). The function identifies the numbers present in both
# lists and writes them down in a new file (as a list of numbers).
# Note: it may happen that not all lines in the input files contain numbers, so,
# after reading in the content of the files, assure that only numerical values are
# considered for comparison.
#
# Note: based on this exercise:
# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html


def read_numbers_from_file(data_src):
    numbers = []
    try:
        with open(data_src, 'r') as fr:
            for line in fr.readlines():
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    stderr.write(f"Not a Number (NaN) detected: '{line.strip()}'; skipping it\n")
    except FileNotFoundError:
        stderr.write(f"ERROR: file '{data_src}' does not exist\n")
    except OSError as err:
        stderr.write(f"ERROR: {err}\n")
    finally:
        return numbers


def write_numbers_in_common(data_src_1, data_src_2):

    numbers_1 = read_numbers_from_file(data_src_1)
    numbers_2 = read_numbers_from_file(data_src_2)

    numbers_in_common = [num for num in numbers_1 if num in numbers_2]
    serialise_to_file(numbers_in_common, get_results_dir() / 'task4_numbers_in_common.pkl')




if __name__ == "__main__":

    read_sort_write(get_data_dir() / 'sample_file_name.txt')

    # read_write_cities_data(get_data_dir() / "cities_and_times.txt")

    # with open(get_results_dir() / 'task2_cities_data.pkl', 'rb') as fpkl:
    #     data = pickle.load(fpkl)
    #     print(data)

    # process_image_files(get_data_dir() / "image_files_for_training.txt")

    # # Note: shelve.open function does not support pathlib.Path, so, we have to
    # # transform the Path object to its string representation
    # with shelve.open(str(get_results_dir() / 'task3_img_shelve'), 'r') as sf:
    #     for cat, img_list in sf.items():
    #         print(f"{cat}: " + ",".join(img_list))


    # t4_f1 = get_data_dir() / "primenumbers.txt"
    # t4_f2 = get_data_dir() / "happynumbers.txt"
    # write_numbers_in_common(t4_f1, t4_f2)

    # with open(get_results_dir() / "task4_numbers_in_common.pkl", "rb") as bf:
    #     results = pickle.load(bf)
    #     print(results)