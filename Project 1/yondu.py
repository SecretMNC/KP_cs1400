total_pirates = int(input("How many pirates: \n"))
total_units = float(input("How many units: \n"))

# Remove 3 units for each pirate except Yondu & Peter
crew_deduction = round(3 * (total_pirates - 2), 2)

'''
1. Get Yondu's secret share from remainder
2. Get Peter's secret share from remainder after Yondu
3. Calculate remaining amount per pirate
'''
yondu_secret = round((total_units - crew_deduction) * 0.13, 2)
peter_secret = round((total_units - (crew_deduction + yondu_secret)) * 0.11, 2)
units_per_pirate = round(((total_units - crew_deduction) - (yondu_secret + peter_secret)) / total_pirates, 2)

'''
1. Calculate Yondu's true share (secret + crew share)
2. Calculate Peter's true share (secret + crew share)
3. Calculate amount given per pirate plus the 3 units per pirate
    Note: Yondu's and Peter's portion of final_crew_share doesn't include 3 units since they didn't get that
'''
yondu_share = round(yondu_secret + units_per_pirate, 2)
peter_share = round(peter_secret + units_per_pirate, 2)
final_crew_share = round(units_per_pirate + (3 * (total_pirates - 2) / (total_pirates - 2)), 2)

print(f"""\nYondu's share: {yondu_share : .2f}
Peter's share: {peter_share : .2f}
Crew's share: {final_crew_share : .2f}""")

'''
# TEST CODE
print(final_crew_share * total_pirates)
test_total = (yondu_share + peter_share + (final_crew_share * (total_pirates - 2)))

print(f"Does {yondu_share} + {peter_share} + ({final_crew_share} * pirates) (or {test_total})= {total_units}?")
'''
