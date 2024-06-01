import numpy as np             #Import Numpy for numerical operations
from scipy.optimize import minimize    #Import minimize function from scipy.optimize
import matplotlib.pyplot as plt          #Import pyplot module from matplotlib for plotting
import sys                               #Import the sys module


def main():
    display_info()
    # Input number of items , weight capacity  and cost per unit weight of the box
    num_items = int(input('Enter the number of items: '))            #Prompting the user to enter items
    capacity = float(input('Enter the weight capacity of the box: ')) #Prompting the user to enter weight capacity
    cost_per_unitweight = float(input('Enter the cost per unit weight :')) #Prmpting the user to enter cost per unit weight

    weights = np.zeros(num_items)        # Initilize an array to store weights of each item

    # Input weights of each item
    print('Enter the weights  of each item:')
    for i in range(num_items):
        weights[i] = float(input(f'Weight of item {i+1}: ')) #Prompting the user to input weight of each item
    # Check if total weight exceeds capacity
    if np.sum(weights) > capacity:
        print('Error: Total weight exceeds capacity.')      #Print error message if total weight exceeds capacity
        sys.exit()   #Exit the Program
    else:
        # Perform optimization
        optimized_quantities, total_weight = perform_optimization(weights , capacity )

        #Calculate total cost
        total_cost = cost_per_unitweight * total_weight

        # Display optimization results
        display_results(optimized_quantities, total_weight , weights  , capacity , total_cost , cost_per_unitweight )

#Function to display student info
def display_info () :
    print("Welcome to Our Software House")
    print("Developed By Team ")
    print("- Muhammad Noor {ID : I23-2520}")
    print("- Shahoud Shahid {ID : I23-2515}")
    print("- Saif Shahzad {ID : I23-2634}")

# Function to perform optimization
def perform_optimization(weights , capacity):
    # Objective function: minimizes the sum of quantities
    def objective(x):
       return -np.sum(weights * x)        # Return negative sum of product of weights and quantities

    #Minimize total weight used

    # Constraint function: Total weight shouldn't exceed box's capacity
    def weight_constraint(x):
        return  capacity -np.dot(weights, x)  #Return difference between weight capacity and dot product of weights and quantities

    #Non-negative constraint
    bounds = [(0,capacity) for _ in weights]  #Defining bounds for qunatities of each item(non-negative constraint)

    # Initial guess: equal quantities for each item
    x0 = np.full(len(weights), capacity / sum(weights))    #Initialize quantities for each item
    #Provides a more balanced start

    # Optimization using scipy's minimize function
    opt_result = minimize(objective , x0 , bounds = bounds , constraints={'type': 'ineq', 'fun': weight_constraint})

    # Extracting optimized quantities and total weight
    optimized_quantities = opt_result.x
    total_weight = np.dot(weights,optimized_quantities)

    return optimized_quantities, total_weight

# Function to display optimization results
def display_results(optimized_quantities, total_weight ,weights  , capacity  , total_cost , cost_per_unitweight):
    print('Optimized quantities of each item:')
    for i, qty in enumerate(optimized_quantities):
        print(f'Item {i+1}: {qty:.3f}(Weight:{weights[i]*qty:.3f})')  #Printing optimized quantties and corresponding weights

    print(f'Total weight of the packaged items: {total_weight:.3f}')
    print(f'Total cost  of the packaged items: {total_cost:.3f}')

    if total_weight > capacity :
              print("Warning : Total weight exceeds the capacity !")   #Printing warning if total weight exceeds capacity
              sys.exit()                                               #Exit the Program
    else :
              print ("Total weight is within the box's capacity.")     #Printing message if total weight is within capacity


    # Plotting the optimized quantities
    plt.bar(range(1, len(optimized_quantities) + 1), weights*optimized_quantities , color=['blue'])
    plt.xlabel('Item Number')
    plt.ylabel('Quantity')
    plt.title('Optimized Weights  of Each Item')
    plt.grid(True)
    plt.show()
# Calling main function to start the program
if __name__ == "__main__":
    main()    #Execute the main function if the script is executed directly
