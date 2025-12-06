import random
import secrets
import string


def generate_temp_password():
    num_chars = 8
    potential_chars = string.ascii_letters + string.digits + "@#$%^()/"
    password = "".join(secrets.choice(potential_chars) for _ in range(num_chars))
    return password


def generate_strong_password():
    num_chars = 16
    potential_chars = string.ascii_letters + string.digits + "@#$%^()/"
    password = "".join(secrets.choice(potential_chars) for _ in range(num_chars - 2))
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password_list = random.sample(password, k=len(password))
    random.shuffle(password_list)
    return "".join(password_list)


def main():
    password = generate_temp_password()
    strong_password = generate_strong_password()
    print(f"Your temporary password is: {password}")
    print(f"Your strong password is: {strong_password}")


if __name__ == "__main__":
    main()
