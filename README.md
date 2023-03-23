# madlib-cli

## LAB 03

### Project: File IO and Exceptions

Create a madlib game that prompts the user for inputs and placing these inputs into the correct position within the template. Return the completed results to the user in the command line.

#### Author: Dutch Foy

#### Links and Resources

- [Stack Overflow](https://stackoverflow.com/)
- [Single-responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle)
- [Madlib File Template](https://codefellows.github.io/code-401-python-guide/curriculum/class-03/lab/assets/make_me_a_video_game_template.txt)



#### Setup
- .venv requirements
- connect local repo to GitHub
- install packages (such as pytest, pip freeze, etc.)

##### How to initialize/run your application (where applicable)

- pytest-watch - runs tests
- python madlib.py - executes the code, prompting the user and returning results


##### Tests
- How do you run tests?
  - import pytest
  - from package_name.module_name import function_name
  - create tests (example: def test_read_template()) to check if the function or code is running properly without errors
  - pytest-watch on terminal (to run tests as you modify the code)
- Any tests of note?
  - attention to detail, small things like : instead of = can cause errors
- Describe any tests that you did not complete, skipped, etc
  - need to create a function parse_template() in order to test it
  - need to create a function merge() in order to test it
