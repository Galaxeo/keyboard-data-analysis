import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = "whitegrid")

keydf = pd.read_excel('C:\\Users\\Justin\\PycharmProjects\\keyboard\\keyb1.xlsx')
keydf2 = pd.read_excel('C:\\Users\\Justin\\Documents\\keyb2.xlsx')

print(keydf.iat[0,9])

#we want to parse through all of the users here and underestand where they stand

tactile = []
clicky = []
linear = []

for i in range(len(keydf)):
    if keydf.iat[i, 2] == "Tactile":
        tactile.append(i)
    elif keydf.iat[i, 2] == "Linear":
        linear.append(i)
    elif keydf.iat[i, 2] == "Clicky":
        clicky.append(i)

def categorize(lst):
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

def calculate_weights(lst):
    reasons = categorize(lst)
    return [reasons.count('Gaming'), reasons.count('Quality'),
            reasons.count('Productivity'), reasons.count('Aesthetics'), reasons.count('Price')]


#Min and Max plots with both people who are in and not in, as well as updated versus with previous
#Both Together
f, ax = plt.subplots()
sns.violinplot(x="Keyboard", y="Min", hue="Heard?", data=keydf, split=True)
ax.set(xlabel="Type of Keyboard", ylabel="Minimum $ for a custom keyboard")
plt.ylim(0, 5)
plt.legend(title = "Heard of custom?", loc='upper right')
plt.savefig("minplot.png")
plt.close()

f, ax = plt.subplots()
sns.violinplot(x="Keyboard", y="Max", hue="Heard?", data=keydf, split=True)
ax.set(xlabel="Type of Keyboard", ylabel="Minimum $ for a custom keyboard")
plt.ylim(0, 15)
plt.legend(title = "Heard of custom?", loc='upper right')
plt.savefig("maxplot.png")
plt.close()

#Both Separately
f, ax = plt.subplots()
sns.violinplot(x="Keyboard", y="Min", hue="Heard?", data=keydf2, split=True)
ax.set(xlabel="", ylabel="Minimum $ for a custom keyboard")
plt.ylim(0, 5)
plt.legend(title = "Heard of custom?", loc='upper right')
plt.savefig("minplot2.png")
plt.close()

f, ax = plt.subplots()
sns.violinplot(x="Keyboard", y="Max", hue="Heard?", data=keydf2, split=True)
ax.set(xlabel="", ylabel="Minimum $ for a custom keyboard")
plt.ylim(0, 15)
plt.legend(title = "Heard of custom?", loc='upper right')
plt.savefig("maxplot2.png")
plt.close()
# f, ax = plt.subplots()
# #Minimum price plot
# sns.violinplot(x = "Switches", y = "Min", data=keydf)
# plt.ylim(0, 5)
# ax.set(ylabel = "Minimum Amount for a Custom (hundreds)", xlabel = "Type of Switch")
# plt.title('Min. $ for Custom v.s. Type of Switch')
# plt.savefig("minplot.png")
# plt.close()
# #Maximum price plot
# sns.violinplot(x = "Switches", y = "Max", data=keydf)
# plt.ylim(0, 20)
# ax.set(ylabel = "Maximum Amount for a Custom (hundreds)", xlabel = "Type of Switch")
# plt.title('Max. $ for Custom v.s. Type of Switch')
# plt.savefig("maxplot.png")
# plt.close()
#
# #Tactile pie Chart
# labels = 'Gaming', 'Quality of life', 'Productivity', 'Aesthetics', 'Price'
# sizes = calculate_weights(tactile)
# explode = (.1, 0, 0, 0, 0)
#
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode = explode, labels=labels, shadow = True, autopct = '%1.1f%%',
#         startangle = 90)
# ax1.axis('equal')
# plt.title("Reasons of Purchase for Tactile Users")
# plt.savefig('tactilepie.png')
# plt.close()
#
# #Linear pie chart
#
# labels = 'Gaming', 'Quality of life', 'Productivity', 'Aesthetics', 'Price'
# sizes = calculate_weights(linear)
# explode = (.1, 0, 0, 0, 0)
#
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode = explode, labels=labels, shadow = True, autopct = '%1.1f%%',
#         startangle = 90)
# ax1.axis('equal')
# plt.title("Reasons of Purchase for Linear Users")
# plt.savefig('linearpie.png')
# plt.close()
#
# #Clicky Chart
# labels = 'Gaming', 'Quality of life', 'Productivity', 'Aesthetics', 'Price'
# sizes = calculate_weights(clicky)
# explode = (.1, 0, 0, 0, 0)
#
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode = explode, labels=labels, shadow = True, autopct = '%1.1f%%',
#         startangle = 90)
# ax1.axis('equal')
# plt.title("Reasons of Purchase for Clicky Users")
# plt.savefig('clickypie.png')
# plt.close()
#
# #Violin Productive
# f, ax = plt.subplots()
# sns.violinplot(x = "Switches", y = "Productivity", data=keydf)
# plt.ylim(0, 8)
# plt.title("Time Spent Productively (per day)")
# ax.set(ylabel = "Hours spent Productively", xlabel = "Type of Switch")
# plt.savefig('productivity.png')
# plt.close()
# #Violin Gaming
# f, ax = plt.subplots()
# sns.violinplot(x = "Switches", y = "Gaming", data=keydf)
# plt.ylim(0, 8)
# plt.title("Time Spent Gaming (per day)")
# ax.set(ylabel = "Hours spent Gaming", xlabel = "Type of Switch")
# plt.savefig('gaming.png')
# plt.close()
# #Violin Unproductive
# f, ax = plt.subplots()
# sns.violinplot(x = "Switches", y = "Social", data=keydf)
# plt.ylim(0, 8)
# plt.title("Time Spent On Unproductive Work - Gaming (per day)")
# ax.set(ylabel = "Hours spent Unproductively (- Gaming)", xlabel = "Type of Switch")
# plt.savefig('social.png')

# class User:
#     def __init__(self, usernum, switches, prod, game, unprod):
#         self.usernum = usernum
#         self.switches = switches
#         self.prio = prio(prod, game, unprod)
#
# def prio(prod, game, unprod):
#     Dict = {"Productivity": prod, "Gaming": game, "Unproductive": unprod}
#     maxprio = max(prod, game, unprod)
#     return [k for k, v in Dict.items() if v == maxprio]