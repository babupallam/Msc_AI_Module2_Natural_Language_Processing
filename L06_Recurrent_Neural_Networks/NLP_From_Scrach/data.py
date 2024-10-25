import torch
import glob
import unicodedata
import string

# All possible letters including lowercase/uppercase alphabet, space, punctuation, etc.
all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)  # The total number of valid characters (for one-hot encoding)

# Function to find all files in the given path pattern (names dataset in this case)
def findFiles(path):
    return glob.glob(path)  # Uses glob to match files by pattern (wildcards)

# Function to convert a Unicode string to plain ASCII
# It removes accents and non-letter characters from the string
def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)  # Normalize the Unicode string to decomposed form
        if unicodedata.category(c) != 'Mn'  # 'Mn' category refers to non-spacing marks (accents)
        and c in all_letters  # Ensure the character is part of the allowed letters (removes others)
    )

# Function to read a file, split it into lines, and convert each line to plain ASCII
def readLines(filename):
    # Open the file with UTF-8 encoding
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n')
    return [unicodeToAscii(line) for line in lines]

# Dictionary to store names categorized by their language or group (e.g., "English": [names])
category_lines = {}
# List of all categories (each category corresponds to a language/group)
all_categories = []

# Load all text files containing names, each file corresponds to a different category (language or group)
for filename in findFiles('../data/names/*.txt'):
    category = filename.split('/')[-1].split('.')[0]  # Extract the category name from the filename
    all_categories.append(category)  # Add the category (e.g., "English") to the list of categories
    lines = readLines(filename)  # Read and convert all lines in the file to ASCII
    category_lines[category] = lines  # Store the lines under the corresponding category in the dictionary

# Total number of categories (languages or groups of names)
n_categories = len(all_categories)

# Function to convert a letter to its corresponding index in `all_letters`
# This is needed to index the one-hot encoding correctly
def letterToIndex(letter):
    return all_letters.find(letter)  # Returns the index of the letter in `all_letters`

# Function to convert a string (line of text) to a tensor of one-hot vectors
# Each letter is represented by a vector with the size of `n_letters` (total valid characters)
def lineToTensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)  # Create a tensor with shape (line_length, 1, n_letters)
    for li, letter in enumerate(line):  # For each letter in the line
        tensor[li][0][letterToIndex(letter)] = 1  # Set the corresponding index to 1 (one-hot encoding)
    return tensor  # Return the tensor representing the line
