from bd_geoinfo.districts import *
from bd_geoinfo.divisions import *
from bd_geoinfo.terminal import *

c = Division("rangpur")
divs = c.get_division_names()
divsId = [i for i in range(1,9)]
print(divs)
b = District("Thakurgaon")
districts = b.get_district_names()
data = []
for i in districts:
    mm = District(i)
    data.append([f"district_id :{mm.get_id()}",f"district_name:{i}",
                 f"division_id:{divs.index(mm.get_division())+1}",f"division_name:{mm.get_division()}"])




