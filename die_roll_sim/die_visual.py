import plotly.express as px

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000) :
    result = die.roll()
    results.append(result)

# Quickly scan the results to verify the Die class is working.
#print(results)

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results :
    frequency = results.count(value)
    frequencies.append(frequency)

# Print the list before making a visualization; to check if the results 
#   look reasonable and are valid.
#print(frequencies)

# Visualize the results.
title = "Results of Rolling One D6 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()