#!/usr/bin/env python3
import os
import sys
import time
from pathlib import Path

try:
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
except ImportError:
    print("\033[91m[✗] Pillow library not installed. Run: pkg install python-pillow\033[0m")
    sys.exit(1)

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'
DELIMITER = "[END]"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# --- STEGANOGRAPHY ---
def hide_message(image_path, message, output_path):
    try:
        img = Image.open(image_path).convert('RGB')
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
        
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                binary_bits.extend([r & 1, g & 1, b & 1])
        
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

# --- EXIF FORENSICS ---
def convert_to_degrees(value):
    d = float(value[0]); m = float(value[1]); s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)

def show_exif(image_path):
    clear()
    print(f"{C}  [*] Analyzing Image Metadata (EXIF)...{NC}")
    time.sleep(0.5)
    try:
        img = Image.open(image_path)
        exifdata = img.getexif()
        
        if not exifdata:
            print(f"\n{R}  [!] No EXIF data found. (Maybe downloaded from WhatsApp/Insta).{NC}")
            input(f"\n{C}  Press Enter to return...{NC}")
            return

        print(f"\n{G}  ┌───[ G E N E R A L   I N F O ]──────────────────────────────────┐{NC}")
        for tag_id, value in exifdata.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag in ["Make", "Model", "DateTime", "Software", "Artist"]:
                print(f"  {W}▶ {tag:<12} : {C}{value}{NC}")
        print(f"{G}  └──────────────────────────────────────────────────────────────┘{NC}\n")

        if 34853 in exifdata:
            gps_info = exifdata[34853]
            gps_data = {GPSTAGS.get(k, k): v for k, v in gps_info.items()}

            if "GPSLatitude" in gps_data and "GPSLongitude" in gps_data:
                lat = convert_to_degrees(gps_data["GPSLatitude"])
                lon = convert_to_degrees(gps_data["GPSLongitude"])
                if gps_data.get("GPSLatitudeRef") == "S": lat = -lat
                if gps_data.get("GPSLongitudeRef") == "W": lon = -lon
                
                maps_link = f"https://www.google.com/maps?q={lat},{lon}"
                
                print(f"{R}  ┌───[ 🚨 G P S   L O C A T I O N   F O U N D 🚨 ]─────────────────┐{NC}")
                print(f"  {W}▶ Latitude  : {R}{lat}{NC}")
                print(f"  {W}▶ Longitude : {R}{lon}{NC}")
                print(f"  {W}▶ Maps Link : {C}{maps_link}{NC}")
                print(f"{R}  └──────────────────────────────────────────────────────────────┘{NC}\n")
                os.system(f"termux-open-url '{maps_link}' 2>/dev/null")
        else:
            print(f"{Y}  [!] No GPS Location data found in this image.{NC}")

    except Exception as e:
        print(f"\n{R}  [✗] Error reading image: {e}{NC}")

    print("")
    input(f"{C}  Press Enter to return...{NC}")

# --- UI / MENU ---
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
        print("      ██████╗███████╗██╗  ██╗")
        print("     ██╔════╝╚══███╔╝██║  ██║")
        print("     ██║       ███╔╝ ███████║")
        print("     ██║      ███╔╝  ██╔══██║")
        print("     ╚██████╗███████╗██║  ██║")
        print("      ╚═════╝╚══════╝╚═╝  ╚═╝")
        print(f"{NC}")
        print(f"{C}")
        print("      F O R E N S I C S   //   S T E G O   &   E X I F")
        print(f"{NC}")
        print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
        print(f"{BG_R}{W}  ║  ☠  C Z H   I M A G E   F O R E N S I C S  ☠                    ║{NC}")
        print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")
        
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} HIDE SECRET IN IMAGE (Stego)          {C}│{NC}")
        print(f"  {C}│{NC} {Y}[2]{W} EXTRACT MESSAGE FROM IMAGE (Stego)    {C}│{NC}")
        print(f"  {C}│{NC} {G}[3]{W} VIEW IMAGE FORENSICS (EXIF/GPS)       {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")
        
        choice = input(f"{R}  CZH-FORENSICS ➜ {NC}").strip()
        
        if choice == "1":
            path = get_file_path()
            if not path: continue
            print(f"\n{Y}  [?] Enter secret message (Type END on new line):{NC}")
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
                print(f"\n{G}  [✓] SUCCESS! Saved to: {C}{output_path}{NC}")
                print(f"{Y}  [*] Auto-Verifying...{NC}")
                v_succ, v_msg = extract_message(str(output_path))
                if v_succ and v_msg == message:
                     print(f"{G}  [✓] VERIFICATION PASSED!{NC}")
                else:
                     print(f"{R}  [✗] VERIFICATION FAILED!{NC}")
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
                for line in result.split("\n"): print(f"  {W}{line}{NC}")
                print(f"{C}  └────────────────────────────────────────────┘{NC}")
            else:
                print(f"\n{R}  [✗] {result}{NC}")
            input(f"\n{C}  Press Enter to return...{NC}")
            
        elif choice == "3":
            path = get_file_path()
            if path:
                show_exif(str(path))
                
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH Image Forensics closed.{NC}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
