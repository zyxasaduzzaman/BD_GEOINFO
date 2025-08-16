import json
import os

class Union:
    """
    Union class to manage and retrieve information about unions from a JSON data source.

    Usage Example:
        u = Union("Dhalua Union")
        print(u.has_union())         # True or False
        print(u.get_name())          # Returns English name
        print(u.get_name(bn=True))   # Returns Bangla name
        print(u.get_upazila())       # Returns upazila name
        print(u.get_district())      # Returns district name
        print(u.get_division())      # Returns division name
        print(u.get_full_address())  # Returns full address as string
    """

    __data = None  # Class variable to hold loaded JSON data (cached)

    def __init__(self, union_name: str):
        """
        Initialize a Union instance with a given union name.

        :param union_name: Union name in English or Bangla
        """
        self.name = union_name.strip()
        if Union.__data is None:
            Union.__data = self._load_data()
        self.union_data = self._get_union_data()

    @classmethod
    def _data_file(cls):
        """
        Get the absolute path to the unions.json file.

        :return: Absolute file path as string
        """
        current_dir = os.path.dirname(__file__)
        return os.path.abspath(os.path.join(current_dir, "data", "unions.json"))

    @classmethod
    def _load_data(cls):
        """
        Load union data from JSON file. 
        Returns only the list of unions for easier access.

        :return: List of unions
        """
        with open(cls._data_file(), "r", encoding="utf-8") as f:
            data = json.load(f)
            # Handle both dict {"unions": [...]} or list [...]
            if isinstance(data, dict) and "unions" in data:
                return data["unions"]
            elif isinstance(data, list):
                return data
            return []

    @classmethod
    def get_all_unions_info(cls) -> list:
        """
        Return the complete union dataset.

        :return: List of all union dictionaries
        """
        if cls.__data is None:
            cls.__data = cls._load_data()
        return cls.__data

    def _get_union_data(self):
        """
        Find and return the union data matching the instance name.

        Match is case-insensitive for English names and exact match for Bangla names.

        :return: Dictionary of union data or None if not found
        """
        for u in self.get_all_unions_info():
            # English name match
            if u.get("name", "").strip().lower() == self.name.lower():
                return u
            # Bangla name match
            if u.get("bn_name", "").strip() == self.name:
                return u
        return None

    def has_union(self) -> bool:
        """
        Check if the union exists in the dataset.

        :return: True if exists, False otherwise
        """
        return self.union_data is not None

    def get_name(self, bn: bool = False) -> str:
        """
        Get the union's name.

        :param bn: If True, return Bangla name; else return English name
        :return: Name string
        """
        if not self.union_data:
            return ""
        return self.union_data["bn_name"] if bn else self.union_data["name"]

    def get_upazila(self) -> str:
        """
        Get the upazila/sub-district of the union.

        :return: Upazila name string
        """
        if not self.union_data:
            return ""
        return self.union_data.get("upazila_name", "")

    def get_district(self) -> str:
        """
        Get the district of the union.

        :return: District name string
        """
        if not self.union_data:
            return ""
        return self.union_data.get("district_name", "")

    def get_division(self) -> str:
        """
        Get the division of the union.

        :return: Division name string
        """
        if not self.union_data:
            return ""
        return self.union_data.get("division_name", "")

    def get_full_address(self, bn: bool = False) -> str:
        """
        Get the full address of the union as a formatted string.

        :param bn: If True, return address in Bangla; else return in English
        :return: Full address string
        """
        if not self.union_data:
            return ""
        if bn:
            return f"{self.union_data['bn_name']}, {self.union_data['upazila_name']}, {self.union_data['district_name']}, {self.union_data['division_name']}"
        return f"{self.union_data['name']}, {self.union_data['upazila_name']}, {self.union_data['district_name']}, {self.union_data['division_name']}"
