from indexer.abstract_index import AbstractIndex




class ListIndex(AbstractIndex):
    """
    A list data structure implementation of an index.
    This class represents a list index, which allows for simple insertion and search operations, especially for
    sequential processing.

    Stores key-value pairs where each key can have multiple associated values.
    """

    def __init__(self):
        self.index = []  # List to store (key, values_list) pairs

    def insert(self, key: Any, value: Any) -> None:
        """
        Inserts a key-value pair into the index.
        If the key already exists, the value is appended to its list.
        """
        for entry in self.index:
            if entry[0] == key:
                entry[1].append(value)
                return
        # If key is not found, add a new entry
        self.index.append((key, [value]))

    def search(self, key: Any) -> List[Any]:
        """
        Searches for values associated with the given key.
        Returns a list of values, or an empty list if the key is not found.
        """
        for entry in self.index:
            if entry[0] == key:
                return entry[1]
        return []

    def get_keys(self) -> List[Any]:
        """
        Returns a list of all keys in the index.
        """
        return [entry[0] for entry in self.index]

    def count_nodes(self) -> int:
        """
        Returns the number of unique keys in the index.
        """
        return len(self.index)

    def get_avg_value_list_len(self) -> float:
        """
        Calculates the average number of values stored per key.
        """
        if not self.index:
            return 0.0
        total_values = sum(len(entry[1]) for entry in self.index)
        return total_values / len(self.index)
