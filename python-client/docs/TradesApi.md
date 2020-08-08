# swagger_client.TradesApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iserver_account_trades_get**](TradesApi.md#iserver_account_trades_get) | **GET** /iserver/account/trades | List of Trades for the selected account


# **iserver_account_trades_get**
> list[Trade] iserver_account_trades_get()

List of Trades for the selected account

Returns a list of trades for the currently selected account for current day and six previous days.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradesApi()

try:
    # List of Trades for the selected account
    api_response = api_instance.iserver_account_trades_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradesApi->iserver_account_trades_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Trade]**](Trade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

