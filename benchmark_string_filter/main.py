from benchmark_string_filter.default import detect_special_characters

def main() -> None:
    (is_valid, e) = detect_special_characters("Hello, World!")
    print(f'{is_valid} - "{e}"')


if __name__ == "__main__":
    main()
