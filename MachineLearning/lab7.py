import csv
import math

# Read data
data = []
with open("students_Lab7.csv") as f:
    for row in csv.DictReader(f):
        data.append(float(row["Marks"]))

# Initial means
m1, m2 = 50, 90

# EM iterations
for _ in range(10):

    r1, r2 = [], []

    # E-Step
    for x in data:
        p1 = math.exp(-(x-m1)**2 / 200)
        p2 = math.exp(-(x-m2)**2 / 200)
        r1.append(p1/(p1+p2))
        r2.append(p2/(p1+p2))

    # M-Step
    m1 = sum(r1[i]*data[i] for i in range(len(data))) / sum(r1)
    m2 = sum(r2[i]*data[i] for i in range(len(data))) / sum(r2)

# Display clusters
for i, x in enumerate(data):
    cluster = 1 if r1[i] > r2[i] else 2
    print(x, "-> Cluster", cluster)

print("Means:", round(m1, 2), round(m2, 2))
