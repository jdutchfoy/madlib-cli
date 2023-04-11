# get your intro message
def intro():
    print("*" * 32)
    print("Welcome to the Mad Libs Game!")
    print("You will be prompted to enter some random words")
    print("When you're done, a story will be generated based on your input")
    print("*" * 32)
    print("")

# Define your read template


def read_template(filename):
    try:
        # file???
        with open(filename, "r") as template_file:
            # remember the whitespace from last time
            template_content = template_file.read().strip()
            return template_content
    except FileNotFoundError:
        # if I can’t locate raise an error
        raise FileNotFoundError


def parse_template(template):
    count = template.count("{")
    if count == 0:
        return "no prompts!"

    temp_template = template
    parts = []
    stripped = ""

    # Loop through the template and extract the info to show the amount of info to show
    for bracket in range(count):
        # Find the index of the first "{" and "}"
        start = temp_template.index("{")
        end = temp_template.index("}")

        # remove the info to be displayed and the amount of info needed
        stripped = stripped + temp_template[0:start+1] + "}"
        parts.append(temp_template[(start+1):end])

        temp_template = temp_template[(end+1):]

    # Add in the last part of the template after the last "}"
    stripped = stripped + temp_template

    parts = tuple(parts)

    return stripped, parts
# Define the user_input function that prompts the user for input words


def user_input(prompt):
    # Create an empty list to store the user input
    inputs = []

    # Loop through the prompts and ask the user for input
    for word_prompt in prompt:
        inputs.append(input(f"{word_prompt}: "))

    return inputs

# Define the merge function that generates the story based on the user input and the template


def merge(stripped, words):
    new_story = stripped

    # Loop through the user input and replace the prompts with the user input
    for word in words:
        index = new_story.index("{")
        new_story = new_story[0:index] + word + new_story[index+1:]

    return new_story

# Define the save_to_file function that saves the story to a file


def save_to_file(story):
    with open("story.txt", "w") as f:
        f.write(story)

# Define the main function that runs story


def main():
    # Print an introduction message
    intro()
    template_content = read_template(
        "../assets/dark_and_stormy_night_template.txt")
    stripped, parts = parse_template(template_content)
    words = user_input(parts)
    # begin
    new_story = merge(stripped, words)
