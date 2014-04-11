__author__ = 'nick'

import requests
import json
import logging as log

states = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

city_county_links_for_state_of = 'http://api.sba.gov/geodata/city_county_links_for_state_of/%s.json'


def get_data_for_state(state):
    """
        Download data for state and parse JSON into Python dict
    """
    # Substitute state in URL
    url = city_county_links_for_state_of % state
    # Request JSON data
    r = requests.get(url)
    # check that we got a successful result
    if r.status_code == 200:
        try:
            # convert the output into a python object
            return json.loads(r.text)
        except:
            log.exception('Failed to load JSON for %s' % state)
    else:
        err = 'Status: %s for State: %s' % (r.status_code, state)
        raise Exception(err)


def process_states(fp):
    """
        Save state data to file
    """
    fp.write('[\n')
    # Iterate over list of states
    wrote_one = False
    for state in states:
        try:
            # only write out the comma starting with the second record
            # as a way to prevent having a trailing comma in JSON output
            if wrote_one:
                fp.write(',\n')
            state_info = dict()
            state_info['state'] = state
            state_info['geodata'] = get_data_for_state(state)
            # pretty print the dictionary in JSON format
            fp.write(json.dumps(state_info, sort_keys=True, indent=4, separators=(',', ': ')))
            wrote_one = True
        except:
            log.exception('Exception calling get_data_for_state()')
    fp.write('\n]\n')

if __name__ == "__main__":
    # set the logging level
    log.basicConfig(level=log.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
    try:
        # open a file to write
        with open('state_data.json', 'w') as fp:
            process_states(fp)
    except:
        log.exception('Exception call process_states()')