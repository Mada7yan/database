import csv


def csv_dictreader(file_name):
    lines = []
    with open(file_name, "r") as f:
        for item in csv.DictReader(f):
            lines.append(item)
            # for key, value in item.items():
            #     print(key, value)
    return lines


def csv_reader(file_name):
    lines = []
    with open(file_name, "r") as f:
        content = csv.reader(f)
        for item in content:
            lines.append(item)
    return lines


if __name__ == "__main__":
    fname = "dummy_data/restaurant.csv"
    list_rows = csv_reader(fname)
    print(list_rows)
    dt_rows = csv_dictreader(fname)
    print(dt_rows)