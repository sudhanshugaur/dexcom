from functools import reduce

import pytest
import requests
import json


@pytest.mark.parametrize("end_points", ["https://api.dexcom.com/info", "https://sandbox-api.dexcom.com/info"])
def test_response(end_points):
    res_json = requests.get(end_points).json()
    for ele in res_json:
        if ele["Product Name"] == "Dexcom API":
            assert ele["UDI / Device Identifier"] == "00386270000668"
            assert ele["UDI / Production Identifier"]["Part Number (PN)"] == "350-0019"
            assert ele["UDI / Production Identifier"]["Version"] == "3.7.0.0"


@pytest.mark.parametrize("end_points", ["https://api.dexcom.com/info", "https://sandbox-api.dexcom.com/info"])
def test_response_sub_component(end_points):
    res_json = requests.get(end_points).json()
    dexcom_sub_comp = []
    dexcom_sub_comp_values = []
    for ele in res_json:
        if ele["Product Name"] == "Dexcom API":
            dexcom_sub_comp = ele['UDI / Production Identifier']['Sub-Components']
    for val in dexcom_sub_comp:
        dexcom_sub_comp_values.append(list(val.values()))
    dexcom_sub_comp_values = reduce(lambda x, y: x + y, dexcom_sub_comp_values)
    assert "api-gateway" in dexcom_sub_comp_values
    assert "insulin-service" in dexcom_sub_comp_values


@pytest.mark.parametrize("urls", ["https://api.dexcom.com/info", "https://sandbox-api.dexcom.com/info"])
def test_status_and_content_type(urls):
    res = requests.get(urls)
    # print(res.headers)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
