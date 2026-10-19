#!/usr/bin/env python3
import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("\033[91m[✗] Pillow library not installed. Run: pkg install python-pillow\033[0m")
    sys.exit(1)

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; NC='\033[0m'
DELIMITER = "[END]" # Simple delimiter

def hide_message(image_path, message, output_path):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')
        encoded = img.copy()
        width, height = img.size
        
        full_message = message + DELIMITER
        binary_msg = ''.join(format(b, '08b') for b in full_message.encode('utf-8'))
        msg_len = len(binary_msg)
        
        max_capacity = width * height * 3
        if msg_len > max_capacity:
            return False, f"Message too long. Max {max_capacity // 8} chars."
        
        data_index = 0
        for y in range(height):
            for x in range(width):
                if data_index >= msg_len: break
                r, g, b = img.getpixel((x, y))
                
                if data_index < msg_len:
                    r = (r & ~1) | int(binary_msg[data_index]); data_index += 1
                if data_index < msg_len:
                    g = (g & ~1) | int(binary_msg[data_index]); data_index += 1
                if data_index < msg_len:
                    b = (b & ~1) | int(binary_msg[data_index]); data_index += 1
                    
                encoded.putpixel((x, y), (r, g, b))
            if data_index >= msg_len: break
                
        encoded.save(output_path, "PNG")
        return True, output_path
    except Exception as e:
        return False, str(e)

def extract_message(image_path):
    try:
        img = Image.open(image_path).convert('RGB')
        width, height = img.size
        
        binary_bits = []
        # Read bits from image
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                binary_bits.extend([r & 1, g & 1, b & 1])
        
        # Convert bits to bytes
        byte_array = bytearray()
        for i in range(0, len(binary_bits), 8):
            if i + 8 <= len(binary_bits):
                byte_val = 0
                for bit in binary_bits[i:i+8]:
                    byte_val = (byte_val << 1) | bit
                byte_array.append(byte_val)
                
        extracted = byte_array.decode('utf-8', errors='ignore')
        
        if DELIMITER in extracted:
            return True, extracted.split(DELIMITER)[0]
        return False, "No hidden CZH message found in this image."
    except Exception as e:
        return False, str(e)

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_file_path():
    raw = input(f"\n{Y}  [?] Enter image path (e.g., /sdcard/stego/photo.jpg): {NC}").strip()
    if not raw: return None
    path = Path(os.path.expanduser(raw))
    if not path.is_file():
        print(f"{R}  [✗] File not found. Please check the path!{NC}")
        input(f"{C}  Press Enter to try again...{NC}")
        return None
    return path

def main():
    while True:
        clear()
        print(f"{R}")
        print("      ███████╗████████╗███████╗ ██████╗  ██████╗ ")
        print("      ██╔════╝╚══██╔══╝██╔════╝██╔════╝ ██╔═══██╗")
        print("      ███████╗   ██║   █████╗  ██║  ███╗██║   ██║")
        print("      ╚════██║   ██║   ██╔══╝  ██║   ██║██║   ██║")
        print("      ███████║   ██║   ███████╗╚██████╔╝╚██████╔╝")
        print("      ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ")
        print(f"{NC}")
        print(f"{C}")
        print("      V A U L T   //   H I D E   Y O U R   S E C R E T S")
        print(f"{NC}")
        print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
        print(f"  ║  ☠  C Z H   S T E G A N O G R A P H Y   V A U L T  ☠            ║")
        print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")
        
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} HIDE MESSAGE IN IMAGE                  {C}│{NC}")
        print(f"  {C}│{NC} {Y}[2]{W} EXTRACT MESSAGE FROM IMAGE             {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")
        
        choice = input(f"{R}  CZH-STEGO ➜ {NC}").strip()
        
        if choice == "1":
            path = get_file_path()
            if not path: continue
            
            print(f"\n{Y}  [?] Enter your secret message (Type END on a new line to finish):{NC}")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == "END": break
                lines.append(line)
            message = "\n".join(lines)
            
            if not message:
                print(f"\n{R}  [✗] Message is empty.{NC}")
                input(f"{C}  Press Enter...{NC}")
                continue
                
            out_name = f"czh_stego_{path.stem}.png"
            output_path = path.parent / out_name
            
            print(f"\n{C}  [*] Hiding message inside image...{NC}")
            success, result = hide_message(str(path), message, str(output_path))
            
            if success:
                print(f"\n{G}  [✓] SUCCESS! Hidden image saved to:{NC}")
                print(f"  {C}{output_path}{NC}")
                
                # Auto-Verify
                print(f"{Y}  [*] Auto-Verifying extracted message...{NC}")
                verify_success, verify_msg = extract_message(str(output_path))
                if verify_success and verify_msg == message:
                     print(f"{G}  [✓] VERIFICATION PASSED! Message is safely hidden.{NC}")
                else:
                     print(f"{R}  [✗] VERIFICATION FAILED! Something went wrong.{NC}")

            else:
                print(f"\n{R}  [✗] Failed: {result}{NC}")
            input(f"\n{C}  Press Enter to return...{NC}")
            
        elif choice == "2":
            path = get_file_path()
            if not path: continue
            
            print(f"\n{C}  [*] Scanning image for hidden data...{NC}")
            success, result = extract_message(str(path))
            
            if success:
                print(f"\n{G}  [✓] MESSAGE EXTRACTED:{NC}")
                print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
                for line in result.split("\n"):
                    print(f"  {W}{line}{NC}")
                print(f"{C}  └────────────────────────────────────────────┘{NC}")
            else:
                print(f"\n{R}  [✗] {result}{NC}")
            input(f"\n{C}  Press Enter to return...{NC}")
            
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH Steganography Vault closed. Stay Secret.{NC}")
            break
        else:
            import time
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
