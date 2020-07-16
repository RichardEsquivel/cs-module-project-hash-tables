# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# $%$Start
import string

english_frequency = [
    "E",
    "T",
    "A",
    "O",
    "H",
    "N",
    "R",
    "I",
    "S",
    "D",
    "L",
    "W",
    "U",
    "G",
    "F",
    "B",
    "M",
    "Y",
    "C",
    "P",
    "K",
    "V",
    "Q",
    "J",
    "X",
    "Z",
]

# Frequency Analysis

freq = {}
total_chars = 0
ciphertext = ""

# Count all the characters
with open("ciphertext.txt") as f:
    for line in f:
        for char in line:
            # check for uppercase and add those to freq memoization dictionary
            if char in string.ascii_uppercase:
                if char not in freq:
                    freq[char] = 0
                # add one to frequency numeric for each time that char appears and then increase total # of chars seen
                freq[char] += 1
                total_chars += 1
        # add to ciphertext string sequence for analyzing in next step
        ciphertext += line  # Save for decoding later

# Compute the percentage frequency. (Technically we don't need to do
# this because we're just going to sort it later, and we can do that by
# either frequency or total letter count.)
for c in freq:
    freq[c] /= total_chars
    freq[c] *= 100

# Sort by descending frequency
freq_items = list(freq.items())
# This will allow freq items to be sorted from highest to lowest frequency
freq_items.sort(key=lambda e: e[1], reverse=True)

print("FREQ ITEMS holding frequency list of tuples!!", freq_items, end="\n\n\n")

# Make the key
decode_key = {}
# decode_key will equate first value which is the freq_items to the english frequence
for i in range(26):
    decode_key[freq_items[i][0]] = english_frequency[i]

# Print the key
print("Decode KEY!", decode_key, end="\n\n\n")

# Decode the text
for c in ciphertext:
    if c in decode_key:
        # this will loop through ciphertext and if the key is in the decode key dictionary it will print the value held at that key thereby deciphering
        print(decode_key[c], end="")
    else:  # print punctuation and spaces etc
        print(c, end="")
# $%$End
