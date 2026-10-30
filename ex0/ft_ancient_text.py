import sys
import typing

if __name__ == "__main__":
  print("=== Cyber Archives Recovery ===\n")
  file = sys.argv[0]
  print(f"file name: {file}")
  text: typing.IO = open(file)
  print(text.read())

