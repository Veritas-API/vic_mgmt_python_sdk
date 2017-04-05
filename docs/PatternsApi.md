# swagger_client.PatternsApi

All URIs are relative to *http://veritas-nonprod-dev.apigee.net/vic/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pattern**](PatternsApi.md#create_pattern) | **POST** /management/patterns | Create pattern
[**delete_pattern**](PatternsApi.md#delete_pattern) | **DELETE** /management/patterns/{id} | Delete pattern
[**get_pattern**](PatternsApi.md#get_pattern) | **GET** /management/patterns/{id} | Get pattern
[**get_pattern_collection**](PatternsApi.md#get_pattern_collection) | **GET** /management/patterns | List patterns
[**get_policies_by_pattern**](PatternsApi.md#get_policies_by_pattern) | **GET** /management/patterns/{id}/policies | List policies that use a pattern
[**update_pattern**](PatternsApi.md#update_pattern) | **PUT** /management/patterns/{id} | Update pattern


# **create_pattern**
> Pattern create_pattern(body, tenant_id=tenant_id)

Create pattern



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PatternsApi()
body = swagger_client.Pattern() # Pattern | New pattern
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Create pattern
    api_response = api_instance.create_pattern(body, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PatternsApi->create_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pattern**](Pattern.md)| New pattern | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Pattern**](Pattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pattern**
> delete_pattern(id, tenant_id=tenant_id)

Delete pattern



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PatternsApi()
id = 'id_example' # str | The pattern identifier
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Delete pattern
    api_instance.delete_pattern(id, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling PatternsApi->delete_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The pattern identifier | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pattern**
> Pattern get_pattern(id, tenant_id=tenant_id)

Get pattern



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PatternsApi()
id = 'id_example' # str | The pattern identifier
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Get pattern
    api_response = api_instance.get_pattern(id, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PatternsApi->get_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The pattern identifier | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Pattern**](Pattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pattern_collection**
> PatternCollection get_pattern_collection(tenant_id=tenant_id, if_none_match=if_none_match)

List patterns



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PatternsApi()
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)
if_none_match = 'if_none_match_example' # str |  (optional)

try: 
    # List patterns
    api_response = api_instance.get_pattern_collection(tenant_id=tenant_id, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PatternsApi->get_pattern_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]
 **if_none_match** | **str**|  | [optional] 

### Return type

[**PatternCollection**](PatternCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies_by_pattern**
> PolicyCollection get_policies_by_pattern(id, tenant_id=tenant_id)

List policies that use a pattern



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PatternsApi()
id = 'id_example' # str | 
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # List policies that use a pattern
    api_response = api_instance.get_policies_by_pattern(id, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PatternsApi->get_policies_by_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**PolicyCollection**](PolicyCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pattern**
> Pattern update_pattern(id, body, tenant_id=tenant_id)

Update pattern



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PatternsApi()
id = 'id_example' # str | The pattern identifier
body = swagger_client.Pattern() # Pattern | Updated pattern
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Update pattern
    api_response = api_instance.update_pattern(id, body, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PatternsApi->update_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The pattern identifier | 
 **body** | [**Pattern**](Pattern.md)| Updated pattern | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Pattern**](Pattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

