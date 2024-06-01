import sys
import csv
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence = []
    labels = []
    cal = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'June': 5, 'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11}
    true_false = {'FALSE': 0, 'TRUE': 1}
    visitor = {'New_Visitor': 0, 'Returning_Visitor': 1, 'Other': 2}

    # Open csv file for reading
    with open(filename, 'r') as csvfile:
        # Create a csv file reader to read in floats and read the header row
        reader = csv.DictReader(csvfile)

        # Read row by row
        for row in reader:
            r = []

            # Fix formatting for each field
            r.append(int(row["Administrative"]))
            r.append(float(row["Administrative_Duration"]))
            r.append(int(row["Informational"]))
            r.append(float(row["Informational_Duration"]))
            r.append(int(row["ProductRelated"]))
            r.append(float(row["ProductRelated_Duration"]))
            r.append(float(row["BounceRates"]))
            r.append(float(row["ExitRates"]))
            r.append(float(row["PageValues"]))
            r.append(float(row["SpecialDay"]))
            r.append(int(cal[row["Month"]]))
            r.append(int(row["OperatingSystems"]))
            r.append(int(row["Browser"]))
            r.append(int(row["Region"]))
            r.append(int(row["TrafficType"]))
            r.append(int(visitor[row['VisitorType']]))
            r.append(int(true_false[row['Weekend']]))

            # Convert labels to integer
            labels.append(true_false[row['Revenue']])
            evidence.append(r)

    return evidence, labels


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    # Creat a KNN classifier and fit the data
    model = KNeighborsClassifier(n_neighbors=1).fit(evidence, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    n = len(labels)
    for i in range(n):
        if labels[i] == predictions[i] == 0:
            tn += 1
        elif labels[i] == predictions[i] == 1:
            tp += 1
        elif labels[i] == 0:
            fp += 1
        elif labels[i] == 1:
            fn += 1

    specificity = tn/(tn + fp)
    sensitivity = tp/(tp + fn)

    return sensitivity, specificity


if __name__ == "__main__":
    main()
