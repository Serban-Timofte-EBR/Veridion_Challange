import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def readURLs(file):
    df = pd.read_csv(file)
    return df['max(page)']

def crawlPage(link):
    try:
        response = requests.get(link, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    
    except requests.exceptions.RequestException as e:
        print(f"Error accessing URL - {link} - error: {e}")
        return None
    
def crawlAllPages(file, output):
    links = readURLs(file)
    with open(output, 'w') as outFile:
        for link in tqdm(links):
            pageContent = crawlPage(link)
            if pageContent:
                outFile.write(pageContent + '\n---PAGE BREAK---\n')
            else:
                outFile.write(f"Error accessing URL - {link}\n---PAGE BREAK---\n")

# if __name__ == "__main__":
csvPath = 'data/furniture_stores_pages.csv'
outputPath = 'data/output_furniture_stores_pages.txt'
crawlAllPages(csvPath, outputPath)