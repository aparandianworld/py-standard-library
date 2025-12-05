import csv

SAMPLE_SIZE = 1024


def csv_sniffer(file_path):
    if file_path == "":
        print("File path is empty")
        return

    try:
        with open(file_path, "r") as fh:
            dialect = csv.Sniffer().sniff(fh.read(SAMPLE_SIZE))
            fh.seek(0)
            has_header = csv.Sniffer().has_header(fh.read(SAMPLE_SIZE))
            fh.seek(0)
            print(f"Has header: {has_header}")

            print(f"Dialect: {dialect}")
            print(f"Delimiter: {dialect.delimiter}")
            print(f"Quotechar: {dialect.quotechar}")
            print(f"Quoting: {dialect.quoting}")
            print(f"Escapechar: {dialect.escapechar}")

    except Exception as e:
        print(f"Error: {e}")


def csv_reader(file_path):
    if file_path == "":
        print("File path is empty")
        return

    with open(file_path, "r") as fh:
        reader = csv.reader(fh)
        for row in reader:
            print(row)


file_path = "./sample_data.csv"
csv_sniffer(file_path)
csv_reader(file_path)
