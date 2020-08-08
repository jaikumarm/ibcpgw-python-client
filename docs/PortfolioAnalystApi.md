# swagger_client.PortfolioAnalystApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pa_performance_post**](PortfolioAnalystApi.md#pa_performance_post) | **POST** /pa/performance | Account Performance
[**pa_summary_post**](PortfolioAnalystApi.md#pa_summary_post) | **POST** /pa/summary | Account Balance&#39;s Summary


# **pa_performance_post**
> Performance pa_performance_post(body)

Account Performance

Returns the performance (MTM) for the given accounts, if more than one account is passed, the result is consolidated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioAnalystApi()
body = swagger_client.Body2() # Body2 | an array of account ids

try:
    # Account Performance
    api_response = api_instance.pa_performance_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioAnalystApi->pa_performance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)| an array of account ids | 

### Return type

[**Performance**](Performance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pa_summary_post**
> Summary pa_summary_post(body)

Account Balance's Summary

Returns a summary of all account balances for the given accounts, if more than one account is passed, the result is consolidated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioAnalystApi()
body = swagger_client.Body3() # Body3 | an array of account ids

try:
    # Account Balance's Summary
    api_response = api_instance.pa_summary_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioAnalystApi->pa_summary_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)| an array of account ids | 

### Return type

[**Summary**](Summary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

