# swagger_client.SessionApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iserver_auth_status_post**](SessionApi.md#iserver_auth_status_post) | **POST** /iserver/auth/status | Authentication Status
[**iserver_reauthenticate_post**](SessionApi.md#iserver_reauthenticate_post) | **POST** /iserver/reauthenticate | Tries to re-authenticate to Brokerage
[**logout_post**](SessionApi.md#logout_post) | **POST** /logout | Ends the current session
[**sso_validate_get**](SessionApi.md#sso_validate_get) | **GET** /sso/validate | Validate SSO
[**tickle_post**](SessionApi.md#tickle_post) | **POST** /tickle | Ping the server to keep the session open


# **iserver_auth_status_post**
> AuthStatus iserver_auth_status_post()

Authentication Status

Current Authentication status to the Brokerage system. Market Data and Trading is not possible if not authenticated, e.g. authenticated shows false

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()

try:
    # Authentication Status
    api_response = api_instance.iserver_auth_status_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->iserver_auth_status_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthStatus**](AuthStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_reauthenticate_post**
> AuthStatus iserver_reauthenticate_post()

Tries to re-authenticate to Brokerage

Provides a way to reauthenticate to the Brokerage system as long as there is a valid SSO session, see /sso/validate.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()

try:
    # Tries to re-authenticate to Brokerage
    api_response = api_instance.iserver_reauthenticate_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->iserver_reauthenticate_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthStatus**](AuthStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_post**
> InlineResponse2005 logout_post()

Ends the current session

Logs the user out of the gateway session. Any further activity requires re-authentication.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()

try:
    # Ends the current session
    api_response = api_instance.logout_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->logout_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sso_validate_get**
> InlineResponse2007 sso_validate_get()

Validate SSO

Validates the current session for the SSO user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()

try:
    # Validate SSO
    api_response = api_instance.sso_validate_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->sso_validate_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tickle_post**
> tickle_post()

Ping the server to keep the session open

If the gateway has not received any requests for several minutes an open session will automatically timeout. The tickle endpoint pings the server to prevent the session from ending.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()

try:
    # Ping the server to keep the session open
    api_instance.tickle_post()
except ApiException as e:
    print("Exception when calling SessionApi->tickle_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

