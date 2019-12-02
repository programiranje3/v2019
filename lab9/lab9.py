# This task is partially based on an example from the
# "Practical Introduction to Web Scraping in Python" tutorial,
# available at:
# https://realpython.com/python-web-scraping-practical-introduction/

# The task is to write a Python program (script) that determines which nations
# gave the largest number of mathematicians who are considered to be among
# the 100 greatest mathematicians of the past.
# To that end, the program should do the following:
# - collect names of the hundred greatest mathematicians of the past from:
#   http://www.fabpedigree.com/james/greatmm.htm
# - for each mathematician, determine his national origins by scraping the relevant
#   data (nationality or birthplace) from his Wikipedia page
# - stores the data about mathematicians and their national origins in a json file
# - prints a sorted list of identified nations and for each nation, the number
#   of greatest mathematicians it gave

import json


def get_content_from_url(url):
    '''
        Returns the content of the web page with the given URL or None
        if the page content cannot be retrieved
    '''

    pass



def get_mathematicians_names(url):
    '''
        Retrieves the web page with a list of well known mathematicians
        and returns a list of the mathematicians' names
    '''

    pass



def clean_names(names):
    """
        The function is intended for dealing with the diversity of name formats
        (e.g. Hermann G. Grassmann, Hermann K. H. Weyl, M. E. Camille Jordan),
        that is, name formats that cannot be directly used for collecting the
        data from Wikipedia. The names are 'cleaned' so that they consists of
        name and surname only. Name and surname are connected by an underscore.
    """
    pass



def retrieve_nationality(name):
    '''
        Receives the full name of a mathematician.
        Returns the nationality / nationalities of the mathematician extracted from his
        Wikipedia page (or None if the information is not available).
        If the information about nationality is not direectly available, try pulling it
        from the place of birth (if available)
    '''

    pass




def collect_mathematicians_data():
    '''
        The function puts several parts together:
        - obtains a list of mathematicians' names
        - cleans the names so that they can be used for locating
        relevant Wikipedia pages
        - iterates over the list of (cleaned) names to retrieve the nationality
        for each mathematician by 'consulting' his Wikipedia page
        - stores the collected data in a json file
        - prints names of mathematicians whose nationality data could not have
        been collected
    '''

    print("Putting together a list of mathematicians' names...")
    mathematicians_url = 'http://www.fabpedigree.com/james/greatmm.htm'
    mathematicians_names = get_mathematicians_names(mathematicians_url)
    print('...done')
    print(f'Gathered names for {len(mathematicians_names)} mathematicians.')

    names_cleaned = clean_names(mathematicians_names)

    print("Collecting data about the mathematicians' national origines...")
    maths_dict = dict()
    not_found = list()
    for name in names_cleaned:
        nationality = retrieve_nationality(name)
        if nationality:
            maths_dict[name] = nationality
        else:
            not_found.append(name)
    print('...done')

    with open("mathematicians.json", "w") as jsonf:
        json.dump(maths_dict, jsonf, indent=4)

    print(f"Information about national origin was not found for the following {len(not_found)} mathematicians:")
    print(", ".join(not_found))



def create_nation_country_mapping():
    '''
        Creates a mapping between a national origin and different ways it was referred to
        in the collected data.
        :returns a dictionary with nationalities as the keys and the different terms used
        to refer to them as values
    '''
    nation_terms_dict = dict()

    nation_terms_dict['French'] = ['France', 'French']
    nation_terms_dict['German'] = ['German', 'German Confederation', 'German Empire', 'Canton of Bern']
    nation_terms_dict['Polish'] = ['Polish', 'Poland']
    nation_terms_dict['British'] = ['English', 'British', 'United Kingdom', 'London United Kingdom']
    nation_terms_dict['Swiss'] = ['Swiss', 'Switzerland']
    nation_terms_dict['Russian'] = ['Russian', 'Russian Empire']
    nation_terms_dict['Indian'] = ['Indian', 'India', 'Patna India', 'British India']

    return nation_terms_dict


def most_represented_nations():
    '''
        Creates and prints a list of nations based on how well they
        are represented in the collected mathematicians data.
        Note: in cases where multiple nationalities are mentioned,
        take the first nationality as the 'original' one
    '''

    with open("mathematicians.json", 'r') as fjson:
        mathematicians = json.load(fjson)

    # keep the first nationality as the origin


    # map the different ways of referring to the same origin
    # to a common name


    # count the mathematicians for each identified national origin


    # print the number of mathematicians per country of origin
    print("\n\nNumber of world renowned mathematicians per country of origin:")




if __name__ == '__main__':

    pass
    
    # collect_mathematicians_data()
    # most_represented_nations()

