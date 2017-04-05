# swagger_client.TagsApi

All URIs are relative to *http://veritas-nonprod-dev.apigee.net/vic/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_tag**](TagsApi.md#create_or_update_tag) | **PUT** /management/tags/{tag} | Create or update tag
[**delete_tag**](TagsApi.md#delete_tag) | **DELETE** /management/tags/{tag} | Delete tag
[**get_policies_by_tag**](TagsApi.md#get_policies_by_tag) | **GET** /management/tags/{tag}/policies | List policies that use a tag
[**get_tag**](TagsApi.md#get_tag) | **GET** /management/tags/{tag} | Get tag
[**get_tag_property_definitions**](TagsApi.md#get_tag_property_definitions) | **GET** /management/tags/propertyDefinitions | List tag property definitions
[**get_tags_collection**](TagsApi.md#get_tags_collection) | **GET** /management/tags | List tags


# **create_or_update_tag**
> Tag create_or_update_tag(tag, body, tenant_id=tenant_id)

Create or update tag

Create or update a tag.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
tag = 'tag_example' # str | 
body = swagger_client.Tag() # Tag | Tag
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Create or update tag
    api_response = api_instance.create_or_update_tag(tag, body, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->create_or_update_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | 
 **body** | [**Tag**](Tag.md)| Tag | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(tag, tenant_id=tenant_id)

Delete tag

Delete a custom tag.  (Built-in tags cannot be deleted.)

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
tag = 'tag_example' # str | 
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Delete tag
    api_instance.delete_tag(tag, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling TagsApi->delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies_by_tag**
> PolicyCollection get_policies_by_tag(tag, tenant_id=tenant_id)

List policies that use a tag



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
tag = 'tag_example' # str | 
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # List policies that use a tag
    api_response = api_instance.get_policies_by_tag(tag, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_policies_by_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**PolicyCollection**](PolicyCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> Tag get_tag(tag, tenant_id=tenant_id)

Get tag

Get a tag.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
tag = 'tag_example' # str | 
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Get tag
    api_response = api_instance.get_tag(tag, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_property_definitions**
> TagPropertyDefinitionCollection get_tag_property_definitions(tenant_id=tenant_id)

List tag property definitions

Get definitions of properties that can be associated with a tag. This is useful, for example, for user interfaces that need to know the supported values for such properties. Generally the tag properties are application-specific and not part of the core service functionality.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # List tag property definitions
    api_response = api_instance.get_tag_property_definitions(tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tag_property_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**TagPropertyDefinitionCollection**](TagPropertyDefinitionCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_collection**
> TagsCollection get_tags_collection(tenant_id=tenant_id, if_none_match=if_none_match)

List tags

Retrieve all of the tags for a tenant.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)
if_none_match = 'if_none_match_example' # str |  (optional)

try: 
    # List tags
    api_response = api_instance.get_tags_collection(tenant_id=tenant_id, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tags_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]
 **if_none_match** | **str**|  | [optional] 

### Return type

[**TagsCollection**](TagsCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

