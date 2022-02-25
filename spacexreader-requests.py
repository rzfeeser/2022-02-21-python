#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Challenge JSON - Converting JSON from an API to pythonic data types.

                    The API we will be reading from is:
                    https://api.spacexdata.com/v3/dragons/{{id}}
                    Documentation for the SpaceX API is available at:
                    https://docs.spacexdata.com/v3"""

# standard library
import os

# 3rd party imports
# python3 -m pip install requests
import requests     # used to make HTTP requests (GET, POST, PUT, DELETE, etc.)

# this a GLOBAL CONSTANT (this is why it is all capitalized)
API = "https://api.spacexdata.com/v3/dragons/dragon1"

def main():
    """run time code"""

    # from now on all commands are relative to this location
    os.chdir("/home/student/mycode")

    # perform an HTTP GET request
    response = requests.get(API)   # response is an HTTP response object

    #print(response.status_code)   # returns the HTTP status code returned to us

    # strip JSON off of response
    space_data = response.json()   # all requests objects, have a .json() method
                                   # this strips JSON off the 200+JSON and converts it
                                   # to pythonic data types WITHOUT the need to
                                   # "import json" from the standard library

    # test to ensure I can now work with the data in Python
    print(space_data)              # we should now see the data from the file
    print(type(space_data))        # the data type should be 'dict' NOT 'str'
    print(space_data.get('id'))    # perform a test lookup on a 'dict' data type

# best practice to call main()
if __name__ == "__main__":
    main()

