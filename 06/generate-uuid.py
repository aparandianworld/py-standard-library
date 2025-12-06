import uuid


def generate_uuid():
    return uuid.uuid4()


def generate_uuid_hex():
    return generate_uuid().hex


def geenrate_uuid_urn():
    return generate_uuid().urn


def main():
    print(f"UUID(4): {generate_uuid()}")
    print(f"UUID(4) Hex: {generate_uuid_hex()}")
    print(f"UUID(4) URN: {geenrate_uuid_urn()}")


if __name__ == "__main__":
    main()
