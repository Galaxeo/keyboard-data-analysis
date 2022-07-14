import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from venn import venn
import numpy as np
sns.set(style = "whitegrid")

keydf = pd.read_excel('C:\\Users\\Justin\\PycharmProjects\\keyboard\\keyb1.xlsx')
keydf2 = pd.read_excel('C:\\Users\\Justin\\PycharmProjects\\keyboard\\keyb2.xlsx')

#we want to parse through all of the users here and underestand where they stand

tactile = []
clicky = []
linear = []
other = []
for i in range(len(keydf)):
    if keydf.iat[i, 2] == "Tactile":
        tactile.append(i)
    elif keydf.iat[i, 2] == "Linear":
        linear.append(i)
    elif keydf.iat[i, 2] == "Clicky":
        clicky.append(i)
    elif keydf.iat[i, 2] == "Other":
        other.append(i)

# Sum up the reasons behind purchase of each switch type
# Given input of users in the db (as indices), compile a list of reasons behind purchases
def reasons_list(lst):
    global keydf
    reasons = []
    for item in lst:
        if "," in keydf.iat[int(item)-1,3]:
            temp = keydf.iat[int(item)-1,3].replace(" ", "").split(",")
            for item in temp:
                reasons.append(item)
        else:
            reasons.append(keydf.iat[int(item)-1, 3].replace(" ", ""))
    return reasons

# For the purchase reasoning question:
# Want to see how many people bought keyboards for certain reasons
def cal_reasons(lst):
    reasons = reasons_list(lst)
    return [reasons.count('Gaming'), reasons.count('Quality'),
            reasons.count('Productivity'), reasons.count('Aesthetics'), reasons.count('Price')]

# Looking at how much time spent per category for each switch type
def weights(lst):
    global keydf
    game = 0
    prod = 0
    notprod = 0
    for i in lst:
        prod+=keydf.iat[int(i), 4]
        game+=keydf.iat[int(i), 5]
        notprod+=keydf.iat[int(i), 6]
    return game, prod, notprod
# Database categorizing into types of switches
labels = "Tactile", "Linear", "Clicky", "Other"
sizes = [len(tactile), len(linear), len(clicky), len(other)]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct = '%1.1f%%', startangle = 90)
ax1.axis('equal')
plt.savefig('switchtypes.png')
plt.close()

#Venn works by looking at a dictionary, then if the values are in both, add it in.
venndict = dict.fromkeys(["Gaming", "Quality of Life", "Productivity", "Aesthetics", "Price"])
gaming = []
quality = []
prod = []
aesthetics = []
price = []
for i in range(len(keydf)):
    temp = keydf.iat[i, 3].replace(" ", "").split(",")
    for item in temp:
        if item == "Gaming":
            gaming.append(i)
        if item == "Quality":
            quality.append(i)
        if item == "Productivity":
            prod.append(i)
        if item == "Aesthetics":
            aesthetics.append(i)
        if item == "Price":
            price.append(i)
venndict["Gaming"] = set(gaming)
venndict["Quality of Life"] = set(quality)
venndict["Productivity"] = set(prod)
venndict["Aesthetics"] = set(aesthetics)
venndict["Price"] = set(price)

v = venn(venndict, fmt = "{percentage:.1f}%", legend_loc = "upper right")
plt.savefig("venn.png")
plt.close()


# Bar graph, time spent split into those who bought the keyboard for that reason and those who didn't
switches = ['Tactile', 'Linear', 'Clicky']
groups = ['Purchased for gaming', 'Other reasons']
total_gaming = weights(tactile)[0] + weights(linear)[0] + weights(clicky)[0] + weights(other)[0]
gamepercent = [cal_reasons(tactile)[0]/total_gaming, cal_reasons(linear)[0]/total_gaming, cal_reasons(clicky)[0]/total_gaming]
restpercent = [int(weights(tactile)[0] - gamepercent[0])/total_gaming, int(weights(linear)[0] - gamepercent[1])/total_gaming,
             int(weights(clicky)[0] - gamepercent[2])/total_gaming]
r = [0, 1, 2]
barwidth = 1
names = "Tactile, Linear, Clicky"
plt.bar(r, gamepercent, width=barwidth)
plt.bar(r, restpercent, bottom=gamepercent, width=barwidth)
plt.xticks(r, switches)
plt.ylabel("Time spent gaming (hours)")
plt.xlabel("Type of switch")
plt.legend(groups, loc="upper right")
plt.savefig('bargraph.png')

# Pie chart weighing gaming, productivity, and non-productive tasks - gaming
# Tactile
labels = 'Gaming', 'Productive', 'Unproductive'
sizes = weights(tactile)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct = '%1.1f%%', startangle = 90)
ax1.axis('equal')
plt.title("Time Spent (Tactile Users)")
plt.savefig('tactileweights.png')
plt.close()

# Linear
labels = 'Gaming', 'Productive', 'Unproductive'
sizes = weights(linear)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct = '%1.1f%%', startangle = 90)
ax1.axis('equal')
plt.title("Time Spent (Linear Users)")
plt.savefig('linearweights.png')
plt.close()

