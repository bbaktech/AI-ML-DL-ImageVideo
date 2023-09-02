# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:50:59 2023

@author: BBAK TECH
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:43:41 2023

@author: BBAK TECH
"""
import matplotlib.pyplot as plt
import numpy as np

species = ("16", "20", "24", "28","32","36","40")
penguin_means = {
    'EdgeWord Computation': (6208.0, 7760.0, 9312.0, 10864.0, 12416.0, 13968.0, 15520.0),
    'CloudWord Computation': (824890.0, 1037591.0, 1199881.0, 1244721.0, 1254034.0, 1263346.0, 1272658.0),
}

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Network Utilization')
ax.set_xlabel('Number of edge bins')
ax.set_title('Comparison of Network Usage - Edge/fog computing v/s cloud computing')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left')
ax.set_ylim(0, 1600000)

plt.show()
