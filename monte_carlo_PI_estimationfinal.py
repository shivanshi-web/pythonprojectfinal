import random
import matplotlib.pyplot as plt

def estimate_pi(N):
    inside_circle = 0
    
    x_vals, y_vals = [], []  # For visualization
    
    for _ in range(N):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
            x_vals.append(x)
            y_vals.append(y)
    
    pi_estimate = 4 * (inside_circle / N)
    return pi_estimate, x_vals, y_vals

N_values = [10, 100, 1000, 10000, 100000]
pi_estimates = []

for N in N_values:
    pi, x_pts, y_pts = estimate_pi(N)
    pi_estimates.append(pi)
    print(f'N={N}: Estimated π ≈ {pi}')

plt.plot(N_values, pi_estimates, marker='o', linestyle='-')
plt.axhline(y=3.141592653589793, color='r', linestyle='--', label='Actual π')
plt.xscale('log')
plt.xlabel('Number of Points (N)')
plt.ylabel('Estimated π')
plt.title('Monte Carlo π Estimation')
plt.legend()
plt.show()