import csv


def read_csv(file_path):

    data = []

    with open(file_path, newline="") as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            data.append(
                (row["username"], row["password"], row["debe_funcionar"] == "True", row["error_message"])
            )

    return data
