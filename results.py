from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("./results.csv")
print(df)

fig = plt.figure(figsize=(10, 5))
plt.bar(df["Total Time"], df["Accuracy"])
plt.xlabel("Total Time")
plt.ylabel("Accuracy")
plt.title("Total Time vs Accuracy")
plt.show()

plt.scatter(df["Total Time"], df["Accuracy"], c="blue")
plt.xlabel("Total Time")
plt.ylabel("Accuracy")
plt.title("Total Time vs Accuracy")
plt.show()

plt.bar(df["Total Time"], df["Words Per Minute"])
plt.xlabel("Total Time")
plt.ylabel("Words Per Minute")
plt.title("Total Time vs Words Per Minute")
plt.show()
