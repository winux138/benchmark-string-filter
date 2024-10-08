from benchmark_string_filter.default import detect_special_characters
from benchmark_string_filter.samples import *

def main() -> None:
    (is_valid, e) = detect_special_characters(lorem_ipsum_100000_valid)
    print(f'{is_valid} - "{e}"')


if __name__ == "__main__":
    main()
