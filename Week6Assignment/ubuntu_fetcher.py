import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    """Extract a filename from the URL or generate one."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    if not filename:
        filename = "downloaded_image.jpg"
    return filename

def is_duplicate(filepath, content):
    """Check if the file already exists and has the same content."""
    if os.path.exists(filepath):
        existing_hash = hashlib.md5(open(filepath, "rb").read()).hexdigest()
        new_hash = hashlib.md5(content).hexdigest()
        return existing_hash == new_hash
    return False

def fetch_image(url):
    """Fetch and save an image from the web."""
    try:
        # Fetch with timeout and check for errors
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        # Basic precautions: check Content-Type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return
        
        # Create directory if not exists
        os.makedirs("Fetched_Images", exist_ok=True)

        # Determine filename
        filename = get_filename_from_url(url)
        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicates
        if is_duplicate(filepath, response.content):
            print(f"⚠ Duplicate skipped: {filename}")
            return

        # Save image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Allow multiple URLs separated by space
    urls = input("Please enter one or more image URLs (separated by space): ").split()

    for url in urls:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
