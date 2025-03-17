import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function 1: Plotting the Derivative of a Quadratic Function
# Define the main function and its analytical derivative
def f(x):
    return 3 * x ** 2 - 4 * x

# Analytical derivative of the function
def f_prime(x):
    return 6 * x - 4

# Numerical derivative approximation function for visualization
def numerical_derivative(x, h):
    return (f(x + h) - f(x)) / h

# Plotting both the function, its derivative, and numerical tangent approximations
def plot_derivative_numerical_tangent_approximations():
    # Define the range of x values
    x_vals = np.linspace(-3, 3, 100)
    y_vals = f(x_vals)
    dydx_vals = f_prime(x_vals)
    x_point = 1
    h_values = [0.1, 0.01, 0.001, 0.0001]

    plt.figure(figsize=(12, 8))
    
    # Plotting the main function and its analytical derivative
    plt.plot(x_vals, y_vals, label=r'$f(x) = 3x^2 - 4x$', color='blue')
    plt.plot(x_vals, dydx_vals, label=r"$f'(x) = 6x - 4$", linestyle='--', color='red')
    
    # Plot tangent lines with varying h values to show how the slope changes
    for h in h_values:
        slope = numerical_derivative(x_point, h)
        tangent_line = slope * (x_vals - x_point) + f(x_point)
        plt.plot(x_vals, tangent_line, '--', label=f'Tangent at x=1 with h={h:.5f}')
    
    # Highlight the point of interest
    plt.scatter([x_point], [f(x_point)], color='red', zorder=5)
    plt.text(x_point, f(x_point), f"({x_point}, {f(x_point)})", fontsize=12, ha='left')
    
    # Adding additional context and annotations
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title('Quadratic Function, Its Derivative, and Tangent Approximations')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.text(1.5, 10, 'Function: $f(x) = 3x^2 - 4x$', fontsize=12, color='blue')
    plt.text(-2.5, 10, 'Derivative: $f\'(x) = 6x - 4$', fontsize=12, color='red')
    plt.annotate('Slope changes\nwith x', xy=(1, 2), xytext=(1.5, 15),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()


# Function 2: Visualizing the Chain Rule
def plot_chain_rule():
    # Define the range of x values
    x = np.linspace(-2, 2, 100)
    # Define the inner and outer functions
    u = 3 * x**2 - 4 * x
    y = np.exp(u)
    
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    
    ax[0].plot(x, u, label=r'$u = 3x^2 - 4x$', color='green')
    ax[0].set_title('Inner Function $u = 3x^2 - 4x$')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('u')
    ax[0].grid(True)
    ax[0].legend()
    ax[0].annotate('u changes rapidly\nnear x=0', xy=(0, 0), xytext=(-1.5, 10),
                   arrowprops=dict(facecolor='black', shrink=0.05))
    
    ax[1].plot(u, y, label=r'$y = e^u$', color='purple')
    ax[1].set_title('Outer Function $y = e^u$')
    ax[1].set_xlabel('u')
    ax[1].set_ylabel('y')
    ax[1].grid(True)
    ax[1].legend()
    ax[1].annotate('Exponential growth', xy=(0, 1), xytext=(5, 50),
                   arrowprops=dict(facecolor='black', shrink=0.05))
    
    plt.suptitle('Visualization of the Chain Rule')
    plt.show()

# Function 3: Visualizing Partial Derivatives and Gradient Vector
def plot_gradient_vector():
    # Define the range of x and y values
    x = np.linspace(-2, 2, 20)
    y = np.linspace(-2, 2, 20)
    # Create a meshgrid for 3D plotting
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2  # Example function: f(x, y) = x^2 + y^2
    
    # Calculate partial derivatives
    dfdx = 2 * X
    dfdy = 2 * Y
    
    plt.figure(figsize=(10, 8))
    ax = plt.axes(projection='3d')
    # Plot the surface of the function
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    # Add gradient vectors to show the direction of steepest ascent
    ax.quiver(X, Y, Z, dfdx, dfdy, 0, color='red', length=0.1, normalize=True)
    ax.set_title('Partial Derivatives and Gradient Vectors of $f(x, y) = x^2 + y^2$')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    plt.show()

