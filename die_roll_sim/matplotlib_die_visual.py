import matplotlib.pyplot as plt

from die import Die

# Create two D12s.
die_1 = Die(12)
die_2 = Die(12)

# Make rolls and store results in a list.
results = [(die_1.roll() + die_2.roll()) for roll_num in range(100_000)]

# Quickly scan results to verify it works.
#print(results)

# Analyze results. Count frequency of result occurrences.
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results as a bar chart.
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.bar(poss_results, frequencies)

# Add titles and labels.
ax.set_title("Results of Rolling Two D12s 100,000 times.")
ax.set_xlabel("Result")
ax.set_ylabel("Frequency of Result")

# Make sure all results are labeled on the x-axis.
ax.set_xticks(ticks=poss_results)

plt.show()