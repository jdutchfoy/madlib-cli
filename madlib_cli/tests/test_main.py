import os
import pytest
from click.testing import CliRunner
from madlib_cli import __version__
from madlib_cli.main import intro, parse_template, merge, main


def test_intro():
    result = intro()
    assert isinstance(result, str)


def test_parse_template():
    template = "It was a {Adjective} and {Adjective} {Noun}."
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")
    actual_stripped, actual_parts = parse_template(template)
    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


def test_merge():
    template = "It was a {} and {} {}."
    words = ("dark", "stormy", "night")
    expected = "It was a dark and stormy night."
    actual = merge(template, words)
    assert actual == expected


def test_main(monkeypatch):
    input_values = ["dark", "stormy", "night"]
    def mock_input(prompt):
        return input_values.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, ['--template', 'assets/dark_and_stormy_night_template.txt', '--output', 'output.txt'])
        assert result.exit_code == 0
        assert result.output == "It was a dark and stormy night.\n"

        with open('output.txt', 'r') as file:
            contents = file.read()
            assert contents.strip() == "It was a dark and stormy night."
