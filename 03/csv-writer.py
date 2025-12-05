import csv


def csv_writer(file_path):
    if file_path == "":
        print("Error: file path is empty.")
        return

    try:
        with open("output.csv", mode="w") as fh:
            csv_writer = csv.writer(fh)
            csv_writer.writerow(["id", "name", "email"])
            csv_writer.writerow([1, "Alice", "alice@example.com"])
            csv_writer.writerow([2, "Bob", "bob@example.com"])
            csv_writer.writerow([3, "Charlie", "charlie@example.com"])
    except Exception as e:
        print(f"Error: {e}")


file_path = "output.csv"
csv_writer(file_path)
