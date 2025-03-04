import os
import re
import socket
from collections import Counter

if os.path.exists("/home/data/IF-1.txt"):
    input_files = {
        "IF-1.txt": "/home/data/IF-1.txt",
        "AlwaysRememberUsThisWay-1.txt": "/home/data/AlwaysRememberUsThisWay-1.txt",
    }
else:
    input_files = {
        "IF-1.txt": "IF-1.txt",
        "AlwaysRememberUsThisWay-1.txt": "AlwaysRememberUsThisWay-1.txt",
    }

output_file = os.path.join(os.path.dirname(list(input_files.values())[0]), "output", "result.txt")

def process_text(filename, handle_contractions=False):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().lower()
        text = re.sub(r"[^\w\s']", " ", text)
        words = text.split()

        if handle_contractions:
            contractions = {
                "i'm": "i am", "you're": "you are", "he's": "he is", "she's": "she is", 
                "it's": "it is", "we're": "we are", "they're": "they are", "can't": "can not",
                "won't": "will not", "don't": "do not", "doesn't": "does not", "didn't": "did not",
                "isn't": "is not", "aren't": "are not", "wasn't": "was not", "weren't": "were not",
                "haven't": "have not", "hasn't": "has not", "hadn't": "had not", "shouldn't": "should not",
                "wouldn't": "would not", "couldn't": "could not", "mustn't": "must not", "shan't": "shall not"
            }

            expanded_words = []
            for word in words:
                if word in contractions:
                    expanded_words.extend(contractions[word].split())
                else:
                    expanded_words.append(word)

            words = expanded_words

        return words

word_counts = {}
top_words = {}

for name, path in input_files.items():
    is_contractions_handling_needed = "AlwaysRememberUsThisWay" in name
    words = process_text(path, handle_contractions=is_contractions_handling_needed)
    word_counts[name] = len(words)

    if "IF-1.txt" in name:
        top_words[name] = Counter(words).most_common(3)

grand_total = sum(word_counts.values())
ip_address = socket.gethostbyname(socket.gethostname())

os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, "w") as f:
    f.write(f"Total words in {input_files['IF-1.txt']}: {word_counts['IF-1.txt']}\n")
    f.write(f"Total words in {input_files['AlwaysRememberUsThisWay-1.txt']}: {word_counts['AlwaysRememberUsThisWay-1.txt']}\n")
    f.write(f"Grand Total words: {grand_total}\n")
    f.write(f"Top 3 words in IF-1.txt: {top_words['IF-1.txt']}\n")
    f.write(f"Container IP Address: {ip_address}\n")

with open(output_file, "r") as f:
    print(f.read())
