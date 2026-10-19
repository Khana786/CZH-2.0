#!/usr/bin/env python3
import os
import sys
import time
import base64
import binascii

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ' ':'/' }

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(c.upper(), '') for c in text)

def morse_to_text(morse):
    morse = morse.replace('/', ' ')
    return ' '.join(list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(c)] for c in morse.split() if c in MORSE_CODE_DICT.values())

def caesar_cipher(text, shift, decode=False):
    result = ""
    if decode: shift = -shift
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def rot13(text):
    return caesar_cipher(text, 13)

def string_to_binary(text):
    return ' '.join(format(ord(c), '08b') for c in text)

def binary_to_string(binary):
    try:
        return ''.join(chr(int(b, 2)) for b in binary.split())
    except:
        return "Invalid Binary Code"

def menu():
    clear()
    print(f"{C}")
    print("      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ ")
    print("     ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗")
    print("     ██║     ██║██████╔╝███████║█████╗  ██████╔╝")
    print("     ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗")
    print("     ╚██████╗██║██║     ██║  ██║███████╗██║  ██║")
    print("      ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
    print(f"{NC}")
    print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
    print(f"{BG_R}{W}  ║  ☠  C Z H   C I P H E R   S U I T E   //   S E C R E T  ☠        ║{NC}")
    print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")
    
    print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
    print(f"  {C}│{NC} {Y}[1]{W} BASE64 ENCODE / DECODE                 {C}│{NC}")
    print(f"  {C}│{NC} {Y}[2]{W} MORSE CODE                             {C}│{NC}")
    print(f"  {C}│{NC} {Y}[3]{W} HEX ENCODE / DECODE                    {C}│{NC}")
    print(f"  {C}│{NC} {Y}[4]{W} BINARY ENCODE / DECODE                 {C}│{NC}")
    print(f"  {C}│{NC} {Y}[5]{W} CAESAR CIPHER (Army Style)             {C}│{NC}")
    print(f"  {C}│{NC} {Y}[6]{W} ROT13 CIPHER                           {C}│{NC}")
    print(f"  {C}├────────────────────────────────────────────┤{NC}")
    print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
    print(f"{C}  └────────────────────────────────────────────┘{NC}\n")

def main():
    while True:
        menu()
        choice = input(f"{R}  CZH-CIPHER ➜ {NC}").strip()
        
        if choice == "0" or choice == "00":
            print(f"\n{G}  [✓] CZH Cipher Suite closed. Stay Secret.{NC}")
            break
            
        text = input(f"\n{Y}  [?] Enter Text: {NC}")
        
        if choice == "1":
            try:
                if len(text) % 4 == 0 and any(c in text for c in "+/="):
                    print(f"\n{G}  [DECODED] {base64.b64decode(text).decode('utf-8')}{NC}")
                else:
                    print(f"\n{G}  [ENCODED] {base64.b64encode(text.encode()).decode('utf-8')}{NC}")
            except:
                print(f"{R}  [✗] Invalid Base64.{NC}")
                
        elif choice == "2":
            if "." in text or "-" in text:
                try: print(f"\n{G}  [DECODED] {morse_to_text(text)}{NC}")
                except: print(f"{R}  [✗] Invalid Morse Code.{NC}")
            else:
                print(f"\n{G}  [ENCODED] {text_to_morse(text)}{NC}")
                
        elif choice == "3":
            try:
                if all(c in "0123456789abcdefABCDEF" for c in text.replace(" ", "")):
                    print(f"\n{G}  [DECODED] {bytes.fromhex(text).decode('utf-8')}{NC}")
                else:
                    print(f"\n{G}  [ENCODED] {text.encode().hex()}{NC}")
            except:
                print(f"{R}  [✗] Invalid Hex.{NC}")
                
        elif choice == "4":
            if all(c in "01 " for c in text):
                print(f"\n{G}  [DECODED] {binary_to_string(text)}{NC}")
            else:
                print(f"\n{G}  [ENCODED] {string_to_binary(text)}{NC}")
                
        elif choice == "5":
            try:
                shift = int(input(f"{Y}  [?] Enter shift number (1-25): {NC}"))
                mode = input(f"{Y}  [?] Encode or Decode? (e/d): {NC}").lower()
                is_decode = (mode == 'd')
                print(f"\n{G}  [RESULT] {caesar_cipher(text, shift, is_decode)}{NC}")
            except:
                print(f"{R}  [✗] Invalid shift number.{NC}")
                
        elif choice == "6":
            print(f"\n{G}  [RESULT] {rot13(text)}{NC}")
            
        else:
            print(f"{R}  [✗] Invalid option.{NC}")
            
        input(f"\n{C}  Press Enter to return...{NC}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
