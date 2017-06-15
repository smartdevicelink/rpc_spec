# RPC Spec 4.5.0


### Breaking Changes


### Modifications
- [0014](https://github.com/smartdevicelink/sdl_evolution/issues/42) : Added `FILE` element to `SpeechCapabilities` and updated TTSChunk param description
- [0037](https://github.com/smartdevicelink/sdl_evolution/issues/123) : added param `crc` to `PutFile` and added `ResultType` of `CORRUPTED_DATA`.
- [0031](https://github.com/smartdevicelink/sdl_evolution/issues/97): Added `PROJECTION` element to `AppHMIType` 
- [0041](https://github.com/smartdevicelink/sdl_evolution/issues/127) : Added param `iconResumed` to the `RegisterAppInterface` response.
- [0049](https://github.com/smartdevicelink/sdl_evolution/issues/144) : Added `CANCEL` element to `TouchType`
- [0023](https://github.com/smartdevicelink/sdl_evolution/issues/82) : Updated Mobile API to include the `mandatory` flag on all parameters

### New RPCs, Structs, and Enums 