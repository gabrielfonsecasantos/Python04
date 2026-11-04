import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===\n")

    file: str = sys.argv[1]
    print(f"Accessing file '{file}'")
    try:
        text: typing.TextIO = open(file)
        print("---\n")
        print(text.read())
        print("\n")
        print("---")
        text.close()
    except OSError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
