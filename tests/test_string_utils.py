"""Tests for string_utils module."""

import pytest
from skills.string_utils import (
    camel_to_snake,
    slugify,
    snake_to_camel,
    strip_html,
    truncate,
)


class TestSlugify:
    def test_basic(self):
        assert slugify("Hello World!") == "hello-world"

    def test_multiple_spaces(self):
        assert slugify("  Hello   World  ") == "hello-world"

    def test_special_characters(self):
        assert slugify("café & crêpes") == "cafe-crepes"

    def test_already_slug(self):
        assert slugify("hello-world") == "hello-world"

    def test_empty_string(self):
        assert slugify("") == ""


class TestTruncate:
    def test_short_string_unchanged(self):
        assert truncate("Hi", 10) == "Hi"

    def test_exact_length_unchanged(self):
        assert truncate("Hello", 5) == "Hello"

    def test_truncation_with_suffix(self):
        assert truncate("Hello, World!", 8) == "Hello..."

    def test_custom_suffix(self):
        assert truncate("Hello, World!", 8, suffix="…") == "Hello, …"

    def test_no_suffix(self):
        assert truncate("Hello, World!", 5, suffix="") == "Hello"


class TestCamelToSnake:
    def test_camel_case(self):
        assert camel_to_snake("myVariableName") == "my_variable_name"

    def test_pascal_case(self):
        assert camel_to_snake("MyClassName") == "my_class_name"

    def test_already_snake(self):
        assert camel_to_snake("my_variable") == "my_variable"

    def test_single_word(self):
        assert camel_to_snake("hello") == "hello"


class TestSnakeToCamel:
    def test_basic(self):
        assert snake_to_camel("my_variable_name") == "myVariableName"

    def test_single_word(self):
        assert snake_to_camel("hello") == "hello"

    def test_already_camel(self):
        assert snake_to_camel("hello") == "hello"


class TestStripHtml:
    def test_basic_tags(self):
        assert strip_html("<p>Hello <b>World</b></p>") == "Hello World"

    def test_no_tags(self):
        assert strip_html("plain text") == "plain text"

    def test_empty_string(self):
        assert strip_html("") == ""

    def test_self_closing_tag(self):
        assert strip_html("line1<br/>line2") == "line1line2"
