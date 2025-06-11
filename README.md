# Unsplash Image Downloader

A Python script to download images from Unsplash based on a search term.

## Description

This script allows you to download multiple images from Unsplash.com for a given search term. It creates a folder with the search term as its name and saves all found images in that folder.

## Features

- Downloads multiple images from Unsplash search results
- Creates organized folders for each search term
- Handles errors gracefully
- Progress feedback during download

## Requirements

- Python 3.x
- The following Python packages:
  - `requests`
  - `beautifulsoup4`

## Installation

1. Clone this repository or download the script
2. Install the required packages:
   ```bash
   pip install requests beautifulsoup4
Usage
Run the script from the command line with your search term as an argument:

bash
python script.py <search-term>
Example:

bash
python script.py mountains
This will:

Create a folder named "mountains"

Search Unsplash for "mountains"

Download all found images into the "mountains" folder

Notes
The script uses web scraping which means it might break if Unsplash changes its HTML structure

Last tested on June 11, 2025

Use responsibly and respect Unsplash's terms of service

Disclaimer
This script is for educational purposes only. Please respect copyright laws and Unsplash's terms of service when using downloaded images.
