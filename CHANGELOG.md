# RPC Spec 4.4.0


### Breaking Changes


### Modifications
- [0014](https://github.com/smartdevicelink/sdl_evolution/issues/42) : Added `FILE` element to `SpeechCapabilities` and updated TTSChunk param description
- [0037](https://github.com/smartdevicelink/sdl_evolution/issues/123) : added param `crc` to `PutFile` and added `ResultType` of `CORRUPTED_DATA`.
- [0031](https://github.com/smartdevicelink/sdl_evolution/issues/97): Added `PROJECTION` element to `AppHMIType` 
- [0041](https://github.com/smartdevicelink/sdl_evolution/issues/127) : Added param `iconResumed` to the `RegisterAppInterface` response.
- [0049](https://github.com/smartdevicelink/sdl_evolution/issues/144) : Added `CANCEL` element to `TouchType`
- [0050](https://github.com/smartdevicelink/sdl_evolution/issues/151) :`SyncMsgVersion`  now includes a patch version


### New RPCs, Structs, and Enums 