# TODO-7: IMPORT AND PRINT THE LOFO FROM art.py whem the program starts.
import art
print(art.logo)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# TODO-8:What happens if the user enters a number/symbol/space?


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text forwaeds in the alphabet by the shift amount and print the encrpted text.
# hello 2

# def encrypt(original_text, shift_amount):
#     cipher_text = "" 

#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount 
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position] 
#     print(f"here is the encoded result: {cipher_text}")

# TODO-4: What happens if you try to shift z forwards by 9? can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. you should br able to test the code and encrpt a message.

# TODO-4: CREATE a function called 'decryt[pt()' that takes 'original_text' and 'shift_amount' as inputs.
# def decrypt(original_text, shift_amount):
#     output_text = "" 

#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount 
#         shifted_position %= len(alphabet) 
#         output_text += alphabet[shifted_position] 
#     print(f"here is the encoded result: {output_text}")
# TODO-5: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet by the shift amount and print thr decrypted text.
# TODO-6: Cobime the 'encrpt()' and 'decrpt()' function into one function called 'caesar()'.
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
                shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter 
        else:
             shifted_position = alphabet.index(letter) + shift_amount 
             shifted_position %= len(alphabet) 
             output_text += alphabet[shifted_position] 
    print(f"here is the {encode_or_decode}d result: {output_text}")
#  TODO-9: CAN YOU GIVE figure out a way to restart the cipher program?

should_cotinue = True

while should_cotinue:

    direction = input("type 'encode' to encryt, type 'decode' to decrypt:\n").lower()
    text = input("type your message:\n").lower()
    shift = int(input("type the shift number:\n"))


caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)

restart = input("type 'yes' if you want to go again. otherwise, type 'no'.\n").lower()
if restart == "no":
    should_cotinue = False
    print("goodbye")

# decrypt(original_text=text,shift_amount=shift)
# encrypt(original_text=text,shift_amount=shift)
# use the value of the user chosen 'direction' variable to determine which functionality to use.
# encrpt(original_text=text, shift_amount=shift)