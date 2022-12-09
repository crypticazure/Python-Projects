"""Dungeons & Draggons, along with other tabletop RPGs, use dice that can have 2, 4, 6, 8, 10, 12, and 20 sides. These games also have a specific notation for indicating which dice to roll.
For example, 3d6 means to roll 3 six-sided dice, and 1d10+2 means to roll 1 ten-sided die and add 2 to the total.
This program simulates dice rolling, in case you forgot to bring your own. This can also simulate rolling dice that don't physically exist, like a 45-sided die."""

import random, sys

print("""Dice Roller

Enter what kind of die to roll, and how many. You can also add a plus or minus adjustment.
Example: 1d10 or 4d6+2
QUIT quits the program""")

while True: #Main program loop
    try:
        dice_str = input('> ') #the prompt to enter the dice string
        if dice_str.upper() == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        
        #Clean up the dice string
        dice_str.lower().replace(' ', '')

        #Find the d in the dice string input:
        d_index = dice_str.find('d')
        if d_index == -1:
            raise Exception("Missing the \"d\" character")

        #Get the number of dice, such as the 3 in "3d6+1"
        num_dice = dice_str[:d_index]
        if not num_dice.isdecimal():
            raise Exception("Missing the number of dice")
        num_dice = int(num_dice)

        #Find if there is a plus or minus sign for modifier
        mod_index = dice_str.find("+")
        if mod_index == -1:
            num_sides = dice_str[d_index + 1:]
        else:
            num_sides = dice_str[d_index + 1 : mod_index]
        if not num_sides.isdecimal():
            raise Exception("Missing the number ofsides")
        num_sides = int(num_sides)

        #Find the modifier amount (the 1 in "3d6+1")
        if mod_index == -1:
            mod_amount = 0
        else:
            mod_amount = int(dice_str[mod_index + 1:])
            if dice_str[mod_index] == '-':
                mod_amount = 0 - mod_amount #change the modification amount to negative
        
        #Simulate the dice rolls
        rolls = []
        for i in range(num_dice):
            roll_result = random.randint(1, num_sides)
            rolls.append(roll_result)
        
        #Display the total
        print("Total:" sum(rolls) + mod_amount, "(Each Die:", end='')

        #Display the individual rolls:
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        #Display the modifier amount:
        if mod_amount != 0:
            mod_sign = dice_str[mod_index]
            print(", {}{}".format(mod_sign, abs(mod_amount)), end="")
        print(')')
    
    except Exception as exc:
        #Catch any exceptions and display the message to the user:
        print("Invalid input. Enter something formatted similarly to the examples given")
        print("Input was invalid because: " + str(exc))
        continue #Go back to the dice string prompt
    