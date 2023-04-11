import pytest
from main import read_template, parse_template, merge

# Define the intro function that prints an introduction message
def intro():
    print("*" * 32)
    print("Welcome to the Mad Libs Game!")
    print("You will be prompted to enter some random words")
    print("When you're done, a story will be generated based on your input")
    print("*" * 32)
    print("")

# Define the read_template function that reads the template file
def read_template(filename):
    try:
        # Open the file for reading
        with open(filename, "r") as template_file:
            # Read the file contents and remove any leading/trailing whitespace
            template_content = template_file.read().strip()
            return template_content
    except FileNotFoundError:
        # If the file is not found, raise an error
        raise FileNotFoundError

# Define the parse_template function that parses the template to get the number of inputs needed and the text to be displayed
def parse_template(template):
    count = template.count("{")
    if count == 0:
        return "no prompts!"

    temp_template = template
    parts = []
    stripped = ""

    # Loop through the template and extract the text to be displayed and the number of inputs needed
    for bracket in range(count):
        # Find the index of the first "{" and "}"
        start = temp_template.index("{")
        end = temp_template.index("}")

        # Extract the text to be displayed and the number of inputs needed
        stripped = stripped + temp_template[0:start+1] + "}"
        parts.append(temp_template[(start+1):end])

        # Remove the extracted text from the template
        temp_template = temp_template[(end+1):]

    # Add in the last part of the template after the last "}"
    stripped = stripped + temp_template

    # Convert the list of parts to a tuple
    parts = tuple(parts)

    # Return the stripped text and the tuple of parts
    return stripped, parts

# Define the user_input function that prompts the user for input words
def user_input(prompt):
    # Create an empty list to store the user input
    inputs = []

    # Loop through the prompts and ask the user for input
    for word_prompt in prompt:
        inputs.append(input(f"{word_prompt}: "))

    # Return the list of user input
    return inputs

# Define the merge function that generates the story based on the user input and the template
def merge(stripped, words):
    new_story = stripped

    # Loop through the user input and replace the prompts with the user input
    for word in words:
        new_story = new_story.replace("{}", word, 1)

    return new_story

# Define the save_to_file function that saves the story to a file
def save_to_file(story):
    with open("story.txt", "w") as f:
        f.write(story)

# Define the main function that runs the game
def main():
    # Print an introduction message
    intro()

    # Read the template file
    template_content = read_template("../assets/dark_and_stormy_night_template.txt")

    # Parse the template to get the number of inputs needed and the text to be displayed
    stripped, parts = parse_template(template_content)

    # Prompt the user for input words
    words = user_input(parts)

    # Generate the story based on the user input and the template
    new_story = merge(stripped, words)

    # Save the story to a file
    save_to_file(new_story)

if __name__ == '__main__':
    main()
