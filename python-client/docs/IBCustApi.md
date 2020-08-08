# swagger_client.IBCustApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ibcust_entity_info_get**](IBCustApi.md#ibcust_entity_info_get) | **GET** /ibcust/entity/info | IBCust Entity Info


# **ibcust_entity_info_get**
> list[InlineResponse2006] ibcust_entity_info_get()

IBCust Entity Info

Returns Applicant Id with all owner related entities

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IBCustApi()

try:
    # IBCust Entity Info
    api_response = api_instance.ibcust_entity_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IBCustApi->ibcust_entity_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2006]**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

