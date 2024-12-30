def correct_sentence(text):

    text = text[0].upper() + text[1:]

    if not text.endswith('.'):
        text += '.'

    return text

assert correct_sentence("greetings, friends") == "Greetings, friends."
print(correct_sentence("Greetings, friends."))
assert correct_sentence("hello") == "Hello."
print(correct_sentence("Hello."))
assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
print(correct_sentence("Greetings. Friends."))
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
print(correct_sentence("Greetings, friends."))
assert correct_sentence("greetings, friends.") == "Greetings, friends."
print(correct_sentence("Greetings, friends."))
print('ОК')