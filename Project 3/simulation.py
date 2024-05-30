import os
import sys

def main():


    # Validating user input from terminal
    while True:
        try:
            if len(sys.argv) != 5:
                raise Exception(print("""
            Unexpected number of parameters given.
            Format: python3 [scriptfile.py initial_pop growth_rate iterations output_file]"""))
            elif ".py" not in sys.argv[0]:
                raise Exception(print("Please enter a valid .py file or check your path."))
            elif float(sys.argv[1]) < 0 or float(sys.argv[1]) > 1:
                raise Exception(print("Please enter an initial pop number between 0 and 1, inclusive."))
            elif float(sys.argv[2]) < 0 or float(sys.argv[2]) > 4:
                raise Exception(print("Please enter a growth rate number between 0 and 4, inclusive."))
            elif int(sys.argv[3]) < 0:
                raise Exception(print("Please enter in a whole number greater than 0 for # of iterations."))
            elif ".txt" not in sys.argv[4]:
                raise Exception(print("Please enter a valid .txt output file."))
            #else:
            # print(f"""
            #Running simulation with {sys.argv[3]} iterations.
            #Output will be placed in {sys.argv[4]}""")
            break
        except:
            print("Unexpected input. Please try again.")
            quit()
        
    # Assigning user's inputs to variables for readability
    initial_pop = float(sys.argv[1])
    growth_rate = float(sys.argv[2])
    iterations = int(sys.argv[3])
    output_file = sys.argv[4]

    # Making pop_update start at initial_pop so to not change original user input
    pop_update = initial_pop
    data_list = [[0, initial_pop]]

    # Logistic Equation
    def log_equation(pop):
        return growth_rate * pop * (1 - pop)

    # Simulation runs here
    for time in range(1, iterations + 1):       # Progressing through 'time' in the loop
        pop_update = log_equation(pop_update)   # Run calculation, update pop% variable
        data_list.append([time, 0])             # Add a new list element with current time, dummy 0
        data_list[time][1] = pop_update         # Replace dummy 0 with the updated pop%

    # Clear previous simulation data if using same file name
    open(f'{output_file}', 'w')

    # Create .txt file, write data to file, file auto closes
    with open(f'{output_file}', 'a') as file:
        for row in range(len(data_list)):
            file.writelines(f"{data_list[row][0]}\t{data_list[row][1]:.3f}\n")

    # print("Simulation complete! Check your file in the directory.")


if __name__ == "__main__":
    main()
