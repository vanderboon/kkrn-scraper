import requests
from bs4 import BeautifulSoup

def getMaxPages(n: int, m: int) -> int:
    """Get the maximum number of pages for the program.
    
    n is the current page
    m is the max page
    
    """
    baseURI = 'http://kkrn.org/programs/the-piping-hour-with-steve-rook'

    # Grab the initial webpage
    try:
        response = requests.get(f"{baseURI}/page:{n}")
    except Exception as e:
        print(f"There was an error getting the {baseURI}\n{e}")

    # Find the maximum page listed in the pagination block
    soup = BeautifulSoup(response.text, 'html.parser')
    pages = soup.select('div.pagination-inner')
    spans = pages.select('span')
    for span in spans:
        print(span.text)

    return 'm'