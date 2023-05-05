#Calculate the number of words in a text using a defaultdict

from collections import defaultdict



def calculate_words(text = ""):
    words = text.split()
    words_count = defaultdict(lambda: 0)
    for word in words:
        words_count[word]+=1
    print(words_count)
    
    
text = "The sun was setting behind the mountains, casting a warm glow over the valley below. The valley was filled with tall trees that rustled softly in the breeze. As the sun continued to set, the sky turned shades of pink and orange, and the trees were silhouetted against the colorful sky."
calculate_words(text)
