def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()
    cleaned_text = ''
    inside_tag = False

    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            cleaned_text += char
    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

delete_html_tags('draft.html', 'cleaned.txt')