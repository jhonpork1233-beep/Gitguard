#!/usr/bin/env python3
# GitGuard — Enhanced .git/ Folder Scanner
import requests
import sys

def scan_git(domain):
    git_files = ['.git/HEAD', '.git/config', '.git/index']
    protocols = ['http://', 'https://']
    for protocol in protocols:
        for git_file in git_files:
            url = f"{protocol}{domain}/{git_file}"
            try:
                r = requests.get(url, timeout=3, allow_redirects=False)
                if r.status_code == 200:
                    print(f"[+] Exposed: {url}")
                    return  # Report first found exposure, exit early
            except requests.RequestException:
                continue
    print(f"[-] No .git exposure found on {domain}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gitguard.py <domain.com>")
        sys.exit(1)
    scan_git(sys.argv[1].strip())
