from calendar import c
import secrets
import string


def generate_temp_password(num_chars=8):
    potential_chars = string.ascii_letters + string.digits + "@#$%^()/"
    password = "".join(secrets.choice(potential_chars) for _ in range(num_chars))
    return password


def main():
    print(f"Enter the number of characters for the password: ", end="")
    num_chars = int(input())
    if num_chars < 0:
        print("Number of characters cannot be negative.")
        return
    if num_chars < 8:
        print("Number of characters must be at least 8.")
        return
    password = generate_temp_password(num_chars)
    if password:
        print(f"Your temporary password is: {password}")


if __name__ == "__main__":
    main()
c
