import wikipedia


def main():
    search_phrase = input('Please enter the item you are searching:')
    while search_phrase != '':
        try:
            page = wikipedia.page(search_phrase)
            print(page.title)
            print(page.summary)
            print(page.url)
            search_phrase = input('Please enter the item you are searching:')
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)


main()
