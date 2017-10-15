[![Build Status](https://travis-ci.org/rohanbk/Mountain-Project-Scraper.svg?branch=master)](https://travis-ci.org/rohanbk/Mountain-Project-Scraper/)

# Mountain Project Scraper

This is a Scrapy-powered Web-Scraper written in Python 3.6 which is capable of scraping [Mountain Project](https://www.mountainproject.com/), a popular online guide of thousands of rock-climbing routes around the world.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python
- Pip
- Scrapy
- VirtualEnv

### Installing

A step by step series of examples that tell you have to get a development env running

Pull the code down from Github

```
git clone https://github.com/rohanbk/Mountain-Project-Scraper
```

Install PIP
```
Instructions available here: [https://pip.readthedocs.io/en/stable/installing/](https://pip.readthedocs.io/en/stable/installing/)
```

Install VirtualEnv
```
[sudo] pip install virtualenv
```

Install Scrapy
```
pip install Scrapy
```

Enter the cloned project and setup a Virtual Environment
```
cd mountain_project_scraper
virtualenv -p python3.6 env
. env/bin/activate
```

## Running the Scraper

By default, the Spider will run and scrape using the contents of the ```start_urls``` list.

Enter the Scraper project
```
cd mountain_project_scraper
```

Run the coordinates scraper
```
scrapy crawl coordinates -o [file_path of output file]
```

To play around with the markup for a single page (i.e. good way to debug or play around with CSS/Xpath selectors)
```
scrapy shell [url]
```
## Debugging the Scraper

I use Intellij as my IDE of choice. In order to debug the Scraper/Spider code, utilize the following instructions: 

* Create a new Run/Debug Configuration with the following parameters

```
Script: [path to scraper project]/env/bin/scrapy # This folder will get setup when you execute the virtualenv setup above
Script Parameters: crawl [Spider name] # e.g. crawl coordinates
Environment Variables: PYTHONUNBUFFERED=1
Python Interpreter: There should be a dropdown option with an interpreter located in the env folder
Working Directory: [Path to Scraper]/env/bin
Add Content Roots to PYTHONPATH: Checked
Add Source Roots to PYTHONPATH: Checked

All other options are default
```
## Authors

* Rohan Balakrishnan

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
