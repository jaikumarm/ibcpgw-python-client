# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acct** | **str** | account id | [optional] 
**conid** | **int** |  | [optional] 
**order_desc** | **str** |  | [optional] 
**description1** | **str** |  | [optional] 
**ticker** | **str** | for exmple FB | [optional] 
**sec_type** | **str** | for example STK | [optional] 
**listing_exchange** | **str** | for example NASDAQ.NMS | [optional] 
**remaining_quantity** | **str** |  | [optional] 
**filled_quantity** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**status** | **str** | PendingSubmit - Indicates the order was sent, but confirmation has not been received that it has been received by the destination.                  Occurs most commonly if an exchange is closed. PendingCancel - Indicates that a request has been sent to cancel an order but confirmation has not been received of its cancellation. PreSubmitted - Indicates that a simulated order type has been accepted by the IBKR system and that this order has yet to be elected.                 The order is held in the IBKR system until the election criteria are met. At that time the order is transmitted to the order destination as specified.  Submitted - Indicates that the order has been accepted at the order destination and is working. Cancelled - Indicates that the balance of the order has been confirmed cancelled by the IB system.              This could occur unexpectedly when IB or the destination has rejected the order.   Filled - Indicates that the order has been completely filled.  Inactive - Indicates the order is not working, for instance if the order was invalid and triggered an error message,            or if the order was to short a security and shares have not yet been located.   | [optional] 
**orig_order_type** | **str** | for example Limit | [optional] 
**side** | **str** | BUY or SELL | [optional] 
**price** | **float** |  | [optional] 
**bg_color** | **str** | back-ground color | [optional] 
**fg_color** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**parent_id** | **int** | Only exists in child order of bracket | [optional] 
**order_ref** | **str** | User defined string used to identify the order. Value is set using \&quot;cOID\&quot; field while placing an order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


