def main():
    book_path = "books/Frankenstein.txt"
    #"github.com/dbakare2/bookbot/books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_counter(text)
    print(f"{num_words} words found in the document")

def get_book_text(path):
# gets the text from the book in the specified path
    with open(path) as f:
    # A 'with' block to open the file
        return f.read()
    # reads the contents of the file

def word_counter(text):
    words = text.split()
    book_words = len(words)
    return book_words

def letter_counter(text):
    l_count = {}
    for letter in text:
        l_lower = letter.lower()
        if l_lower in l_count:
            l_count[l_lower] += 1
        else:
            l_count[l_lower] = 1
    return l_count
            #l_count.append({'l_string':'count.l_string'})

main()