# Clicky
labels = 'Gaming', 'Productive', 'Unproductive'
sizes = weights(clicky)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct = '%1.1f%%', startangle = 90)
ax1.axis('equal')
plt.title("Time Spent (Clicky Users)")
plt.savefig('clickyweights.png')
plt.close()



# Analyzing those who are outside of the market's perception of minimum and maximum $ for a custom keyboard
# Split into two groups, first with all data combined, second with updated improved groups of data
#Both Together
f, ax = plt.subplots()
sns.violinplot(x="Keyboard", y="Min", hue="Heard?", data=keydf, split=True)
ax.set(xlabel="Type of Keyboard", ylabel="Minimum $ for a custom keyboard (hundreds)")
plt.ylim(0, 5)
plt.legend(title = "Heard of custom?", loc='upper right')
plt.title("Min. $ for a custom (all data)")
plt.savefig("minplot.png")
plt.close()

f, ax = plt.subplots()
sns.violinplot(x="Keyboard", y="Max", hue="Heard?", data=keydf, split=True)
ax.set(xlabel="Type of Keyboard", ylabel="Maximum $ for a custom keyboard (hundreds)")
plt.ylim(0, 15)
plt.legend(title = "Heard of custom?", loc='upper right')
plt.title("Max. $ for a custom (all data)")
plt.savefig("maxplot.png")
plt.close()

# Both Separately
f, ax = plt.subplots()
sns.violinplot(x="Keyboard", y="Min", hue="Heard?", data=keydf2, split=True)
ax.set(xlabel="", ylabel="Minimum $ for a custom keyboard (hundreds)")
plt.ylim(0, 5)
plt.legend(title = "Heard of custom?", loc='upper right')
plt.title("Min. $ for a custom (selective data)")
plt.savefig("minplot2.png")
plt.close()

f, ax = plt.subplots()
sns.violinplot(x="Keyboard", y="Max", hue="Heard?", data=keydf2, split=True)
ax.set(xlabel="", ylabel="Max $ for a custom keyboard (hundreds)")
plt.ylim(0, 15)
plt.legend(title = "Heard of custom?", loc='upper right')
plt.title("Min. $ for a custom (selective data)")
plt.savefig("maxplot2.png")
plt.close()

# Tactility Preference
f, ax = plt.subplots()
labels = 'Prefer', 'Minimal to None', 'N/A'
tactpref = []
for i in range(len(keydf)):
    tactpref.append(keydf.iat[i, 8])
sizes = tactpref.count('Prefer'), tactpref.count('Minimal'), tactpref.count("Other")
print(tactpref)
ax.pie(sizes, labels=labels, autopct = '%1.1f%%', startangle = 90)
ax.axis('equal')
plt.title("Tactility Preference")
plt.savefig("tactpref.png")
plt.close()

# Reasons behind purchase charts
# Tactile pie Chart
labels = 'Gaming', 'Quality of life', 'Productivity', 'Aesthetics', 'Price'
sizes = cal_reasons(tactile)
explode = (.1, 0, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode = explode, labels=labels, shadow = True, autopct = '%1.1f%%',
        startangle = 90)
ax1.axis('equal')
plt.title("Reasons of Purchase for Tactile Users")
plt.savefig('tactilepie.png')
plt.close()

# Linear pie chart

labels = 'Gaming', 'Quality of life', 'Productivity', 'Aesthetics', 'Price'
sizes = cal_reasons(linear)
explode = (.1, 0, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode = explode, labels=labels, shadow = True, autopct = '%1.1f%%',
        startangle = 90)
ax1.axis('equal')
plt.title("Reasons of Purchase for Linear Users")
plt.savefig('linearpie.png')
plt.close()

# Clicky Chart
labels = 'Gaming', 'Quality of life', 'Productivity', 'Aesthetics', 'Price'
sizes = cal_reasons(clicky)
explode = (.1, 0, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode = explode, labels=labels, shadow = True, autopct = '%1.1f%%',
        startangle = 90)
ax1.axis('equal')
plt.title("Reasons of Purchase for Clicky Users")
plt.savefig('clickypie.png')
plt.close()



# Violin Plots looking at time spent
# Violin Productive
f, ax = plt.subplots()
sns.violinplot(x = "Switches", y = "Productivity", data=keydf)
plt.ylim(0, 8)
plt.title("Time Spent Productively (per day)")
ax.set(ylabel = "Hours spent Productively", xlabel = "Type of Switch")
plt.savefig('productivity.png')
plt.close()
# Violin Gaming
f, ax = plt.subplots()
sns.violinplot(x = "Switches", y = "Gaming", data=keydf)
plt.ylim(0, 8)
plt.title("Time Spent Gaming (per day)")
ax.set(ylabel = "Hours spent Gaming", xlabel = "Type of Switch")
plt.savefig('gaming.png')
plt.close()
# Violin Unproductive
f, ax = plt.subplots()
sns.violinplot(x = "Switches", y = "Social", data=keydf)
plt.ylim(0, 8)
plt.title("Time Spent On Unproductive Work w/o Gaming (per day)")
ax.set(ylabel = "Hours spent Unproductively (- Gaming)", xlabel = "Type of Switch")
plt.savefig('social.png')

f, ax = plt.subplots()
sns.violinplot(y = "Max", data = keydf)
ax.set(ylabel = " ")
plt.savefig('violinexample.png')
