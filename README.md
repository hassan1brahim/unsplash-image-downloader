Unsplash Image Scraper
This Python script allows you to download images from Unsplash based on a given search term. It fetches and saves all relevant images from the first search results page using requests and BeautifulSoup.

Requirements
Python 3.x

requests

beautifulsoup4

Install the dependencies (if not already installed):

bash
Copy
Edit
pip install requests beautifulsoup4
Usage
bash
Copy
Edit
python script.py <search-term>
Example:

bash
Copy
Edit
python script.py spiderman
This will:

Search Unsplash for "spiderman"

Create a folder named spiderman (if it doesn’t exist)

Download all found images into that folder, naming them like spiderman_0.jpg, spiderman_1.jpg, etc.

Output
The images are saved in a local directory matching the search term you provided.

markdown
Copy
Edit
project-folder/
├── script.py
└── spiderman/
    ├── spiderman_0.jpg
    ├── spiderman_1.jpg
    └── ...
Notes
This script relies on the structure of Unsplash's HTML, which may change. As of June 11, 2025, it looks for images with the class czQTa.

If the class or site structure changes, the script may stop working until updated.

Disclaimer
This tool is for educational and personal use only. Always respect a website’s robots.txt file and terms of service.
