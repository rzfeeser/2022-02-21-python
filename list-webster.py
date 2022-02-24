#!/usr/bin/python3

my_list = ['Mike Tyson  44','Floyd Mayweather  27']

# how can you convert it to a dictionary
# {'Mike Tyson': '44',' Floyed Mayweather:' '27'}

hall_of_records= {} # init a dictionary we can fill up with info

for fighter in my_list:
    print(fighter) # what did we just do?
    
    print(fighter.split("  ")) # take the STR and SPLIT across double-whitespace
    #["fighter", "kos"]

    # single line approach
    #hall_of_records[fighter.split('  ')[0]] = fighter.split('  ')[1]
    
    # two line approach
    results = fighter.split('  ')
    hall_of_records[results[0]] = results[1]

print(hall_of_records)
