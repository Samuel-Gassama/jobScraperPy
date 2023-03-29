# jobScraperPy

#Job Scraper

This repository contains scripts for scraping job listings for junior developer positions in Toronto using Python. The scripts make use of requests, BeautifulSoup, and Selenium to extract job listing information from Indeed and Glassdoor.

#Prerequisites

To run these scripts, you will need to install the following Python packages:

- requests
- beautifulsoup4
- selenium

You also need to install the appropriate WebDriver for your browser. For Google Chrome, you can download the ChromeDriver and add its location to your system's PATH variable.

#Usage
Indeed Job Scraper
To use the Indeed job scraper, simply run the indeed_scraper.py script:

bash

**python indeed_scraper.py**
The script will scrape junior developer job listings in Toronto from Indeed and display the job title, company name, location, and job URL in the terminal.

Glassdoor Job Scraper
To use the Glassdoor job scraper, run the glassdoor_scraper.py script:

bash
python glassdoor_scraper.py
The script will scrape junior developer job listings in Toronto from Glassdoor and display the job title, company name, location, and job URL in the terminal.

Disclaimer

Please note that web scraping may violate the terms of service of the websites you are scraping. Be aware of the legal and ethical implications of web scraping before using these scripts. Additionally, websites often change their structure, which may cause the scripts to break or provide incorrect information. Always ensure that the scripts are up-to-date and working correctly before using them.
