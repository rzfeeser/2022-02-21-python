#!/usr/bin/python3
'''RZFeeser | Alta3 Research
   Thursday Morning Review - A dive into things we know how to do already,
   but might not realize we actually know how to do...'''

# dictionary
ROOMS = {'Hall': {'south': 'Kitchen', 'west': 'Study'}, 'Kitchen': {'north':'Hall'}, 'Study': {'east': 'Hall'}}

# define some functions
def move_check(move, currentRoom):
    # determine if the player can move in that direction
    if move in ROOMS[currentRoom]:
        currentRoom = ROOMS[currentRoom][move]
        print(f'You move into the {currentRoom}')
    else:
        print("You can't go that way!")
    # return the value of currentRoom
    return currentRoom

def main():
    '''run-time'''

    # variable - mapped to a string
    currentRoom = 'Hall'

    # start and infinite loop
    while True: 
        
        # start by showing the player status
        print(f'You are in the {currentRoom}')  # this is an 'f-string' which is a kind of template (fill in the {var})

        # ask the user what direction they want to move in
        # input question     # input("What direction do you want to move? ")
        # if they just hit ENTER (no input) they should STILL be asked where to move
        move = ''
        while move == '':
            move = input("What direction would you like to travel? ").lower()

        # did they quit?
        if move == 'quit':
            break

        # determine if the player can move in a direction
        currentRoom = move_check(move, currentRoom)

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
