# swagger_client.ContractApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iserver_contract_conid_info_get**](ContractApi.md#iserver_contract_conid_info_get) | **GET** /iserver/contract/{conid}/info | Contract Info
[**iserver_secdef_info_get**](ContractApi.md#iserver_secdef_info_get) | **GET** /iserver/secdef/info | Get available conids of future/option/warrant/cash/CFD
[**iserver_secdef_search_post**](ContractApi.md#iserver_secdef_search_post) | **POST** /iserver/secdef/search | Search by symbol or name
[**iserver_secdef_strikes_get**](ContractApi.md#iserver_secdef_strikes_get) | **GET** /iserver/secdef/strikes | Get strikes for Options/Warrant
[**trsrv_futures_get**](ContractApi.md#trsrv_futures_get) | **GET** /trsrv/futures | Security Futures by Symbol
[**trsrv_secdef_post**](ContractApi.md#trsrv_secdef_post) | **POST** /trsrv/secdef | Secdef by Conid
[**trsrv_stocks_get**](ContractApi.md#trsrv_stocks_get) | **GET** /trsrv/stocks | Security Stocks by Symbol


# **iserver_contract_conid_info_get**
> Contract iserver_contract_conid_info_get(conid)

Contract Info

get contract details, you can use this to prefill your order before you submit an order

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractApi()
conid = 'conid_example' # str | contract id

try:
    # Contract Info
    api_response = api_instance.iserver_contract_conid_info_get(conid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->iserver_contract_conid_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conid** | **str**| contract id | 

### Return type

[**Contract**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_secdef_info_get**
> list[SecdefInfo] iserver_secdef_info_get(conid, sectype, month=month, exchange=exchange, strike=strike, right=right)

Get available conids of future/option/warrant/cash/CFD

For option and warrant, you can get strike price from \"/iserver/secdef/strikes\" endpoint

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractApi()
conid = 'conid_example' # str | underlying stock contract id
sectype = 'sectype_example' # str | FUT/OPT/WAR/CASH/CFD
month = 'month_example' # str | contract month, only required for FUT/OPT/WAR (optional)
exchange = 'exchange_example' # str | optional, default is SMART (optional)
strike = 'strike_example' # str | optional, only required for OPT/WAR (optional)
right = 'right_example' # str | C for call, P for put (optional)

try:
    # Get available conids of future/option/warrant/cash/CFD
    api_response = api_instance.iserver_secdef_info_get(conid, sectype, month=month, exchange=exchange, strike=strike, right=right)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->iserver_secdef_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conid** | **str**| underlying stock contract id | 
 **sectype** | **str**| FUT/OPT/WAR/CASH/CFD | 
 **month** | **str**| contract month, only required for FUT/OPT/WAR | [optional] 
 **exchange** | **str**| optional, default is SMART | [optional] 
 **strike** | **str**| optional, only required for OPT/WAR | [optional] 
 **right** | **str**| C for call, P for put | [optional] 

### Return type

[**list[SecdefInfo]**](SecdefInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_secdef_search_post**
> list[InlineResponse20021] iserver_secdef_search_post(symbol)

Search by symbol or name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractApi()
symbol = swagger_client.Symbol() # Symbol | symbol or name to be searched

try:
    # Search by symbol or name
    api_response = api_instance.iserver_secdef_search_post(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->iserver_secdef_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | [**Symbol**](Symbol.md)| symbol or name to be searched | 

### Return type

[**list[InlineResponse20021]**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_secdef_strikes_get**
> InlineResponse20022 iserver_secdef_strikes_get(conid, sectype, month, exchange=exchange)

Get strikes for Options/Warrant

You can get available contract months and exchanges from \"/iserver/secdef/search\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractApi()
conid = 'conid_example' # str | contract id
sectype = 'sectype_example' # str | OPT/WAR
month = 'month_example' # str | contract month
exchange = 'exchange_example' # str | optional, default is SMART (optional)

try:
    # Get strikes for Options/Warrant
    api_response = api_instance.iserver_secdef_strikes_get(conid, sectype, month, exchange=exchange)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->iserver_secdef_strikes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conid** | **str**| contract id | 
 **sectype** | **str**| OPT/WAR | 
 **month** | **str**| contract month | 
 **exchange** | **str**| optional, default is SMART | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trsrv_futures_get**
> InlineResponse20026 trsrv_futures_get(symbols)

Security Futures by Symbol

Returns a list of non-expired future contracts for given symbol(s)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractApi()
symbols = 'symbols_example' # str | list of case-sensitive symbols separated by comma

try:
    # Security Futures by Symbol
    api_response = api_instance.trsrv_futures_get(symbols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->trsrv_futures_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| list of case-sensitive symbols separated by comma | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trsrv_secdef_post**
> Secdef trsrv_secdef_post(body)

Secdef by Conid

Returns a list of security definitions for the given conids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractApi()
body = swagger_client.Body7() # Body7 | request body

try:
    # Secdef by Conid
    api_response = api_instance.trsrv_secdef_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->trsrv_secdef_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body7**](Body7.md)| request body | 

### Return type

[**Secdef**](Secdef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trsrv_stocks_get**
> InlineResponse20027 trsrv_stocks_get(symbols)

Security Stocks by Symbol

Returns an object contains all stock contracts for given symbol(s)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractApi()
symbols = 'symbols_example' # str | list of upper-sensitive symbols separated by comma

try:
    # Security Stocks by Symbol
    api_response = api_instance.trsrv_stocks_get(symbols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->trsrv_stocks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| list of upper-sensitive symbols separated by comma | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

