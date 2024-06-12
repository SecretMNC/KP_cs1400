
'''
Project: Random walk
Author: Kevin Pett
Date: June , 2024

'''
import matplotlib.pyplot as plt
import random as r
###### DO NOT change this function #####
# Function to plot the random walk for each animal
def plot_walk(animal):
    xs, ys = zip(*animal['positions'])

    plt.figure(figsize=(10,10))
    plt.scatter(xs, ys, color=animal['color'], edgecolor='k', alpha=0.7, s=100, marker=animal['marker'])
    plt.plot(xs, ys, lw=1.5, ls='--', color=animal['color'])
    plt.grid(True)
    plt.title(f'Path of Random Walk for {animal["name"]}')
    plt.xlabel('East-West')
    plt.ylabel('North-South')
    
    # Save the plot to a file
    plt.savefig(f'{animal["name"]}_random_walk.png', dpi=300)
    plt.close()  # Close the figure

# You need to create the animal dictionary inside the main function where each animal has
# direction, probabilities, positions, marker and color attributes

def main():
    
    animal = {'Chicken': 'Chuck',
              'Dog': 'Daisy',
              'Cat': 'Chester'}
    
    def chicken_step():
        chick_cors = [[0], [0]]
        for step in range(1, 1001):
            direction = r.getrandbits(2)
            if direction == 0:
                chick_cors[0].append((chick_cors[0][step - 1]) - 1)
                chick_cors[1].append((chick_cors[1][step - 1]))
            elif direction == 1:
                chick_cors[0].append((chick_cors[0][step - 1]) + 1)
                chick_cors[1].append((chick_cors[1][step - 1]))
            elif direction == 2:
                chick_cors[0].append((chick_cors[0][step - 1]))
                chick_cors[1].append((chick_cors[1][step - 1]) - 1)
            elif direction == 3:
                chick_cors[0].append((chick_cors[0][step - 1]))
                chick_cors[1].append((chick_cors[1][step - 1]) + 1)
        return chick_cors
    
    def dog_step():
        dog_cors = [[0], [0]]
        for step in range(1, 1001):
            direction = r.getrandbits(2)
            if direction == 0:
                chick_cors[0].append((chick_cors[0][step - 1]) - 1)
                chick_cors[1].append((chick_cors[1][step - 1]))
            elif direction == 1:
                chick_cors[0].append((chick_cors[0][step - 1]) + 1)
                chick_cors[1].append((chick_cors[1][step - 1]))
            elif direction == 2:
                chick_cors[0].append((chick_cors[0][step - 1]))
                chick_cors[1].append((chick_cors[1][step - 1]) - 1)
            elif direction == 3:
                chick_cors[0].append((chick_cors[0][step - 1]))
                chick_cors[1].append((chick_cors[1][step - 1]) + 1)            
        return dog_cors
    
    def cat_step():
        cat_xcor = [0]
        for step in range(1, 1001):
            cat_x.append((cat_xcor[step - 1]) + r.choice(-1, 1))
        return cat_xcor
    
    plt.plot([1, 2, -3, 4], [5, 10, 20, 40], '-ro')
    plt.ylabel('some numbers')
    plt.show()
    

if __name__ == '__main__':
    main()