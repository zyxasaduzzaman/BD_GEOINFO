# 🌍 BD-GeoInfo

[![PyPI version](https://badge.fury.io/py/bd-geoinfo.svg)](https://pypi.org/project/bd-geoinfo/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)

🔎 **A simple yet powerful Python library for fetching geographical information about Bangladesh.**

---

## ✨ Key Features
- 📍 **Comprehensive Data:** Access detailed information about **divisions, districts, upazilas, unions, and postcodes** (name, population, area, etc.).  
- 🌐 **Bangla & English Support:** Search for and retrieve data using both **Bangla and English names**.  
- ⚡ **Easy to Use:** Intuitive **class-based interface** for effortless data access.  
- 🖥️ **Terminal Viewer:** Visualize your output directly in a **stylish HTML terminal window**.  

---

## 🚀 Installation
Install the library using pip:

```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps bd-geoinfo==0.0.1
👨‍💻 Usage
📌 Getting Division Info
python
Copy
Edit
from bd_geoinfo import Division

dhaka = Division("Dhaka")
if dhaka.has_division():
    print(f"Name (EN): {dhaka.get_name()}")
    print(f"Name (BN): {dhaka.get_name(bn=True)}")
    print(f"Area: {dhaka.get_area()} sq km")
    print(f"Districts: {dhaka.get_districts()}")
📌 Getting District Info
python
Copy
Edit
from bd_geoinfo import District

sylhet = District("সিলেট")
if sylhet.has_district():
    print(f"Name (EN): {sylhet.get_name()}")
    print(f"Division: {sylhet.get_division()}")
    print(f"Upazilas: {sylhet.get_upazilas()}")
📌 Getting Upazila Info
python
Copy
Edit
from bd_geoinfo import Upazila

amtali = Upazila("Amtali")
if amtali.has_upazila():
    print(f"Name (BN): {amtali.get_name(bn=True)}")
    print(f"District: {amtali.get_district()}")
    print(f"Unions Count: {amtali.get_unions_count()}")
📌 Getting Union Info
python
Copy
Edit
from bd_geoinfo import Union

burirchar = Union("Burirchar Union")
if burirchar.has_union():
    print(f"Name (EN): {burirchar.get_name()}")
    print(f"Full Address (BN): {burirchar.get_full_address(bn=True)}")
📌 Getting Postcode Info
python
Copy
Edit
from bd_geoinfo import Postcode

postcode = Postcode("8710")
if postcode.has_postcode():
    print(f"Area: {postcode.get_name(bn=True)}")
    print(f"Upazila: {postcode.get_upazila()}")
    print(f"District: {postcode.get_district()}")
    print(f"Division: {postcode.get_division()}")
🖥️ Using the Terminal Viewer
python
Copy
Edit
from bd_geoinfo import add_to_terminal, show_terminal

add_to_terminal("Welcome to BD-GeoInfo Terminal!")
add_to_terminal("Checking Sylhet division info...")

# Pass any data to add_to_terminal()
from bd_geoinfo import Division
sylhet_div = Division("Sylhet")
add_to_terminal(sylhet_div.get_division_data())

# Show all the data
show_terminal()
🤝 Contribution
Your contributions are always welcome! 🎉
If you have any feature requests, bug reports, or code suggestions, feel free to submit a Pull Request or open an Issue.

📂 Data Source
All geographical information is stored as static JSON files inside the package (bd-geoinfo/data/).
If you find any inaccuracies or want to add new data, please submit an issue or a PR.

📜 License
This project is licensed under the MIT License.