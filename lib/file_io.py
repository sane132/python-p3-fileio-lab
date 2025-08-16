def write_file(file_name, file_content):
    """
    Creates a new .txt file with the given content.
    If the file exists, it will be overwritten.
    """
    with open(f"{file_name}.txt", mode='w', encoding='utf-8') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """
    Appends content to an existing .txt file.
    Creates the file if it doesn't exist.
    """
    with open(f"{file_name}.txt", mode='a', encoding='utf-8') as file:
        file.write(append_content)

def read_file(file_name):
    """
    Reads and returns the content of a .txt file.
    Returns an empty string if file doesn't exist.
    """
    try:
        with open(f"{file_name}.txt", encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return ""