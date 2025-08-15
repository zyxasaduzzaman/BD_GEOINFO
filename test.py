from bd_geoinfo.districts import *
from bd_geoinfo.divisions import *
from bd_geoinfo.terminal import *
from bd_geoinfo.upzilas import *
import json
import os

# c = Division("rangpur")
# divs = c.get_division_names()
# divsId = [i for i in range(1,9)]
# print(divs)
# b = District("Thakurgaon")
# districts = b.get_district_names()
# data = []
# for i in districts:
#     mm = District(i)
#     data.append([f"district_id :{mm.get_id()}",f"district_name:{i}",
#                  f"division_id:{divs.index(mm.get_division())+1}",f"division_name:{mm.get_division()}"])


up = Upazila("Thakurgaon Sadar")
up_all = up.get_upazila_names()


# with open("test.json","r",encoding="utf-8") as f:
#     data = json.load(f)

# m_data = data['up']

# name = [key for d in m_data for key in d.keys()]


# with open("upazilas.json", "r", encoding="utf-8") as file:
#     da = json.load(file)


# ra_data = da['upazilas']

# for i in ra_data:
#     if i['name'] in name:
#         i['unions_count']=

