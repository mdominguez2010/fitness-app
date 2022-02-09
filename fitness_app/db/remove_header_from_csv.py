import csv

FILENAME = "weight.csv"
#FILENAME = "WorkoutExport.csv"

def remove_header_from_csv(filename):
    """
    Removes first row from csv file
    """
    # Open csv file
    file = open(FILENAME)
    csvreader = csv.reader(file)

    # Extract data
    rows = []
    for row in csvreader:
        rows.append(row)
    header = rows[0]
    data = rows[1:]

    # Close file
    file.close()

    # Write the rows data into the file
    with open(FILENAME, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

    # Confirm written file
    file = open(FILENAME)
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)

    # print(rows[:10])

    file.close()

remove_header_from_csv(filename=FILENAME)