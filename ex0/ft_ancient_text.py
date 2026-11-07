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
        print("---\n")
        print(f"File '{file}' closed.")
    except OSError as e:
        print(f"Error: {e}")
    except UnicodeDecodeError:
        print(f"Error: File {file} contains invalid text.")
    finally:
        text.close()
        print(f"Closing {file}.")


if __name__ == "__main__":
    main()
