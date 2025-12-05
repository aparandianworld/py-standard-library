import urllib.request
import json


def main():
    endpoint = "https://jsonplaceholder.typicode.com/todos"

    try:
        with urllib.request.urlopen(endpoint) as response:
            if response.getcode() == 200:
                data = response.read().decode("utf-8")
                object_data = json.loads(data)
                with open("title.txt", "w") as fh:
                    for item in object_data:
                        fh.write(item["title"] + "\n")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
