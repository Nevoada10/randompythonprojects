#######################################################################################################################
# Nevoada
#######################################################################################################################
# Title: Model
# Author: Nevoada
# Date: 2023-05-23
# Description: A simple model in Python.

# ===================================================================================================================
# PSEUDOCODE:
# ===================================================================================================================

# =================================================================================================================
# IMPORTS
# =================================================================================================================

import sys
import random

# ===================================================================================================================
# DEFINING PHASE: CONSTANTS AND INITIAL VARIABLES
# ===================================================================================================================

s_var = 1


# ===================================================================================================================
# CLASSES
# ===================================================================================================================

class Human:  # Class
    def __init__(self, name, strength, dexterity, stamina, charisma, manipulation, composure, intelligence, willpower,
                 luck):
        self.name = name

        self.strength = strength
        self.dexterity = dexterity
        self.stamina = stamina * 20

        self.charisma = charisma
        self.manipulation = manipulation
        self.composure = composure

        self.intelligence = intelligence
        self.willpower = willpower

        self.luck = luck

    def grapple(self, target):

        attacker_dice_pool = self.strength + self.dexterity
        attacker_successes = 0

        defender_dice_pool = target.strength + target.dexterity
        defender_successes = 0

        # Counting attacker successes to grapple.
        for i in range(attacker_dice_pool):
            attacker_roll = random.randint(1, 10)
            if attacker_roll >= 5:
                attacker_successes += 1
            elif attacker_roll == 1:
                attacker_successes -= 1
            print(self.name, "Attacker roll:", attacker_roll)
        print(self.name, "Attacker successes:", attacker_successes)

        # Counting defender successes to evade.
        for i in range(defender_dice_pool):
            defender_roll = random.randint(1, 10)
            if defender_roll >= 5:
                defender_successes += 1
            elif defender_roll == 1:
                defender_successes -= 1
            print(target.name, "Defender roll:", defender_roll)
        print(target.name, "Defender successes:", defender_successes)

        if attacker_successes > defender_successes:
            print( "{} {} {}.".format(self.name, "grappled", target.name))
            # Apply grappled status function

        elif attacker_successes == defender_successes:  # If attacker and defender have same successes, they both evade.
            self.grapple(target)  # Recursion
        else:
            print( "{} {} {}.".format(target.name, "evaded", self.name))


# ===================================================================================================================
# FUNCTIONS
# ===================================================================================================================

def status_grappled(target):  # Function
    grappled = True


    return 0


# ===================================================================================================================
# MAIN
# ===================================================================================================================

def main():  # Main function
    # Summon characters
    player = Human("Player", 1, 1, 1, 1, 1, 1, 1, 1, 1)
    eudora = Human("Eudora", 2, 2, 1, 1, 1, 1, 1, 1, 1)
    eudora.grapple(player)
    return 0


if __name__ == "__main__":  # Check if it's main otherwise it won't run
    exit_code = main()  # Exit code means the program will exit with that code
    sys.exit(exit_code)  # Exit
