#!/usr/bin/env python3


def main():
    test_content = "Che guevara was cheeky while eating quiche"
    test_string = "che"
    count = 0

    test_content_list = test_content.lower().split()
    test_string_lower = test_string.lower()

    for word in test_content_list:
        if test_string_lower == word or test_string_lower in word:
            print("Found")
            count += 1

    if count == 0:
        print("Not Found")

    print("Count: ", count)
    print("Count: ", test_content.lower().count(test_string_lower))


if __name__ == "__main__":
    main()
