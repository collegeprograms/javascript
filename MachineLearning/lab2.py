import csv

# Read training data
with open("training_lab2.csv") as f:
    data = list(csv.DictReader(f))

A = ["Sky", "AirTemp", "Humidity", "Wind", "Water", "Forecast"]

S = ["0"] * 6
G = [["?"] * 6]


def covers(h, x):
    return all(h[i] == "?" or h[i] == x[A[i]] for i in range(6))


for n, x in enumerate(data, 1):

    if x["EnjoySport"] == "Yes":

        # Generalize S
        for i in range(6):
            if S[i] == "0":
                S[i] = x[A[i]]
            elif S[i] != x[A[i]]:
                S[i] = "?"

        # Keep only G hypotheses covering the positive example
        G = [h for h in G if covers(h, x)]

    else:

        # Specialize G
        new_G = []

        for h in G:
            if covers(h, x):
                for i in range(6):
                    if h[i] == "?":
                        new_h = h.copy()
                        new_h[i] = S[i]
                        if new_h[i] != "Ø":
                            new_G.append(new_h)
            else:
                new_G.append(h)

        G = new_G

    print(f"\nExample {n}: {x['EnjoySport']}")
    print("S =", S)
    print("G =", G)


print("\n========== FINAL RESULT ==========")
print("Specific Boundary (S):", S)
print("General Boundary (G):")

for h in G:
    print(h)
