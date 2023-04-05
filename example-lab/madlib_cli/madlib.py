# Define the main function that runs the game
def main():
    # Print an introduction message
    intro()

    # Read the template file
    template_content = read_template(
        "../assets/dark_and_stormy_night_template.txt")

    # Parse the template to get the number of inputs needed and the text to be displayed
    stripped, parts = parse_template(template_content)

    words = user_input(parts)

    new_story = merge(stripped, words)

    save_to_file(new_story)

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

        with open(filename, "r") as template_file:

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

# Define the user_info function that prompts the user for info


def user_input(prompt):
    # Create an empty list to store the user info
    inputs = []

    # Loop through the prompts and ask the user for info
    for word_prompt in prompt:
        inputs.append(input(f"{word_prompt}: "))

    return inputs

# Define merge function that generates the story based on the user info and the template


def merge(stripped, words):
    new_story = stripped

    # Loop through the user info and replace in the template with the user info
    for word in words:
        index = new_story.index("{")

        new_story = new_story[0:index] + word + new_story[index+2:]

    # Print it


def save_to_file(story):
    with open('story.txt', 'w') as file:
        file.write(story)
