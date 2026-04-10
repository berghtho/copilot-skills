"""String utility functions for daily use."""

import re
import unicodedata


def slugify(text: str) -> str:
    """Convert a string to a URL-friendly slug.

    Example:
        >>> slugify("Hello World!")
        'hello-world'
    """
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s]+", "-", text).strip("-")


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate *text* to *max_length* characters, appending *suffix* if trimmed.

    Example:
        >>> truncate("Hello, World!", 8)
        'Hello...'
    """
    if len(text) <= max_length:
        return text
    if max_length <= len(suffix):
        return suffix[:max_length]
    return text[: max_length - len(suffix)] + suffix


def camel_to_snake(name: str) -> str:
    """Convert a camelCase or PascalCase string to snake_case.

    Example:
        >>> camel_to_snake("myVariableName")
        'my_variable_name'
    """
    name = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def snake_to_camel(name: str) -> str:
    """Convert a snake_case string to camelCase.

    Example:
        >>> snake_to_camel("my_variable_name")
        'myVariableName'
    """
    if name == "":
        return ""
    components = name.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def strip_html(html: str) -> str:
    """Remove HTML tags from a string.

    Example:
        >>> strip_html("<p>Hello <b>World</b></p>")
        'Hello World'
    """
    return re.sub(r"<[^>]+>", "", html)
