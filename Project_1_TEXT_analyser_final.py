print("""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ester Bubíková
email: ester.bubikova@gmail.com
discord: Ester #st8115
""")


registered_users = {
  "bob": "123",
  "ann": "pass123",
  "mike": "password123",
  "liz": "pass123"
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

separator = "-" * 45

word_count = 0
word_title = 0
word_all_caps = 0
word_lower = 0
number_count = 0
sum_numbers = 0

word_lenghts = {}




print("TEXT ANALYZER")
user_name = input("Username: ")
password = input("Password: ")

if user_name in registered_users.keys():
  if password == registered_users[user_name]:
    print(f"Welcome to the app, {user_name}!")
    print("We have 3 texts to be analyzed.")

  else:
    print("Incorrect password. Terminating program.")
    quit()

else:
  print("Unregistered user. Terminating program.")
  quit()


text_choice = input("Enter a number between 1 and 3 to select: ")

if text_choice.isdigit():
  text_choice = int(text_choice)

  if text_choice < 1 or text_choice > 3:
    print("There is no text under this number. Terminating program.")
    quit()

else:
  print("You have to input a positive integer. Terminating program.")
  quit()




for word in TEXTS[text_choice - 1].split():
  word = word.strip(",.")
  word_count += 1
  word_length = str(len(word))
  dict_code = "len_" + word_length


  if word.istitle():
    word_title += 1

  elif word.isupper():
    word_all_caps += 1

  elif word.islower():
    word_lower += 1

  if word.isdigit():
    number_count += 1
    sum_numbers += int(word)

  
  if dict_code in word_lenghts:
    word_lenghts[dict_code] += 1

  else:
    word_lenghts[dict_code] = 1


word_lenghts = dict(sorted(word_lenghts.items(), key=lambda items: int(items[0].split("_")[1])))


print(separator)

print(f"""There are {word_count} words in the selected text.
There are {word_title} titlecase words.
There are {word_all_caps} uppercase words.
There are {word_lower} lowercase words.
There are {number_count} numeric strings.
The sum of all the numbers: {sum_numbers}.""")

print(separator)

print("LEN", "OCCURENCES".center(20), "NR.", sep="|")

print(separator)

for key in word_lenghts.keys():
  print(str(key.split("_")[1]).rjust(3), ("*" * int(word_lenghts[key])).ljust(20), int(word_lenghts[key]), sep="|")
