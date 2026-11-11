import numpy as np
import matplotlib.pyplot as plt

days = np.array([1, 2, 3, 4, 5, 6, 7])

revenue = np.array([500, 600, 989, 700, 100, 600, 520])

costs = np.array([400, 250, 500, 700, 50, 200, 310])

print(days)
print(revenue)
print(costs)

profit = revenue - costs
print("Daily profit:", profit)

print("Average profit:", np.mean(profit))

print("Maximum profit:", np.max(profit))

print("Minimum profit:", np.min(profit))

plt.plot(days, profit)

plt.title("Daily Business Profit")
plt.xlabel("Day")
plt.ylabel("Profit")

plt.show()