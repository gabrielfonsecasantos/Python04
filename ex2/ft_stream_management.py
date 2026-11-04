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
        text.close()
    except OSError as e:
        print(f"[STDERR] Error opening file '{file}': {e}", file=sys.stderr)
        return
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
        print("Enter new file name (or empty): ", end="")
        sys.stdout.flush()
        new_file_name: str = sys.stdin.readline()
        if new_file_name != "" and new_file_name[-1] == '\n':
            new_file_name = new_file_name[:-1]
            
        if new_file_name == "":
            print("Not saving data.")
        else:
            new_file: typing.TextIO = open(new_file_name, "w")
            print(f"Saving data to '{new_file_name}'")
            new_file.write(transformed_content)
            new_file.close()
            print(f"Data saved in file '{new_file_name}'.\n")
    except OSError as e:
        print(f"Error on new file: {e}", file=sys.stderr)
        print("Data not saved.")
        return



if __name__ == "__main__":
    main()
