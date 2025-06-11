# 📸 Unsplash Image Downloader

This is a Python script that downloads images from Unsplash based on a search term you provide as a command-line argument. It uses the `requests` and `BeautifulSoup` libraries to scrape image URLs and save them locally in a folder named after the search term.

---

## Features

- Downloads all images from Unsplash search results for a given keyword.
- Saves images in a folder named after the search term.
- Handles HTTP request exceptions gracefully.
- Uses standard Python libraries (`requests`, `os`, `bs4`, and `sys`).

---

## Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`

To install the required libraries, run:

```bash
pip install requests beautifulsoup4
```

---

## Usage

Run the script using:

```bash
python unscraper.py <search-term>
```

**Example:**

```bash
python unscraper.py spiderman
```

This will:
1. Visit the Unsplash search page for **spiderman**.
2. Create a folder named `spiderman` (if it doesn't exist).
3. Download all images found (based on the site's HTML class structure as of June 11, 2025).
4. Save the images in the `spiderman` folder as `spiderman_0.jpg`, `spiderman_1.jpg`, etc.

> **Note:** If you search for "spiderman," a folder named `spiderman` will be created, and images matching the search term will be downloaded inside that folder.

---

## Notes

- **Targeted HTML Class:** The script looks for `<img>` tags with the class `czQTa` (as of June 11, 2025). If Unsplash changes its HTML structure, you may need to update the target class in the script.
- **Rate Limiting:** Unsplash may limit or block requests if too many are made in quick succession. For a more stable solution, consider using the [Unsplash API](https://unsplash.com/developers) (requires an API key).
- **Legal:** Please respect Unsplash’s [Terms of Service](https://unsplash.com/terms) when downloading and using images.

---

## Disclaimer

This script is intended for educational purposes only. Make sure you use the downloaded images in accordance with Unsplash’s licensing agreements.

---

## Contact

If you run into any issues or have questions, feel free to reach out!
