# Caesar cipher Encryption

The caesar cipher is a program invented by caesar to send encoded messages. The major aim of this program is to enable us to encode a text using a particular shift number and decode a text using the given shift number.

## How it works

The parties(people) who want to send each other encoded messages usually agree on a shift number. When the party receives the encoded message, they use the agreed shift number to decode the message.

To encode a message, each letter in the words are shifted to the right by the shift number.

Similarly, to decode a message each letter in the word are shifted to the left. By shifting we mean the letters change to the letter in the shift position away from the actual character.

## Example Encoding Input

Throughout the examples, we would be using a shift number of **5**

```
Hello
```

## Example Output

```
mjqqt
```

Each letter in the word "Hello" is shifted by 5 to the right when Encoding.

## Example Decoding Input

Let's say we give the encoded version of hello(mjqqt) to the decoder

```
mjqqt
```

## Example Decoding output

```
hello
```

## Considerations

There are some considerations that needs to be taken when creating the caesar cipher program. The precautions are as follows:

- We should be able to handle inputs that includes Capital letters. There are different ways of handling this. We can either convert all inputs of capital letters into lower case or create a seperate character set for Uppercase letters so uppercase letters can appear in the encoded or decoded output.
- The user experience of the app should be seamless and there should be adequate error validation
- The program should be able to handle shift numbers given by the user. An important consideration is the fact thata user can give a shift number that is greater than 26(letters of the alphabet). The best thing to do in that case is to use the modulus(%) operator to get an index that is below 26.
- Inputs or text with symbols should be handled and in this case, when the symbols passes through our caesar cipher program they remain unchanged.

## Project

- [Check out my Project solution here](./main.py)
