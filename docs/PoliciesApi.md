# swagger_client.PoliciesApi

All URIs are relative to *http://veritas-nonprod-dev.apigee.net/vic/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy**](PoliciesApi.md#create_policy) | **POST** /management/policies | Create policy
[**delete_policy**](PoliciesApi.md#delete_policy) | **DELETE** /management/policies/{id} | Delete policy
[**get_metadata_definitions**](PoliciesApi.md#get_metadata_definitions) | **GET** /management/policies/metadata | List metadata definitions
[**get_policy**](PoliciesApi.md#get_policy) | **GET** /management/policies/{id} | Get policy
[**get_policy_collection**](PoliciesApi.md#get_policy_collection) | **GET** /management/policies | List policies
[**patch_policy**](PoliciesApi.md#patch_policy) | **PATCH** /management/policies/{id} | Patch policy
[**reset_policy**](PoliciesApi.md#reset_policy) | **DELETE** /management/policies/{id}/overrides | Reset policy to defaults
[**update_policy**](PoliciesApi.md#update_policy) | **PUT** /management/policies/{id} | Update policy


# **create_policy**
> Policy create_policy(body, tenant_id=tenant_id)

Create policy

Create a custom policy.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.Policy() # Policy | New policy
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Create policy
    api_response = api_instance.create_policy(body, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Policy**](Policy.md)| New policy | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Policy**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(id, tenant_id=tenant_id)

Delete policy

Delete a custom policy.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
id = 'id_example' # str | The policy identifier
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Delete policy
    api_instance.delete_policy(id, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling PoliciesApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The policy identifier | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_definitions**
> MetadataDefinitionCollection get_metadata_definitions(tenant_id=tenant_id)

List metadata definitions



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # List metadata definitions
    api_response = api_instance.get_metadata_definitions(tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_metadata_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**MetadataDefinitionCollection**](MetadataDefinitionCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> Policy get_policy(id, tenant_id=tenant_id)

Get policy

Retrieve a policy

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
id = 'id_example' # str | The policy identifier
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Get policy
    api_response = api_instance.get_policy(id, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The policy identifier | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Policy**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_collection**
> PolicyCollection get_policy_collection(tenant_id=tenant_id, include_disabled=include_disabled, include_engine_body=include_engine_body, if_none_match=if_none_match)

List policies

Retrieve the policies for a tenant.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)
include_disabled = true # bool | Include disabled policies (as well as enabled ones) (optional)
include_engine_body = true # bool | Include the engine body for policies, and the engine rule sets. (optional)
if_none_match = 'if_none_match_example' # str |  (optional)

try: 
    # List policies
    api_response = api_instance.get_policy_collection(tenant_id=tenant_id, include_disabled=include_disabled, include_engine_body=include_engine_body, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policy_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]
 **include_disabled** | **bool**| Include disabled policies (as well as enabled ones) | [optional] 
 **include_engine_body** | **bool**| Include the engine body for policies, and the engine rule sets. | [optional] 
 **if_none_match** | **str**|  | [optional] 

### Return type

[**PolicyCollection**](PolicyCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_policy**
> Policy patch_policy(id, patch, tenant_id=tenant_id)

Patch policy

Update part of a policy.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
id = 'id_example' # str | The policy identifier
patch = [swagger_client.JsonPatchDocument()] # list[JsonPatchDocument] | A patch containing instructions for how the policy should be modified. See RFC 6902.
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Patch policy
    api_response = api_instance.patch_policy(id, patch, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->patch_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The policy identifier | 
 **patch** | [**list[JsonPatchDocument]**](JsonPatchDocument.md)| A patch containing instructions for how the policy should be modified. See RFC 6902. | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Policy**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_policy**
> reset_policy(id, tenant_id=tenant_id)

Reset policy to defaults

Reset a policy to its default settings.  Only valid for built-in policies.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
id = 'id_example' # str | The policy identifier
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Reset policy to defaults
    api_instance.reset_policy(id, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling PoliciesApi->reset_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The policy identifier | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> Policy update_policy(id, body, tenant_id=tenant_id)

Update policy

Update a policy.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
id = 'id_example' # str | The policy identifier
body = swagger_client.Policy() # Policy | Updated policy
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Update policy
    api_response = api_instance.update_policy(id, body, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The policy identifier | 
 **body** | [**Policy**](Policy.md)| Updated policy | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Policy**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

