# HistoryData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | start date time | [optional] 
**md_availability** | **str** | Market Data Availability. The field may contain two chars. The first char is the primary code: S &#x3D; Streaming, R &#x3D; Realtime, D &#x3D; Delayed, Z &#x3D; Frozen, Y &#x3D; Frozen Delayed. The second char is the secondary code: P &#x3D; Snapshot Available, p &#x3D; Consolidated.  | [optional] 
**bar_length** | **int** |  | [optional] 
**delay** | **int** |  | [optional] 
**high** | **str** | High value during this time series with format %h/%v/%t. %h is the high price (scaled by priceFactor), %v is volume (volume factor will always be 100 (reported volume &#x3D; actual volume/100)) and %t is minutes from start time of the chart  | [optional] 
**low** | **str** | Low value during this time series with format %l/%v/%t. %l is the low price (scaled by priceFactor), %v is volume (volume factor will always be 100 (reported volume &#x3D; actual volume/100)) and %t is minutes from start time of the chart  | [optional] 
**symbol** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**tick_num** | **str** |  | [optional] 
**time_period** | **str** |  | [optional] 
**price_factor** | **int** | priceFactor is price increment obtained from display rule | [optional] 
**data** | [**list[HistorydataData]**](HistorydataData.md) |  | [optional] 
**points** | **float** | total number of points | [optional] 
**travel_time** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


