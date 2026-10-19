import os
import http.server
import socketserver
import threading
import time
import json
from pathlib import Path

PORT = 8082
ID_DIR = Path.home() / "CZH/PrivateData/ID_Profiles"

print("\033[96m[+] CZH ELITE ID SYSTEM\033[0m")
alias = input("  Enter Hacker Alias: ").strip()

profile_file = ID_DIR / f"{alias}.json"
if not profile_file.exists():
    print("\033[91m  [✗] ID not found. Admin must issue it first using 'czh-issue-id'.\033[0m")
    exit(1)

with open(profile_file) as f:
    profile = json.load(f)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CZH ELITE ID - {profile['alias']}</title>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@600;800&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        :root {{
            --green: #00ff66;
            --blue: #00e5ff;
            --dark: #02060a;
            --panel: #040b14;
        }}
        body {{
            background-color: var(--dark);
            background-image: 
                radial-gradient(circle at 15% 50%, rgba(0, 255, 102, 0.08), transparent 25%),
                radial-gradient(circle at 85% 30%, rgba(0, 229, 255, 0.08), transparent 25%);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: 'Share Tech Mono', monospace;
            color: #fff;
            overflow: hidden;
        }}
        
        .btn-download {{
            background: transparent;
            color: var(--green);
            border: 1px solid var(--green);
            padding: 10px 25px;
            font-family: 'Orbitron', sans-serif;
            font-weight: 600;
            cursor: pointer;
            margin-bottom: 25px;
            transition: 0.3s;
            box-shadow: 0 0 10px rgba(0, 255, 102, 0.2);
            letter-spacing: 1px;
        }}
        .btn-download:hover {{
            background: var(--green);
            color: #000;
            box-shadow: 0 0 20px var(--green);
        }}

        .scene {{
            width: 95vw;
            max-width: 420px;
            aspect-ratio: 1.58; 
            perspective: 1200px;
            cursor: pointer;
        }}
        
        .card {{
            width: 100%;
            height: 100%;
            position: relative;
            transition: transform 0.7s cubic-bezier(0.4, 0.2, 0.2, 1);
            transform-style: preserve-3d;
        }}
        
        .card.is-flipped {{ transform: rotateY(180deg); }}
        
        .card-face {{
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            border-radius: 10px;
            overflow: hidden;
            padding: 15px;
            box-sizing: border-box;
            background: var(--panel);
            border: 2px solid var(--blue);
            box-shadow: 0 0 15px rgba(0, 229, 255, 0.3), inset 0 0 20px rgba(0, 229, 255, 0.1);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .card-back {{
            transform: rotateY(180deg);
            border-color: var(--green);
            box-shadow: 0 0 15px rgba(0, 255, 102, 0.3), inset 0 0 20px rgba(0, 255, 102, 0.1);
        }}

        /* Tech Grid Background */
        .tech-bg {{
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: 
                linear-gradient(rgba(0, 229, 255, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 229, 255, 0.05) 1px, transparent 1px);
            background-size: 15px 15px;
            z-index: 0;
            pointer-events: none;
        }}
        .card-back .tech-bg {{
            background-image: 
                linear-gradient(rgba(0, 255, 102, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 255, 102, 0.05) 1px, transparent 1px);
        }}

        /* FRONT SIDE */
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(0, 229, 255, 0.3);
            padding-bottom: 5px;
            z-index: 2;
        }}
        .logo-area {{
            font-family: 'Orbitron', sans-serif;
            font-weight: 800;
            font-size: 16px;
            color: #fff;
            letter-spacing: 2px;
            text-shadow: 0 0 8px var(--blue);
        }}
        .logo-area span {{ color: var(--green); }}
        .access-tag {{
            color: var(--green);
            font-size: 10px;
            border: 1px solid var(--green);
            padding: 2px 5px;
            border-radius: 3px;
            background: rgba(0, 255, 102, 0.1);
            letter-spacing: 1px;
        }}

        .main-body {{
            display: flex;
            z-index: 2;
            margin-top: 5px;
            flex-grow: 1;
        }}
        .photo-container {{
            width: 70px;
            height: 85px;
            border: 1px solid var(--blue);
            box-shadow: 0 0 10px rgba(0, 229, 255, 0.2);
            background: #000;
            overflow: hidden;
        }}
        .photo-container img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.9;
        }}
        .info-container {{
            margin-left: 15px;
            flex-grow: 1;
        }}
        .alias-text {{
            font-family: 'Orbitron', sans-serif;
            font-size: 20px;
            font-weight: 800;
            color: var(--green);
            margin: 0 0 2px 0;
            text-transform: uppercase;
            letter-spacing: 1px;
            text-shadow: 0 0 5px rgba(0,255,102,0.5);
        }}
        .real-name {{
            font-size: 11px;
            color: #a0b0c0;
            margin-bottom: 8px;
            letter-spacing: 1px;
            text-transform: uppercase;
        }}
        .data-row {{
            display: flex;
            font-size: 10px;
            margin-bottom: 3px;
        }}
        .data-label {{ color: var(--blue); width: 50px; }}
        .data-value {{ color: #fff; font-weight: bold; }}

        .footer {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            border-top: 1px solid rgba(0, 255, 102, 0.3);
            padding-top: 5px;
            z-index: 2;
        }}
        .signature-area {{
            font-size: 9px;
            color: #a0b0c0;
        }}
        .sig-text {{
            font-family: 'Brush Script MT', cursive;
            font-size: 22px;
            color: var(--blue);
            line-height: 1;
            text-shadow: 0 0 8px rgba(0, 229, 255, 0.6);
        }}
        .auth-title {{ color: var(--green); font-weight: bold; letter-spacing: 1px; }}
        
        .hologram {{
            width: 35px;
            height: 35px;
            border-radius: 50%;
            background: conic-gradient(from 0deg, var(--blue), var(--green), var(--blue));
            padding: 2px;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 0 10px rgba(0, 255, 102, 0.5);
        }}
        .hologram-inner {{
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: var(--dark);
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 8px;
            text-align: center;
            font-family: 'Orbitron', sans-serif;
            color: var(--green);
        }}

        /* BACK SIDE */
        .back-header {{
            text-align: center;
            font-family: 'Orbitron', sans-serif;
            font-size: 12px;
            font-weight: 800;
            color: var(--green);
            border-bottom: 1px dashed var(--green);
            padding-bottom: 5px;
            z-index: 2;
            text-shadow: 0 0 5px var(--green);
        }}
        .terms-text {{
            font-size: 8px;
            color: #b0c0d0;
            line-height: 1.4;
            z-index: 2;
            margin: 8px 0;
            padding-left: 8px;
            border-left: 2px solid var(--blue);
        }}
        .terms-text span {{ color: var(--blue); font-weight: bold; }}
        
        .barcode-area {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            z-index: 2;
        }}
        .barcode {{
            font-family: 'Libre Barcode 39', cursive;
            font-size: 38px;
            color: var(--green);
            line-height: 1;
        }}
        .founding-info {{
            font-size: 8px;
            color: var(--blue);
            text-align: right;
            line-height: 1.3;
        }}
    </style>
