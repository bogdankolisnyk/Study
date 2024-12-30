import string

def create_hashtag(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).replace(' ', '')
    words = text.split()
    hashtag = ''.join(["{}".format(word.capitalize()) for word in words])

    if len(hashtag) > 140:
        hashtag = hashtag[:140]
    return "#{}".format(hashtag)

input_text = input("Enter a string: ")
result = create_hashtag(input_text)
print(result)