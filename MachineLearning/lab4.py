import csv

# ---------------------------------------
# STEP 1: Read Training Data
# ---------------------------------------

with open("training_lab4.csv", "r") as file:

    reader = csv.DictReader(file)

    training_data = list(reader)


# ---------------------------------------
# STEP 2: Read Test Data
# ---------------------------------------

with open("test_lab4.csv", "r") as file:

    reader = csv.DictReader(file)

    test_data = list(reader)


# ---------------------------------------
# STEP 3: Count Yes and No
# ---------------------------------------

yes_count = 0
no_count = 0

for row in training_data:

    if row["Play"] == "Yes":
        yes_count += 1
    else:
        no_count += 1


total = len(training_data)


# ---------------------------------------
# STEP 4: Calculate Prior Probability
# ---------------------------------------

p_yes = yes_count / total
p_no = no_count / total


print("Prior Probabilities")
print("-------------------")

print("P(Yes) =", p_yes)
print("P(No)  =", p_no)


# ---------------------------------------
# STEP 5: Calculate Conditional
# Probability
# ---------------------------------------

def probability(feature, value, target):

    count = 0
    target_count = 0

    for row in training_data:

        if row["Play"] == target:

            target_count += 1

            if row[feature] == value:
                count += 1

    return count / target_count


# ---------------------------------------
# STEP 6: Prediction Function
# ---------------------------------------

def predict(outlook, temperature, humidity, wind):

    # Probability for Yes

    p_outlook_yes = probability(
        "Outlook", outlook, "Yes"
    )

    p_temperature_yes = probability(
        "Temperature", temperature, "Yes"
    )

    p_humidity_yes = probability(
        "Humidity", humidity, "Yes"
    )

    p_wind_yes = probability(
        "Wind", wind, "Yes"
    )

    yes_probability = (
        p_yes *
        p_outlook_yes *
        p_temperature_yes *
        p_humidity_yes *
        p_wind_yes
    )


    # Probability for No

    p_outlook_no = probability(
        "Outlook", outlook, "No"
    )

    p_temperature_no = probability(
        "Temperature", temperature, "No"
    )

    p_humidity_no = probability(
        "Humidity", humidity, "No"
    )

    p_wind_no = probability(
        "Wind", wind, "No"
    )

    no_probability = (
        p_no *
        p_outlook_no *
        p_temperature_no *
        p_humidity_no *
        p_wind_no
    )


    # Choose the class with
    # higher probability

    if yes_probability > no_probability:

        return "Yes"

    else:

        return "No"


# ---------------------------------------
# STEP 7: Test the Classifier
# ---------------------------------------

correct = 0

print("\nPredictions")
print("-------------------")


for row in test_data:

    prediction = predict(
        row["Outlook"],
        row["Temperature"],
        row["Humidity"],
        row["Wind"]
    )

    actual = row["Play"]

    print(
        "Actual:",
        actual,
        " Predicted:",
        prediction
    )


    if prediction == actual:

        correct += 1


# ---------------------------------------
# STEP 8: Calculate Accuracy
# ---------------------------------------

total_test_records = len(test_data)

accuracy = (
    correct / total_test_records
) * 100


print("\nPerformance")
print("-------------------")

print(
    "Correct Predictions:",
    correct
)

print(
    "Total Test Records:",
    total_test_records
)

print(
    "Accuracy:",
    accuracy,
    "%"
)
