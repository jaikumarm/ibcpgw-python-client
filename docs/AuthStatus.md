# AuthStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticated** | **bool** | Brokerage session is authenticated | [optional] 
**connected** | **bool** | Connected to backend | [optional] 
**competing** | **bool** | Brokerage session is competing, e.g. user is logged in to IBKR Mobile, WebTrader, TWS or other trading platforms. | [optional] 
**fail** | **str** | Authentication failed, why. | [optional] 
**message** | **str** | System messages that may affect trading | [optional] 
**prompts** | **list[str]** | Prompt messages that may affect trading or the account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


