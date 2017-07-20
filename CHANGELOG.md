# RPC Spec 4.5.0


### Breaking Changes


### Modifications
- [0031](https://github.com/smartdevicelink/sdl_evolution/issues/97): Added `PROJECTION` element to `AppHMIType` 
- [0049](https://github.com/smartdevicelink/sdl_evolution/issues/144) : Added `CANCEL` element to `TouchType`
- [0055] : Added `DATA_NOT_AVAILABLE` to `Result`
- [0058] : Added `videoStreaming ` to `HMICapabilities`
- [0060] , [0076] : Added `EN-IN`, `TH-TH`, `EN-SA`, `HE-IL`, `RO-RO`, `UK-UA`,`ID-ID`, `VI-VN`, `MS-MY`, and `HI-IN` to elements to `Language` 
- [0076] : Added `REMOTE_CONTROL` element to `AppHMIType`
- [0076] : Added `AC_MAX`, `AC`, `RECIRCULATE`, `FAN_UP`, `FAN_DOWN`, `TEMP_UP`, `TEMP_DOWN`, `DEFROST_MAX`, `DEFROST`, `DEFROST_REAR`, `UPPER_VENT`, `LOWER_VENT`, `LOWER_VENT`, `DEFROST_MAX`, `VOLUME_UP`, `VOLUME_DOWN`, `EJECT`, `SOURCE`, `SHUFFLE`, and `REPEAT` elements to `ButtonNames` 

### New RPCs, Structs, and Enums 

#### Functions
- [0055] , [0058] , [0076] : `GetSystemCapability`
- [0076] : `GetInteriorVehicleData`
- [0076] : `SetInteriorVehicleData`
- [0076] : `OnInteriorVehicleData`
- [0076] : `ButtonPress`

#### Structs
- [0055] , [0058] , [0076] : `SystemCapability`
- [0055] : `NavigationCapability`
- [0055] : `PhoneCapability`
- [0058] : `VideoStreamingCapability`
- [0058] : `VideoStreamingFormat`
- [0076] : `RemoteControlCapabilities `
- [0076] : `ClimateControlCapabilities `
- [0076] : `RadioControlCapabilities `
- [0076] : `ModuleDescription`
- [0076] : `RdsData`
- [0076] : `RadioControlData`
- [0076] : `Temperature `
- [0076] : `ClimateControlData `
- [0076] : `ModuleData`

#### Enums
- [0055] , [0058] , [0076] : `SystemCapabilityType`
- [0058] : `VideoStreamingCodec`
- [0058] : `VideoStreamingProtocol`
- [0076] : `RadioState`
- [0076] : `ModuleType `
- [0076] : `DefrostZone `
- [0076] : `VentilationMode `
- [0076] : `RadioBand`
- [0076] : `RadioState`
- [0076] : `TemperatureUnit `



[0055]:https://github.com/smartdevicelink/sdl_evolution/issues/166
[0058]:https://github.com/smartdevicelink/sdl_evolution/issues/176
[0060]:https://github.com/smartdevicelink/sdl_evolution/issues/178
[0071]:https://github.com/smartdevicelink/sdl_evolution/issues/206

[0076]:https://github.com/smartdevicelink/sdl_evolution/issues/220