def get_user_input():
		plaintext = input("Enter Text: ")
		return plaintext
  
  
def get_key():
  key = input("Enter Key: ")
  return key


def cipher(plaintext, key):
  pass

def encrypt():
  plaintext = get_user_input()
  key = get_key()
  cipher(plaintext, key)


if __name__ == "__main__":
	encrypt()