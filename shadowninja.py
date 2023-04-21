#!/usr/bin/env python3
import argparse
import shodan
import ipaddress

def shodan_scan(ip):
    api_key = "your-api-key"
    api = shodan.Shodan(api_key)
    try:
        results = api.host(ip)
        print("-" * 60)
        print("IP: {}".format(ip))
        print("Organization: {}".format(results.get("org", "n/a")))
        print("Operating System: {}".format(results.get("os", "n/a")))
        for item in results["data"]:
            print("{}\n".format(item["data"]))
            with open("{}_results.txt".format(ip), "a") as f:
                f.write("{}\n".format(item["data"]))
    except shodan.APIError as e:
        print("Error: {}".format(e))

def main():
    parser = argparse.ArgumentParser(description="Shodan Ninja - A tool for scanning IPs with Shodan by SU6HAN 1BN WAS1M")
    parser.add_argument("ip_range", type=str, help="The IP range to scan, in CIDR notation (e.g. 192.168.0.0/24)")
    parser.add_argument("-v", "--version", action="version", version="Shodan Ninja v1.0")
    args = parser.parse_args()

    ip_range = ipaddress.ip_network(args.ip_range, strict=False)

    for ip in ip_range:
        shodan_scan(str(ip))

if __name__ == "__main__":
    print("""
 ____  _   _    _    ____   _____        __  _   _ ___ _   _     _   _
/ ___|| | | |  / \  |  _ \ / _ \ \      / / | \ | |_ _| \ | |   | | / \   
\___ \| |_| | / _ \ | | | | | | \ \ /\ / /  |  \| || ||  \| |_  | |/ _ \  
 ___) |  _  |/ ___ \| |_| | |_| |\ V  V /   | |\  || || |\  | |_| / ___ \ 
|____/|_| |_/_/   \_\____/ \___/  \_/\_/    |_| \_|___|_| \_|\___/_/   \_\ 

    Shadow Ninja - A tool for scanning IPs with Shodan by SU6HAN 1BN WAS1M
    """)
    main()
