# Project: Web Scraping for Registered Projects

## Overview
This project is part of the Python Data and Backend Engineer internship assignment for Primenumbers Technologies. The task involves writing a Python program to scrape specific details from the "Registered Projects" section on the [HPRERA Public Dashboard](https://hprera.nic.in/PublicDashboard). The required details for each project include:

- GSTIN No
- PAN No
- Name
- Permanent Address

## Requirements
Ensure the following packages are installed before running the script:

```
pip install selenium beautifulsoup4 
```

Setup

1-Download the ChromeDriver and place it in a directory of your choice.

2-Update the chromedriver_path variable in the script with the path to your ChromeDriver executable.

Usage
To run the script, use the following command:
```
python main.py
```

The script will:

Open the HPRERA Public Dashboard.
Extract the first 6 project details under the "Registered Projects" heading.
Print the project details in the following format:

```
1. Name: <name>
   PAN No: <pan_no>
   GSTIN No: <gstin_no>
   Permanent Address: <address>
```

Code Explanation

The script uses Selenium and BeautifulSoup for web scraping. Below is a brief overview of the key steps:

1-Setup Chrome Options: Configures Chrome to run in headless mode.

2-Navigate to URL: Opens the HPRERA Public Dashboard URL.

3-Extract Project Links: Extracts JavaScript links for the first 6 projects.

4-Scrape Project Details: Navigates to each project's detail page and extracts the required information using BeautifulSoup.

5-Print Project Details: Outputs the collected project details in a structured format.

6-The script includes a delay to ensure pages load completely before scraping data.

Example Output

```
1. Name: ABC Developers
   PAN No: ABC1234P
   GSTIN No: 27AAEFA1234P1Z9
   Permanent Address: 123 Main Street, City, State

2. Name: XYZ Builders
   PAN No: XYZ5678P
   GSTIN No: 27AAEFA5678P1Z9
   Permanent Address: 456 Another Street, City, State

... (and so on for 6 projects)
```

