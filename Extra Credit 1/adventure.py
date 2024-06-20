import random
import ascii_art

def main():

    name = input("What is your character's name?\n")
    free_stat_points = 10
    player_stats = {
        'Health': 1,
        'Strength': 1,
        'Luck': 1
    }
    inventory = []
    state = 'start'

    print("""Your character gets 10 stat points.
You get to choose where those points go between 3 different skills:""")
    press_enter(1)
    print("Health,") 
    press_enter()
    print("Strength,")
    press_enter()
    print("and Luck. All three of which start at 1 point. Choose wisely!")
    press_enter(1)

    while 10 >= free_stat_points > 0:
        for key, value in player_stats.items():
            if 0 < free_stat_points <= 10:  
                player_stats[key] = 1 + stat_assignment(key, value, free_stat_points)
                free_stat_points -= player_stats[key] - 1
            '''elif free_stat_points > 0:
        confirm = confirm_choice()
        if confirm == 1:
            break
        elif confirm == 0:
            free_stat_points,
            player_stats['Health'],
            player_stats['Strength'],
            player_stats['Luck'] = reset_stats()
            continue'''

    #Decision 1
    while True:
        print('\nYou find yourself in an open meadow.')
        first_dec = input("""What would you like to do?
        Choices:
        directions
        act
        check stats\n\n""")
        if first_dec.lower() == 'directions':
            directions()
        elif first_dec.lower() == 'act':
            continue
        elif first_dec.lower() == 'look':
                print("There's a mountain to the north, a cottage the east, more plains to the west, and a cliff to the south.")
        elif first_dec.lower() == 'check stats':
            print("\nYou check your stats and continue to think about what to do next.")
            check_stats(player_stats)
            continue
        
        elif first_dec.lower() == 'north':
            state = 'traveler'
            decision_2(state, player_stats)
            break
        elif first_dec.lower() == 'east':
            decision_7(player_stats)
            break
        elif first_dec.lower() == 'west':
            state = 'curious'
            decision_6()
            break
        elif first_dec.lower() == 'south':
            if player_stats['Luck'] < 7:
                print('''\nYou underestimate how close the cliff was and slip and fall to your death.
Game over!''')
                break
            else:
                print('''\nBy sheer luck, you catch yourself from falling down the cliff!
You return to the meadow you originally found yourself.''')
                continue
        else:
            print(f"I don't know what {first_dec} means.")
            continue
        

def stat_assignment(stat_name, stat_point, spendable_points):
    print(f"\n{stat_name} is currently at {stat_point} points.")
    try:    
        add_points = int(input(
f"""You have {spendable_points} points left.
How many points do you wish to add to {stat_name}?
Enter any number between 0 and {spendable_points}\n"""))
    except ValueError:
        print(f'\nPlease enter a whole number between 0 and {spendable_points}.')
        stat_assignment(stat_name, stat_point, spendable_points)
    if 0 > add_points > spendable_points:
        print(f'''\nYou must pick a number between 0 and {spendable_points}!''')
        stat_assignment(stat_name, stat_point, spendable_points)
    else:
        return add_points

def confirm_choice():
    ans = input("""
You have unspent stat points.
Are you SURE you want to proceed? You will lose any unspent points.
Type 'yes' if you're sure or type 'no' if you want to restart point allocation.\n""")
    if ans.lower() == 'yes':
        return 1
    elif ans.lower() == 'no':
        return 0
    else:
        print("Please enter 'yes' or 'no'")

def reset_stats():
    return 10, 1, 1, 1


def press_enter(a = 0):
    if a == 1:
        input("Press enter to continue...") 
    else:
        input("...")


def decision_2(state, stats):
    if state:
        print('You get closer to the mountain but find a large frog!')
    first_dec = input("""What would you like to do?
    Choices:
    attack
    check stats""")
    frog = True
    if first_dec.lower() == 'attack' and stats['Strength'] >= 4:
        print("You successfully kill the legendary frog and return home a hero!")
        print("\nGame over.")
    elif first_dec.lower() == 'attack' and stats['Strength'] < 4:
        print("You attempt to kill the legendary frog but end up dying.")
        print("\nGame over!")
    else:
        print("The frog is still there and won't let you leave!")
        decision_2(state, stats)
    if first_dec.lower() == 'act':
        pass
    if first_dec.lower() == 'look' and frog:
        print("The frog notices you're distracted and attacks you!")
        stats['Health'] -= 1
        decision_2(frog, stats)
    elif first_dec.lower() == 'check stats':
        print("\nYou check your stats and continue to think about what to do next.")
        check_stats(stats)
        decision_2(state, stats)
    else:
        print(f"I don't know what {first_dec} means.")
        decision_2(state, stats)

def decision_3(state, inventory, stats):
    pass

def decision_4(state, inventory, stats):
    pass

def decision_5():
    print('You find the treasure in the mountain and you win!')

def decision_6():
    print("""\nYou wander the great plains of this world for the rest of your life.
\nGame over!""")

def decision_7(stats):
    print("You find your family's long lost sword stuck, stabbed into the ground in the middle of the cottage.")
    if stats['Strength'] >= 3:
        print("You're strong enough to successfully pull the sword out of the ground!")
        print("You return home to your family with honor. Game over.")
    else:
        print("You aren't strong enough to pull out the sword.")
        ask = input('Keep trying?')
        if ask.lower == 'yes':
            print("You try as hard as you can to pull out the sword, only to strain yourself enough to stumble backwards, hit your head and die.")
            print("\nGame over!")
        else:
            print("You decide to return home without the sword. Your family is disappointed in you.")
            print("Game over!")


def decision_8(state, inventory, stats):
    pass


def directions(go_ = 4):
    if go_ == 4:
        return input('You may go north, west, east, or south.\n')
    elif go_ == 3:
        return input('You may go north, west, or east.\n')
    elif go_ == 2:
        return input('You may go north or west.\n')
    else:
        return input('The only path you can take is north.\n')

def act(do_ = 1):
    if do_ == 1:
        return input('The only thing you can do is look around.\n')
    elif do_ == 2:
        return input ('You can look around or use an item.\n')
    elif do_ == 3:
        return input('You can look around or attack!\n')
    else:
        return input('You can look around, use an item, or attack!\n')

def check_stats(stats):
    return [print(f'\n{key}: {value}') for key, value in stats.items()]


if __name__ == '__main__':
    main()