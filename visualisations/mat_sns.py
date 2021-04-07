import matplotlib.pyplot as plt
from random import randint
import pandas as pd


# create random data and store in a dataframe
months  = [i for i in range(1, 13)]
rand_nums = [randint(1000, 10000) for i in range(1,13)]
df = pd.DataFrame({"month": months, "data": rand_nums})

# create figure and 4 subplots, unpack in the variable names
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(8,8))

print(type(fig))
print(type(ax1))

print(id(fig)) # figure and gcf (get current figure) return same id
print(id(plt.gcf())) # figure and gcf (get current figure) return same id

print(id(ax4)) # most recently created axes and gca (get current axes) return same id
print(id(plt.gca())) # most recently created axes and gca (get current axes) return same id

print(plt.get_fignums()) # return a list of all the figures stored in memory

# all figures will be stored in memory
# plt.close() # close current figure
# plt.close(num) # close specified figure
plt.close('all') # close all figures

def mat_subplots():
    x = df['month']
    y = df['data']

    # create figure and 4 subplots, unpack in the variable names
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(8,8))

    # ax1; simple scatter graph with data
    ax1.set_title("simple scatter")
    ax1.set_xlabel("month")
    ax1.set_ylabel("random_data")

    ax1.scatter(x=x, y=y, c=y,
            cmap = 'YlGnBu')
    ax1.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)

    # ax2; histogram
    ax2.set_title("simple histogram")
    ax2.set_xlabel("month")
    ax2.set_ylabel("count")

    ax2.hist(x=y,
            color = 'cyan',
            edgecolor = 'darkblue')


    # ax3; plot with a joining line
    ax3.set_title("simple joined scatter")
    ax3.set_xlabel("month")
    ax3.set_ylabel("random_data")
    ax3.plot(x,y, linestyle='solid',color='blue')

    # ax4; bar/barh
    ax4.set_title("simple bar chart")
    ax4.set_xlabel("month")
    ax4.set_ylabel("random_data")
    ax4.barh(x, y, color='red')

    fig.tight_layout()
    plt.show()


def mat_gant():
    """
    Create a Gantt chart of activity using matplotlib.
    """
    fig, ax = plt.subplots(figsize=(8,8)) # create new figure/axes

    ax.set_ylim(0, 50)
    ax.set_xlim(0, 160)

    ax.set_title("Gant chart of activity")
    ax.set_xlabel('date') # label x axis
    ax.set_ylabel('task') # label y axis
    
    ax.set_yticks([15, 25, 35]) # add 3 y ticks at specified points
    ax.set_yticklabels(['1', '2', '3']) # relabel y ticks to 1, 2 and 3
    #ax.set_xticklabels(['1', '2', '3', '4', '5', '6', '7', '8'])
    ax.grid(True) # add grid lines
    
    ax.broken_barh([(40, 50)], (30, 9), facecolors =('tab:orange'))
    # start at 40 on x axis, add 50 to fill to 90. 
    # start at 30 on y axis, add 9 to fill to 39
    ax.broken_barh([(110, 10), (150, 10)], (10, 9),
                            facecolors ='tab:blue')
    ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
                                    facecolors =('tab:red'))

    fig.tight_layout()
    plt.show()


mat_subplots()
mat_gant()

plt.close('all')