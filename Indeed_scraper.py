import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_job_listings(url):
    user_agent = UserAgent()
    headers = {
        "User-Agent": user_agent.random
    }
    
    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Error: Unable to fetch the web page (Status code: {response.status_code})")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all('div', {'class': 'jobsearch-SerpJobCard'})

        if not jobs:
            print("No job listings found.")
            return

        for job in jobs:
            title = job.find('a', {'class': 'jobtitle'})
            company = job.find('span', {'class': 'company'})
            location = job.find('span', {'class': 'location'})

            print('Title:', title.get_text(strip=True) if title else "N/A")
            print('Company:', company.get_text(strip=True) if company else "N/A")
            print('Location:', location.get_text(strip=True) if location else "N/A")
            print('---')

    except Exception as e:
        print(f"An error occurred while fetching job listings: {e}")

if __name__ == '__main__':
    base_url = 'https://www.glassdoor.ca/Job/toronto-on-canada-junior-developer-jobs-SRCH_IL.0,17_IC2281069_KO18,34.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=Junior%2520Developer%2520&typedLocation=Toronto%252C%2520ON%2520(Canada)&context=Jobs&dropdown=0'
    get_job_listings(base_url)
