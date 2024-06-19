import csv
import sys


def main():

    jobs_data = {}
    pres_data = {}
    r_jobs = []
    d_jobs = []

    with open('BLS_private.csv', newline='') as jobscsv:
        raw_data = csv.reader(jobscsv, skipinitialspace=True)
        for iter in range(6):
            next(raw_data)
        for row in raw_data:
            output = [int(ele) for ele in row]
            jobs_data[output[0]] = output[1:]
            
    with open('presidents.csv', newline='') as pres_csv:
        presidents = csv.reader(pres_csv)
        next(presidents)
        for row in presidents:
            pres_data[int(row[0])] = row[1:]

    sort_job_nums(jobs_data, pres_data)

def sort_job_nums(jobs_dict, terms_dict):
    jobs = [[ele for ele in jobs_dict[key]] for key in jobs_dict]
    terms = [[ele for ele in terms_dict[key]] for key in terms_dict]
    d_jobs= []
    r_jobs= []
    for row in terms:
        row_index = 0
        print(row)
        for party in row:
            inner_index = row.index(party)
            print(row_index, inner_index, party)
            if party == 'D':
                d_jobs.append(jobs[row_index][inner_index])
            else:
                r_jobs.append(jobs[row_index][inner_index])
    #print(r_jobs, d_jobs)
    #return d_jobs, r_jobs

    '''for key, value in jobs_dict.items():
        for jobs in value:
            index = value.index(jobs)
            if terms_dict[key].values():'''
    


if __name__ == '__main__':
    main()
