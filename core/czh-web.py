#!/usr/bin/env python3
import http.server
import socketserver
import urllib.parse
import os
import json
from pathlib import Path

HOME = Path.home()
PRIVATE = HOME / "CZH/PrivateData"
MEMBERS_DB = PRIVATE / "Members/members.db"
REPORTS_DB = PRIVATE / "BugBounty/reports.db"

PORT = 8081

class CZHDashboardHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            # Read Members
            members_html = ""
            if MEMBERS_DB.exists():
                with open(MEMBERS_DB, "r") as f:
                    for line in f:
                        parts = line.strip().split(":")
                        if len(parts) >= 5:
                            members_html += f"<tr><td>{parts[0]}</td><td>{parts[2]}</td><td>{parts[3]}</td><td>{parts[4]}</td></tr>"
            
            # Read Reports
            reports_html = ""
            if REPORTS_DB.exists():
                with open(REPORTS_DB, "r") as f:
                    for line in f:
                        parts = line.strip().split("|")
                        if len(parts) >= 7:
                            status_class = parts[5].lower()
                            reports_html += f"<tr class='{status_class}'><td>{parts[0]}</td><td>{parts[1]}</td><td>{parts[2]}</td><td>{parts[4]}</td><td>{parts[5]}</td></tr>"

            # HTML Design
            html = f"""<!DOCTYPE html>
<html>
<head>
    <title>CZH Web Dashboard</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ background-color: #000; color: #00ffcc; font-family: monospace; padding: 20px; }}
        h1 {{ color: #ff0033; text-shadow: 0 0 10px #ff0033; text-align: center; border-bottom: 2px solid #ff0033; padding-bottom: 10px;}}
        h2 {{ color: #ffcc00; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 30px; font-size: 14px; }}
        th, td {{ border: 1px solid #00ffcc; padding: 8px; text-align: left; }}
        th {{ background-color: #003333; color: #fff; }}
        .pending {{ color: yellow; }}
        .accepted {{ color: #00ff00; }}
        .rejected {{ color: #ff0000; }}
        .container {{ border: 2px solid #00ffcc; padding: 15px; border-radius: 10px; box-shadow: 0 0 15px #00ffcc; }}
        .header-status {{ text-align: center; color: #00ff00; margin-bottom: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>☠ CZH WEB DASHBOARD ☠</h1>
        <div class="header-status">[ SYSTEM ONLINE // CIPHER ZERO HACKERS ]</div>
        
        <h2>[+] REGISTERED MEMBERS</h2>
        <table>
            <tr><th>ALIAS</th><th>ROLE</th><th>JOINED</th><th>POINTS</th></tr>
            {members_html if members_html else "<tr><td colspan='4'>No members found.</td></tr>"}
        </table>

        <h2>[+] BUG BOUNTY REPORTS</h2>
        <table>
            <tr><th>ID</th><th>ALIAS</th><th>TARGET</th><th>SEVERITY</th><th>STATUS</th></tr>
            {reports_html if reports_html else "<tr><td colspan='5'>No reports found.</td></tr>"}
        </table>
        
        <div class="header-status">[ SESSION MONITORED BY AARHIV HACKERS ]</div>
    </div>
</body>
</html>"""
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_error(404, "File not found")

def run():
    os.system("clear")
    print("\033[96m")
    print("==================================================")
    print("        ☠  CZH WEB DASHBOARD SERVER  ☠")
    print("==================================================")
    print("\033[0m")
    print(f"\033[92m[+] Server running at: http://localhost:{PORT}\033[0m")
    print("\033[93m[!] Open this URL in your mobile browser.\033[0m")
    print("\033[91m[!] Press Ctrl+C to stop the server.\033[0m\n")
    
    with socketserver.TCPServer(("", PORT), CZHDashboardHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\033[91m[✗] Server stopped.\033[0m")
            os._exit(0)

if __name__ == "__main__":
    run()
