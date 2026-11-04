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
input_name = input("Enter student name: ")
input_course = input("Enter student course: ")
input_marks = input("Enter student marks in grade ie(A, B, C): ")



def name_cleaner(name):
    name = name.title()
    cleaned_name = name.strip()
    print (f"Title Case: {cleaned_name}")

def text_statistics(text):
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



def main():
    name_cleaner(input_name)
    text_statistics(input_sentence)
    search_and_replace(input_paragraph, input_search, input_replace)
    email_validator(input_email)
    word_frequency(input_text, input_search)
    text_reformatting(list_of_words)
    palindrome_checker(input_text)
    student_record(input_id, input_name, input_course, input_marks) 

if __name__ == "__main__":
    main()
    



    
# name_cleaner(input_name)
# text_statistics(input_sentence)
# search_and_replace(input_paragraph, input_search, input_replace)
# email_validator(input_email)
# word_frequency(input_text, selected_word)
# text_reformatting(list_of_words)
# palindrome_checker(input_text)
# student_record(input_id, input_name, input_course, input_marks)
