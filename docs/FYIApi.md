# swagger_client.FYIApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fyi_deliveryoptions_device_id_delete**](FYIApi.md#fyi_deliveryoptions_device_id_delete) | **DELETE** /fyi/deliveryoptions/{deviceId} | delete a device
[**fyi_deliveryoptions_device_post**](FYIApi.md#fyi_deliveryoptions_device_post) | **POST** /fyi/deliveryoptions/device | enable/disable device option
[**fyi_deliveryoptions_email_put**](FYIApi.md#fyi_deliveryoptions_email_put) | **PUT** /fyi/deliveryoptions/email | enable/disable email option
[**fyi_deliveryoptions_get**](FYIApi.md#fyi_deliveryoptions_get) | **GET** /fyi/deliveryoptions | Get delivery options
[**fyi_disclaimer_typecode_get**](FYIApi.md#fyi_disclaimer_typecode_get) | **GET** /fyi/disclaimer/{typecode} | get disclaimer for a certain kind of fyi
[**fyi_disclaimer_typecode_put**](FYIApi.md#fyi_disclaimer_typecode_put) | **PUT** /fyi/disclaimer/{typecode} | mark disclaimer read
[**fyi_notifications_get**](FYIApi.md#fyi_notifications_get) | **GET** /fyi/notifications | Get a list of notifications
[**fyi_notifications_more_get**](FYIApi.md#fyi_notifications_more_get) | **GET** /fyi/notifications/more | Get more notifications based on a certain one
[**fyi_notifications_notification_id_put**](FYIApi.md#fyi_notifications_notification_id_put) | **PUT** /fyi/notifications/{notificationId} | Get a list of notifications
[**fyi_settings_get**](FYIApi.md#fyi_settings_get) | **GET** /fyi/settings | Get a list of subscriptions
[**fyi_settings_typecode_post**](FYIApi.md#fyi_settings_typecode_post) | **POST** /fyi/settings/{typecode} | enable/disable certain subscription
[**fyi_unreadnumber_get**](FYIApi.md#fyi_unreadnumber_get) | **GET** /fyi/unreadnumber | Get unread number of fyis


# **fyi_deliveryoptions_device_id_delete**
> object fyi_deliveryoptions_device_id_delete(device_id)

delete a device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FYIApi()
device_id = 'device_id_example' # str | device ID

try:
    # delete a device
    api_response = api_instance.fyi_deliveryoptions_device_id_delete(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FYIApi->fyi_deliveryoptions_device_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| device ID | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fyi_deliveryoptions_device_post**
> InlineResponse2003 fyi_deliveryoptions_device_post(body)

enable/disable device option

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FYIApi()
body = swagger_client.Body1() # Body1 | device info

try:
    # enable/disable device option
    api_response = api_instance.fyi_deliveryoptions_device_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FYIApi->fyi_deliveryoptions_device_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)| device info | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fyi_deliveryoptions_email_put**
> InlineResponse2003 fyi_deliveryoptions_email_put(enabled)

enable/disable email option

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FYIApi()
enabled = 'enabled_example' # str | true/false

try:
    # enable/disable email option
    api_response = api_instance.fyi_deliveryoptions_email_put(enabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FYIApi->fyi_deliveryoptions_email_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **str**| true/false | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fyi_deliveryoptions_get**
> InlineResponse2004 fyi_deliveryoptions_get()

Get delivery options

options for sending fyis to email and other devices 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FYIApi()

try:
    # Get delivery options
    api_response = api_instance.fyi_deliveryoptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FYIApi->fyi_deliveryoptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fyi_disclaimer_typecode_get**
> InlineResponse2002 fyi_disclaimer_typecode_get(typecode)

get disclaimer for a certain kind of fyi

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FYIApi()
typecode = 'typecode_example' # str | fyi code, for example --M8, EA

try:
    # get disclaimer for a certain kind of fyi
    api_response = api_instance.fyi_disclaimer_typecode_get(typecode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FYIApi->fyi_disclaimer_typecode_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **typecode** | **str**| fyi code, for example --M8, EA | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fyi_disclaimer_typecode_put**
> InlineResponse2003 fyi_disclaimer_typecode_put(typecode)

mark disclaimer read

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FYIApi()
typecode = 'typecode_example' # str | fyi code, for example --M8, EA

try:
    # mark disclaimer read
    api_response = api_instance.fyi_disclaimer_typecode_put(typecode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FYIApi->fyi_disclaimer_typecode_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **typecode** | **str**| fyi code, for example --M8, EA | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fyi_notifications_get**
> Notifications fyi_notifications_get(max, exclude=exclude, include=include)

Get a list of notifications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FYIApi()
max = 'max_example' # str | max number of fyis in response
exclude = 'exclude_example' # str | if set, don't set include (optional)
include = 'include_example' # str | if set, don't set exclude (optional)

try:
    # Get a list of notifications
    api_response = api_instance.fyi_notifications_get(max, exclude=exclude, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FYIApi->fyi_notifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **str**| max number of fyis in response | 
 **exclude** | **str**| if set, don&#39;t set include | [optional] 
 **include** | **str**| if set, don&#39;t set exclude | [optional] 

### Return type

[**Notifications**](Notifications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fyi_notifications_more_get**
> Notifications fyi_notifications_more_get(id)

Get more notifications based on a certain one

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FYIApi()
id = 'id_example' # str | id of last notification in the list

try:
    # Get more notifications based on a certain one
    api_response = api_instance.fyi_notifications_more_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FYIApi->fyi_notifications_more_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of last notification in the list | 

### Return type

[**Notifications**](Notifications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fyi_notifications_notification_id_put**
> object fyi_notifications_notification_id_put(notification_id)

Get a list of notifications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FYIApi()
notification_id = 'notification_id_example' # str | mark a notification read

try:
    # Get a list of notifications
    api_response = api_instance.fyi_notifications_notification_id_put(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FYIApi->fyi_notifications_notification_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| mark a notification read | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fyi_settings_get**
> list[InlineResponse2001] fyi_settings_get()

Get a list of subscriptions

return the current choices of subscriptions, we can toggle the option 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FYIApi()

try:
    # Get a list of subscriptions
    api_response = api_instance.fyi_settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FYIApi->fyi_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fyi_settings_typecode_post**
> object fyi_settings_typecode_post(typecode, body)

enable/disable certain subscription

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FYIApi()
typecode = 'typecode_example' # str | fyi code
body = swagger_client.Body() # Body | 

try:
    # enable/disable certain subscription
    api_response = api_instance.fyi_settings_typecode_post(typecode, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FYIApi->fyi_settings_typecode_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **typecode** | **str**| fyi code | 
 **body** | [**Body**](Body.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fyi_unreadnumber_get**
> InlineResponse200 fyi_unreadnumber_get()

Get unread number of fyis

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FYIApi()

try:
    # Get unread number of fyis
    api_response = api_instance.fyi_unreadnumber_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FYIApi->fyi_unreadnumber_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

