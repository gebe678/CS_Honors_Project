# Going to use beautiful soup to parse the html data from the website
# to retrieve the html infomration we will use the requests python library

# alternatively using requests-html to take care of both tasks

# this script will use requests-html to take care of all the webscraping tasks.

import requests
from bs4 import BeautifulSoup as bs
import csv

def getHtml(url):
    """
    This function is responsible for retrieving html content from a webpage
    """

    # make a request to get the html from the server using the requests library (html is saved as bytes)
    r = requests.get(url)

    file = open("htmlout.txt", "r+")
    file.write(str(r.text))

    return r.content

def getSoupObject(file):
    
    with open(file) as file:
        soup = bs(file, "html.parser")

    return soup

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

def parseData(file):
    """
    This function uses beautiful soup to parse the data from the page
    """
    data_list = []
    data_row = []
    department = ""
    counter = 100

    soup = getSoupObject(file)
    
    for element in soup.find_all("td"):

        if element.has_attr("class") and element["class"][0] == "hdrDept":
            department = element.text.strip()

        elif (element.text.strip() == "Filled" or element.text.strip() == "Open") and department != "":
            data_row.append(department)
            data_row.append(element.text.strip())
            counter = 1

        elif counter < 10:
            data_row.append(element.text.strip())

        elif counter == 11:
            data_row.append(element.text.strip())
            data_list.append(data_row)
            data_row = []

        counter += 1
    return data_list

def createCSVData():
    """
    This function is responsible for creating the csv files for the data
    """
    headers = ["Department", "Status", "AVAIL/CAP/(WL)", "Course", "Course Title", "Credits", "Time", "Days", "Location", "Instructor", "Competency/GenEd", "Pre-Reqs/Comments"]
    url_list = []

    # get the urls for the data parsing from the urls.txt file
    urls = open("urls.txt", "r")
    
    for url in urls:
        url_list.append(url.strip())

    # loop through all of the pages to get info from
    for url in url_list:
        data = parseData(url)
        # open the csv file to write the data too
        csv_location = url
        csv_location = csv_location.replace(".html", ".csv")
        csv_file = open(csv_location, "w", newline="")

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)
        csv_writer.writerows(data)

    csv_file.close()

if __name__ == "__main__":

    createCSVData()
