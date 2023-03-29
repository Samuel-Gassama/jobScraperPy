import time
import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver

def create_database():
    conn = sqlite3.connect('job_listings.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS job_listings
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       link TEXT UNIQUE)''')
    conn.commit()
    return conn

def save_job_to_database(conn, job_data):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO job_listings (title, company, location, link) VALUES (?, ?, ?, ?)",
                       (job_data['title'], job_data['company'], job_data['location'], job_data['link']))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def get_job_listings(url, conn):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    jobs = soup.find_all('li', {'class': 'react-job-listing'})

    if not jobs:
        print("No job listings found.")
        return

    job_listings = []

    for job in jobs:
        title = job.find('a', {'class': 'jobLink'})
        company = job.find('div', {'class': 'jobHeader'})
        location = job.find('span', {'class': 'loc'})

        job_data = {
            'title': title.get_text(strip=True) if title else "N/A",
            'company': company.get_text(strip=True) if company else "N/A",
            'location': location.get_text(strip=True) if location else "N/A",
            'link': 'https://www.glassdoor.ca' + title['href'] if title else "N/A",
        }
        
        if save_job_to_database(conn, job_data):
            job_listings.append(job_data)

    driver.quit()
    return job_listings

if __name__ == '__main__':
    base_url = 'https://www.glassdoor.ca/Job/toronto-on-canada-junior-developer-jobs-SRCH_IL.0,17_IC2281069_KO18,34.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=Junior%2520Developer%2520&typedLocation=Toronto%252C%2520ON%2520(Canada)&context=Jobs&dropdown=0'
    
    conn = create_database()
    job_listings = get_job_listings(base_url, conn)
    
    for job in job_listings:
        print('Title:', job['title'])
        print('Company:', job['company'])
        print('Location:', job['location'])
        print('Link:', job['link'])
        print('---')

    conn.close()
