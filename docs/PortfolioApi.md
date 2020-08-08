# swagger_client.PortfolioApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portfolio_account_id_allocation_get**](PortfolioApi.md#portfolio_account_id_allocation_get) | **GET** /portfolio/{accountId}/allocation | Account Allocation
[**portfolio_account_id_ledger_get**](PortfolioApi.md#portfolio_account_id_ledger_get) | **GET** /portfolio/{accountId}/ledger | Account Ledger
[**portfolio_account_id_meta_get**](PortfolioApi.md#portfolio_account_id_meta_get) | **GET** /portfolio/{accountId}/meta | Account Information
[**portfolio_account_id_position_conid_get**](PortfolioApi.md#portfolio_account_id_position_conid_get) | **GET** /portfolio/{accountId}/position/{conid} | Position by Conid
[**portfolio_account_id_positions_invalidate_post**](PortfolioApi.md#portfolio_account_id_positions_invalidate_post) | **POST** /portfolio/{accountId}/positions/invalidate | Invalidates the backend cache of the Portfolio
[**portfolio_account_id_positions_page_id_get**](PortfolioApi.md#portfolio_account_id_positions_page_id_get) | **GET** /portfolio/{accountId}/positions/{pageId} | Portfolio Positions
[**portfolio_account_id_summary_get**](PortfolioApi.md#portfolio_account_id_summary_get) | **GET** /portfolio/{accountId}/summary | Account Summary
[**portfolio_accounts_get**](PortfolioApi.md#portfolio_accounts_get) | **GET** /portfolio/accounts | Portfolio Accounts
[**portfolio_allocation_post**](PortfolioApi.md#portfolio_allocation_post) | **POST** /portfolio/allocation | Account Alloction (All Accounts)
[**portfolio_positions_conid_get**](PortfolioApi.md#portfolio_positions_conid_get) | **GET** /portfolio/positions/{conid} | Positions by Conid
[**portfolio_subaccounts_get**](PortfolioApi.md#portfolio_subaccounts_get) | **GET** /portfolio/subaccounts | List of Sub-Accounts


# **portfolio_account_id_allocation_get**
> Allocation portfolio_account_id_allocation_get(account_id)

Account Allocation

Information about the account's portfolio allocation by Asset Class, Industry and Category.  /portfolio/accounts or /portfolio/subaccounts must be called prior to this endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioApi()
account_id = 'account_id_example' # str | account id

try:
    # Account Allocation
    api_response = api_instance.portfolio_account_id_allocation_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->portfolio_account_id_allocation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 

### Return type

[**Allocation**](Allocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_account_id_ledger_get**
> InlineResponse2009 portfolio_account_id_ledger_get(account_id)

Account Ledger

Information regarding settled cash, cash balances, etc. in the account's base currency and any other cash balances hold in other currencies.  /portfolio/accounts or /portfolio/subaccounts must be called prior to this endpoint. The list of supported currencies is available at https://www.interactivebrokers.com/en/index.php?f=3185.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioApi()
account_id = 'account_id_example' # str | account id

try:
    # Account Ledger
    api_response = api_instance.portfolio_account_id_ledger_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->portfolio_account_id_ledger_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_account_id_meta_get**
> Accounts portfolio_account_id_meta_get(account_id)

Account Information

Account information related to account Id /portfolio/accounts or /portfolio/subaccounts must be called prior to this endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioApi()
account_id = 'account_id_example' # str | account id

try:
    # Account Information
    api_response = api_instance.portfolio_account_id_meta_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->portfolio_account_id_meta_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_account_id_position_conid_get**
> Position portfolio_account_id_position_conid_get(account_id, conid)

Position by Conid

Returns a list of all positions matching the conid. For portfolio models the conid could be in more than one model, returning an array with the name of the model it belongs to.  /portfolio/accounts or /portfolio/subaccounts must be called prior to this endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioApi()
account_id = 'account_id_example' # str | account id
conid = 56 # int | contract id

try:
    # Position by Conid
    api_response = api_instance.portfolio_account_id_position_conid_get(account_id, conid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->portfolio_account_id_position_conid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 
 **conid** | **int**| contract id | 

### Return type

[**Position**](Position.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_account_id_positions_invalidate_post**
> object portfolio_account_id_positions_invalidate_post(account_id)

Invalidates the backend cache of the Portfolio

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioApi()
account_id = 'account_id_example' # str | account id

try:
    # Invalidates the backend cache of the Portfolio
    api_response = api_instance.portfolio_account_id_positions_invalidate_post(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->portfolio_account_id_positions_invalidate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_account_id_positions_page_id_get**
> Position portfolio_account_id_positions_page_id_get(account_id, page_id, model=model, sort=sort, direction=direction, period=period)

Portfolio Positions

Returns a list of positions for the given account. The endpoint supports paging, page's default size is 30 positions. /portfolio/accounts or /portfolio/subaccounts must be called prior to this endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioApi()
account_id = 'account_id_example' # str | account id
page_id = 'page_id_example' # str | page id
model = 'model_example' # str | optional (optional)
sort = 'sort_example' # str | declare the table to be sorted by which column (optional)
direction = 'direction_example' # str | in which order, a means ascending - d means descending (optional)
period = 'period_example' # str | period for pnl column, can be 1D, 7D, 1M... (optional)

try:
    # Portfolio Positions
    api_response = api_instance.portfolio_account_id_positions_page_id_get(account_id, page_id, model=model, sort=sort, direction=direction, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->portfolio_account_id_positions_page_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 
 **page_id** | **str**| page id | 
 **model** | **str**| optional | [optional] 
 **sort** | **str**| declare the table to be sorted by which column | [optional] 
 **direction** | **str**| in which order, a means ascending - d means descending | [optional] 
 **period** | **str**| period for pnl column, can be 1D, 7D, 1M... | [optional] 

### Return type

[**Position**](Position.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_account_id_summary_get**
> InlineResponse2008 portfolio_account_id_summary_get(account_id)

Account Summary

Returns information about margin, cash balances and other information related to specified account. See also /portfolio/{accountId}/ledger. /portfolio/accounts or /portfolio/subaccounts must be called prior to this endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioApi()
account_id = 'account_id_example' # str | account id

try:
    # Account Summary
    api_response = api_instance.portfolio_account_id_summary_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->portfolio_account_id_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_accounts_get**
> Accounts portfolio_accounts_get()

Portfolio Accounts

In non-tiered account structures, returns a list of accounts for which the user can view position and account information. This endpoint must be called prior  to calling other /portfolio endpoints for those accounts. For querying a list of accounts  which the user can trade, see /iserver/accounts. For a list of subaccounts in tiered  account structures (e.g. financial advisor or ibroker accounts) see /portfolio/subaccounts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioApi()

try:
    # Portfolio Accounts
    api_response = api_instance.portfolio_accounts_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->portfolio_accounts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Accounts**](Accounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_allocation_post**
> Allocation portfolio_allocation_post(body)

Account Alloction (All Accounts)

Similar to /portfolio/{accountId}/allocation but returns a consolidated view of of all the accounts returned by /portfolio/accounts. /portfolio/accounts or /portfolio/subaccounts must be called prior to this endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioApi()
body = swagger_client.Body4() # Body4 | accounts info

try:
    # Account Alloction (All Accounts)
    api_response = api_instance.portfolio_allocation_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->portfolio_allocation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body4**](Body4.md)| accounts info | 

### Return type

[**Allocation**](Allocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_positions_conid_get**
> InlineResponse20010 portfolio_positions_conid_get(conid)

Positions by Conid

Returns an object of all positions matching the conid for all the selected accounts. For portfolio models the conid could be in more than one model, returning an array with the name of the model it belongs to. /portfolio/accounts or /portfolio/subaccounts must be called prior to this endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioApi()
conid = 56 # int | contract id

try:
    # Positions by Conid
    api_response = api_instance.portfolio_positions_conid_get(conid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->portfolio_positions_conid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conid** | **int**| contract id | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_subaccounts_get**
> Account portfolio_subaccounts_get()

List of Sub-Accounts

Used in tiered account structures (such as financial advisor and ibroker accounts)  to return a list of sub-accounts for which the user can view position and  account-related information. This endpoint must be called prior to calling other  /portfolio endpoints for those subaccounts.  To query a list of accounts the user can trade, see /iserver/accounts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioApi()

try:
    # List of Sub-Accounts
    api_response = api_instance.portfolio_subaccounts_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->portfolio_subaccounts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

