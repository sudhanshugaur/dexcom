import pytest
import requests
from functools import reduce
import json

# @pytest.mark.parametrize("end_points", ["https://api.dexcom.com/info", "https://sandbox-api.dexcom.com/info"])
# def test_other_values(end_points):
#     res_json = requests.get(end_points).json()
#     print(len(res_json))
#     dexcom_sub_comp = []
#     for ele in res_json:
#         if ele["Product Name"] == "Dexcom API":
#             assert ele["UDI / Device Identifier"] == "00386270000668"
#             # assert ele["UDI / Production Identifier"]["Version"] == "3.7.0.0"
#             assert ele["UDI / Production Identifier"]["Part Number (PN)"] == "350-0019"
#             dexcom_sub_comp = ele['UDI / Production Identifier']['Sub-Components']
#     print(f"for URL: {end_points}, the value of UDI / Production Identifier']['Sub-Components']= {dexcom_sub_comp}")
#
#     dexcom_sub_comp_values = []
#     for val in dexcom_sub_comp:
#         dexcom_sub_comp_values.append(list(val.values()))
#     single_list = reduce(lambda x, y: x + y, dexcom_sub_comp_values)
#     assert "api-gateway" in single_list


# @pytest.mark.parametrize("urls", ["https://api.dexcom.com/info", "https://sandbox-api.dexcom.com/info"])
# def test_status_and_content_type(urls):
#     res = requests.get(urls)
#     # print(res.headers)
#     assert res.status_code == 200
#     assert res.headers['Content-Type'] == "application/json"

import xml.etree.ElementTree as ET
def test_status_and_content_type():
    headers = {'Content-Type': 'application/xml'}
    res = requests.get("https://api.dexcom.com/info", headers=headers)
    print(res)
    # # xmlDict = {}
    # root = ET.fromstring(res.content)
    # for child in root.iter('*'):
    #     print(child.tag)