import math
import matplotlib.pyplot as plt
import numpy as np

def solve_expression(x_values, expression):
    y_values = [max(0, expression(x)) for x in x_values]
    return y_values

def write_to_file(x_values, y_values_dict):
    with open("output_val.txt", "w") as file:
        for expression_name, values in y_values_dict.items():
            file.write(f"{expression_name}:\n")
            for value in values:
                file.write(f"{int(round(value))}\n")  # Write rounded integer value
            file.write("\n")

def plot_expression(x_values, y_values, expression_name):
    plt.figure(figsize=(12, 8))
    plt.plot(x_values, y_values, label=expression_name, linewidth=2)
    
    plt.title(f"Graph of {expression_name}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

def plot_all_expressions(x_values, y_values_dict):
    plt.figure(figsize=(12, 8))
    
    for expression_name, y_values in y_values_dict.items():
        plt.plot(x_values, y_values, label=expression_name, linewidth=2)
    
    plt.title("Graph of All Expressions")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

# Generate x values
x_values = np.linspace(0,50)

# Write x values to file
write_to_file(x_values, {})

# List of expressions
expressions = {
    "x^2 + 7x + 2": lambda x: x**2 + 7*x + 2,
    "3x + 2": lambda x: 3*x + 2,
    "x^2": lambda x: x**2,
    "x^3": lambda x: x**3,
    "x^5": lambda x: x**5,
    "x^3 + 2x^2 + x + 10": lambda x: x**3 + 2*x**2 + x + 10,
    "x^4 - 3x^3 + 2x^2 + 100": lambda x: x**4 - 3*x**3 + 2*x**2 + 100,
    "sin(x)": lambda x: math.sin(x),
    "cos(x)": lambda x: math.cos(x),
    "x^5 + 4x^4 + x^3 - 2x^2 + 100": lambda x: x**5 + 4*x**4 + x**3 - 2*x**2 + 100
}

# Display available expressions
print("Available Expressions:")
for i, expression_name in enumerate(expressions.keys()):
    print(f"{i + 1}. {expression_name}")

# Prompt user to choose an expression or solve all
try:
    choice = int(input("\nEnter the number of the expression you want to plot (or 0 to solve all): "))
    
    if choice == 0:
        y_values_dict = {}
        for expression_name, expression in expressions.items():
            y_values = solve_expression(x_values, expression)
            y_values_dict[expression_name] = y_values
        
        # Plot all expressions in one graph
        plot_all_expressions(x_values, y_values_dict)
        
        # Write results to file
        write_to_file(x_values, y_values_dict)
        
    elif 1 <= choice <= len(expressions):
        expression_name = list(expressions.keys())[choice - 1]
        expression = expressions[expression_name]
        
        # Solve and plot the chosen expression
        y_values = solve_expression(x_values, expression)
        plot_expression(x_values, y_values, expression_name)
        
        # Write results to file
        write_to_file(x_values, {expression_name: y_values})
        
    else:
        print("Invalid choice. Please enter a number between 0 and")
        
except ValueError:
    print("Invalid input. Please enter a number.")