import hashlib


def generate_password(text):
    hasher = hashlib.md5()

    text_bytes = text.encode('utf-8')

    hasher.update(text_bytes)

    password_hash = hasher.hexdigest()

    return password_hash


input_text = "Qwerty123!"
generated_password = generate_password(input_text)
print("Generated password:", generated_password)
