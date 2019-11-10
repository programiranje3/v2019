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

# Use the file 'sample_file_names.txt'






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







if __name__ == "__main__":

	pass

    # read_sort_write("data/sample_file_name.txt")

    # read_write_cities_data("data/cities_and_times.txt")

    # with open('results/task2_cities_data.pkl', 'rb') as fpkl:
    #     data = pickle.load(fpkl)
    #     print(data)

    # process_image_files("data/image_files_for_training.txt")

    # with shelve.open('results/task3_img_shelve', 'r') as sf:
    #     for cat, img_list in sf.items():
    #         print(f"{cat}: " + ",".join(img_list))

    # t4_f1 = "data/primenumbers.txt"
    # t4_f2 = "data/happynumbers.txt"
    # write_numbers_in_common(t4_f1, t4_f2)

    # with open("results/task4_numbers_in_common.pkl", "rb") as bf:
    #    results = pickle.load(bf)
    #    print(results)