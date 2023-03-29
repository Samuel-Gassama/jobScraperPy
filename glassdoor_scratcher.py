import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_job_listings(url):
    # Set up the WebDriver
    driver = webdriver.Chrome() # Add 'executable_path' parameter if needed: webdriver.Chrome(executable_path='/path/to/chromedriver')

    # Load the web page
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the job listings
    jobs = soup.find_all('li', {'class': 'react-job-listing'})

    if not jobs:
        print("No job listings found.")
        return

    for job in jobs:
        title = job.find('a', {'class': 'jobLink'})
        company = job.find('div', {'class': 'job-search-key-6is2u_1'})
        location = job.find('div', {'class': 'job-search-key-6is2u_2'})

        print('Title:', title.get_text(strip=True) if title else "N/A") #Not WORKING 
        print('Company:', company.get_text(strip=True) if company else "N/A") # Not WORKING 
        print('Location:', location.get_text(strip=True) if location else "N/A") # Not WORKING
        print('Link:', 'https://www.glassdoor.ca' + title['href'] if title else "N/A")
        print('---')

    # Close the WebDriver
    driver.quit()
    # replace the link of the base url with the link of the job you want to scrape and the website  
if __name__ == '__main__':
    base_url = 'https://www.glassdoor.ca/Job/toronto-on-canada-junior-developer-jobs-SRCH_IL.0,17_IC2281069_KO18,34.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=Junior%2520Developer%2520&typedLocation=Toronto%252C%2520ON%2520(Canada)&context=Jobs&dropdown=0'
    get_job_listings(base_url)
