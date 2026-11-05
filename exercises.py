input_name = input("Enter your name: ")
input_sentence = input("Enter your sentence: ")
input_paragraph = input("Enter your paragraph: ")
input_search = input("Enter the word to search for: ")
input_replace = input("Enter the word to replace with: ")
input_email = input("Enter your email address: ")
input_text = input("Enter your text: ")
list_of_words = input("Enter a list of words separated by commas: ")
input_text = input("Enter your text/word: ")
input_id = input("Enter student ID: ")
input_student_name = input("Enter student name: ")
input_course = input("Enter student course: ")
input_marks = input("Enter student marks in grade ie(A, B, C): ")
input_paragraph = input("Enter a paragraph: ")

# Exercise 1 — Name Cleaner (Basic)
# Ask the user to enter their full name. Remove leading and trailing whitespace, then display the cleaned name in title
# case.
# Requirements: use input(), strip(), title() and an f-string
# Exercise 2 — Text Statistics (Basic)
# Ask for a sentence and display: number of characters, number of words, uppercase version and lowercase version.
# Decide whether spaces at the beginning and end should be included in your character count, and explain your
# choice.
# Exercise 3 — Search and Replace (Basic–Intermediate)
# Ask the user for a paragraph, a word to search for, and a replacement word. Display whether the search term
# occurs, how many times it occurs, and the paragraph after replacement.
# Hint: use in, count() and replace(). Explain that count() is case-sensitive.
# Exercise 4 — Email Text Check (Intermediate)
# Ask for an email address, trim whitespace and convert it to lowercase. Check that it contains exactly one @
# character and that there is at least one dot after the @ character. Display a simple accepted/rejected message. This
# is a classroom validation exercise, not a complete email-standard validator.
# Exercise 5 — Word Frequency (Intermediate)
# Ask the user for a sentence, convert it to lowercase, split it into words and display how many times a selected word
# occurs. Make sure the selected word is also normalised.
# Exercise 6 — Text Reformatter (Intermediate)
# Ask for a comma-separated list of names. Split the list, trim each name, remove empty entries and join the
# remaining names using a vertical bar separator, such as Amina | Brian | Carol.
# Exercise 7 — Palindrome Checker (Challenge)
# Ask the user for a word or phrase. Create a normalised version by converting it to lowercase and removing spaces.
# Compare the normalised text with its reverse using slicing. Extend the solution to ignore punctuation, and explain
# any limitations.
# Exercise 8 — Student Record Parser (Challenge)
# Accept a single record in the format Student ID|Full Name|Course|Mark. Split using the pipe character,
# validate the number of fields, clean the text fields, convert the mark to a number, validate the mark range, and
# display a formatted report.
# Exercise 9 — Character Analysis (Challenge)
# Ask for a paragraph and count vowels, consonants, digits, whitespace characters and punctuation. State how your
# program treats accented letters and non-English characters. Use a loop and suitable string methods.
# Exercise 10 — Reusable Text Utility (Extension)
# Create functions called clean_text(text), count_words(text), and normalise_label(text). Test each
# function with at least three inputs, including an empty string.
# Lab submission checklist
# • Submit source code for each completed exercise.
# • Include sample inputs and outputs for at least five exercises.
# • Add short comments explaining the purpose of important processing steps.
# • Test boundary cases: empty text, repeated spaces, uppercase and lowercase input, missing search terms, and
# malformed records.
# • Be ready to explain the difference between a string method returning a new string and modifying the original value.

def name_cleaner(name):
    name = name.title()
    cleaned_name = name.strip()
    print (f"Title Case: {cleaned_name}")

def text_statistics(text):
# cleared whitespaces after and before the text to avoid being counted and counted the number of words and characters in the text. 
# Also converted the text to uppercase and lowercase.
    cleaned_text = text.strip() 
    number_of_words = len(cleaned_text.split(" "))
    number_of_characters = len(cleaned_text)
    print(f"Upper Case: {cleaned_text.upper()}")
    print(f"Lower Case: {cleaned_text.lower()}")  
    print(f"Number of words: {number_of_words}")
    print(f"Number of characters: {number_of_characters}")

def search_and_replace(paragraph, search, replace):
    if not search:
        print(f"{search} is not found in the paragraph.")

    while search in paragraph:
        print(f"Found '{search}' in the paragraph.")
        search_count = paragraph.count(search)
        print(f"Found '{search}' {search_count} times in the paragraph.")
        paragraph = paragraph.replace(search, replace)
        print(f"Updated paragraph: {paragraph}")

def email_validator(email):
    cleaned_email = email.strip() and email.lower()
    first_part = cleaned_email.split("@")[0]
    second_part = cleaned_email.split("@")[1]
    if "@" in cleaned_email and "." in second_part and len(first_part) > 0 and len(second_part) > 0 and second_part.endswith(".com") and cleaned_email.count("@") == 1 and first_part.isalnum() and second_part.replace(".", "").isalnum():
        print(f"{cleaned_email} is a valid email address.")
    else:
        print(f"{cleaned_email} is not a valid email address.")

