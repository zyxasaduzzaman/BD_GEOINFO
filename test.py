from bd_geoinfo.upzilas import Upazila
from bd_geoinfo.divisions import Division
from bd_geoinfo.districts import District
from bd_geoinfo.terminal import *


add_to_terminal(Division("Rangpur").get_division_names())
show_terminal()