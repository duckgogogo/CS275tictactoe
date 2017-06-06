import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

raw_data = {'TrainingNumber': ['10,000', '20,000', '30,000', '40,000', '50,000'],
        'NaiveAgent': [4, 24, 31, 2, 3],
        'MinimaxAgent': [25, 94, 57, 62, 70],
        'PrimitiveAgent': [5, 43, 23, 23, 51]}
df = pd.DataFrame(raw_data, columns = ['TrainingNumber', 'NaiveAgent', 'MinimaxAgent', 'PrimitiveAgent'])
df

# Setting the positions and width for the bars
pos = list(range(len(df['NaiveAgent'])))
width = 0.25

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with NaiveAgent data,
# in position pos,
plt.bar(pos,
        #using df['NaiveAgent'] data,
        df['NaiveAgent'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#EE3224',
        # with label the first value in TrainingNumber
        label=df['TrainingNumber'][0])

# Create a bar with MinimaxAgent data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos],
        #using df['MinimaxAgent'] data,
        df['MinimaxAgent'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#F78F1E',
        # with label the second value in TrainingNumber
        label=df['TrainingNumber'][1])

# Create a bar with PrimitiveAgent data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos],
        #using df['PrimitiveAgent'] data,
        df['PrimitiveAgent'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#FFC222',
        # with label the third value in TrainingNumber
        label=df['TrainingNumber'][2])

# Set the y axis label
ax.set_ylabel('Score')

# Set the chart's title
ax.set_title('3 X 3 Board 3 Streaks')

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['TrainingNumber'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df['NaiveAgent'] + df['MinimaxAgent'] + df['PrimitiveAgent'])] )

# Adding the legend and showing the plot
plt.legend(['Naive Agent', 'Minimax Agent', 'Primitive Agent'], loc='upper left')
plt.grid()
plt.show()