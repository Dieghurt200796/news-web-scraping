# news-web-scraping
## Overview
This project is a simple web scraper built with Python and Selenium. Its primary purpose is to serve as an educational exercise for those new to web scraping. The script automatically opens the BBC News website, extracts the top headlines, 
and saves them into a text file. This project demonstrates the basics of:

 - Automating a web browser with Selenium.
 - Waiting for dynamic content to load.
 - Selecting elements from a webpage using CSS selectors.
 - Handling environment variables for configuration.
 - Basic logging to monitor the script's execution.

## Features
 - Navigates to the BBC News homepage.
 - Waits for the main headlines to be present on the page.
 - Extracts the text content of each headline.
 - Removes duplicate headlines.
 - Saves the unique headlines to a headlines.txt file.


## Setup & Installation
### Prerequisites
 - Python 3.8 or newer.
 - A web browser (e.g., Google Chrome).
 - The corresponding WebDriver for your browser (e.g., ChromeDriver). Make sure the WebDriver is in your system's 
PATH or its location is specified in the src/setup.py file.

### Installation
1. Clone the repository:
```bash
git clone https://github.com/Dieghurt200796/news-web-scraping
cd news-web-scraping
```

2. Create and activate a virtual environment:
macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage:
Run the scraper.py file in your IDE.

## Author
 - Diego Hurtado
 - dieghurt200796@gmail.com

## Disclamer:
 - This project is for educational purposes only. Always respect the robots.txt 
file and the terms of service of the website you are scraping.
 - Web scraping, especially using CSS selectors, is fragile. Websites frequently update their structure, 
which can break the HEADLINE_SELECTOR. If the script stops working, you will likely need to inspect the 
BBC News website again to find the new correct selector.