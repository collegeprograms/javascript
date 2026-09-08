import csv

# ---------------------------------------
# STEP 1: Read training data
# ---------------------------------------

data = []

with open("heart.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data.append(row)

print("Number of records:", len(data))


# ---------------------------------------
# STEP 2: Count Yes and No cases
# ---------------------------------------

yes = 0
no = 0

for row in data:
    if row["HeartDisease"] == "Yes":
        yes += 1
    else:
        no += 1


# ---------------------------------------
# STEP 3: Prior probabilities
# ---------------------------------------

p_yes = yes / len(data)
p_no = no / len(data)


# ---------------------------------------
# STEP 4: Patient to be diagnosed
# ---------------------------------------

patient = {
    "Age": "Old",
    "Sex": "Male",
    "ChestPain": "Typical",
    "BP": "High",
    "Cholesterol": "High",
    "HeartRate": "Normal"
}


# ---------------------------------------
# STEP 5: Calculate conditional probability
# ---------------------------------------

def probability(attribute, value, disease):

    count = 0
    disease_count = 0

    for row in data:

        if row["HeartDisease"] == disease:

            disease_count += 1

            if row[attribute] == value:
                count += 1

    return count / disease_count


# ---------------------------------------
# STEP 6: Calculate probability for Yes
# ---------------------------------------

prob_yes = p_yes

for attribute in patient:

    prob_yes = prob_yes * probability(
        attribute,
        patient[attribute],
        "Yes"
    )


# ---------------------------------------
# STEP 7: Calculate probability for No
# ---------------------------------------

prob_no = p_no

for attribute in patient:

    prob_no = prob_no * probability(
        attribute,
        patient[attribute],
        "No"
    )


# ---------------------------------------
# STEP 8: Display probabilities
# ---------------------------------------

print("\nProbability of Heart Disease:", prob_yes)
print("Probability of No Heart Disease:", prob_no)


# ---------------------------------------
# STEP 9: Diagnosis
# ---------------------------------------

if prob_yes > prob_no:
    print("\nDiagnosis: Heart Disease")
else:
    print("\nDiagnosis: No Heart Disease")
