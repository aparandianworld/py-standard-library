import secrets
import string


def generate_reservation_code():
    # 6 uppercase letters with dash in the middle ABC-DEF
    # letters are allowed to repeat
    # uppercase letters only
    allowed_letters = string.ascii_uppercase
    allowed_chars = "-"
    allowed_length = 6

    reservation_code_p1 = "".join(
        secrets.choice(allowed_letters) for _ in range(0, allowed_length // 2)
    )
    reservation_code_mid = allowed_chars
    reservation_code_p2 = "".join(
        secrets.choice(allowed_letters) for _ in range(4, allowed_length + 1)
    )

    return reservation_code_p1 + reservation_code_mid + reservation_code_p2


def main():
    reservation_code = generate_reservation_code()
    print(f"Your reservation code is: {reservation_code}")


if __name__ == "__main__":
    main()
