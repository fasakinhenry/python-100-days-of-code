alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(text, shift, direction):
  result = ""
  if direction == "decode":
    shift *= -1
  elif direction == "encode":
    shift = shift
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = (position + shift) % 26
      result += alphabet[new_position]
    else:
      result += char
  print(f"The {direction}d text is {result}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text, shift, direction)
