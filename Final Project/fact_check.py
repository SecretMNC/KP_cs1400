import csv
import sys
import itertools

def main():
    '''Opens two CSV files: first is a user-specified CSV file which expects
    data from the Bureau of Labor Statistics, second is data on which political
    party occupied the White House that month (or the majority of that month).
    Data is taken from both CSV files and organized into initialized
    dictionaries for later calculations.

    Job growth by party is calculated by calling the below functions.
    These calculations are placed into variables and printed into
    informative data for the end-user.'''

    while True:
        try:
            user_data = sys.argv[1]
            print("Running script.\n")
            break
        except IndexError:
            sys.exit('''Please include a CSV file with labor data such as
<BLS_private.csv> that contains expected formatting.''')

    jobs_data = {}
    party_data = {}

    try:
        with open(user_data, newline='') as jobscsv:
            raw_data = csv.reader(jobscsv, skipinitialspace=True)
            for ele in range(6):
                next(raw_data)
            for row in raw_data:
                output = [int(ele) for ele in row]
                jobs_data[output[0]] = output[1:]
    except FileNotFoundError:
        sys.exit('''The specified file was not found.
Double check the spelling of the file's name and try again.''')
    except ValueError:
        sys.exit('''
An error occurred while reading the specified CSV jobs data file.
The specified jobs CSV file has an unexpected format.
Make sure the file follows the format used by bls.gov's exported data.''')

    with open('presidents.csv', newline='') as pres_csv:
        presidents = csv.reader(pres_csv)
        next(presidents)
        for row in presidents:
            party_data[int(row[0])] = row[1:]

    t_jobs = job_figures(jobs_data)
    d_jobs, r_jobs = party_jobs_growth(jobs_data, party_data)
    d_growth, r_growth, total_growth = growth_by_party(d_jobs, r_jobs, t_jobs)

    print(f'''
    Democrats job growth total: {(d_growth * 1000):,d}
    Clinton's Democratic Party job growth claim: {42000000:,d}\n
    Republicans job growth total: {(r_growth * 1000):,d}
    Clinton's Republican Party job growth claim: {24000000:,d}\n
    Total job growth: {((total_growth) * 1000):,d}
    Clinton's total job growth claim: {66000000:,d}\n
    For further analysis, refer to the conclusions.md file.''')

def job_figures(jobs_dict):
    '''Returns a 1-D list of all monthly jobs figures
    from Jan. 1961 to Oct. 2012 in chronological order.'''

    jobs = [list(jobs_dict[key]) for key in jobs_dict]
    return list(itertools.chain.from_iterable(jobs))

def party_jobs_growth(jobs_data, party_data):
    '''Returns jobs figures attributed to each political party,
    organized by consecutive party occupancy of the White House.
    If party occupancy of the White House changes, the outgoing party is
    given credit for that month's jobs figure and also passes that figure
    to the incoming party's jobs data for later growth calculation.'''

    d_jobs = [[]]
    r_jobs = [[]]

    counter = 0
    for year, jobs in jobs_data.items():
        if len(set(party_data[year])) == 2 and party_data[year][0] == 'R':
            if counter >= 1: #Accounts for edge case with D.D.E.'s final month
                r_jobs[len(r_jobs) - 1].append(jobs[0])
                r_jobs += [[]]
            counter += 1
            d_jobs[len(d_jobs) - 1] += list(jobs)
        elif len(set(party_data[year])) == 2 and party_data[year][0] == 'D':
            d_jobs[len(d_jobs) - 1].append(jobs[0])
            d_jobs += [[]]
            r_jobs[len(r_jobs) - 1] += list(jobs)
        elif len(set(party_data[year])) == 1 and party_data[year][0] == 'R':
            r_jobs[len(r_jobs) - 1] += list(jobs)
        else:
            d_jobs[len(d_jobs) - 1] += list(jobs)
    return d_jobs, r_jobs

def growth_by_party(d_jobs, r_jobs, t_jobs):
    '''Returns the total job growth figure by party and total combined.
    Each instance of consecutive party control of the White House is
    calculated as its own figure at first and then each of these figures
    are summed together for that party's total job growth.'''

    d_list = []
    r_list = []

    for lst in d_jobs:
        d_list += [recursive_difference(lst)]
    d_job_growth = sum(d_list)

    for lst in r_jobs:
        r_list += [recursive_difference(lst)]
    r_job_growth = sum(r_list)

    total_job_growth = recursive_difference(t_jobs)
    return d_job_growth, r_job_growth, total_job_growth

def recursive_difference(lst):
    '''Take a list of numbers, subtract the 2nd number with the 1st,
    repeat this until the final 2 remaining numbers are subtracted.
    Return total difference.'''

    if len(lst) <= 1: #Makes function error-resistant to single/empty lists
        return 0
    elif len(lst) == 2:
        return lst[1] - lst[0]
    else:
        return lst[1] - lst[0] + recursive_difference(lst[1:])

if __name__ == '__main__':
    main()
