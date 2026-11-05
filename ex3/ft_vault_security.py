def secure_archive(
    file_name: str, opt: int = 1, input_content: str = ""
) -> tuple[bool, str]:
    try:
        if opt == 1:
            with open(file_name, "r") as f:
                content: str = f.read()
            return True, content
        elif opt == 0:
            with open(file_name, "w") as f:
                f.write(input_content)
            return True, "Content successfully written to file"
        else:
            return False, "Invalid action."
    except OSError as e:
        error: str = str(e)
        return False, error


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive('sample.txt', 1)}\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print("\n")

    print("Using 'secure_archive' to read from a regular file:")
    print(f"{secure_archive('sample1.txt', 1)}\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    print(f"{secure_archive('sample.txt', 0, 'mundo')}")
