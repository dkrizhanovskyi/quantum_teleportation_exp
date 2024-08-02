import matplotlib.pyplot as plt
import pandas as pd

# Data from the experiments with stabilizer error correction
results_plus = [
    {'00100': 8121, '00101': 8228, '00001': 8117, '00000': 8027, '01101': 8379, '01001': 8313, '01100': 8183, '01000': 8168},
    {'01101': 8253, '00000': 8182, '00101': 8349, '00001': 7997, '01100': 8115, '01000': 8122, '01001': 8225, '00100': 8293}
]

results_minus = [
    {'00100': 8197, '00001': 8015, '01100': 8253, '01001': 8167, '01000': 8313, '00000': 8202, '01101': 8150, '00101': 8239},
    {'00001': 8137, '01000': 8187, '01100': 8107, '01001': 8292, '00000': 8293, '00100': 8272, '01101': 8124, '00101': 8124}
]

# Creating dataframes for statistical analysis
df_plus = pd.DataFrame(results_plus)
df_minus = pd.DataFrame(results_minus)

# Calculating statistics
stats_plus = df_plus.describe().transpose()
stats_minus = df_minus.describe().transpose()

# Display statistics
print("Statistics for state |+⟩ with stabilizer error correction")
print(stats_plus)
print("\nStatistics for state |-⟩ with stabilizer error correction")
print(stats_minus)

# Plotting the results
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

def plot_stats(stats, state, ax):
    ax.errorbar(stats.index, stats['mean'], yerr=stats['std'], fmt='o', capsize=5, label='Mean ± Std')
    ax.set_title(f'Statistics for state |{state}⟩ with stabilizer error correction')
    ax.set_xlabel('State')
    ax.set_ylabel('Counts')
    ax.legend()

plot_stats(stats_plus, '+', axs[0])
plot_stats(stats_minus, '-', axs[1])

plt.tight_layout()
plt.show()
