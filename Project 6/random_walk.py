
'''
Project: Random walk
Author: Kevin Pett
Date: June 12, 2024

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
    
    def chicken_step():
        '''
        1: Initialize a positional list of tuples, containing 2 ints each
        2: For loop with 1000 iterations, starting at step 1
        3: Randomly set a variable between ints 0 and 4
        4: Grab the most recent coordinates from the latest tuple in chick_pos
        5: Depending on random result, one cor is either added or subtracted
        6: Return full list of tuples
        '''
        chick_pos = [(0, 0)]
        for step in range(1, 1001):
            direction = r.getrandbits(2)
            x_cor, y_cor = chick_pos[-1]
            if direction == 0:    # West
                chick_pos.append((x_cor - 1, y_cor))
            elif direction == 1:  # East
                chick_pos.append((x_cor + 1, y_cor))
            elif direction == 2:  # South
                chick_pos.append((x_cor, y_cor - 1))
            elif direction == 3:  # North
                chick_pos.append((x_cor, y_cor + 1))
        return chick_pos
    
    def dog_step():
        '''
        1: Initialize a positional list of tuples, containing 2 ints each
        2: For loop with 1000 iterations, starting at step 1
        3: Randomly set a variable between 4 directions, north 50% weighted
        4: Grab the most recent coordinates from the latest tuple in dog_pos
        5: Depending on random result, one cor is either added or subtracted
        6: Return full list of tuples
        '''
        dog_pos = [(0, 0)]
        directions = ['n', 'e', 's', 'w']
        for step in range(1, 1001):
            direction = r.choices(directions, weights = [3, 1, 1, 1])[0]
            x_cor, y_cor = dog_pos[-1]
            if direction == 'w':
                dog_pos.append((x_cor - 1, y_cor))
            elif direction == 'e':
                dog_pos.append((x_cor + 1, y_cor))
            elif direction == 's':
                dog_pos.append((x_cor, y_cor - 1))
            elif direction == 'n':
                dog_pos.append((x_cor, y_cor + 1))
        return dog_pos
    
    def cat_step():
        '''
        1: Initialize a positional list of tuples, containing 2 ints each
        2: For loop with 1000 iterations, starting at step 1
        3: Randomly decide to add or subtract the x_cor by one
        3.1: Y coordinate never changes from 0, just append 0 every time
        4: Return full list of tuples
        '''
        cat_pos = [(0, 0)]
        for step in range(1, 1001):
            x_cor = cat_pos[-1][0] + r.choice([-1, 1])
            cat_pos.append((x_cor, 0))
        return cat_pos
    
    chicken_pos = chicken_step()
    dog_pos = dog_step()
    cat_pos = cat_step()

    animal = {'Chicken': 
                {'name': 'Chuck',
                 'color': 'blue',
                 'marker': 'o',
                 'positions': chicken_pos},
              'Dog': 
                {'name': 'Daisy',
                 'color': 'red',
                 'marker': 's',
                 'positions': dog_pos},
              'Cat': 
                {'name': 'Chester',
                 'color': 'green',
                 'marker': '^',
                 'positions': cat_pos}}

    plot_walk(animal['Chicken'])
    plot_walk(animal['Dog'])
    plot_walk(animal['Cat'])
    plt.show()
    

if __name__ == '__main__':
    main()
