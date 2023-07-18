
freq = {}
filename="" #file path 
for piece in open(filename).read().lower().split():
    # from the file filename, read everything that is lower case character 

    word = ''.join(c for c in piece if c.isalpha())

    if word: #require at least one alphabetical character
        freq[word] = 1+ freq.get(word, 0)

max_word=''
max_count = 0
for(w,c) in freq.items(): #(key, value) tuples represent (word, count)
    if c > max_count:
        max_word= w
        max_count = c

print("Most frequent word is" ,max_word)
print(f"The number of occurrences of '{max_word}' is {max_count}")