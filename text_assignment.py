# Task: Build a Text Processing Utility. Write a menu-driven Python program that lets the user choose at least four
# operations: clean text, change case, count words and characters, search and replace a substring, split a line into
# words, or check whether a word is a palindrome.
# Minimum requirements:
# • use input() to collect text and menu selections;
# Python Programming • Week 8: Strings & Text Processing Page 12
# • use at least six different string methods or string operations;
# • use conditions to handle menu choices and invalid selections;
# • use a loop so the user can perform multiple operations before exiting;
# • use at least one reusable function;
# • handle empty input sensibly and include comments;
# • test the program with at least five test cases and document the expected results.


input_text = input("Enter the text to process: ")
def clean_text(text):
    # Remove leading and trailing whitespace
    cleaned_text = text.strip()
    # Replace multiple spaces with a single space
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text

def change_case(text, case_type):
    if case_type == 'upper':
        return text.upper()
    elif case_type == 'lower':
        return text.lower()
    elif case_type == 'title':
        return text.title()
    else:
        return "Invalid case type. Please choose 'upper', 'lower', or 'title'."

def count_words_and_characters(text):
    word_count = len(text.split())
    character_count = len(text)
    return word_count, character_count  

def search_and_replace(text, search, replace):
    return text.replace(search, replace)

def split_into_words(text):
    return text.split()     

def is_palindrome(word):
    cleaned_word = word.lower().replace(" ", "")
    return cleaned_word == cleaned_word[::-1]

def main():
    while True:
        print("\nMenu:")
        print("1. Clean Text")
        print("2. Change Case")
        print("3. Count Words and Characters")
        print("4. Search and Replace")
        print("5. Split into Words")
        print("6. Check Palindrome")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            cleaned = clean_text(input_text)
            print(f"Cleaned Text: {cleaned}")
        elif choice == '2':
            case_type = input("Enter case type (upper/lower/title): ")
            changed_case = change_case(input_text, case_type)
            print(f"Changed Case: {changed_case}")
        elif choice == '3':
            words, characters = count_words_and_characters(input_text)
            print(f"Word Count: {words}, Character Count: {characters}")
        elif choice == '4':
            search = input("Enter the substring to search for: ")
            replace = input("Enter the substring to replace with: ")
            replaced_text = search_and_replace(input_text, search, replace)
            print(f"Replaced Text: {replaced_text}")
        elif choice == '5':
            words_list = split_into_words(input_text)
            print(f"Words List: {words_list}")
        elif choice == '6':
            word_to_check = input("Enter the word to check for palindrome: ")
            if is_palindrome(word_to_check):
                print(f"{word_to_check} is a palindrome.")
            else:
                print(f"{word_to_check} is not a palindrome.")
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

def test_cases():
    # Test case 1: Clean text
    assert clean_text("   Hello   World   ") == "Hello World"
    
    # Test case 2: Change case
    assert change_case("hello world", "upper") == "HELLO WORLD"
    assert change_case("HELLO WORLD", "lower") == "hello world"
    assert change_case("hello world", "title") == "Hello World"
    
    # Test case 3: Count words and characters
    assert count_words_and_characters("Hello World") == (2, 11)
    
    # Test case 4: Search and replace
    assert search_and_replace("Hello World", "World", "Python") == "Hello Python"
    
    # Test case 5: Check palindrome
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("Hello") == False
