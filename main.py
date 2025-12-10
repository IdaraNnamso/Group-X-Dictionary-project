from dictionaries.hausa import dictionary as hausa_dict
from dictionaries.yoruba import dictionary as yoruba_dict
from dictionaries.igbo import dictionary as igbo_dict
from dictionaries.efik import dictionary as efik_dict
from dictionaries.tiv import dictionary as tiv_dict

languages = {
    "1": ("Hausa", hausa_dict),
    "2": ("Yoruba", yoruba_dict),
    "3": ("Igbo", igbo_dict),
    "4": ("Efik", efik_dict),
    "5": ("Tiv", tiv_dict)
}

print("African Language Translator")
print("Select a language:")
for key, value in languages.items():
    print(f"{key}. {value[0]}")

choice = input("Enter number: ")

if choice not in languages:
    print("Invalid choice.")
    exit()

lang_name, lang_dict = languages[choice]

word = input(f"Enter an English word to translate to {lang_name}: ").lower()

if word in lang_dict:
    print(f"{word} → {lang_dict[word]}")
else:
    print(f"'{word}' not found in {lang_name} dictionary.")
