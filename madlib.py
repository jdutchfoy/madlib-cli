def read_template(path):
    """
    Read a template file from disk and return its contents as a string.
    """
    try:
        with open(path) as file:
            return file.read().strip()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise

def parse_template(template):
    """
    Parse a Madlib template string and return a tuple of its text with
    placeholders removed and a list of the placeholders.
    """
    placeholders = []
    parsed_template = ""

    in_placeholder = False
    current_placeholder = ""

    for char in template:
        if char == "{":
            in_placeholder = True
        elif char == "}":
            in_placeholder = False
            parsed_template += "{}"
            placeholders.append(current_placeholder.strip())
            current_placeholder = ""
        elif in_placeholder:
            current_placeholder += char
        else:
            parsed_template += char

    return parsed_template, placeholders


def merge(template, words):
    """
    Merge a Madlib template string with user-submitted words and return
    the result.
    """
    return template.format(*words)
