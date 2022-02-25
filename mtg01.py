#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""

    # create resp, which is our request object
    resp = requests.get("https://api.magicthegathering.io/v1/sets")

    # display the methods available to our new object
    print( dir(resp) )

    print(resp.reason)
    print(resp.status_code)
    print(resp.url)

    print( resp.json().keys() )

    cardsets = resp.json().get("sets")

    for cardset in cardsets:  # loop across ALL of the sets of MTG cards (they are stored as dict objects)
        print(cardset)  # each dictionary represents a set of cards

    print(len(cardsets))

if __name__ == "__main__":
    main()

