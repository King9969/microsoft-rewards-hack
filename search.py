import webbrowser
import random
import time

# List of random words to search for
random_words = ["apple", "banana", "carrot", "dog", "elephant", "fire", "guitar", "house", "ice cream", "jacket"]

# Perform 30 searches
for i in range(30):
    # Choose a random word from the list
    search_term = random.choice(random_words)
    
    # Construct the Bing search URL with the search term
    url = f"https://www.bing.com/search?q={search_term}"
    
    # Open the URL in the default web browser
    webbrowser.open(url)
    
    # Wait for a random amount of time (between 1 and 5 seconds) before performing the next search
    time.sleep(random.randint(1, 5))
