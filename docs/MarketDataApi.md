# swagger_client.MarketDataApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iserver_marketdata_conid_unsubscribe_get**](MarketDataApi.md#iserver_marketdata_conid_unsubscribe_get) | **GET** /iserver/marketdata/{conid}/unsubscribe | Market Data Cancel (Single)
[**iserver_marketdata_history_get**](MarketDataApi.md#iserver_marketdata_history_get) | **GET** /iserver/marketdata/history | Market Data History
[**iserver_marketdata_snapshot_get**](MarketDataApi.md#iserver_marketdata_snapshot_get) | **GET** /iserver/marketdata/snapshot | Market Data
[**iserver_marketdata_unsubscribeall_get**](MarketDataApi.md#iserver_marketdata_unsubscribeall_get) | **GET** /iserver/marketdata/unsubscribeall | Market Data Cancel (All)


# **iserver_marketdata_conid_unsubscribe_get**
> InlineResponse20019 iserver_marketdata_conid_unsubscribe_get(conid)

Market Data Cancel (Single)

Cancel market data for given conid. To cancel all market data request(s), see /iserver/marketdata/unsubscribeall. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketDataApi()
conid = 'conid_example' # str | contract id

try:
    # Market Data Cancel (Single)
    api_response = api_instance.iserver_marketdata_conid_unsubscribe_get(conid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->iserver_marketdata_conid_unsubscribe_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conid** | **str**| contract id | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_marketdata_history_get**
> HistoryData iserver_marketdata_history_get(conid, period, exchange=exchange, bar=bar)

Market Data History

Get historical market Data for given conid, length of data is controlled by 'period' and 'bar'. Formatted as: min=minute, h=hour, d=day, w=week, m=month, y=year e.g. period =1y with bar =1w returns 52 data points (Max of 1000 data points supported). **Note**: There's a limit of 5 concurrent requests. Excessive requests will return a 'Too many requests' status 429 response. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketDataApi()
conid = 'conid_example' # str | contract id
period = 'period_example' # str | available time period-- {1-30}min, {1-8}h, {1-1000}d, {1-792}w, {1-182}m, {1-15}y
exchange = 'exchange_example' # str | Exchange of the conid (e.g. ISLAND, NYSE, etc.). Default value is empty which corresponds to primary exchange of the conid. (optional)
bar = 'bar_example' # str | possible value-- 1min, 2min, 3min, 5min, 10min, 15min, 30min, 1h, 2h, 3h, 4h, 8h, 1d, 1w, 1m (optional)

try:
    # Market Data History
    api_response = api_instance.iserver_marketdata_history_get(conid, period, exchange=exchange, bar=bar)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->iserver_marketdata_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conid** | **str**| contract id | 
 **period** | **str**| available time period-- {1-30}min, {1-8}h, {1-1000}d, {1-792}w, {1-182}m, {1-15}y | 
 **exchange** | **str**| Exchange of the conid (e.g. ISLAND, NYSE, etc.). Default value is empty which corresponds to primary exchange of the conid. | [optional] 
 **bar** | **str**| possible value-- 1min, 2min, 3min, 5min, 10min, 15min, 30min, 1h, 2h, 3h, 4h, 8h, 1d, 1w, 1m | [optional] 

### Return type

[**HistoryData**](HistoryData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_marketdata_snapshot_get**
> list[InlineResponse20018] iserver_marketdata_snapshot_get(conids, since=since, fields=fields)

Market Data

Get Market Data for the given conid(s). The endpoint will return by default bid, ask, last, change, change pct, close, listing exchange. See response fields for a list of available fields that can be request via fields argument. The endpoint /iserver/accounts must be called prior to /iserver/marketdata/snapshot. First /snapshot endpoint call for given conid will initiate the market data request.  To receive all available fields the /snapshot endpoint will need to be called several times. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketDataApi()
conids = 'conids_example' # str | list of conids separated by comma
since = 56 # int | time period since which updates are required. uses epoch time with milliseconds. (optional)
fields = 'fields_example' # str | list of fields separated by comma (optional)

try:
    # Market Data
    api_response = api_instance.iserver_marketdata_snapshot_get(conids, since=since, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->iserver_marketdata_snapshot_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conids** | **str**| list of conids separated by comma | 
 **since** | **int**| time period since which updates are required. uses epoch time with milliseconds. | [optional] 
 **fields** | **str**| list of fields separated by comma | [optional] 

### Return type

[**list[InlineResponse20018]**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_marketdata_unsubscribeall_get**
> InlineResponse20020 iserver_marketdata_unsubscribeall_get()

Market Data Cancel (All)

Cancel all market data request(s). To cancel market data for given conid, see /iserver/marketdata/{conid}/unsubscribe.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketDataApi()

try:
    # Market Data Cancel (All)
    api_response = api_instance.iserver_marketdata_unsubscribeall_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->iserver_marketdata_unsubscribeall_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

