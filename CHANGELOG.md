# RPC Spec 4.5.0


### Breaking Changes


### Modifications
- [0031](https://github.com/smartdevicelink/sdl_evolution/issues/97): Added `PROJECTION` element to `AppHMIType` 
- [0049](https://github.com/smartdevicelink/sdl_evolution/issues/144) : Added `CANCEL` element to `TouchType`
- [0055] : Added `DATA_NOT_AVAILABLE` to `Result`
- [0058] : Added `videoStreaming ` to `HMICapabilities`
- [0060] , [0076] : Added `EN-IN`, `TH-TH`, `EN-SA`, `HE-IL`, `RO-RO`, `UK-UA`,`ID-ID`, `VI-VN`, `MS-MY`, and `HI-IN` to elements to `Language` 
- [0071] : Added `REMOTE_CONTROL` element to `AppHMIType`
- [0071] : Added `AC_MAX`, `AC`, `RECIRCULATE`, `FAN_UP`, `FAN_DOWN`, `TEMP_UP`, `TEMP_DOWN`, `DEFROST_MAX`, `DEFROST`, `DEFROST_REAR`, `UPPER_VENT`, `LOWER_VENT`, `LOWER_VENT`, `DEFROST_MAX`, `VOLUME_UP`, `VOLUME_DOWN`, `EJECT`, `SOURCE`, `SHUFFLE`, and `REPEAT` elements to `ButtonNames` 
- [0073] : Added `textFieldMetadata` parameter to `Show`

### New RPCs, Structs, and Enums 

#### Functions
- [0055] , [0058] , [0076] : `GetSystemCapability`
- [0071] : `GetInteriorVehicleData`
- [0071] : `SetInteriorVehicleData`
- [0071] : `OnInteriorVehicleData`
- [0071] : `ButtonPress`

#### Structs
- [0055] , [0058] , [0076] : `SystemCapability`
- [0055] : `NavigationCapability`
- [0055] : `PhoneCapability`
- [0058] : `VideoStreamingCapability`
- [0058] : `VideoStreamingFormat`
- [0071] : `RemoteControlCapabilities `
- [0071] : `ClimateControlCapabilities `
- [0071] : `RadioControlCapabilities `
- [0071] : `ModuleDescription`
- [0071] : `RdsData`
- [0071] : `RadioControlData`
- [0071] : `Temperature `
- [0071] : `ClimateControlData `
- [0071] : `ModuleData`
- [0073] : `MetadataStruct`

#### Enums
- [0055] , [0058] , [0076] : `SystemCapabilityType`
- [0058] : `VideoStreamingCodec`
- [0058] : `VideoStreamingProtocol`
- [0076] : `RadioState`
- [0071] : `ModuleType `
- [0071] : `DefrostZone `
- [0071] : `VentilationMode `
- [0071] : `RadioBand`
- [0071] : `RadioState`
- [0071] : `TemperatureUnit `
- [0073] : `TextFieldType`



[0055]:https://github.com/smartdevicelink/sdl_evolution/issues/166
[0058]:https://github.com/smartdevicelink/sdl_evolution/issues/176
[0060]:https://github.com/smartdevicelink/sdl_evolution/issues/178
[0071]:https://github.com/smartdevicelink/sdl_evolution/issues/206
[0073]:https://github.com/smartdevicelink/sdl_evolution/issues/208
[0076]:https://github.com/smartdevicelink/sdl_evolution/issues/220