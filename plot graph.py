import pandas as pd
import matplotlib.pyplot as plt 

columns = ["row_num","star_name","distance","mass","radius","gravity"]
df  = pd.read_csv("main3.csv",names=columns)

distance = df["distance"].tolist()
mass = df["mass"].tolist()
star_name = df["star_name"].tolist()
radius = df["radius"].tolist()
gravity = df["gravity"].tolist()


plt.figure(figsize=(12,8))
plt.plot(star_name,mass)
plt.show()

plt.figure(figsize=(12,8))
plt.plot(star_name,radius)
plt.show()

plt.figure(figsize=(12,8))
plt.plot(star_name,distance)
plt.show()

plt.figure(figsize=(12,8))
plt.plot(star_name,gravity)
plt.show()