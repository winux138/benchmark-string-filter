import typing

from benchmark_string_filter.benchmark import st_time


@st_time
def detect_special_characters(
    input_str: str,
) -> typing.Tuple[bool, typing.Optional[str]]:
    """Check if input string contains any characters not in the whitelist."""
    whitelist = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for char in input_str:
        if char not in whitelist:
            return True, char
    return False, None
