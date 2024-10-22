# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:42:17 2024

@author: JHarris
"""

alphabet = [
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
]


def caesar(original_text, shift_amount, encode_or_decode):
    output_text=""
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "decode":
                shift_amount *= -1
                
            new_letter = alphabet.index(letter) + shift_amount
            
            new_letter %= len(alphabet)
            output_text += alphabet[new_letter]    
    print(f"Here is the {encode_or_decode}d result:{output_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to excrypt, type 'decode' to decrypt: \n").lower()
    text = input("type your message: \n")
    shift = int(input("Type the shift number: \n"))
    caesar(text,shift,direction)
    restart =  input("Type 'yes' if you want to continue. Otherwise type 'no'.\n")
    if restart == "no":
       should_continue = False
       print("Goodbye")

























