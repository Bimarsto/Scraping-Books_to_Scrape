# Scraping-Books_to_Scrape
>python script to get information from the "[_Book to Scrap_](http://books.toscrape.com/index.html)" website.
***
## Table of Contents
1. [General Information](#general-information)
2. [Technologies](#technologies)
3. [Setup](#setup)
4. [Usage](#usage)
***

## General Information
Script functions:
* For each category, create a .csv file with the information for each book. 
* For each book, the extracted information are:
  * The URL of the book page
  * The universal product code (upc)
  * The title
  * The price including tax
  * The price excluding tax
  * The number of available books
  * The description
  * The category
  * The review rating
  * The URL of the book image
* For each book, download the image.

## Technologies
<img src=https://img.shields.io/badge/Python-3.10-blue>

## Setup
### Requirments
For this script, you need following packages and :

<img src='https://img.shields.io/badge/requests-v2.24.0-blue'>
<img src='https://img.shields.io/badge/bs4-v0.0.1-blue'>
<img src='https://img.shields.io/badge/lxml-v4.9.1-blue'>

It is recommended to use a virtual environment. To do this, follow the instructions below:

For all the following instructions, you must be in the terminal in the folder chosen to run the script.
```
# Create the vitrual environment
$ python -m venv env

# Activate the environment on Windows
$ source env/Scripts/activate
---
or
---
# Activate the envirenment on Linux or MacOS
$ source env/bin/activate

```

To install this packages in your environment you can use the following pip instruction:
```
pip install requests==2.24.0

pip install bs4==0.0.1

pip install lxml==4.9.1
```

## Usage
To clone and run this script you'll need [Git](https://git-scm.com) installed on your computer.
```
# clone this repository
$ git clone https://github.com/Bimarsto/Scraping-Books_to_Scrape

# Go into the repository
$ cd Scraping-Books_to_Scrape

# Run the script
$ python main.py
```

