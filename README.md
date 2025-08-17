

# I LOVE MY BANGLADESH

---

<img src="bn.png" alt="Logo" style="width:100%; height:auto;background-color:black;">

---

# Package Name : bd-geoinfo

---
[![PyPI version](https://badge.fury.io/py/bd-geoinfo.svg)](https://pypi.org/project/bd-geoinfo/) [![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/) [![Developer Facebook](https://img.shields.io/badge/Facebook-magenta)](https://www.facebook.com/zyxasaduzzaman) [![Developer Facebook](https://img.shields.io/badge/LinkedIn-orange)](https://www.linkedin.com/in/asaduzzaman-asad-801a80323/)

**A simple yet powerful Python library for fetching comprehensive geographical information about Bangladesh.**

### Key Features :

* **🔍 Data Search:** Easily find detailed information on divisions, districts, upazilas, unions, and postcodes.

* **🌐 Multilingual Support:** Access data using both Bangla and English geographical names.

* **📊 Detailed Information:** Get population, area, and other relevant data for each location.

* **💡 Interactive Terminal:** Use a built-in terminal viewer to display your program's output in a stylish, live-like interface.

---

## Installation :

**Install this library from PyPI using pip:**

```bash
pip install bd-geoinfo

```

## Usage :

**Using this library is straightforward. Here are a few examples to get you started.**

#### 🗺️ Accessing Geographical Data

```bash

from bd_geoinfo import Division, District, Upazila, Union, Postcode

```

##### Or


```bash

from bd_geoinfo import *

```

---

**Get Information About Division**

```bash

dhaka = Division("Dhaka")
print(f"Name (BN): {dhaka.get_name()}")
print(f"All Division name {dhaka.get_division_names()}")


```

---

**Get Information About District**

```bash

mymensingh = District("Mymensingh")
print(f"Name (EN): {mymensingh.get_name()}")
print(f"Division: {mymensingh.get_division()}")

```

---

**Get Information About Upazila**

```bash

amtali = Upazila("Amtali")
print(f"Is Upzila : {has_upazila()})

```

---

**Get Information About Union**

```bash

burirchar = Union("Burirchar Union")
print(burirchar.get_upazila())

```

---

**Get Information About Postcode**

```bash

postcode = Postcode("8710")
print(f"Area Name: {postcode.get_name()}")
print(f"Upazila: {postcode.get_upazila()}")

```

---

#### 🖥️ Interactive Terminal Viewer

**Use these built-in functions to display your output more attractively. This is especially useful for visualizing data in a clean, terminal-like format.**

```bash
from bd_geoinfo import Division, add_to_terminal, show_terminal, clear_from_terminal

# Clear the terminal output
clear_from_terminal()

# Add a welcome message
add_to_terminal("Welcome to the BD-GeoInfo Terminal!")
add_to_terminal("Fetching data for Sylhet Division...")

# Create a Division object
sylhet_division = Division("Sylhet")

# Add the division's data to the terminal
add_to_terminal(sylhet_division.get_division_data())
add_to_terminal("Data loaded successfully.")

# Display the terminal window
show_terminal()

```
---


### ✨ Acknowledgements

**A big thank you to the following people who helped make this project a reality by collecting data:**

* **Naim Islam:** For providing your  valuabel time.**--Mnt(TPI)**
* **Monir:** For providing your valuabel time.**--RAC(TPI)**
* **Habib:**  For providing your valuabel time.**--FOOD(TPI)**

---

### Contribution

**Your contributions are highly valued! If you have any feature requests, bug reports, or code suggestions, please feel free to submit a Pull Request or open an Issue on the GitHub repository.**

