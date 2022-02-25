#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Challenge JSON - Converting JSON from a file type to pythonic data types.
                    
                    The file we will be reading from is ~/mycode/spacex.json
                    
                    Python has differences from JSON, those are best reviewed using
                    the following link:
                    https://docs.python.org/3/library/json.html#json-to-py-table"""
                    
# standard library
import os 
import json   # string data into json

def main():
    """run time code"""

    # from now on all commands are relative to this location
    #os.chdir("/home/student/")

    # open the file ~/spacex.json
    with open("spacex.json", "r") as of:
        # space_data is python data types returned by our conversion tool json.load()
        space_data = json.load(of)

    # test to ensure I can now work with the data in Python
    print(space_data)            # we should now see the data from the file
    print(type(space_data))      # the data type should be 'dict' NOT 'str'
    print(space_data.get('id'))  # perform a test lookup on a 'dict' data type


    # the file of was automatically closed when we
    # stopped indenting under the 'with' statement

# best practice to call main()
if __name__ == "__main__":
    main()

