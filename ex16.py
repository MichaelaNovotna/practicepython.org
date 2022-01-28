import random

seznam = "aábcčdeéěfghiíjklmnopqrřsštuvwxyýžAÁBCČDEÉĚFGHIÍJKLMNOPQRŘSŠTUVWXYÝZŽ0123456789?!@()%#"


def create_password_from_seznam(seznam):
    password = []
    password = "".join(random.choices(seznam, k=8))
    return password


print(create_password_from_seznam(seznam))
