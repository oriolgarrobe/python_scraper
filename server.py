# Libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser
import time


def create_soup(url):
    """
    Function that takes as an input a url and returns a bs4.BeautifulSoup object.
    A bs4.BeautifulSoup object contains the HTML code of the given URL.
    """
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return BeautifulSoup(html, "html.parser")

def get_title(soup):
    """
    Function that takes a bs4.BeautifulSoup object and returns the title of the URL as string.
    """
    return soup.title.string

def get_body(soup, news_paper):
    """
    Function that takes as an input a bs4.BeautifulSoup object and the newspaper type and return the text
    of the article unprocessed.
    """
    if news_paper == "LV":
        result = soup.find("div", {"class":"article-modules"})
    return result

def process_body(result):
    """
    Function that takes as an input the unprocessed text of the article and formats it so it is easier to read.
    """
    body = ""
    for i in result.find_all("p"):
        body = body + "<p>" + i.getText() + "</p>"
    return body

def create_html_content(title, body):
    """
    Function that takes two strings (title, body) and creates a readable HTML content.
    """
    return f'<html> <h1> {title} </h1> <body> {body} </body> </html>'





if __name__ == "__main__":
    url = "https://www.lavanguardia.com/deportes/futbol/20210812/7658984/asamblea-clubes-aprueba-acuerdo-cvc-real-madrid-barca.html"
    news_paper = "LV"

    soup = create_soup(url)
    title = get_title(soup)
    body = get_body(soup, news_paper)
    processed_body = process_body(body)
    html_content = create_html_content(title, processed_body)

    with open("index.html", "w") as html_file:
        html_file.write(html_content)
        print("HTML created succesfully!")

    time.sleep(2)
    webbrowser.open_new_tab("index.html")
