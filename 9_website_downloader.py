#!/usr/bin/env python3
"""
Website Data Downloader - Download and parse website content
"""

import requests
from bs4 import BeautifulSoup
import os

def download_website_data():
    """Download and display website data"""
    print("=== Website Data Downloader ===")
    
    url = input("Enter website URL (include http:// or https://): ")
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        print(f"Downloading data from: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print("\n=== Website Content ===")
        print(f"Title: {soup.title.string if soup.title else 'No title found'}")
        print(f"Status Code: {response.status_code}")
        print(f"Content Length: {len(response.text)} characters")
        
        # Display first 2000 characters of prettified HTML
        prettified = soup.prettify()
        print("\n=== HTML Content (First 2000 characters) ===")
        print(prettified[:2000])
        if len(prettified) > 2000:
            print("\n... (content truncated)")
        
        # Save to file option
        save_option = input("\nSave to file? (y/n): ").lower()
        if save_option == 'y':
            filename = input("Enter filename (default: website_data.html): ") or "website_data.html"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(prettified)
            print(f"✅ Content saved to {filename}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading website: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    download_website_data() 