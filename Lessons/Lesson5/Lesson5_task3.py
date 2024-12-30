import string

text = input("Enter a string: ")
text = text.translate(str.maketrans('', '', string.punctuation)).replace(' ', '')
words = text.split()
hashtag = ''.join([word.capitalize() for word in words])

if len(hashtag) > 140:
    hashtag = hashtag[:140]
hashtag = "#" + hashtag
print(hashtag)