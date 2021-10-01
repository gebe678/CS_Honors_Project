# Going to use beautiful soup to parse the html data from the website
# to retrieve the html infomration we will use the requests python library

# alternatively using requests-html to take care of both tasks

# this script will use requests-html to take care of all the webscraping tasks.

import requests
from bs4 import BeautifulSoup as bs

def getHtml(url):
    """
    This function is responsible for retrieving html content from a webpage
    """

    # make a request to get the html from the server using the requests library (html is saved as bytes)
    r = requests.get(url)

    return r.content

def getHtmlFromFile(file):
    """
    This function is responsible for reading several different urls from a list and returning the html content from the urls as a list
    """
    # variable to hold the html data
    html_data = []

    # open the file where the data is contianed
    file = open(file, "r")

    for data in file:
        # check to make sure the information is not a "comment"
        if data[0] != '#':
            # create a request for the html
            html_data.append(getHtml(data))

    file.close()

    # return the html array
    return html_data

def parseData():
    """
    This function uses beautiful soup to parse the data from the page
    """
    # gets the html data from the url's in the urls.txt file
    html_data = getHtmlFromFile("urls.txt")

    # create a new Beautiful Soup object called soup that parsed the data from the first url
    soup = bs(html_data[0], "html.parser")

    # get the body of the html
    body = soup.select_one("body")

    print(body)

if __name__ == "__main__":

    parseData()
