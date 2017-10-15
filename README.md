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
Instructions available here: https://pip.readthedocs.io/en/stable/installing/
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
cd steam-scraper
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

## Authors

* Rohan Balakrishnan

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
