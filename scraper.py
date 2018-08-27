import argparse
import requests
import re
import unicodedata

def scrape(website):
    r = requests.get(website)
    website_content = r.text
    urls = re.findall(r"https\S+?(?=\")", website_content)
    emails = re.findall(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", website_content)
    phone_numbers = re.findall(r"\d\d\d-\d\d\d-\d\d\d\d", website_content)
    print "URLs"
    for url in urls:
        print url
    print "Emails"
    for email in emails:
        print email
    print "Phone Numbers"
    for num in phone_numbers:
        print num

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("web", type=str, help="The web address you would like to scrape")
    args = parser.parse_args()
    scrape(args.web)

if __name__ == "__main__":
    main()