import requests, os, bs4, sys, webbrowser as web

# Base URL for Unsplash search
url = 'https://unsplash.com/s/photos/' 
fileName = ''

# Check if a search term was provided via command line arguments
if len(sys.argv) > 1:
    fileName = sys.argv[1]  # Use the search term for both the URL and folder name
    url += fileName
else:
    print("Usage: python script.py <search-term>")
    sys.exit()  # Exit if no search term is given

# Attempt to send a GET request to the constructed URL
try:
    res = requests.get(url)
    res.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    sys.exit()

# Create a folder named after the search term if it doesn't exist
os.makedirs(fileName, exist_ok=True)

# Parse the HTML content of the page using BeautifulSoup
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Attempt to find all image elements with the target class (as of 11th June 2025)
images = soup.find_all('img', class_='czQTa')

# Iterate through each image tag found
for i, img in enumerate(images):
    img_url = img.get('src')  # Get the image URL from the 'src' attribute

    if not img_url:
        continue  # Skip if no src found

    # Attempt to download the image
    try:
        res = requests.get(img_url)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to download image {i}: {e}")
        continue

    # Define a clean file path using the search term and index
    image_path = os.path.join(fileName, f"{fileName}_{i}.jpg")
    print(f"Downloading: {image_path}")

    # Write the image content to the file in chunks
    with open(image_path, 'wb') as f:
        for chunk in res.iter_content(100000):
            f.write(chunk)
