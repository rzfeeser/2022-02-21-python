#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   JSON API - Converting JSON from an API to pythonic data types using the Python standard library.
                    
                    The API we will be reading from is:
                    https://api.spacexdata.com/v3/dragons/{{id}}
                    
                    Documentation for the SpaceX API is available at:
                    https://docs.spacexdata.com/v3"""

# standard library
import os
import urllib.request     # used to make HTTP requests (GET, POST, PUT, DELETE, etc.)
import json

# this a GLOBAL CONSTANT (this is why it is all capitalized)
API = "https://api.spacexdata.com/v3/dragons/dragon1"

def main():
    """run time code"""

    # from now on all commands are relative to this location
    os.chdir("/home/student/mycode")

    # perform an HTTP GET request
    response = urllib.request.urlopen(API)   # response is an HTTP response object


    # strip JSON off of response
    data = response.read()   # read off all attached content
    encoding = response.info().get_content_charset('utf-8') # prep bytes decode
    space_data = json.loads(data.decode(encoding)) # decode data
    # Yes, that WAS a lot of work (3 lines and 2 libraries) to get our JSON
    # 3rd party libraries offer an EASIER way to do this

    # test to ensure I can now work with the data in Python
    print(space_data)              # we should now see the data from the file
    print(type(space_data))        # the data type should be 'dict' NOT 'str'
    print(space_data.get('id'))    # perform a test lookup on a 'dict' data type

# best practice to call main()
if __name__ == "__main__":
    main()

