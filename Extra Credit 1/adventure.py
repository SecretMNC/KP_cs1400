import random

def press_enter(a = 0):
    if a == 1:
        input("Press enter to continue...") 
    else:
        input("...")

name = input("What is your character's name?\n")

health = 1
strength = 1
luck = 1
free_stat_points = 10

stat_dict = {'Health': health, 'Strength': strength, 'Luck': luck}

def reset_stats():
    global health
    global strength
    global luck
    global free_stat_points
    health = 1
    strength = 1
    luck = 1
    free_stat_points = 10


'''
print("""Your character get 10 stat points.
You get to choose where those stats go
between 3 different skills: ...
""")

press_enter(1)

print("Health,") 
press_enter()
print("Strength,")
press_enter()
print("and Luck.")
press_enter()
'''
def stat_assignment(stat_name, stat):
    print(f"{stat_name} is currently {stat}")
    stat = int(input(f"""
You have {free_stat_points} points left
How many points do you wish to put into {stat_name}?
Enter any number between 0 and {free_stat_points}\n"""))
    return stat

def confirm_choice():
    check_for_yes = ('Yes', 'yes', 'YES')
    check_for_no = ('No', 'no', 'NO')
    while True:
        ans = input("""
    You have unspent stat points.
    Are you SURE you want to proceed?
    You will lose any unspent points.\n""")   
        if ans in check_for_yes:
            return 1
        if ans in check_for_no:
            return 0
        else:
            print("Please enter 'yes' or 'no'")
        
while 10 >= free_stat_points > 0:
    if free_stat_points == 10:  
        for key, value in stat_dict.items():
            stat_dict[key] = stat_assignment(key, value)
            free_stat_points -= stat_dict[key]
    elif 10 < free_stat_points < 0:
        print("You cheated!")
        quit()
    if 10 > free_stat_points > 0:
        confirm = confirm_choice()
        print(f"confirm = {confirm}")
        if confirm == 1:
            break
        elif confirm == 0:
            reset_stats()
            continue

            
        
    
print(free_stat_points)
print(stat_dict)
