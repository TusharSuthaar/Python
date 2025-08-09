#!/usr/bin/env python3
"""
Google Search - Perform Google searches and display results
"""

from googlesearch import search

def google_search():
    """Perform a Google search and display results"""
    print("=== Google Search ===")
    
    query = input("Enter your search query: ")
    num_results = input("Number of results (default 5): ")
    
    try:
        num_results = int(num_results) if num_results else 5
    except ValueError:
        num_results = 5
    
    print(f"\nSearching for: '{query}'")
    print("=" * 50)
    
    try:
        results = list(search(query, num_results=num_results))
        
        if results:
            for i, result in enumerate(results, 1):
                print(f"{i}. {result}")
        else:
            print("No results found.")
            
    except Exception as e:
        print(f"❌ Error performing search: {e}")
        print("Note: You might need to install googlesearch-python: pip install googlesearch-python")

if __name__ == "__main__":
    google_search() 