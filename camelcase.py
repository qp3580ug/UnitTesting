def camelcase(sentence):
    """ Convert sentence to camelCase, for example, "Display all books" is converted to "displayAllBooks" """

    title_case = sentence.title()
    upper_camel_cased = title_case.replace(' ', '')

    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def main():
    print("Enter a sentence to convert to camelCase!!")
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()
