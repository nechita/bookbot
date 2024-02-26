path_to_file = "books/frankenstein.txt"

def get_num_words(file):
  words = file.split()
  return len(words)

def get_char_dict(file):
  occurences = {}
  for letter in file:
    if letter.isalpha() == False:
      continue
    lowercase_letter = letter.lower()
    if lowercase_letter in occurences.keys():
      occurences[lowercase_letter] += 1
    else:
      occurences[lowercase_letter] = 1
  return occurences

def get_book_contents(path_to_file):
  with open(path_to_file) as f:
    return f.read()

def sorted_by_occurences(char_dict):
  return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)

def print_report(num_words, char_dict):
  print(f"--- Begin report of {path_to_file} ---")
  print(f"{num_words} words found in the document")
  print()
  for char, occurences in sorted_by_occurences(char_dict):
    print(f"The '{char}' character was found {occurences} times")
  print(f"--- End report ---")

def main():
  text = get_book_contents(path_to_file)
  num_words = get_num_words(text)
  chars_dict = get_char_dict(text)
  print_report(num_words, chars_dict)

main()