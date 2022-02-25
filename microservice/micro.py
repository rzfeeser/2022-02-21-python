#!/usr/bin/python3

import time

# this is dependency:
# python3 -m pip install requests
import requests

def main():

    while True:
        resp = requests.get('https://api.magicthegathering.io/v1/cards')

        print(resp.json())

        time.sleep(10)

        print('time to run again!\n\n')

        time.sleep(1)

if __name__ == "__main__":
    main()
