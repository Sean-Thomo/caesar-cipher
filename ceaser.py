import string

def get_user_input():
	plaintext = input("Enter Text: ")

	return plaintext


def get_key():
  key = int(input("Enter Key: "))

  return key


def encrypt(plaintext, key):
  result = ""
  alphabet = string.ascii_lowercase
  for i in plaintext:
    if i in alphabet:
      letter_index = (alphabet.find(i) + key) % len(alphabet)

      result += alphabet[letter_index]


  return result


def run_encryption():
  plaintext = get_user_input()
  key = get_key()
  print(encrypt(plaintext, key))


if __name__ == "__main__":
	run_encryption()
# qrvhdfdghpb
