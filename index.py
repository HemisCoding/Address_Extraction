import re
import requests
from bs4 import BeautifulSoup

def extract_postcode(url):
    # make a request to the website
    page = requests.get(url)

    # parse the HTML content
    soup = BeautifulSoup(page.content, "html.parser")

    # find the postcode using regular expressions
    postcode_pattern = re.compile(r'\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b')
    postcode = postcode_pattern.search(soup.text)
    if postcode:
        return postcode.group(0)
    else:
        return None

# list of websites to extract the postcode from
websites = [
    "https://www.birdbrand.co.uk/",
    "https://thorntonlodgenorthyorkshire.co.uk/",
    "https://www.mackay.co.uk/"
]

# extract the postcode from each website
for website in websites:
    postcode = extract_postcode(website)
    if postcode:
        print(f"Postcode from {website}: {postcode}")
    else:
        print(f"Postcode not found for {website}")







