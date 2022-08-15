#!/usr/bin/env python3


import pandas as pd
import matplotlib.pyplot as plt

# create data frame (recreation of excel csv file) using python

df = pd.DataFrame(
    {"Name":["Patricia Ann Knight", "Gerald Lynn Knight", "Scott Christopher Knight",
             "Debra Ann Nichols", "Joseph Michael Knight", "Laura Lynn Jones",
             "Christopher Scott Knight", "Emily Debra Jones", "Mason Carder Knight",
             "Addison Lynn Jones", "Gabrielle Marie Knight"],
     "Age":[80, 82, 59, 58, 53, 49, 26, 21, 20, 19, 16],
     "Hair Color":["Light Brown", "Light Brown", "Light Brown", "Dark Brown", "Light Brown",
                  "Light Blonde", "Light Brown", "Light Blonde", "Dark Brown", "Light Blonde",
                  "Light Brown"],
     "Eye Color":["Brown", "Blue", "Blue", "Brown", "Blue", "Blue", "Blue", "Blue", "Green",
                   "Blue", "Green"],
     "Skin Shade":["Olive", "Pale", "Pale", "Tan", "Olive", "Pale", "Pale", "Pale", "Olive",
                   "Pale", "Tan"]

     }
)

print(df.shape)
print(df)


# count occurrences for each hair color

hairlb = df["Hair Color"].value_counts()["Light Brown"]
hairdb = df["Hair Color"].value_counts()["Dark Brown"]
hairbl = df["Hair Color"].value_counts()["Light Blonde"]


# count occurrences for each eye color

browneye = df["Eye Color"].value_counts()["Brown"]
blueeye = df["Eye Color"].value_counts()["Blue"]
greeneye = df["Eye Color"].value_counts()["Green"]


# count occurrences for each skin shade

tanskin = df["Skin Shade"].value_counts()["Tan"]
oliveskin = df["Skin Shade"].value_counts()["Olive"]
paleskin = df["Skin Shade"].value_counts()["Pale"]

#organize hair color data
hairdata = {"Hair Color": ["Light Blonde", "Light Brown", "Dark Brown"],
        "Number of Family Members": [hairbl, hairlb, hairdb]
        }

#create hair data chart

print(hairdata)
dataFrame1 = pd.DataFrame(data=hairdata)
dataFrame1.plot.bar(x="Hair Color", y="Number of Family Members", title="Knight Hair Color",
                    color=['#F8EEC5', '#BAA271', '#504131'])
plt.xlabel("Hair Color")
plt.ylabel("Number of Family Members")
plt.show()


#organize eye color data
eyedata = {"Eye Color": ["Brown Eyes", "Blue Eyes", "Green Eyes"],
           "Number of Family Members": [browneye, blueeye, greeneye]
           }
mylabels = ["Brown Eyes", "Blue Eyes", "Green Eyes"]
color = ["#5C3F2A", "#4372C0", "#54823B"]

print(eyedata)
dataFrame2 = pd.DataFrame(data=eyedata)
dataFrame2.plot.pie(x = "Eye Color", y = "Number of Family Members", title="Knight Eye Color", labels = mylabels, colors=color)
plt.legend()
plt.show()


#organize skin shade data
skindata = {"Skin Shade": ["Tan", "Olive", "Pale"],
            "Number of Family Members": [tanskin, oliveskin, paleskin]
            }

skinx = [tanskin, oliveskin, paleskin]
skiny = [4,8,12]



print(skindata)
dataFrame3 = pd.DataFrame(data=skindata)
dataFrame3.plot.bar(x="Skin Shade", y="Number of Family Members", title="Knight Skin Shade",
                    color=['#D2B48F', '#DDC9AF', '#F2DBBE'])
plt.xlabel("Skin Shade")
plt.ylabel("Number of Family Members")
plt.show()














