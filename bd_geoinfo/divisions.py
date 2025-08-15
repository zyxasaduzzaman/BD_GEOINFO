import json
import os

class Division:
    """
    Division class to manage and retrieve information about divisions from a JSON data source.

    Usage:
        div = Division("Dhaka")
        print(div.get_name())
        print(div.get_area(unit="mile"))
        print(div.has_division())
        # etc.
    """

    __data = None  # class variable to hold loaded data

    def __init__(self, div_name: str):
        """
        Initialize Division instance with division name (English or Bangla).

        :param div_name: Name of the division (English or Bangla)
        """
        self.name = div_name.strip()
        if Division.__data is None:
            Division.__data = self._load_data()
        self.division_data = self._get_division_data()

    @classmethod
    def _data_file(cls):
        """Returns the absolute path to the divisions.json file."""
        current_dir = os.path.dirname(__file__)
        return os.path.abspath(os.path.join(current_dir, "data", "divisions.json"))

    @classmethod
    def _load_data(cls):
        """Load division data from JSON file once and cache it."""
        file_path = cls._data_file()
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    @classmethod
    def get_all_divisions_info(cls) -> dict:
        """Returns the full JSON data of all divisions."""
        if cls.__data is None:
            cls.__data = cls._load_data()
        return cls.__data

    @classmethod
    def get_division_names(cls, bn: bool = False) -> list:
        """Returns a list of all division names."""
        data = cls.get_all_divisions_info()
        return [div["bn_name"] if bn else div["name"] for div in data["divisions"]]

    def _get_division_data(self) -> dict | None:
        """Get the JSON data dict of the current division instance."""
        data = self.get_all_divisions_info()
        for div in data["divisions"]:
            if div["name"].strip().lower() == self.name.lower() or div["bn_name"] == self.name:
                return div
        return None

    def has_division(self) -> bool:
        """Check if the division exists in the data."""
        return self.division_data is not None

    def get_name(self, bn: bool = False) -> str:
        """Get the division name in English or Bangla."""
        if not self.division_data:
            return ""
        return self.division_data["bn_name"] if bn else self.division_data["name"]

    def get_id(self) -> int | None:
        """Returns the division ID."""
        if not self.division_data:
            return None
        return self.division_data.get("id")

    def get_map(self) -> str:
        """Returns a string like 'map:lat,long' for Google Maps."""
        if not self.division_data:
            return ""
        return f"map:{self.division_data['lat']},{self.division_data['long']}"

    def get_lat_long(self) -> list:
        """Returns [latitude, longitude]."""
        if not self.division_data:
            return []
        return [self.division_data['lat'], self.division_data['long']]

    def get_area(self, unit: str = "km") -> dict | None:
        """Returns the area of the division in km² or miles²."""
        if not self.division_data:
            return None
        area_km2 = self.division_data.get("area_km2")
        if area_km2 is None:
            return None
        if unit.lower() == "mile":
            return {"unit": "mile", "value": round(area_km2 * 0.386102, 2)}
        return {"unit": "km", "value": area_km2}

    def get_headquarter(self) -> dict | None:
        """Returns headquarter information dict or None."""
        if not self.division_data:
            return None
        return self.division_data.get("headquarter")

    def get_population(self) -> dict | None:
        """Returns population data with year."""
        if not self.division_data:
            return None
        return {
            "population": self.division_data.get("population"),
            "population_year": self.division_data.get("population_year")
        }

    def get_districts(self) -> dict | None:
        """Returns districts count and list."""
        if not self.division_data:
            return None
        return {
            "districts": self.division_data.get("districts", [])
        }

    def get_stats(self) -> dict | None:
        """Returns various statistics of the division."""
        if not self.division_data:
            return None
        return {
            "literacy_rate": self.division_data.get("literacy_rate"),
            "hospitals_count": self.division_data.get("hospitals_count"),
            "schools_count": self.division_data.get("schools_count"),
            "police_stations": self.division_data.get("police_stations"),
             "districts_count": self.division_data.get("districts_count"),
           "courts": self.division_data.get("courts"),
            "voter_population": self.division_data.get("voter_population"),
            "polling_centers": self.division_data.get("polling_centers")
        }

    def get_weather(self) -> dict | None:
        """Returns average weather info."""
        if not self.division_data:
            return None
        return {
            "avg_temp_celsius": self.division_data.get("avg_temp_celsius"),
            "avg_rainfall_mm": self.division_data.get("avg_rainfall_mm"),
            "weather_zone": self.division_data.get("weather_zone")
        }

    def get_tourist_spots(self) -> list:
        """Returns list of tourist spots."""
        if not self.division_data:
            return []
        return self.division_data.get("tourist_spots", [])

    def get_festivals(self) -> list:
        """Returns list of festivals."""
        if not self.division_data:
            return []
        return self.division_data.get("festivals", [])

    def get_cultural_heritage(self) -> list:
        """Returns list of cultural heritage items."""
        if not self.division_data:
            return []
        return self.division_data.get("cultural_heritage", [])

    def get_notes(self) -> str:
        """Returns notes or description string."""
        if not self.division_data:
            return ""
        return self.division_data.get("notes", "")

    def get_website(self) -> str:
        """Returns official website URL."""
        if not self.division_data:
            return ""
        return self.division_data.get("website", "")

    def get_established_date(self) -> str:
        """Returns establishment date string (e.g. 'YYYY-MM-DD')."""
        if not self.division_data:
            return ""
        return self.division_data.get("established", "")
