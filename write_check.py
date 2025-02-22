import os

def can_write_to_file(file_path):
    try:
        # Attempt to open the file in write mode
        with open(file_path, mode='w') as file:
            file.write('Test write\n')  # Try writing a test string to the file
        print(f"Write access to {file_path} is successful.")
        return True
    except Exception as e:
        print(f"Failed to write to {file_path}. Error: {e}")
        return False

if __name__ == "__main__":
    # Specify the file path
    file_path = os.path.abspath("security_results.json")

    # Check if it is possible to write to the file
    can_write_to_file(file_path)
