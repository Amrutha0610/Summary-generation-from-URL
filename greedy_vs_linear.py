import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
import time

# Visualization of solution comparison
def visualize_solution(url):
    keywords = Get_Summary.extract_keywords(url)
    # Solve using Greedy Approximation
    start_time = time.time()
    greedy_cover = Get_Summary.greedy_summary(url,keywords)
    greedy_time = time.time() - start_time
    greedy_cost = len(greedy_cover)

    # Solve using Linear Programming
    start_time = time.time()
    lp_cover = generate_summary_with_lp(url)
    lp_time = time.time() - start_time
    lp_cost = len(lp_cover)

    # Visualize the comparison
    algorithms = ['Greedy Approximation', 'Linear Programming']
    times = [greedy_time, lp_time]
    costs = [greedy_cost, lp_cost]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Plot the time comparison
    ax1.bar(algorithms, times, color=['blue', 'green'])
    ax1.set_title('Running Time Comparison')
    ax1.set_ylabel('Time (seconds)')

    # Plot the cost (number of sets chosen)
    ax2.bar(algorithms, costs, color=['blue', 'green'])
    ax2.set_title('Cost Comparison (Number of Sets Chosen)')
    ax2.set_ylabel('Number of Sets')

    plt.show()

if __name__ == "__main__":
    url = input("Enter the URL: ")
    # Run the visualization
    visualize_solution(url)