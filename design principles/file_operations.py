from abc import ABC, abstractmethod
import os

class DataStorage(ABC):
    #Abstract base class for data storage.

    @abstractmethod
    def write(self, key, value):
        pass

    @abstractmethod
    def read(self, key):
        pass

    @abstractmethod
    def delete(self, key):
        pass

class FileStorage(DataStorage):
    def __init__(self, directory):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def write(self, key, value):
        filepath = os.path.join(self.directory, f"{key}.txt")
        with open(filepath, 'w') as file:
            file.write(value)
        print(f"Data written to {filepath}.")

    def read(self, key):
        filepath = os.path.join(self.directory, f"{key}.txt")
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"No file found for key '{key}'.")
        with open(filepath, 'r') as file:
            data = file.read()
        print(f"Data read from {filepath}: {data}")
        return data

    def delete(self, key):
        filepath = os.path.join(self.directory, f"{key}.txt")
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"File {filepath} deleted.")
        else:
            print(f"File {filepath} does not exist.")

def main():
    directory = "data_storage"
    storage = FileStorage(directory)
    storage.write("username", "JohnDoe")
    storage.write("email", "john.doe@example.com")

    #Read data
    try:
        username = storage.read("username")
        email = storage.read("email")
        print(f"Username: {username}")
        print(f"Email: {email}")
    except FileNotFoundError as e:
        print(e)

    #Delete data
    storage.delete("username")
    storage.delete("email")

if __name__ == "__main__":
    main()
