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
import requests
from contextlib import closing
from sys import stderr
from bs4 import BeautifulSoup
from collections import defaultdict

def get_content_from_url(url):
    '''
        Returns the content of the web page with the given URL or None
        if the page content cannot be retrieved
    '''

    def response_OK():
        content_type = response.headers['Content-Type']
        return response.status_code == 200 and content_type and ('html' in content_type.lower())

    try:
        with closing(requests.get(url)) as response:
            return response.text if response_OK() else None
    except requests.RequestException as err:
        stderr.write(f"ERROR when requesting Web page: {url}:\n{err}")
        return None


def get_mathematicians_names(url):
    '''
        Retrieves the web page with a list of well known mathematicians
        and returns a list of the mathematicians' names
    '''

    def get_a_tag_content(parent_tag):
        a_tag = parent_tag.find(name='a')
        if a_tag.string:
            return a_tag.string.strip()
        elif a_tag.strings:
            return " ".join(s for s in a_tag.stripped_strings)
        return ""

    names = []

    page = get_content_from_url(url)
    if page is None:
        stderr.write("ERROR: not able to retrieve the page with mathematicians' names\n")
        return names

    page_content = BeautifulSoup(page, features='html.parser')
    if page_content is None:
        stderr.write("ERROR: not able to parse the page with mathematicians' names\n")
        return names

    ol_tags = page_content.find_all(name='ol')
    for ol_tag in ol_tags:
        li_tags = ol_tag.find_all(name='li')
        for li_tag in li_tags:
            if li_tag.children:
                name = " ".join(li_child.string.strip() for li_child in li_tag.children if li_child.string)
                if name == " ":
                    name = get_a_tag_content(li_tag)
                if name != "":
                    names.append(name)

    return names


def clean_names(names):  ## UPDATE for class: 2nd condition for keeping a name_part: or len(name_part) > 2)
    """
        The function is intended for dealing with the diversity of name formats
        (e.g. Hermann G. Grassmann, Hermann K. H. Weyl, M. E. Camille Jordan),
        that is, name formats that cannot be directly used for collecting the
        data from Wikipedia. The names are 'cleaned' so that they consists of
        name and surname only. Name and surname are connected by an underscore.
    """
    cleaned_names = []
    for name in names:
        name_parts = [name_part for name_part in name.split() if (not name_part.endswith('.') or len(name_part) > 2)]
        cleaned_name = "_".join([name_part.strip("`',") for name_part in name_parts])
        cleaned_names.append(cleaned_name)

    return cleaned_names


def is_disambigution_page(webpage):
    return webpage.find(name='table', id='disambigbox') is not None

def proper_nationality_string(string):
    return string.strip("[]() ,") and string.strip("[]() ,")[0].isupper()

def clean_nationality_str(string):
    if len(string.split()) > 1:
        return " ".join([s.strip('()') for s in string.split() if s.strip('()') and s.strip('()')[0].isupper()])
    else:
        return string.strip(" ,")

def retrieve_nationality(name):
    '''
        Receives the full name of a mathematician.
        Returns the nationality / nationalities of the mathematician extracted from his
        Wikipedia page (or None if the information is not available).
        If the information about nationality is not direectly available, try pulling it
        from the place of birth (if available)
    '''

    wikipedia_url = f"https://en.wikipedia.org/wiki/{name}"
    wikipedia_page = get_content_from_url(wikipedia_url)
    if wikipedia_page is None:
        stderr.write(f"ERROR: Could not retrieve Wikipedia page for {name}\n")
        return None

    wikipedia_page = BeautifulSoup(wikipedia_page, features='html.parser')
    if wikipedia_page is None:
        stderr.write(f"ERROR: Could not parse Wikipedia page for {name}\n")
        return None

    infobox = wikipedia_page.find(name='table', class_='infobox biography vcard')
    if infobox is None:
        if is_disambigution_page(wikipedia_page):
            stderr.write(f"ERROR: reached the disambiguation page for name '{name}'\n")
        else:
            stderr.write(f"ERROR: No infobox data for the Wikipedia page of {name}\n")
        return None

    th_nationality = infobox.find_next(name='th', string='Nationality')
    if th_nationality:
        td_nationality = th_nationality.find_next_sibling(name='td')
        if td_nationality.string:
            return td_nationality.string.strip()
        elif td_nationality.strings:
            return ",".join([clean_nationality_str(s) for s in td_nationality.stripped_strings if proper_nationality_string(s)])

    # if Nationality is not available...
    th_born = infobox.find_next(name='th', string='Born')
    if th_born:
        birthplace_div = th_born.find_next(name='div', class_='birthplace')
        if birthplace_div and birthplace_div.string:
            return birthplace_div.string.strip()
        elif birthplace_div and birthplace_div.strings:
            origin = [clean_nationality_str(bp) for bp in birthplace_div.stripped_strings if proper_nationality_string(bp)][-1]
            if len(origin.split(',')) > 1:
                origin = (origin.split(',')[-1]).strip()
            return origin



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
    # for original, cleaned in dict(zip(mathematicians_names, names_cleaned)).items():
    #     print(f"{original} -> {cleaned}")

    print("Collecting data about the mathematicians' national origins...")
    maths_dict = dict()
    not_found = list()
    for name in names_cleaned:
        nationality = retrieve_nationality(name)
        if nationality:
            maths_dict[name] = nationality
        else:
            not_found.append(name)
    print('...done')

    for mathematician, origin in maths_dict.items():
        print(f"{mathematician}: {origin}")

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

    # read the mathematicians data from the json file
    with open("mathematicians.json") as fjson:
        mathematicians_data = json.load(fjson)

    # keep the first nationality as the origin
    for mathematician, origin in mathematicians_data.items():
        if len(origin.split(',')) > 1:
            mathematicians_data[mathematician] = origin.split(',')[0]

    # map the different ways of referring to the same origin
    # to a common name
    nation_country_map = create_nation_country_mapping()
    for mathematician, origin in mathematicians_data.items():
        for nation, countries in nation_country_map.items():
            if origin in countries:
                mathematicians_data[mathematician] = nation
                break

    # count the mathematicians for each identified national origin
    nation_counts = defaultdict(int)
    for origin in mathematicians_data.values():
        nation_counts[origin] += 1

    # print the number of mathematicians per country of origin
    # sort first by the number of mathematicians (desc), and then by the origin name (asc)
    print("\n\nNumber of world renowned mathematicians per country of origin:")
    for origin, count in sorted(sorted(nation_counts.items()), key=lambda item: item[1], reverse=True):
        print(f"\t-{origin}: {count}")




if __name__ == '__main__':

    collect_mathematicians_data()
    most_represented_nations()
