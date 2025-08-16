from bd_geoinfo.upzilas import Upazila
from bd_geoinfo.divisions import Division
from bd_geoinfo.districts import District
from bd_geoinfo.terminal import *
from bd_geoinfo.unions import *
from bd_geoinfo.postcodes import *


p = Postcode("8718")
print(p.get_full_address())

