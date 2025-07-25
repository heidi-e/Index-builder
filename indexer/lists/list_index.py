from typing import Optional, Any, List, Generator
from indexer.abstract_index import AbstractIndex


class ListIndex(AbstractIndex):
    """
    A list data structure implementation of an index.
    This class represents a list index, which allows for simple insertion and search operations, especially for
    sequential processing.

    Methods:
        insert(key: Any, value: Any) -> None:
            Inserts a new key-value pair into the list
        search(key: Any) -> List[Any]:
            Searches for tuple with given key in the list and returns their values
        get_keys_in_order() -> List[Any]:
            Returns a list of keys in the list in ascending order.
        count_keys() -> int:
            Returns the number of unique keys in the list
        get_avg_value_list_len() -> float:
            Calculates the average length of values in the list
    """

    def __init__(self):
        super().__init__()
        self.list_index = []  


    def insert(self, key: Any, value: Any) -> None:
        """
        Inserts a key-value pair into the index.
        If the key already exists, the value is appended to its list.
        """

        for entry in self.list_index:
            if entry[0] == key:
                entry[1].append(value)
                
        return self.list_index.append((key, [value]))

    def search(self, key: Any) -> List[Any]:
        """
        Searches for values associated with the given key.
        Returns a list of values, or an empty list if the key is not found.
        """
        values = []
        for entry in self.list_index:
            if entry[0] == key:
                values.extend(entry[1])

        if not values:
            return []

        return values


    def get_keys_in_order(self) -> List[Any]:
        """
        Returns a list of all keys in the index in ascending order.
        """
        return sorted([entry[0] for entry in self.list_index])

    def count_keys(self) -> int:
        """
        Returns the number of unique keys in the index.
        """
        return len(self.list_index)

    def get_avg_value_list_len(self) -> float:
        """
        Calculates the average number of values stored per key.
        """
        if not self.list_index:
            return 0.0

        total_values = sum(len(entry[1]) for entry in self.list_index)

        return total_values / len(self.list_index)

    def __iter__(self):
        return iter(self.list_index)