</head>
<body>
    <button class="btn-download" onclick="downloadCard()">[ DOWNLOAD ID CARD ]</button>
    
    <div class="scene" onclick="document.querySelector('.card').classList.toggle('is-flipped')">
        <div class="card" id="czh-id-card">
            
            <!-- FRONT SIDE -->
            <div class="card-face">
                <div class="tech-bg"></div>
                
                <div class="header">
                    <div class="logo-area">CZH<span>//</span>ELITE</div>
                    <div class="access-tag">VIP CLEARANCE</div>
                </div>
                
                <div class="main-body">
                    <div class="photo-container">
                        <img src="{profile['photo']}" crossorigin="anonymous">
                    </div>
                    <div class="info-container">
                        <h2 class="alias-text">{profile['alias']}</h2>
                        <div class="real-name">{profile['real_name']}</div>
                        
                        <div class="data-row">
                            <div class="data-label">ROLE:</div>
                            <div class="data-value">{profile['role'].upper()}</div>
                        </div>
                        <div class="data-row">
                            <div class="data-label">STATUS:</div>
                            <div class="data-value" style="color:var(--green);">ACTIVE & VERIFIED</div>
                        </div>
                        <div class="data-row">
                            <div class="data-label">SECTOR:</div>
                            <div class="data-value">WHITE HAT CYBER LAB</div>
                        </div>
                    </div>
                </div>
                
                <div class="footer">
                    <div class="signature-area">
                        <div class="auth-title">AUTHORIZED SIGNATORY</div>
                        <div class="sig-text">KHAN</div>
                        <div>CEO / FOUNDER</div>
                    </div>
                    <div class="hologram">
                        <div class="hologram-inner">CZH<br>SEC</div>
                    </div>
                </div>
            </div>

            <!-- BACK SIDE -->
            <div class="card-face card-back">
                <div class="tech-bg"></div>
                
                <div class="back-header">CZH ELITE PROTOCOL & TERMS</div>
                
                <div class="terms-text">
                    <span>01. AUTHORIZED ACCESS ONLY.</span> This credential is the property of Cipher Zero Hackers. Unauthorized use or duplication is strictly prohibited.<br>
                    <span>02. WHITE HAT MANDATE.</span> The holder must strictly adhere to ethical hacking principles. Any malicious activity will result in immediate revocation.<br>
                    <span>03. DATA PROTECTION.</span> All CZH tools, data, and member identities are classified. Do not share outside the network.
                </div>
                
                <div class="barcode-area">
                    <div class="barcode">*{profile['alias'].upper()}*</div>
                    <div class="founding-info">
                        FOUNDED BY<br>
                        <span style="color:var(--green); font-weight:bold;">AARHIV HACKERS</span><br>
                        EST. 2026
                    </div>
                </div>
            </div>
            
        </div>
    </div>

    <script>
        function downloadCard() {{
            const card = document.getElementById('czh-id-card');
            const isFlipped = card.classList.contains('is-flipped');
            if (isFlipped) card.classList.remove('is-flipped'); // Download front
            
            setTimeout(() => {{
                html2canvas(card, {{
                    backgroundColor: "#02060a",
                    scale: 3, // Ultra HD
                    useCORS: true
                }}).then(canvas => {{
                    const link = document.createElement('a');
                    link.download = 'CZH_ELITE_{profile['alias']}.png';
                    link.href = canvas.toDataURL('image/png');
                    link.click();
                    if (isFlipped) card.classList.add('is-flipped');
                }});
            }}, 400);
        }}
    </script>
</body>
</html>
"""

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))
    def log_message(self, format, *args): pass

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

print(f"\n\033[92m[✓] Elite ID Loaded Successfully!\033[0m")
print(f"\033[96m[!] Opening http://localhost:{PORT}\033[0m")

threading.Thread(target=start_server, daemon=True).start()
time.sleep(1)

os.system(f"termux-open-url http://localhost:{PORT} 2>/dev/null")

print("\n\033[93m[!] Press Ctrl+C to stop the server.\033[0m")
try:
    while True: time.sleep(1)
except KeyboardInterrupt:
    print("\n\033[91m[✗] Server stopped.\033[0m")
