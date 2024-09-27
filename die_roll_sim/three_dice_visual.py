import plotly.express as px

from die import Die

# Create two D8s.
die_1 = Die()
die_2 = Die()
die_3 = Die()


# Make some rolls, and store results in a list.
#results = []
#for roll_num in range(100_000) :
#    result = die_1.roll() + die_2.roll() + die_3.roll()
#    results.append(result)

# Using list comprehension.
results = [(die_1.roll() + die_2.roll() + die_3.roll()) for 
           roll_num in range(100_000)]


# Quickly scan the results to verify the Die class is working.
#print(results)


# Analyze the results.
#frequencies = []
#max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
#poss_results = range(3, max_result+1)
#for value in poss_results :
#    frequency = results.count(value)
#    frequencies.append(frequency)

# Using list comprehension.
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result+1)
frequencies = [results.count(value) for value in poss_results]


# Print the list before making a visualization; to check if the results 
#   look reasonable and are valid.
#print(frequencies)

# Visualize the results.
title = "Results of Rolling Three D6s 100,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()