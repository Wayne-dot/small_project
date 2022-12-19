# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as name_file:
    list_of_name = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    format_letter = letter.read()

    for name in list_of_name:
        stripped_name = name.strip()
        new_letter = format_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as complete_let:
            complete_let.write(new_letter)
