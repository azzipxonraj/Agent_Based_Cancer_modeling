import csv


def save_tumor_history(TUMOR_HISTORY, filename="tumor_history.csv"):

    with open(filename, 'w', newline='') as csvfile:
        tumor_list = [[tumor] for tumor in TUMOR_HISTORY]
        writer = csv.writer(csvfile)
        writer.writerows(tumor_list)


