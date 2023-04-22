import webbrowser
import random
import string
import time

# Perform 30 searches
for i in range(30):
    # Generate a random search term of length between 3 and 8 characters
    search_term = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))
    
    # Construct the Bing search URL with the search term
    url = f"https://www.bing.com/search?q={search_term}"
    
    # Open the URL in the default web browser
    webbrowser.open(url)
    
    # Wait for a random amount of time (between 1 and 5 seconds) before performing the next search
    time.sleep(1)
