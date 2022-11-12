import string

def get_user_input():
	plaintext = input("Enter Text: ")

	return plaintext


def get_key():
  try:
    key = int(input("Enter Key: "))
    return key
  except ValueError:
    print("Key should be a number:")
    get_key()


def get_function():
  desired_func = input("Do you want to encrypt or decrypt? [en/de]: ")
  
  return desired_func


def encrypt(plaintext, key):
  result = ""
  alphabet = string.ascii_lowercase
  for i in plaintext:
    if i in alphabet:
      letter_index = (alphabet.find(i) + key) % len(alphabet)

      result += alphabet[letter_index]
    else:
      result += i

  return result


def decrypt(plaintext, key):
  result = ""
  alphabet = string.ascii_lowercase
  for i in plaintext:
    if i in alphabet:
      letter_index = (alphabet.find(i) - key) % len(alphabet)

      result += alphabet[letter_index]
    else:
      result += i

  return result


def run_encryption():
  plaintext = get_user_input()
  key = get_key()
  desired_function = get_function()
  
  if desired_function == "en":
    print(encrypt(plaintext, key))
  elif desired_function == "de":
    print(decrypt(plaintext, key))
  else:
    print("Please choose between [en/de]: ")


if __name__ == "__main__":
	run_encryption()
