# swagger_client.AccountApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iserver_account_pnl_partitioned_get**](AccountApi.md#iserver_account_pnl_partitioned_get) | **GET** /iserver/account/pnl/partitioned | PnL for the selected account
[**iserver_account_post**](AccountApi.md#iserver_account_post) | **POST** /iserver/account | Updates currently selected account to the provided account
[**iserver_accounts_get**](AccountApi.md#iserver_accounts_get) | **GET** /iserver/accounts | Brokerage Accounts
[**portfolio_account_id_ledger_get**](AccountApi.md#portfolio_account_id_ledger_get) | **GET** /portfolio/{accountId}/ledger | Account Ledger
[**portfolio_account_id_meta_get**](AccountApi.md#portfolio_account_id_meta_get) | **GET** /portfolio/{accountId}/meta | Account Information
[**portfolio_account_id_summary_get**](AccountApi.md#portfolio_account_id_summary_get) | **GET** /portfolio/{accountId}/summary | Account Summary
[**portfolio_accounts_get**](AccountApi.md#portfolio_accounts_get) | **GET** /portfolio/accounts | Portfolio Accounts
[**portfolio_subaccounts_get**](AccountApi.md#portfolio_subaccounts_get) | **GET** /portfolio/subaccounts | List of Sub-Accounts


# **iserver_account_pnl_partitioned_get**
> InlineResponse20025 iserver_account_pnl_partitioned_get()

PnL for the selected account

Returns an object containing PnLfor the selected account and its models (if any).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()

try:
    # PnL for the selected account
    api_response = api_instance.iserver_account_pnl_partitioned_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->iserver_account_pnl_partitioned_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_account_post**
> InlineResponse20012 iserver_account_post(body)

Updates currently selected account to the provided account

If an user has multiple accounts, and user wants to get orders, trades, etc. of an account other than currently selected account, then user can update the currently selected account using this API and then can fetch required information for the newly updated account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
body = swagger_client.SetAccount() # SetAccount | account id

try:
    # Updates currently selected account to the provided account
    api_response = api_instance.iserver_account_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->iserver_account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetAccount**](SetAccount.md)| account id | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_accounts_get**
> InlineResponse20011 iserver_accounts_get()

Brokerage Accounts

Returns a list of accounts the user has trading access to, their respective aliases and the currently selected account. Note this endpoint must be called before modifying an order or querying open orders.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()

try:
    # Brokerage Accounts
    api_response = api_instance.iserver_accounts_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->iserver_accounts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

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
api_instance = swagger_client.AccountApi()
account_id = 'account_id_example' # str | account id

try:
    # Account Ledger
    api_response = api_instance.portfolio_account_id_ledger_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->portfolio_account_id_ledger_get: %s\n" % e)
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
api_instance = swagger_client.AccountApi()
account_id = 'account_id_example' # str | account id

try:
    # Account Information
    api_response = api_instance.portfolio_account_id_meta_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->portfolio_account_id_meta_get: %s\n" % e)
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
api_instance = swagger_client.AccountApi()
account_id = 'account_id_example' # str | account id

try:
    # Account Summary
    api_response = api_instance.portfolio_account_id_summary_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->portfolio_account_id_summary_get: %s\n" % e)
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
api_instance = swagger_client.AccountApi()

try:
    # Portfolio Accounts
    api_response = api_instance.portfolio_accounts_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->portfolio_accounts_get: %s\n" % e)
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
api_instance = swagger_client.AccountApi()

try:
    # List of Sub-Accounts
    api_response = api_instance.portfolio_subaccounts_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->portfolio_subaccounts_get: %s\n" % e)
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

