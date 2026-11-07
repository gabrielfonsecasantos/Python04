import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===\n")

    file: str = sys.argv[1]
    print(f"Accessing file '{file}'")
    try:
        text: typing.TextIO = open(file)
        print("---\n")
        content: str = text.read()
        print(content)
        print("\n---")
    except OSError as e:
        print(f"Error: {e}")
        return
    except UnicodeDecodeError:
        print(f"Error: File {file} contains invalid text.")
    finally:
        print(f"Closing '{file}'.")

    print("Transform data:\n---\n")
    transformed_content: str = ""
    for char in content:
        if char == '\n':
            transformed_content += "#\n"
        else:
            transformed_content += char

    if transformed_content != "" and content[-1] != '\n':
        transformed_content += "#\n"

    print(transformed_content)
    print("---")

    try:
        new_file_name: str = input("Enter new file name (or empty): ")
        if new_file_name == "":
            print("Not saving data.")
        else:
            new_file: typing.TextIO = open(new_file_name, "w")
            print(f"Saving data to '{new_file_name}'")
            new_file.write(transformed_content)
            new_file.close()
            print(f"Data saved in file '{new_file_name}'.\n")
    except OSError as e:
        print(f"Error on new file: {e}")
        print("Data not saved.")
        return
    finally:
        print(f"Closing {new_file_name}.")
        new_file_name.close()


if __name__ == "__main__":
    main()
