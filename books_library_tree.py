#Implementing as binary tree:
#Pros: O(logn) search and insertion.
#Cons: Harder to implement than a list. Extra space for tree nodes.



class Book:
    def __init__(self, title, authors, genre, publication_year, isbn=None):
        self.title = title
        self.authors = authors
        self.genre = genre
        self.publication_year = publication_year
        self.isbn = isbn

    def __str__(self):
        return (f"Title: {self.title}, Authors: {', '.join(self.authors)}, "
                f"Genre: {self.genre}, Year: {self.publication_year}, "
                f"ISBN: {self.isbn or 'N/A'}")


class TreeNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


class LibraryBST:
    def __init__(self):
        self.root = None

    def insert(self, book):
        new_node = TreeNode(book)
        if not self.root:
            self.root = new_node
            print(f"Book '{book.title}' added successfully as the root.")
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.book.title.lower() < current.book.title.lower():
            if current.left:
                self._insert_recursive(current.left, new_node)
            else:
                current.left = new_node
                print(f"Book '{new_node.book.title}' added to the left of '{current.book.title}'.")
        elif new_node.book.title.lower() > current.book.title.lower():
            if current.right:
                self._insert_recursive(current.right, new_node)
            else:
                current.right = new_node
                print(f"Book '{new_node.book.title}' added to the right of '{current.book.title}'.")
        else:
            print(f"Book '{new_node.book.title}' already exists in the library.")

    def search_by_title(self, title):
        return self._search_title_recursive(self.root, title.lower())

    def _search_title_recursive(self, current, title):
        if not current:
            print(f"No book found with title '{title}'.")
            return None
        if current.book.title.lower() == title:
            print(f"Book found: {current.book}")
            return current.book
        elif title < current.book.title.lower():
            return self._search_title_recursive(current.left, title)
        else:
            return self._search_title_recursive(current.right, title)

    def inorder_traversal(self):
        print("Library Catalog (Inorder Traversal):")
        self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, current):
        if current:
            self._inorder_traversal_recursive(current.left)
            print(current.book)
            self._inorder_traversal_recursive(current.right)