def word_frequency(text, word):
    ar_words = []
    cleaned_word = word.strip().lower()
    cleaned_text = text.strip().lower()
    words = cleaned_text.split(" ")
    words.extend(ar_words)

    if cleaned_word in words:
        frequency = words.count(cleaned_word)
        print(f"The word '{cleaned_word}' appears {frequency} times in the text.")

def text_reformatting(text):
    cleaned_text = text.strip()
    split_words = cleaned_text.split(",")
    cleaned_words = [word.strip().title() for word in split_words]
    print(f"Reformatted text: {'|'.join(cleaned_words)}")

def palindrome_checker(text):
    
# Limitations: The current implementation only ignores spaces and converts the text to lowercase.
# It does not ignore punctuation or special characters, which may affect the palindrome check.
# For example, "A man, a plan, a canal: Panama" would not be recognized as a palindrome due to the punctuation.
# To improve this, we could use regular expressions to remove all non-alphanumeric characters before checking for palindromes.

    cleaned_text = text.strip().lower()
    reversed_text = cleaned_text[::-1]
    if cleaned_text == reversed_text:
        print(f"{cleaned_text} is a palindrome.")
    else:
        print(f"{cleaned_text} is not a palindrome.")

def student_record(id, name, course, marks):
    if not id and not name and not course and not marks:
        print("All fields are required.")
        return
    if not id.isdigit() and not marks.isalpha() and not name.isalpha() and not course.isalnum():
        print("Invalid inputs.")
        return
    
    cleaned_id = id.strip()
    cleaned_name = name.strip().title()
    cleaned_course = course.strip().title()
    cleaned_marks = marks.strip().upper()
    result = "|".join([cleaned_id, cleaned_name, cleaned_course, cleaned_marks])

    if cleaned_marks not in ["A","B", "C", "D", "E", "F"] and not cleaned_marks.isalpha() and (len(cleaned_marks) > 1 or len(cleaned_marks) < 1):
        print("Invalid marks. Please enter a valid grade (A, B, C, D, E, F).")

    if cleaned_marks == "A":
        result = f"Results: {result} (Excellent)"
    elif cleaned_marks == "B":
        result = f"Results: {result} (Good)"
    elif cleaned_marks == "C":      
        result = f"Results: {result} (Average)"
    elif cleaned_marks == "D":
        result = f"Results: {result} (Below Average)"
    elif cleaned_marks == "E":
        result = f"Results: {result} (Poor)"
    elif cleaned_marks == "F":
        result = f"Results: {result} (Fail)" 

    print(f"Results: {result}")

def character_analysis(paragraph):
    vowels = "aeiou"
    non_english_characters = "àáâäæãåāçćčèéêëēėęîïíīįìłñńôöòóœøōõßśšûüùúūÿžźż"
    consonants = "bcdfghjklmnpqrstvwxyz"
    punctuation_marks = ".,!?;:'\"-()[]{}"
    non_alnum = "!@#$%^&*()_+=-[]{}|;:'\",.<>?/`~"
    cleaned_paragraph = paragraph.strip().lower()

    non_english_characters = 0
    non_alnum_count = 0
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    spaces_count = 0
    punctuation_count = 0
    for char in cleaned_paragraph:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char == " ":
            spaces_count += 1
        elif char in punctuation_marks:
            punctuation_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in non_english_characters:
            non_english_characters += 1
        elif char in non_alnum:
            non_alnum_count += 1
        else:
            continue
            

    print(f"Number of punctuation marks: {punctuation_count}")
    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")
    print(f"Number of spaces: {spaces_count}")
    print(f"Number of digits: {digit_count}")
    print(f"Number of non-English characters: {non_english_characters}")
    print(f"Number of non-alphanumeric characters: {non_alnum_count}")


text1 = "This is a sample text. It contains multiple sentences, words, and characters."
text2 = "This is another sample text. It also contains multiple sentences, words, and characters."
text3 = ""

def clean_text(text):
    cleaned_text = text.strip()
    # Replace multiple spaces with a single space
    cleaned_text = ' '.join(cleaned_text.split())
    print(f"Cleaned text: {cleaned_text}")

def count_words(text):
    cleaned_text = text.strip()
    words = cleaned_text.split()
    print(f"Number of words: {len(words)}")

def normalise_label(text):
    cleaned_text = text.strip()
    # Replace multiple spaces with a single space
    cleaned_text = ' '.join(cleaned_text.split())
    print(f"Normalised label: {cleaned_text}")


def main():
    name_cleaner(input_name)
    text_statistics(input_sentence)
    search_and_replace(input_paragraph, input_search, input_replace)
    email_validator(input_email)
    word_frequency(input_text, input_search)
    text_reformatting(list_of_words)
    character_analysis(input_paragraph)
    clean_text(text3)
    count_words(text2)
    normalise_label(text1)
    palindrome_checker(input_text)
    student_record(input_id, input_student_name, input_course, input_marks) 

if __name__ == "__main__":
    main()
    



