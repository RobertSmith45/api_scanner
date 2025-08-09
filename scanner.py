#!/usr/bin/env python3
import requests
import argparse
import json
from config import API_KEY

def check_endpoint(url):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        r = requests.get(url, headers=headers, timeout=5)
        print(f"[+] {url} - {r.status_code}")
        try:
            print(json.dumps(r.json(), indent=2))
        except:
            pass
    except Exception as e:
        print(f"[-] {url} - Error: {e}")

def load_wordlist(path):
    with open(path, "r") as f:
        return [l.strip() for l in f if l.strip()]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True, help="Base URL (e.g. https://api.example.com)")
    parser.add_argument("-w", "--wordlist", default="wordlist.txt")
    args = parser.parse_args()
    endpoints = load_wordlist(args.wordlist)
    for e in endpoints:
        check_endpoint(args.url.rstrip('/') + '/' + e.lstrip('/'))
