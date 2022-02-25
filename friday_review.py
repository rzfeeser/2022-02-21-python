#!/usr/bin/python3
'''Alta3 Research | RZFeeser@alta3.com
   Review on Friday morning

   Making request to NASA APOD API service

   example:
   https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'''

# standard library
import sys

# to install requests, run...
# python3 -m pip install requests
import requests


def nasa_api_token():
    """look up token"""

    # read cred out of a file
    with open('/home/student/nasa.cred', 'r') as cred:
        nasa_api_token = cred.readline()

    # 'cleanup' the nasa_api_token
    nasa_api_token = nasa_api_token.rstrip('\n')

    # return the token (string)
    return nasa_api_token


def main():
    """run time code"""

    # call the function to return the string nasa_api_token
    nasa_api_token = nasa_api_token()

    # construct the API we wish to lookup
    api = f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_token}'

    # make a lookup to a NASA API
    resp = requests.get(api)

    # ensure HTTP response is valid
    if resp.status_code != 200:
        print(f"A non-200 status code was returned!\nStatus Code: {resp.status_code}")
        sys.exit() # exit the program because have a fault

    # retrieve json from HTTP response
    nasa_apod_data = resp.json()

    # print data to screen so humans can read it
    print(nasa_apod_data)

    print(nasa_apod_data.get("date"))
    print(nasa_apod_data.get("explanation"))
    print(nasa_apod_data.get("hdurl"))

if __name__ == "__main__":
    main()
