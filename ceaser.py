import string

def get_user_input():
	plaintext = input("Enter Text: ")
	return plaintext


def get_key():
  key = int(input("Enter Key: "))
  return key


def cipher(plaintext, key):
  cipher_text = ""
  alphabet = string.ascii_lowercase
  shifted_alphabet = string.ascii_lowercase[key:] + string.ascii_lowercase[0:key]
  key_value_alphabet = {key: value for key, value in zip(alphabet, shifted_alphabet)}
  for i in plaintext:
    cipher_char = key_value_alphabet[i]
    cipher_text += cipher_char

  print(cipher_text)


def encrypt():
  plaintext = get_user_input()
  key = get_key()
  cipher(plaintext, key)


if __name__ == "__main__":
	encrypt()