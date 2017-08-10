# SmartDeviceLink
# RPC Spec

###### Version: 4.5.0

## Enumerations

### Result
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`SUCCESS`|The request succeeded|
|`UNSUPPORTED_REQUEST`|The request is not supported by the headunit|
|`UNSUPPORTED_RESOURCE`|A button that was requested for subscription is not supported under the current system.            |
|`DISALLOWED`|RPC is not authorized in local policy table.|
|`REJECTED`|The requested command was rejected, e.g. because mobile app is in background and cannot perform any HMI commands.                Or an HMI command (e.g. Speak) is rejected because a higher priority HMI command (e.g. Alert) is playing.            |
|`ABORTED`|A command was aborted, for example due to user interaction (e.g. user pressed button).                Or an HMI command (e.g. Speak) is aborted because a higher priority HMI command (e.g. Alert) was requested.            |
|`IGNORED`|A command was ignored, because the intended result is already in effect.                For example, SetMediaClockTimer was used to pause the media clock although the clock is paused already.                NOTE: potentially replaces SUBSCRIBED_ALREADY            |
|`RETRY`|The user interrupted the RPC (e.g. PerformAudioPassThru) and indicated to start over.  Note, the app must issue the new RPC.|
|`IN_USE`|The data may not be changed, because it is currently in use.                For example when trying to delete a command set that is currently involved in an interaction.            |
|`VEHICLE_DATA_NOT_AVAILABLE`|The requested vehicle data is not available on this vehicle or is not published.|
|`TIMED_OUT`|Overlay reached the maximum timeout and closed.|
|`INVALID_DATA`|The data sent is invalid. For example:                Invalid Json syntax                Parameters out of bounds (number or enum range)                Mandatory parameters not provided                Parameter provided with wrong type                Invalid characters                Empty string            |
|`CHAR_LIMIT_EXCEEDED`||
|`INVALID_ID`|One of the provided IDs is not valid. For example                This applies to CorrelationID, SubscriptionID, CommandID, MenuID, etc.            |
|`DUPLICATE_NAME`|There was a conflict with an registered name (application or menu item) or vr command|
|`APPLICATION_NOT_REGISTERED`|An command can not be executed because no application has been registered with RegisterApplication.|
|`WRONG_LANGUAGE`|The requested language is currently not supported.                Might be because of a mismatch of the currently active language on the headunit and the requested language            |
|`OUT_OF_MEMORY`|The system could not process the request because the necessary memory couldn't be allocated|
|`TOO_MANY_PENDING_REQUESTS`|There are too many requests pending (means, that the response has not been delivered, yet).|
|`TOO_MANY_APPLICATIONS`|There are already too many registered applications|
|`APPLICATION_REGISTERED_ALREADY`|RegisterApplication has been called again, after a RegisterApplication was successful before.|
|`WARNINGS`|The RPC (e.g. SubscribeVehicleData) executed successfully but one or more items have a warning or failure.|
|`GENERIC_ERROR`|Provided data is valid but something went wrong in the lower layers.|
|`USER_DISALLOWED`|RPC is included in a functional group explicitly blocked by the user.|
|`TRUNCATED_DATA`|The RPC (e.g. ReadDID) executed successfully but the data exceeded the platform maximum threshold and thus, only part of the data is available.|
|`UNSUPPORTED_VERSION`|Sync doesn't support the protocol that is requested by the mobile application|
|`VEHICLE_DATA_NOT_ALLOWED`|The user has turned off access to vehicle data, and it is globally unavailable to mobile applications.|
|`FILE_NOT_FOUND`|A specified file could not be found on the headunit.|
|`CANCEL_ROUTE`|User selected to Cancel Route.|
|`SAVED`|The RPC (e.g. Slider) executed successfully and the user elected to save the current position / value.|
|`INVALID_CERT`|The certificate provided during authentication is invalid.|
|`EXPIRED_CERT`|The certificate provided during authentication is expired.|
|`RESUME_FAILED`|The provided hash ID does not match the hash of the current set of registered data or the core could not resume the previous data.|
|`DATA_NOT_AVAILABLE`|The requested information is currently nnot available. This is different than UNSUPPORTED_RESOURCE because it implies the data is at some point available. |


### ButtonPressMode
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`LONG`|A button was released, after it was pressed for a long time                Actual timing is defined by the headunit and may vary            |
|`SHORT`|A button was released, after it was pressed for a short time                Actual timing is defined by the headunit and may vary            |


### ButtonEventMode
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`BUTTONUP`|A button has been released up|
|`BUTTONDOWN`|A button has been pressed down|


### Language
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`EN-US`|English - US|
|`ES-MX`|Spanish - Mexico|
|`FR-CA`|French - Canada|
|`DE-DE`|German - Germany|
|`ES-ES`|Spanish - Spain|
|`EN-GB`|English - GB|
|`RU-RU`|Russian - Russia|
|`TR-TR`|Turkish - Turkey|
|`PL-PL`|Polish - Poland|
|`FR-FR`|French - France|
|`IT-IT`|Italian - Italy|
|`SV-SE`|Swedish - Sweden|
|`PT-PT`|Portuguese - Portugal|
|`NL-NL`|Dutch (Standard) - Netherlands|
|`EN-AU`|English - Australia|
|`ZH-CN`|Mandarin - China|
|`ZH-TW`|Mandarin - Taiwan|
|`JA-JP`|Japanese - Japan|
|`AR-SA`|Arabic - Saudi Arabia|
|`KO-KR`|Korean - South Korea|
|`PT-BR`|Portuguese - Brazil|
|`CS-CZ`|Czech - Czech Republic|
|`DA-DK`|Danish - Denmark|
|`NO-NO`|Norwegian - Norway|
|`NL-BE`|Dutch (Flemish) - Belgium|
|`EL-GR`|Greek - Greece|
|`HU-HU`|Hungarian - Hungary|
|`FI-FI`|Finnish - Finland|
|`SK-SK`|Slovak - Slovakia|
|`EN-IN`|English - India|
|`TH-TH`|Thai - Thailand|
|`EN-SA`|English - Middle East|
|`HE-IL`|Hebrew - Israel|
|`RO-RO`|Romanian - Romania|
|`UK-UA`|Ukrainian - Ukraine|
|`ID-ID`|Indonesian - Indonesia|
|`VI-VN`|Vietnamese - Vietnam|
|`MS-MY`|Malay - Malaysia|
|`HI-IN`|Hindi - India|


### UpdateMode
Describes how the media clock timer should behave on the platform

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`COUNTUP`|Starts the media clock timer counting upwards, as in time elapsed.|
|`COUNTDOWN`|Starts the media clock timer counting downwards, as in time remaining.|
|`PAUSE`|Pauses the media clock timer|
|`RESUME`|Resume the media clock timer|
|`CLEAR`|Clears the media clock timer (previously done through Show->mediaClock)|


### TimerMode
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`UP`|Causes the media clock timer to update from 0:00 to a specified time|
|`DOWN`|Causes the media clock timer to update from a specified time to 0:00|
|`NONE`|Indicates to not use the media clock timer|


### InteractionMode
For application-requested interactions, this mode indicates the method in which the user is notified and uses the interaction.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`MANUAL_ONLY`|This mode causes the interaction to only occur on the display, meaning the choices are provided only via the display. No Voice Interaction.|
|`VR_ONLY`|This mode causes the interaction to only occur using the headunits VR system. Selections are made by saying the command.|
|`BOTH`|This mode causes both a VR and display selection option for an interaction. The user will first be asked via Voice Interaction (if available). If this is unsuccessfull, the system will switch to manual input.|


### LayoutMode
For touchscreen interactions, the mode of how the choices are presented.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`ICON_ONLY`|This mode causes the interaction to display the previous set of choices as icons.|
|`ICON_WITH_SEARCH`|This mode causes the interaction to display the previous set of choices as icons along with a search field in the HMI.|
|`LIST_ONLY`|This mode causes the interaction to display the previous set of choices as a list.|
|`LIST_WITH_SEARCH`|This mode causes the interaction to display the previous set of choices as a list along with a search field in the HMI.|
|`KEYBOARD`|This mode causes the interaction to immediately display a keyboard entry through the HMI.|


### HMILevel
Enumeraction that describes current levels of HMI.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`FULL`||
|`LIMITED`||
|`BACKGROUND`||
|`NONE`||


### AudioStreamingState
Enumeraction that describes possible states of audio streaming.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`AUDIBLE`||
|`ATTENUATED`||
|`NOT_AUDIBLE`||


### SystemAction
Enumeration that describes system actions that can be triggered.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`DEFAULT_ACTION`|Default action occurs.  Standard behavior (e.g. SoftButton clears overlay).|
|`STEAL_FOCUS`|App is brought into HMI_FULL.|
|`KEEP_CONTEXT`|Current system context is maintained.  An overlay is persisted even though a SoftButton has been pressed and the notification sent.|


### SystemContext
Enumeration that describes possible contexts an app's HMI might be in. Communicated to whichever app is in HMI FULL, except Alert.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`MAIN`|The app's persistent display (whether media/non-media/navigation) is fully visible onscreen.|
|`VRSESSION`|The system is currently in a VR session (with whatever dedicated VR screen being overlaid onscreen).|
|`MENU`|The system is currently displaying an in-App menu onscreen.|
|`HMI_OBSCURED`|The app's display HMI is currently being obscured by either a system or other app's overlay.|
|`ALERT`|Broadcast only to whichever app has an alert currently being displayed.|


### SoftButtonType
Contains information about the SoftButton capabilities.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`TEXT`||
|`IMAGE`||
|`BOTH`||


### AppInterfaceUnregisteredReason
Error code, which comes from the module side.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`IGNITION_OFF`||
|`BLUETOOTH_OFF`||
|`USB_DISCONNECTED`||
|`REQUEST_WHILE_IN_NONE_HMI_LEVEL`||
|`TOO_MANY_REQUESTS`||
|`DRIVER_DISTRACTION_VIOLATION`||
|`LANGUAGE_CHANGE`||
|`MASTER_RESET`||
|`FACTORY_DEFAULTS`||
|`APP_UNAUTHORIZED`||
|`PROTOCOL_VIOLATION`||
|`UNSUPPORTED_HMI_RESOURCE`||


### TriggerSource
Indicates the source from where the command was triggered.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`MENU`||
|`VR`||
|`KEYBOARD`||


### HmiZoneCapabilities
Contains information about the HMI zone capabilities.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`FRONT`||
|`BACK`||


### SpeechCapabilities
Contains information about the TTS capabilities.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`TEXT`||
|`SAPI_PHONEMES`||
|`LHPLUS_PHONEMES`||
|`PRE_RECORDED`||
|`SILENCE`||


### VrCapabilities
Contains information about the VR capabilities.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`TEXT`||


### PrerecordedSpeech
Contains a list of prerecorded speech items present on the platform.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`HELP_JINGLE`||
|`INITIAL_JINGLE`||
|`LISTEN_JINGLE`||
|`POSITIVE_JINGLE`||
|`NEGATIVE_JINGLE`||


### SamplingRate
Describes different sampling options for PerformAudioPassThru.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`8KHZ`||
|`16KHZ`||
|`22KHZ`||
|`44KHZ`||


### BitsPerSample
Describes different quality options for PerformAudioPassThru.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`8_BIT`||
|`16_BIT`||


### AudioType
Describes different audio type options for PerformAudioPassThru.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`PCM`||


### VehicleDataType
Defines the data types that can be published and subscribed to.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`VEHICLEDATA_GPS`|Notifies GPSData may be subscribed|
|`VEHICLEDATA_SPEED`||
|`VEHICLEDATA_RPM`||
|`VEHICLEDATA_FUELLEVEL`||
|`VEHICLEDATA_FUELLEVEL_STATE`||
|`VEHICLEDATA_FUELCONSUMPTION`||
|`VEHICLEDATA_EXTERNTEMP`||
|`VEHICLEDATA_VIN`||
|`VEHICLEDATA_PRNDL`||
|`VEHICLEDATA_TIREPRESSURE`||
|`VEHICLEDATA_ODOMETER`||
|`VEHICLEDATA_BELTSTATUS`||
|`VEHICLEDATA_BODYINFO`||
|`VEHICLEDATA_DEVICESTATUS`||
|`VEHICLEDATA_ECALLINFO`||
|`VEHICLEDATA_AIRBAGSTATUS`||
|`VEHICLEDATA_EMERGENCYEVENT`||
|`VEHICLEDATA_CLUSTERMODESTATUS`||
|`VEHICLEDATA_MYKEY`||
|`VEHICLEDATA_BRAKING`||
|`VEHICLEDATA_WIPERSTATUS`||
|`VEHICLEDATA_HEADLAMPSTATUS`||
|`VEHICLEDATA_BATTVOLTAGE`||
|`VEHICLEDATA_ENGINETORQUE`||
|`VEHICLEDATA_ACCPEDAL`||
|`VEHICLEDATA_STEERINGWHEEL`||


### ButtonName
Defines the hard (physical) and soft (touchscreen) buttons available from the module

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`OK`||
|`SEEKLEFT`||
|`SEEKRIGHT`||
|`TUNEUP`||
|`TUNEDOWN`||
|`PRESET_0`||
|`PRESET_1`||
|`PRESET_2`||
|`PRESET_3`||
|`PRESET_4`||
|`PRESET_5`||
|`PRESET_6`||
|`PRESET_7`||
|`PRESET_8`||
|`PRESET_9`||
|`CUSTOM_BUTTON`||
|`SEARCH`||
|`AC_MAX`||
|`AC`||
|`RECIRCULATE`||
|`FAN_UP`||
|`FAN_DOWN`||
|`TEMP_UP`||
|`TEMP_DOWN`||
|`DEFROST_MAX`||
|`DEFROST`||
|`DEFROST_REAR`||
|`UPPER_VENT`||
|`LOWER_VENT`||
|`VOLUME_UP`||
|`VOLUME_DOWN`||
|`EJECT`||
|`SOURCE`||
|`SHUFFLE`||
|`REPEAT`||


### MediaClockFormat
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`CLOCK1`|minutesFieldWidth = 2;minutesFieldMax = 19;secondsFieldWidth = 2;secondsFieldMax = 99;maxHours = 19;maxMinutes = 59;maxSeconds = 59;                used for Type II and CID headunits            |
|`CLOCK2`|minutesFieldWidth = 3;minutesFieldMax = 199;secondsFieldWidth = 2;secondsFieldMax = 99;maxHours = 59;maxMinutes = 59;maxSeconds = 59;                used for Type V headunit            |
|`CLOCK3`|minutesFieldWidth = 2;minutesFieldMax = 59;secondsFieldWidth = 2;secondsFieldMax = 59;maxHours = 9;maxMinutes = 59;maxSeconds = 59;                used for GEN1.1 MFD3/4/5 headunits            |
|`CLOCKTEXT1`|5 characters possible                Format:      1|sp   c   :|sp   c   c                1|sp : digit "1" or space                c    : character out of following character set: sp|0-9|[letters, see TypeII column in XLS. See [@TODO: create file ref]]                :|sp : colon or space                used for Type II headunit            |
|`CLOCKTEXT2`|5 chars possible                Format:      1|sp   c   :|sp   c   c                1|sp : digit "1" or space                c    : character out of following character set: sp|0-9|[letters, see CID column in XLS. See [@TODO: create file ref]]                :|sp : colon or space                used for CID headunit                NOTE: difference between CLOCKTEXT1 and CLOCKTEXT2 is the supported character set            |
|`CLOCKTEXT3`|6 chars possible                Format:      1|sp   c   c   :|sp   c   c                1|sp : digit "1" or space                c    : character out of following character set: sp|0-9|[letters, see Type 5 column in XLS]. See [@TODO: create file ref]                :|sp : colon or space                used for Type V headunit            |
|`CLOCKTEXT4`|6 chars possible                Format:      c   :|sp   c   c   :   c   c                :|sp : colon or space                c    : character out of following character set: sp|0-9|[letters].                used for GEN1.1 MFD3/4/5 headunits            |


### DisplayType
See DAES for further infos regarding the displays

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`CID`||
|`TYPE2`||
|`TYPE5`||
|`NGN`||
|`GEN2_8_DMA`||
|`GEN2_6_DMA`||
|`MFD3`||
|`MFD4`||
|`MFD5`||
|`GEN3_8-INCH`||
|`SDL_GENERIC`||


### TextFieldName
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`mainField1`|The first line of first set of main fields of the persistent display; applies to "Show"|
|`mainField2`|The second line of first set of main fields of the persistent display; applies to "Show"|
|`mainField3`|The first line of second set of main fields of persistent display; applies to "Show"|
|`mainField4`|The second line of second set of main fields of the persistent display; applies to "Show"|
|`statusBar`|The status bar on NGN; applies to "Show"|
|`mediaClock`|Text value for MediaClock field; applies to "Show"|
|`mediaTrack`|The track field of NGN and GEN1.1 MFD displays. This field is only available for media applications; applies to "Show"|
|`alertText1`|The first line of the alert text field; applies to "Alert"|
|`alertText2`|The second line of the alert text field; applies to "Alert"|
|`alertText3`|The third line of the alert text field; applies to "Alert"|
|`scrollableMessageBody`|Long form body of text that can include newlines and tabs; applies to "ScrollableMessage"|
|`initialInteractionText`|First line suggestion for a user response (in the case of VR enabled interaction)|
|`navigationText1`|First line of navigation text|
|`navigationText2`|Second line of navigation text|
|`ETA`|Estimated Time of Arrival time for navigation|
|`totalDistance`|Total distance to destination for navigation|
|`audioPassThruDisplayText1`|First line of text for audio pass thru|
|`audioPassThruDisplayText2`|Second line of text for audio pass thru|
|`sliderHeader`|Header text for slider|
|`sliderFooter`|Footer text for slider|
|`menuName`|Primary text for Choice|
|`secondaryText`|Secondary text for Choice|
|`tertiaryText`|Tertiary text for Choice|
|`menuTitle`|Optional text to label an app menu button (for certain touchscreen platforms).|
|`locationName`|Optional name / title of intended location for SendLocation.|
|`locationDescription`|Optional description of intended location / establishment (if applicable) for SendLocation.|
|`addressLines`|Optional location address (if applicable) for SendLocation.|
|`phoneNumber`|Optional hone number of intended location / establishment (if applicable) for SendLocation.|


### ImageFieldName
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`softButtonImage`|The image field for SoftButton|
|`choiceImage`|The first image field for Choice|
|`choiceSecondaryImage`|The secondary image field for Choice|
|`vrHelpItem`|The image field for vrHelpItem|
|`turnIcon`|The image field for Turn|
|`menuIcon`|The image field for the menu icon in SetGlobalProperties|
|`cmdIcon`|The image field for AddCommand|
|`appIcon`|The image field for the app icon (set by setAppIcon)|
|`graphic`|The image field for Show|
|`showConstantTBTIcon`|The primary image field for ShowConstantTBT|
|`showConstantTBTNextTurnIcon`|The secondary image field for ShowConstantTBT|
|`locationImage`|The optional image of a destination / location|


### CharacterSet
The list of potential character sets

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`TYPE2SET`|See [@TODO: create file ref]|
|`TYPE5SET`|See [@TODO: create file ref]|
|`CID1SET`|See [@TODO: create file ref]|
|`CID2SET`|See [@TODO: create file ref]|


### TextAlignment
The list of possible alignments, left, right, or centered

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`LEFT_ALIGNED`||
|`RIGHT_ALIGNED`||
|`CENTERED`||


### TBTState
Enumeration that describes possible states of turn-by-turn client or AppLink app.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`ROUTE_UPDATE_REQUEST`||
|`ROUTE_ACCEPTED`||
|`ROUTE_REFUSED`||
|`ROUTE_CANCELLED`||
|`ETA_REQUEST`||
|`NEXT_TURN_REQUEST`||
|`ROUTE_STATUS_REQUEST`||
|`ROUTE_SUMMARY_REQUEST`||
|`TRIP_STATUS_REQUEST`||
|`ROUTE_UPDATE_REQUEST_TIMEOUT`||


### DriverDistractionState
Enumeration that describes possible states of driver distraction.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`DD_ON`||
|`DD_OFF`||


### ImageType
Contains information about the type of image.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`STATIC`||
|`DYNAMIC`||


### DeliveryMode
The mode in which the SendLocation request is sent

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`PROMPT`||
|`DESTINATION`||
|`QUEUE`||


### GlobalProperty
The different global properties.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`HELPPROMPT`|The property helpPrompt of setGlobalProperties|
|`TIMEOUTPROMPT`|The property timeoutPrompt of setGlobalProperties|
|`VRHELPTITLE`|The property vrHelpTitle of setGlobalProperties|
|`VRHELPITEMS`|The property array of vrHelp of setGlobalProperties|
|`MENUNAME`|The property in-app menu name of setGlobalProperties|
|`MENUICON`|The property in-app menu icon of setGlobalProperties|
|`KEYBOARDPROPERTIES`|The on-screen keyboard configuration of setGlobalProperties|


### CompassDirection
The list of potential compass directions

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`NORTH`||
|`NORTHWEST`||
|`WEST`||
|`SOUTHWEST`||
|`SOUTH`||
|`SOUTHEAST`||
|`EAST`||
|`NORTHEAST`||


### Dimension
The supported dimensions of the GPS

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`NO_FIX`|No GPS at all|
|`2D`|Longitude and lattitude|
|`3D`|Longitude and lattitude and altitude|


### PRNDL
The selected gear.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`PARK`|Parking|
|`REVERSE`|Reverse gear|
|`NEUTRAL`|No gear|
|`DRIVE`||
|`SPORT`|Drive Sport mode|
|`LOWGEAR`|1st gear hold|
|`FIRST`||
|`SECOND`||
|`THIRD`||
|`FOURTH`||
|`FIFTH`||
|`SIXTH`||
|`SEVENTH`||
|`EIGHTH`||
|`UNKNOWN`||
|`FAULT`||


### ComponentVolumeStatus
The volume status of a vehicle component.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`UNKNOWN`||
|`NORMAL`||
|`LOW`||
|`FAULT`||
|`ALERT`||
|`NOT_SUPPORTED`||


### WarningLightStatus
Reflects the status of a cluster instrument warning light.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`OFF`||
|`ON`||
|`FLASH`||
|`NOT_USED`||


### VehicleDataNotificationStatus
Reflects the status of a vehicle data notification.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`NOT_SUPPORTED`||
|`NORMAL`||
|`ACTIVE`||
|`NOT_USED`||


### IgnitionStableStatus
Reflects the ignition switch stability.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`IGNITION_SWITCH_NOT_STABLE`||
|`IGNITION_SWITCH_STABLE`||
|`MISSING_FROM_TRANSMITTER`||


### IgnitionStatus
Reflects the status of ignition.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`UNKNOWN`||
|`OFF`||
|`ACCESSORY`||
|`RUN`||
|`START`||
|`INVALID`||


### VehicleDataEventStatus
Reflects the status of a vehicle data event; e.g. a seat belt event status.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`NO_EVENT`||
|`NO`||
|`YES`||
|`NOT_SUPPORTED`||
|`FAULT`||


### DeviceLevelStatus
Reflects the reported battery status of the connected device, if reported.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`ZERO_LEVEL_BARS`||
|`ONE_LEVEL_BARS`||
|`TWO_LEVEL_BARS`||
|`THREE_LEVEL_BARS`||
|`FOUR_LEVEL_BARS`||
|`NOT_PROVIDED`||


### PrimaryAudioSource
Reflects the current primary audio source (if selected).

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`NO_SOURCE_SELECTED`||
|`USB`||
|`USB2`||
|`BLUETOOTH_STEREO_BTST`||
|`LINE_IN`||
|`IPOD`||
|`MOBILE_APP`||


### WiperStatus
Reflects the status of the wipers.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`OFF`||
|`AUTO_OFF`||
|`OFF_MOVING`||
|`MAN_INT_OFF`||
|`MAN_INT_ON`||
|`MAN_LOW`||
|`MAN_HIGH`||
|`MAN_FLICK`||
|`WASH`||
|`AUTO_LOW`||
|`AUTO_HIGH`||
|`COURTESYWIPE`||
|`AUTO_ADJUST`||
|`STALLED`||
|`NO_DATA_EXISTS`||


### VehicleDataStatus
Reflects the status of a binary vehicle data item.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`NO_DATA_EXISTS`||
|`OFF`||
|`ON`||


### MaintenanceModeStatus
Reflects the status of a vehicle maintenance mode.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`NORMAL`||
|`NEAR`||
|`ACTIVE`||
|`FEATURE_NOT_PRESENT`||


### VehicleDataActiveStatus
Reflects the status of given vehicle component.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`INACTIVE_NOT_CONFIRMED`||
|`INACTIVE_CONFIRMED`||
|`ACTIVE_NOT_CONFIRMED`||
|`ACTIVE_CONFIRMED`||
|`FAULT`||


### AmbientLightStatus
Reflects the status of the ambient light sensor.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`NIGHT`||
|`TWILIGHT_1`||
|`TWILIGHT_2`||
|`TWILIGHT_3`||
|`TWILIGHT_4`||
|`DAY`||
|`UNKNOWN`||
|`INVALID`||


### FileType
Enumeration listing possible file types.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`GRAPHIC_BMP`||
|`GRAPHIC_JPEG`||
|`GRAPHIC_PNG`||
|`AUDIO_WAVE`||
|`AUDIO_MP3`||
|`AUDIO_AAC`||
|`BINARY`||
|`JSON`||


### FuelCutoffStatus
Reflects the status of the RCM fuel cutoff.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`TERMINATE_FUEL`||
|`NORMAL_OPERATION`||
|`FAULT`||


### EmergencyEventType
Reflects the emergency event status of the vehicle.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`NO_EVENT`||
|`FRONTAL`||
|`SIDE`||
|`REAR`||
|`ROLLOVER`||
|`NOT_SUPPORTED`||
|`FAULT`||


### ECallConfirmationStatus
Reflects the status of the eCall Notification.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`NORMAL`||
|`CALL_IN_PROGRESS`||
|`CALL_CANCELLED`||
|`CALL_COMPLETED`||
|`CALL_UNSUCCESSFUL`||
|`ECALL_CONFIGURED_OFF`||
|`CALL_COMPLETE_DTMF_TIMEOUT`||


### PowerModeQualificationStatus
Reflects the status of the current power mode qualification.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`POWER_MODE_UNDEFINED`||
|`POWER_MODE_EVALUATION_IN_PROGRESS`||
|`NOT_DEFINED`||
|`POWER_MODE_OK`||


### PowerModeStatus
Reflects the status of the current power mode.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`KEY_OUT`||
|`KEY_RECENTLY_OUT`||
|`KEY_APPROVED_0`||
|`POST_ACCESORY_0`||
|`ACCESORY_1`||
|`POST_IGNITION_1`||
|`IGNITION_ON_2`||
|`RUNNING_2`||
|`CRANK_3`||


### CarModeStatus
Reflects the status of the current car mode.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`NORMAL`||
|`FACTORY`||
|`TRANSPORT`||
|`CRASH`||


### VehicleDataResultCode
Enumeration that describes possible result codes of a vehicle data entry request.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`SUCCESS`|Individual vehicle data item / DTC / DID request or subscription successful|
|`TRUNCATED_DATA`|DTC / DID request successful, however, not all active DTCs or full contents of DID location available|
|`DISALLOWED`|This vehicle data item is not allowed for this app by Ford.|
|`USER_DISALLOWED`|The user has not granted access to this type of vehicle data item at this time.|
|`INVALID_ID`|The ECU ID referenced is not a valid ID on the bus / system.|
|`VEHICLE_DATA_NOT_AVAILABLE`|The requested vehicle data item / DTC / DID is not currently available or responding on the bus / system.|
|`DATA_ALREADY_SUBSCRIBED`|The vehicle data item is already subscribed.|
|`DATA_NOT_SUBSCRIBED`|The vehicle data item cannot be unsubscribed because it is not currently subscribed.|
|`IGNORED`|The request for this item is ignored because it is already in progress.|


### TouchType
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`BEGIN`||
|`MOVE`||
|`END`||
|`CANCEL`||


### PermissionStatus
Enumeration that describes possible permission states of a policy table entry.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`ALLOWED`||
|`DISALLOWED`||
|`USER_DISALLOWED`||
|`USER_CONSENT_PENDING`||


### KeyboardLayout
Enumeration listing possible keyboard layouts.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`QWERTY`||
|`QWERTZ`||
|`AZERTY`||


### KeyboardEvent
Enumeration listing possible keyboard events.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`KEYPRESS`||
|`ENTRY_SUBMITTED`||
|`ENTRY_VOICE`||
|`ENTRY_CANCELLED`||
|`ENTRY_ABORTED`||


### KeypressMode
Enumeration listing possible keyboard events.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`SINGLE_KEYPRESS`|Each keypress is individually sent as the user presses the keyboard keys.|
|`QUEUE_KEYPRESSES`|The keypresses are queued and a string is eventually sent once the user chooses to submit their entry.|
|`RESEND_CURRENT_ENTRY`|The keypresses are queue and a string is sent each time the user presses a keyboard key; the string contains the entire current entry.|


### RequestType
Enumeration listing possible asynchronous requests.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`HTTP`||
|`FILE_RESUME`||
|`AUTH_REQUEST`||
|`AUTH_CHALLENGE`||
|`AUTH_ACK`||
|`PROPRIETARY`||
|`QUERY_APPS`||
|`LAUNCH_APP`||
|`LOCK_SCREEN_ICON_URL`||
|`TRAFFIC_MESSAGE_CHANNEL`||
|`DRIVER_PROFILE`||
|`VOICE_SEARCH`||
|`NAVIGATION`||
|`PHONE`||
|`CLIMATE`||
|`SETTINGS`||
|`VEHICLE_DIAGNOSTICS`||
|`EMERGENCY`||
|`MEDIA`||
|`FOTA`||


### AppHMIType
Enumeration listing possible app types.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`DEFAULT`||
|`COMMUNICATION`||
|`MEDIA`||
|`MESSAGING`||
|`NAVIGATION`||
|`INFORMATION`||
|`SOCIAL`||
|`BACKGROUND_PROCESS`||
|`TESTING`||
|`SYSTEM`||
|`PROJECTION`||
|`REMOTE_CONTROL`||


### PredefinedLayout
Predefined screen layout.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`DEFAULT`|Default media / non-media screen.         Can be set as a root screen.         |
|`MEDIA`|Default Media screen.         Can be set as a root screen.         |
|`NON-MEDIA`|Default Non-media screen.         Can be set as a root screen.         |
|`ONSCREEN_PRESETS`|Custom root media screen containing app-defined onscreen presets.         Can be set as a root screen.         |
|`NAV_FULLSCREEN_MAP`|Custom root template screen containing full screen map with navigation controls.         Can be set as a root screen.         |
|`NAV_LIST`|Custom root template screen containing video represented list.         Can be set as a root screen.         |
|`NAV_KEYBOARD`|Custom root template screen containing video represented keyboard.         Can be set as a root screen.         |
|`GRAPHIC_WITH_TEXT`|Custom root template screen containing half-screen graphic with lines of text.         Can be set as a root screen.         |
|`TEXT_WITH_GRAPHIC`|Custom root template screen containing lines of text with half-screen graphic.         Can be set as a root screen.         |
|`TILES_ONLY`|Custom root template screen containing only tiled SoftButtons.         Can be set as a root screen.         |
|`TEXTBUTTONS_ONLY`|Custom root template screen containing only text SoftButtons.         Can be set as a root screen.         |
|`GRAPHIC_WITH_TILES`|Custom root template screen containing half-screen graphic with tiled SoftButtons.         Can be set as a root screen.         |
|`TILES_WITH_GRAPHIC`|Custom root template screen containing tiled SoftButtons with half-screen graphic.         Can be set as a root screen.         |
|`GRAPHIC_WITH_TEXT_AND_SOFTBUTTONS`|Custom root template screen containing half-screen graphic with text and SoftButtons.         Can be set as a root screen.         |
|`TEXT_AND_SOFTBUTTONS_WITH_GRAPHIC`|Custom root template screen containing text and SoftButtons with half-screen graphic.         Can be set as a root screen.         |
|`GRAPHIC_WITH_TEXTBUTTONS`|Custom root template screen containing half-screen graphic with text only SoftButtons.         Can be set as a root screen.         |
|`TEXTBUTTONS_WITH_GRAPHIC`|Custom root template screen containing text only SoftButtons with half-screen graphic.         Can be set as a root screen.         |
|`LARGE_GRAPHIC_WITH_SOFTBUTTONS`|Custom root template screen containing a large graphic and SoftButtons.         Can be set as a root screen.         |
|`DOUBLE_GRAPHIC_WITH_SOFTBUTTONS`|Custom root template screen containing two graphics and SoftButtons.         Can be set as a root screen.         |
|`LARGE_GRAPHIC_ONLY`|Custom root template screen containing only a large graphic.         Can be set as a root screen.         |


### FunctionID
Enumeration linking function names with function IDs in AppLink protocol. Assumes enumeration starts at value 0.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`RESERVED`||
|`RegisterAppInterfaceID`||
|`UnregisterAppInterfaceID`||
|`SetGlobalPropertiesID`||
|`ResetGlobalPropertiesID`||
|`AddCommandID`||
|`DeleteCommandID`||
|`AddSubMenuID`||
|`DeleteSubMenuID`||
|`CreateInteractionChoiceSetID`||
|`PerformInteractionID`||
|`DeleteInteractionChoiceSetID`||
|`AlertID`||
|`ShowID`||
|`SpeakID`||
|`SetMediaClockTimerID`||
|`PerformAudioPassThruID`||
|`EndAudioPassThruID`||
|`SubscribeButtonID`||
|`UnsubscribeButtonID`||
|`SubscribeVehicleDataID`||
|`UnsubscribeVehicleDataID`||
|`GetVehicleDataID`||
|`ReadDIDID`||
|`GetDTCsID`||
|`ScrollableMessageID`||
|`SliderID`||
|`ShowConstantTBTID`||
|`AlertManeuverID`||
|`UpdateTurnListID`||
|`ChangeRegistrationID`||
|`GenericResponseID`||
|`PutFileID`||
|`DeleteFileID`||
|`ListFilesID`||
|`SetAppIconID`||
|`SetDisplayLayoutID`||
|`DiagnosticMessageID`||
|`SystemRequestID`||
|`SendLocationID`||
|`DialNumberID`||
|`ButtonPressID`||
|`GetInteriorVehicleDataID`||
|`SetInteriorVehicleDataID`||
|`GetWayPointsID`||
|`SubscribeWayPointsID`||
|`UnsubscribeWayPointsID`||
|`GetSystemCapabilityID`||
|`SendHapticDataID`||
|`OnHMIStatusID`||
|`OnAppInterfaceUnregisteredID`||
|`OnButtonEventID`||
|`OnButtonPressID`||
|`OnVehicleDataID`||
|`OnCommandID`||
|`OnTBTClientStateID`||
|`OnDriverDistractionID`||
|`OnPermissionsChangeID`||
|`OnAudioPassThruID`||
|`OnLanguageChangeID`||
|`OnKeyboardInputID`||
|`OnTouchEventID`||
|`OnSystemRequestID`||
|`OnHashChangeID`||
|`OnInteriorVehicleDataID`||
|`OnWayPointChangeID`||
|`EncodedSyncPDataID`||
|`SyncPDataID`||
|`OnEncodedSyncPDataID`||
|`OnSyncPDataID`||


### messageType
Enumeration linking message types with function types in WiPro protocol.
            Assumes enumeration starts at value 0.
        

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`request`||
|`response`||
|`notification`||


### WayPointType
Describes what kind of waypoint is requested/provided.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`ALL`||
|`DESTINATION`||


### SystemCapabilityType
Enumerations of all available system capability types

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`NAVIGATION`||
|`PHONE_CALL`||
|`VIDEO_STREAMING`||
|`REMOTE_CONTROL`||


### VideoStreamingProtocol
Enum for each type of video streaming protocol type.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`RAW`|Raw stream bytes that contains no timestamp data and is the lowest supported video streaming|
|`RTP`|RTP facilitates the transfer of real-time data. Information provided by this protocol include timestamps (for synchronization), sequence numbers (for packet loss and reordering detection) and the payload format which indicates the encoded format of the data.|
|`RTSP`|The transmission of streaming data itself is not a task of RTSP. Most RTSP servers use the Real-time Transport Protocol (RTP) in conjunction with Real-time Control Protocol (RTCP) for media stream delivery. However, some vendors implement proprietary transport protocols. |
|`RTMP`|Real-Time Messaging Protocol (RTMP) was initially a proprietary protocol developed by Macromedia for streaming audio, video and data over the Internet, between a Flash player and a server. Macromedia is now owned by Adobe, which has released an incomplete version of the specification of the protocol for public use.|
|`WEBM`|The WebM container is based on a profile of Matroska. WebM initially supported VP8 video and Vorbis audio streams. In 2013 it was updated to accommodate VP9 video and Opus audio.|


### VideoStreamingCodec
Enum for each type of video streaming codec.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`H264`|A block-oriented motion-compensation-based video compression standard. As of 2014 it is one of the most commonly used formats for the recording, compression, and distribution of video content.|
|`H265`|High Efficiency Video Coding (HEVC), also known as H.265 and MPEG-H Part 2, is a video compression standard, one of several potential successors to the widely used AVC (H.264 or MPEG-4 Part 10). In comparison to AVC, HEVC offers about double the data compression ratio at the same level of video quality, or substantially improved video quality at the same bit rate. It supports resolutions up to 8192x4320, including 8K UHD.|
|`Theora`|Theora is derived from the formerly proprietary VP3 codec, released into the public domain by On2 Technologies. It is broadly comparable in design and bitrate efficiency to MPEG-4 Part 2, early versions of Windows Media Video, and RealVideo while lacking some of the features present in some of these other codecs. It is comparable in open standards philosophy to the BBC's Dirac codec.|
|`VP8`|VP8 can be multiplexed into the Matroska-based container format WebM along with Vorbis and Opus audio. The image format WebP is based on VP8's intra-frame coding. VP8's direct successor, VP9, and the emerging royalty-free internet video format AV1 from the Alliance for Open Media (AOMedia) are based on VP8.|
|`VP9`|Similar to VP8, but VP9 is customized for video resolutions beyond high-definition video (UHD) and also enables lossless compression.|


### ModuleType
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`CLIMATE`||
|`RADIO`||


### DefrostZone
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`FRONT`||
|`REAR`||
|`ALL`||
|`NONE`||


### VentilationMode
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`UPPER`||
|`LOWER`||
|`BOTH`||
|`NONE`||


### RadioBand
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`AM`||
|`FM`||
|`XM`||


### RadioState
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`ACQUIRING`||
|`ACQUIRED`||
|`MULTICAST`||
|`NOT_FOUND`||


### TemperatureUnit
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`FAHRENHEIT`||
|`CELSIUS`||


### TextFieldType
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`mediaTitle`|The data in this field contains the title of the currently playing audio track.|
|`mediaArtist`|The data in this field contains the artist or creator of the currently playing audio track.|
|`mediaAlbum`|The data in this field contains the album title of the currently playing audio track.|
|`mediaYear`|The data in this field contains the creation year of the currently playing audio track.|
|`mediaGenre`|The data in this field contains the genre of the currently playing audio track.|
|`mediaStation`|The data in this field contains the name of the current source for the media.|
|`rating`|The data in this field is a rating.|
|`currentTemperature`|The data in this field is the current temperature.|
|`maximumTemperature`|The data in this field is the maximum temperature for the day.|
|`minimumTemperature`|The data in this field is the minimum temperature for the day.|
|`weatherTerm`|The data in this field describes the current weather (ex. cloudy, clear, etc.).|
|`humidity`|The data in this field describes the current humidity value.|



<div style="page-break-after: always;"></div>

## Structs

### AudioPassThruCapabilities
Describes different audio type configurations for PerformAudioPassThru.
            e.g. {8kHz,8-bit,PCM}
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`samplingRate`|True||
|`bitsPerSample`|True||
|`audioType`|True||


### Image
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`value`|True|Either the static hex icon value or the binary image file name identifier (sent by PutFile).|
|`imageType`|True|Describes, whether it is a static or dynamic image.|


### SoftButton
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`type`|True|Describes, whether it is text, highlighted text, icon, or dynamic image. See softButtonType|
|`text`|False|Optional text to display (if defined as TEXT or BOTH)|
|`image`|False|Optional image struct for SoftButton (if defined as IMAGE or BOTH)|
|`isHighlighted`|False|True, if highlighted                False, if not highlighted            |
|`softButtonID`|True|Value which is returned via OnButtonPress / OnButtonEvent|
|`systemAction`|False|Parameter indicating whether selecting a SoftButton shall call a specific system action.  This is intended to allow Notifications to bring the callee into full / focus; or in the case of persistent overlays, the overlay can persist when a SoftButton is pressed.|


### Choice
A choice is an option given to the user, which can be selected either by menu, or through voice recognition system.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`choiceID`|True||
|`menuName`|True||
|`vrCommands`|True||
|`image`|False||
|`secondaryText`|False|Optional secondary text to display; e.g. address of POI in a search result entry|
|`tertiaryText`|False|Optional tertiary text to display; e.g. distance to POI for a search result entry|
|`secondaryImage`|False|Optional secondary image struct for choice|


### VrHelpItem
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`text`|True|Text to display for VR Help item|
|`image`|False|Image struct for VR Help item|
|`position`|True|Position to display item in VR Help list|


### SyncMsgVersion
Specifies the version number of the SmartDeviceLink protocol that is supported by the mobile application

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`majorVersion`|True|The major version indicates versions that is not-compatible to previous versions.|
|`minorVersion`|True|The minor version indicates a change to a previous version that should still allow to be run on an older version (with limited functionality)|
|`patchVersion`|False|The patch version indicates a fix to existing functionality in a previous version that should still be able to be run on an older version |


### SingleTireStatus
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`status`|True|See ComponentVolumeStatus.|


### BeltStatus
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`driverBeltDeployed`|True|References signal "VedsDrvBelt_D_Ltchd". See VehicleDataEventStatus.|
|`passengerBeltDeployed`|True|References signal "VedsPasBelt_D_Ltchd". See VehicleDataEventStatus.|
|`passengerBuckleBelted`|True|References signal "VedsRw1PasBckl_D_Ltchd". See VehicleDataEventStatus.|
|`driverBuckleBelted`|True|References signal "VedsRw1DrvBckl_D_Ltchd". See VehicleDataEventStatus.|
|`leftRow2BuckleBelted`|True|References signal "VedsRw2lBckl_D_Ltchd". See VehicleDataEventStatus.|
|`passengerChildDetected`|True|References signal "VedsRw1PasChld_D_Ltchd". See VehicleDataEventStatus.|
|`rightRow2BuckleBelted`|True|References signal "VedsRw2rBckl_D_Ltchd". See VehicleDataEventStatus.|
|`middleRow2BuckleBelted`|True|References signal "VedsRw2mBckl_D_Ltchd". See VehicleDataEventStatus.|
|`middleRow3BuckleBelted`|True|References signal "VedsRw3mBckl_D_Ltchd". See VehicleDataEventStatus.|
|`leftRow3BuckleBelted`|True|References signal "VedsRw3lBckl_D_Ltchd". See VehicleDataEventStatus.|
|`rightRow3BuckleBelted`|True|References signal "VedsRw3rBckl_D_Ltchd". See VehicleDataEventStatus.|
|`leftRearInflatableBelted`|True|References signal "VedsRw2lRib_D_Ltchd". See VehicleDataEventStatus.|
|`rightRearInflatableBelted`|True|References signal "VedsRw2rRib_D_Ltchd". See VehicleDataEventStatus.|
|`middleRow1BeltDeployed`|True|References signal "VedsRw1mBelt_D_Ltchd". See VehicleDataEventStatus.|
|`middleRow1BuckleBelted`|True|References signal "VedsRw1mBckl_D_Ltchd". See VehicleDataEventStatus.|


### BodyInformation
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`parkBrakeActive`|True|References signal "PrkBrkActv_B_Actl".|
|`ignitionStableStatus`|True|References signal "Ignition_Switch_Stable". See IgnitionStableStatus.|
|`ignitionStatus`|True|References signal "Ignition_status". See IgnitionStatus.|
|`driverDoorAjar`|False|References signal "DrStatDrv_B_Actl".|
|`passengerDoorAjar`|False|References signal "DrStatPsngr_B_Actl".|
|`rearLeftDoorAjar`|False|References signal "DrStatRl_B_Actl".|
|`rearRightDoorAjar`|False|References signal "DrStatRr_B_Actl".|


### DeviceStatus
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`voiceRecOn`|True|References signal "CPM_VoiceRec_STAT".|
|`btIconOn`|True|References signal "BT_ICON".|
|`callActive`|True|References signal "CPM_Call_Active_STAT".|
|`phoneRoaming`|True|References signal "CPM_Phone_Roaming_STAT".|
|`textMsgAvailable`|True|References signal "CPM_TextMsg_AVAL".|
|`battLevelStatus`|True|Device battery level status.  References signal "CPM_Batt_Level_STAT". See DeviceLevelStatus.|
|`stereoAudioOutputMuted`|True|References signal "CPM_Stereo_Audio_Output".|
|`monoAudioOutputMuted`|True|References signal "CPM_Mono_Audio_Output".|
|`signalLevelStatus`|True|Device signal level status.  References signal "CPM_Signal_Strength_STAT". See DeviceLevelStatus.|
|`primaryAudioSource`|True|References signal "CPM_Stereo_PAS_Source". See PrimaryAudioSource.|
|`eCallEventActive`|True|References signal "eCall_Event".|


### HeadLampStatus
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`lowBeamsOn`|True|Status of the low beam lamps.  References signal "HeadLampLoActv_B_Stat".|
|`highBeamsOn`|True|Status of the high beam lamps.  References signal "HeadLghtHiOn_B_Stat".|
|`ambientLightSensorStatus`|False|Status of the ambient light sensor.|


### AppInfo
Contains detailed information about the registered application.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`appDisplayName`|True|The name displayed for the mobile application on the mobile device (can differ from the app name set in the initial RAI request).|
|`appBundleID`|True|The AppBundleID of an iOS application or package name of the Android application. This supports App Launch strategies for each platform.|
|`appVersion`|True|Represents the build version number of this particular mobile app.|
|`appIcon`|False|A file reference to the icon utilized by this app (simplifies the process of setting an app icon during app registration).|


### ECallInfo
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`eCallNotificationStatus`|True|References signal "eCallNotification_4A". See VehicleDataNotificationStatus.|
|`auxECallNotificationStatus`|True|References signal "eCallNotification". See VehicleDataNotificationStatus.|
|`eCallConfirmationStatus`|True|References signal "eCallConfirmation". See ECallConfirmationStatus.|


### AirbagStatus
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`driverAirbagDeployed`|True|References signal "VedsDrvBag_D_Ltchd". See VehicleDataEventStatus.|
|`driverSideAirbagDeployed`|True|References signal "VedsDrvSideBag_D_Ltchd". See VehicleDataEventStatus.|
|`driverCurtainAirbagDeployed`|True|References signal "VedsDrvCrtnBag_D_Ltchd". See VehicleDataEventStatus.|
|`passengerAirbagDeployed`|True|References signal "VedsPasBag_D_Ltchd". See VehicleDataEventStatus.|
|`passengerCurtainAirbagDeployed`|True|References signal "VedsPasCrtnBag_D_Ltchd". See VehicleDataEventStatus.|
|`driverKneeAirbagDeployed`|True|References signal "VedsKneeDrvBag_D_Ltchd". See VehicleDataEventStatus.|
|`passengerSideAirbagDeployed`|True|References signal "VedsPasSideBag_D_Ltchd". See VehicleDataEventStatus.|
|`passengerKneeAirbagDeployed`|True|References signal "VedsKneePasBag_D_Ltchd". See VehicleDataEventStatus.|


### EmergencyEvent
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`emergencyEventType`|True|References signal "VedsEvntType_D_Ltchd". See EmergencyEventType.|
|`fuelCutoffStatus`|True|References signal "RCM_FuelCutoff". See FuelCutoffStatus.|
|`rolloverEvent`|True|References signal "VedsEvntRoll_D_Ltchd". See VehicleDataEventStatus.|
|`maximumChangeVelocity`|True|References signal "VedsMaxDeltaV_D_Ltchd". Change in velocity in KPH.  Additional reserved values:                0x00 No event                0xFE Not supported                0xFF Fault            |
|`multipleEvents`|True|References signal "VedsMultiEvnt_D_Ltchd". See VehicleDataEventStatus.|


### ClusterModeStatus
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`powerModeActive`|True|References signal "PowerMode_UB".|
|`powerModeQualificationStatus`|True|References signal "PowerModeQF". See PowerModeQualificationStatus.|
|`carModeStatus`|True|References signal "CarMode". See CarMode.|
|`powerModeStatus`|True|References signal "PowerMode". See PowerMode.|


### MyKey
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`e911Override`|True|Indicates whether e911 override is on.  References signal "MyKey_e911Override_St". See VehicleDataStatus.|


### TireStatus
The status and pressure of the tires.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`pressureTelltale`|True|Status of the Tire Pressure Telltale. See WarningLightStatus.|
|`leftFront`|True|The status of the left front tire.|
|`rightFront`|True|The status of the right front tire.|
|`leftRear`|True|The status of the left rear tire.|
|`rightRear`|True|The status of the right rear tire.|
|`innerLeftRear`|True|The status of the inner left rear.|
|`innerRightRear`|True|The status of the inner right rear.|


### GPSData
Struct with the GPS data.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`longitudeDegrees`|True||
|`latitudeDegrees`|True||
|`utcYear`|True|The current UTC year.|
|`utcMonth`|True|The current UTC month.|
|`utcDay`|True|The current UTC day.|
|`utcHours`|True|The current UTC hour.|
|`utcMinutes`|True|The current UTC minute.|
|`utcSeconds`|True|The current UTC second.|
|`compassDirection`|True|See CompassDirection.|
|`pdop`|True|PDOP.  If undefined or unavailable, then value shall be set to 0.|
|`hdop`|True|HDOP.  If value is unknown, value shall be set to 0.|
|`vdop`|True|VDOP.  If value is unknown, value shall be set to 0.|
|`actual`|True|True, if actual.                False, if infered.            |
|`satellites`|True|Number of satellites in view|
|`dimension`|True|See Dimension|
|`altitude`|True|Altitude in meters|
|`heading`|True|The heading. North is 0. Resolution is 0.01|
|`speed`|True|The speed in KPH|


### VehicleDataResult
Individual published data request result

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`dataType`|True|Defined published data element type.|
|`resultCode`|True|Published data result code.|


### DIDResult
Individual requested DID result and data

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`resultCode`|True|Individual DID result code.|
|`didLocation`|True|Location of raw data from vehicle data DID|
|`data`|False|Raw DID-based data returned for requested element.|


### StartTime
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`hours`|True|The hour of the media clock.                Some radios only support a max of 19 hours. If out of range, it will be rejected.            |
|`minutes`|True||
|`seconds`|True||


### TextField
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`name`|True|The name that identifies the field. See TextFieldName.|
|`characterSet`|True|The character set that is supported in this field. See CharacterSet.|
|`width`|True|The number of characters in one row of this field.|
|`rows`|True|The number of rows of this field.|


### ImageResolution
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`resolutionWidth`|True|The image resolution width.|
|`resolutionHeight`|True|The image resolution height.|


### ImageField
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`name`|True|The name that identifies the field. See ImageFieldName.|
|`imageTypeSupported`|True|The image types that are supported in this field. See FileType.|
|`imageResolution`|False|The image resolution of this field.|


### TouchCoord
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`x`|True|The x coordinate of the touch.|
|`y`|True|The y coordinate of the touch.|


### TouchEvent
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`id`|True|A touch's unique identifier.  The application can track the current touch events by id.                If a touch event has type begin, the id should be added to the set of touches.                If a touch event has type end, the id should be removed from the set of touches.            |
|`ts`|True|The time that the touch was recorded.  This number can the time since the beginning of the session or something else as long as the units are in milliseconds.                The timestamp is used to determined the rate of change of position of a touch.                The application also uses the time to verify whether two touches, with different ids, are part of a single action by the user.                If there is only a single timestamp in this array, it is the same for every coordinate in the coordinates array.            |
|`c`|True||


### TouchEventCapabilities
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`pressAvailable`|True||
|`multiTouchAvailable`|True||
|`doublePressAvailable`|True||


### ScreenParams
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`resolution`|True|The resolution of the prescribed screen area.|
|`touchEventAvailable`|False|Types of screen touch events available in screen area.|


### HMIPermissions
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`allowed`|True|A set of all HMI levels that are permitted for this given RPC.|
|`userDisallowed`|True|A set of all HMI levels that are prohibited for this given RPC.|


### ParameterPermissions
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`allowed`|True|A set of all parameters that are permitted for this given RPC.|
|`userDisallowed`|True|A set of all parameters that are prohibited for this given RPC.|


### PermissionItem
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`rpcName`|True|Name of the individual RPC in the policy table.|
|`hmiPermissions`|True||
|`parameterPermissions`|True||


### DisplayCapabilities
Contains information about the display capabilities.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`displayType`|True|The type of the display. See DisplayType|
|`textFields`|True|A set of all fields that support text data. See TextField|
|`imageFields`|False|A set of all fields that support images. See ImageField|
|`mediaClockFormats`|True|A set of all supported formats of the media clock. See MediaClockFormat|
|`graphicSupported`|True|The display's persistent screen supports referencing a static or dynamic image.|
|`templatesAvailable`|False|A set of all predefined persistent display templates available on headunit.  To be referenced in SetDisplayLayout.|
|`screenParams`|False|A set of all parameters related to a prescribed screen area (e.g. for video / touch input).|
|`numCustomPresetsAvailable`|False|The number of on-screen custom presets available (if any); otherwise omitted.|


### ButtonCapabilities
Contains information about a button's capabilities.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`name`|True|The name of the button. See ButtonName.|
|`shortPressAvailable`|True|The button supports a short press.         Whenever the button is pressed short, onButtonPressed( SHORT) will be invoked.         |
|`longPressAvailable`|True|The button supports a LONG press.         Whenever the button is pressed long, onButtonPressed( LONG) will be invoked.         |
|`upDownAvailable`|True|The button supports "button down" and "button up".         Whenever the button is pressed, onButtonEvent( DOWN) will be invoked.         Whenever the button is released, onButtonEvent( UP) will be invoked.         |


### SoftButtonCapabilities
Contains information about a SoftButton's capabilities.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`shortPressAvailable`|True|The button supports a short press.         Whenever the button is pressed short, onButtonPressed( SHORT) will be invoked.         |
|`longPressAvailable`|True|The button supports a LONG press.         Whenever the button is pressed long, onButtonPressed( LONG) will be invoked.         |
|`upDownAvailable`|True|The button supports "button down" and "button up".         Whenever the button is pressed, onButtonEvent( DOWN) will be invoked.         Whenever the button is released, onButtonEvent( UP) will be invoked.         |
|`imageSupported`|True|The button supports referencing a static or dynamic image.|


### PresetBankCapabilities
Contains information about on-screen preset capabilities.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`onScreenPresetsAvailable`|True|Onscreen custom presets are available.|


### HMICapabilities
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`navigation`|False|Availability of build in Nav. True: Available, False: Not Available|
|`phoneCall`|False|Availability of build in phone. True: Available, False: Not Available |
|`videoStreaming`|False|Availability of video streaming. |


### MenuParams
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`parentID`|False|unique ID of the sub menu, the command will be added to.         If not provided, it will be provided to the top level of the in application menu.         |
|`position`|False|Position within the items that are are at top level of the in application menu.         0 will insert at the front.         1 will insert at the second position.         if position is greater or equal than the number of items on top level, the sub menu will be appended to the end.         If this param was omitted the entry will be added at the end.         |
|`menuName`|True|Text to show in the menu for this sub menu.|


### TTSChunk
A TTS chunk, that consists of the text/phonemes to speak and the type (like text or SAPI)

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`text`|True|The text or phonemes to speak.         May not be empty.         |
|`type`|True|Describes, whether it is text or a specific phoneme set. See SpeechCapabilities|


### Turn
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`navigationText`|False|Individual turn text.  Must provide at least text or icon for a given turn.|
|`turnIcon`|False|Individual turn icon.  Must provide at least text or icon for a given turn.|


### VehicleType
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`make`|False|Make of the vehicle, e.g. Ford|
|`model`|False|Model of the vehicle, e.g. Fiesta|
|`modelYear`|False|Model Year of the vehicle, e.g. 2013|
|`trim`|False|Trim of the vehicle, e.g. SE|


### KeyboardProperties
Configuration of on-screen keyboard (if available).

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`language`|False|The keyboard language.|
|`keyboardLayout`|False|Desired keyboard layout.|
|`keypressMode`|False|Desired keypress mode.         If omitted, this value will be set to RESEND_CURRENT_ENTRY.         |
|`limitedCharacterList`|False|Array of keyboard characters to enable.|
|`autoCompleteText`|False|Allows an app to prepopulate the text field with a suggested or completed entry as the user types|


### DeviceInfo
Various information abount connecting device.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`hardware`|False|Device model|
|`firmwareRev`|False|Device firmware revision|
|`os`|False|Device OS|
|`osVersion`|False|Device OS version|
|`carrier`|False|Device mobile carrier (if applicable)|
|`maxNumberRFCOMMPorts`|False|Omitted if connected not via BT.|


### DateTime
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`millisecond`|False|Milliseconds |
|`second`|False|Seconds part of time|
|`minute`|False|Minutes part of time|
|`hour`|False|Hours part of time. Note that this structure accepts time only in 24 Hr format|
|`day`|False|Day of the month|
|`month`|False|Month of the year|
|`year`|False|The year in YYYY format|
|`tz_hour`|False|Time zone offset in Hours wrt UTC.|
|`tz_minute`|False|Time zone offset in Min wrt UTC.|


### Coordinate
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`latitudeDegrees`|True|Latitude of the location.|
|`longitudeDegrees`|True|Longitude of the location.|


### OASISAddress
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`countryName`|False|Name of the country (localized)|
|`countryCode`|False|Name of country (ISO 3166-2)|
|`postalCode`|False|(PLZ, ZIP, PIN, CAP etc.)|
|`administrativeArea`|False|Portion of country (e.g. state)|
|`subAdministrativeArea`|False|Portion of e.g. state (e.g. county)|
|`locality`|False|Hypernym for e.g. city/village|
|`subLocality`|False|Hypernym for e.g. district|
|`thoroughfare`|False|Hypernym for street, road etc.|
|`subThoroughfare`|False|Portion of thoroughfare e.g. house number|


### LocationDetails
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`coordinate`|False|Latitude/Longitude of the location.|
|`locationName`|False|Name of location.|
|`addressLines`|False|Location address for display purposes only|
|`locationDescription`|False|Description intended location / establishment (if applicable)|
|`phoneNumber`|False|Phone number of location / establishment.|
|`locationImage`|False|Image / icon of intended location.|
|`searchAddress`|False|Address to be used by navigation engines for search|


### NavigationCapability
Extended capabilities for an onboard navigation system

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`sendLocationEnabled`|False|If the module has the ability to add locations to the onboard nav|
|`getWayPointsEnabled`|False|If the module has the ability to return way points from onboard nav|


### PhoneCapability
Extended capabilities of the module's phone feature

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`dialNumberEnabled`|False|If the module has the abiulity to perform dial number|


### VideoStreamingCapability
Contains information about this system's video streaming capabilities.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`preferredResolution`|False|The preferred resolution of a video stream for decoding and rendering on HMI.|
|`maxBitrate`|False|The maximum bitrate of video stream that is supported, in kbps.|
|`supportedFormats`|False|Detailed information on each format supported by this system, in its preferred order (i.e. the first element in the array is most preferable to the system). Each object will contain a VideoStreamingFormat that describes what can be expected.|
|`hapticSpatialDataSupported`|False|True if the system can utilize the haptic spatial data from the source being streamed. If not included, it can be assumed the module doesn't support haptic spatial data'. |


### VideoStreamingFormat
Video streaming formats and their specifications.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`protocol`|True|Protocol type, see VideoStreamingProtocol|
|`codec`|True|Codec type, see VideoStreamingCodec|


### Temperature
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`unit`|Temperature Unit|
|`value`|Temperature Value in TemperatureUnit specified unit. Range depends on OEM and is not checked by SDL.|


### RdsData
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`PS`|False|Program Service Name|
|`RT`|False|Radio Text|
|`CT`|False|The clock text in UTC format as YYYY-MM-DDThh:mm:ss.sTZD|
|`PI`|False|Program Identification - the call sign for the radio station|
|`PTY`|False|The program type - The region should be used to differentiate between EU and North America program types|
|`TP`|False|Traffic Program Identification - Identifies a station that offers traffic|
|`TA`|False|Traffic Announcement Identification - Indicates an ongoing traffic announcement|
|`REG`|False|Region|


### RadioControlData
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`frequencyInteger`|False|The integer part of the frequency ie for 101.7 this value should be 101|
|`frequencyFraction`|False|The fractional part of the frequency for 101.7 is 7|
|`band`|False||
|`rdsData`|False||
|`availableHDs`|False|number of HD sub-channels if available|
|`hdChannel`|False|Current HD sub-channel if available|
|`signalStrength`|False||
|`signalChangeThreshold`|False|If the signal strength falls below the set value for this parameter, the radio will tune to an alternative frequency|
|`radioEnable`|False|True if the radio is on, false is the radio is off|
|`state`|False||


### ClimateControlData
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`fanSpeed`|False||
|`currentTemperature`|False||
|`desiredTemperature`|False||
|`acEnable`|False||
|`circulateAirEnable`|False||
|`autoModeEnable`|False||
|`defrostZone`|False||
|`dualModeEnable`|False||
|`acMaxEnable`|False||
|`ventilationMode`|False||


### ModuleData
The moduleType indicates which type of data should be changed and identifies which data object exists in this struct. For example, if the moduleType is CLIMATE then a "climateControlData" should exist

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`moduleType`||
|`radioControlData`|False||
|`climateControlData`|False||


### RemoteControlCapabilities
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`climateControlCapabilities`|False|If included, the platform supports RC climate controls. For this baseline version, maxsize=1. i.e. only one climate control module is supported.|
|`radioControlCapabilities`|False|If included, the platform supports RC radio controls.For this baseline version, maxsize=1. i.e. only one radio control module is supported.|
|`buttonCapabilities`|False|If included, the platform supports RC button controls with the included button names.|


### RadioControlCapabilities
Contains information about a radio control module's capabilities.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`moduleName`|The short friendly name of the climate control module.            It should not be used to identify a module by mobile application.        |
|`radioEnableAvailable`|False|Availability of the control of enable/disable radio.        True: Available, False: Not Available, Not present: Not Available.    |
|`radioBandAvailable`|False|Availability of the control of radio band.        True: Available, False: Not Available, Not present: Not Available.    |
|`radioFrequencyAvailable`|False|Availability of the control of radio frequency.        True: Available, False: Not Available, Not present: Not Available.    |
|`hdChannelAvailable`|False|Availability of the control of HD radio channel.        True: Available, False: Not Available, Not present: Not Available.    |
|`rdsDataAvailable`|False|Availability of the getting Radio Data System (RDS) data.        True: Available, False: Not Available, Not present: Not Available.    |
|`availableHDsAvailable`|False|Availability of the getting the number of available HD channels.        True: Available, False: Not Available, Not present: Not Available.    |
|`stateAvailable`|False|Availability of the getting the Radio state.        True: Available, False: Not Available, Not present: Not Available.    |
|`signalStrengthAvailable`|False|Availability of the getting the signal strength.        True: Available, False: Not Available, Not present: Not Available.    |
|`signalChangeThresholdAvailable`|False|Availability of the getting the signal Change Threshold.        True: Available, False: Not Available, Not present: Not Available.    |


### ClimateControlCapabilities
Contains information about a climate control module's capabilities.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`moduleName`|The short friendly name of the climate control module.            It should not be used to identify a module by mobile application.|
|`fanSpeedAvailable`|False|Availability of the control of fan speed.        True: Available, False: Not Available, Not present: Not Available.    |
|`desiredTemperatureAvailable`|False|Availability of the control of desired temperature.        True: Available, False: Not Available, Not present: Not Available.    |
|`acEnableAvailable`|False|Availability of the control of turn on/off AC.        True: Available, False: Not Available, Not present: Not Available.    |
|`acMaxEnableAvailable`|False|Availability of the control of enable/disable air conditioning is ON on the maximum level.        True: Available, False: Not Available, Not present: Not Available.    |
|`circulateAirEnableAvailable`|False|Availability of the control of enable/disable circulate Air mode.        True: Available, False: Not Available, Not present: Not Available.    |
|`autoModeEnableAvailable`|False|Availability of the control of enable/disable auto mode.        True: Available, False: Not Available, Not present: Not Available.    |
|`dualModeEnableAvailable`|False|Availability of the control of enable/disable dual mode.        True: Available, False: Not Available, Not present: Not Available.    |
|`defrostZoneAvailable`|False|Availability of the control of defrost zones.        True: Available, False: Not Available, Not present: Not Available.    |
|`defrostZone`|False|A set of all defrost zones that are controllable.    |
|`ventilationModeAvailable`|False|Availability of the control of air ventilation mode.        True: Available, False: Not Available, Not present: Not Available.    |
|`ventilationMode`|False|A set of all ventilation modes that are controllable.    |


### SystemCapability
The systemCapabilityType indicates which type of data should be changed and identifies which data object exists in this struct. For example, if the SystemCapability Type is NAVIGATION then a "navigationCapability" should exist

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`systemCapabilityType`|True|Used as a descriptor of what data to expect in this struct. The corresponding param to this enum should be included and the only other para included.|
|`navigationCapability`|False|Describes extended capabilities for onboard navigation system |
|`phoneCapability`|False|Describes extended capabilities of the module's phone feature|
|`videoStreamingCapability`|False|Describes extended capabilities of the module's phone feature|
|`remoteControlCapability`|False|Describes extended capabilities of the module's phone feature|


### MetadataStruct
##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`mainField1`|False|The type of data contained in the "mainField1" text field.|
|`mainField2`|False|The type of data contained in the "mainField2" text field.|
|`mainField3`|False|The type of data contained in the "MainField3" text field.|
|`mainField4`|False|The type of data contained in the "mainField4" text field.|


### SpatialStruct
Defines spatial for each user control object for video streaming application

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`id`|True|A user control spatial identifier|
|`x`|True|The X-coordinate of the user control|
|`y`|True|The Y-coordinate of the user control|
|`width`|True|The width of the user control's bounding rectangle|
|`height`|True|The height of the user control's bounding rectangle|



<div style="page-break-after: always;"></div>


## Remote Procedure Calls

### RegisterAppInterface
Message Type: **request**

Establishes an interface with a mobile application.
            Before registerAppInterface no other commands will be accepted/executed.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`syncMsgVersion`|True|See SyncMsgVersion|
|`appName`|True|The mobile application name, e.g. "Ford Drive Green".                Needs to be unique over all applications.                May not be empty.                May not start with a new line character.                May not interfere with any name or synonym of previously registered applications and any predefined blacklist of words (global commands)                Needs to be unique over all applications. Applications with the same name will be rejected.                Only characters from char set [@TODO: Create char set (character/hex value) for each ACM and refer to] are supported.            |
|`ttsName`|False|TTS string for VR recognition of the mobile application name, e.g. "Ford Drive Green".                Meant to overcome any failing on speech engine in properly pronouncing / understanding app name.                Needs to be unique over all applications.                May not be empty.                May not start with a new line character.                Only characters from char set [@TODO: Create char set (character/hex value) for each ACM and refer to] are supported.            |
|`ngnMediaScreenAppName`|False|Provides an abbreviated version of the app name (if needed), that will be displayed on the NGN media screen.                If not provided, the appName is used instead (and will be truncated if too long)                Only characters from char set [@TODO: Create char set (character/hex value) for each ACM and refer to] are supported.            |
|`vrSynonyms`|False|Defines an additional voice recognition command.                May not interfere with any app name of previously registered applications and any predefined blacklist of words (global commands)                Only characters from char set [@TODO: Create char set (character/hex value) for each ACM and refer to] are supported.            |
|`isMediaApplication`|True|Indicates if the application is a media or a non-media application.                Only media applications will be able to stream audio to the module that is audible outside of the BT media source.            |
|`languageDesired`|True|See Language                Current app's expected VR+TTS language                If there is a mismatch with the module, the app will be able to change this registration with changeRegistration prior to app being brought into focus.            |
|`hmiDisplayLanguageDesired`|True|See Language                Current app's expected display language                If there is a mismatch with the module, the app will be able to change this registration with changeRegistration prior to app being brought into focus.            |
|`appHMIType`|False|See AppHMIType                List of all applicable app HMI types stating which HMI classifications to be given to the app.            |
|`hashID`|False|ID used to uniquely identify current state of all app data that can persist through connection cycles (e.g. ignition cycles).                This registered data (commands, submenus, choice sets, etc.) can be reestablished without needing to explicitly reregister each piece.                If omitted, then the previous state of an app's commands, etc. will not be restored.                When sending hashID, all RegisterAppInterface parameters should still be provided (e.g. ttsName, etc.).            |
|`deviceInfo`|False|See DeviceInfo.            |
|`appID`|True|ID used to validate app with policy table entries|
|`appInfo`|False|See AppInfo.            |


### RegisterAppInterface
Message Type: **response**

The response to registerAppInterface

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|
|`syncMsgVersion`|False|See SyncMsgVersion|
|`language`|False|The currently active VR+TTS language on the module. See "Language" for options.|
|`hmiDisplayLanguage`|False|The currently active display language on the module. See "Language" for options.|
|`displayCapabilities`|False|See DisplayCapabilities|
|`buttonCapabilities`|False|See ButtonCapabilities|
|`softButtonCapabilities`|False|If returned, the platform supports on-screen SoftButtons; see SoftButtonCapabilities.|
|`presetBankCapabilities`|False|If returned, the platform supports custom on-screen Presets; see PresetBankCapabilities.|
|`hmiZoneCapabilities`|False|See HmiZoneCapabilities|
|`speechCapabilities`|False|See SpeechCapabilities|
|`prerecordedSpeech`|False|See PrerecordedSpeech|
|`vrCapabilities`|False|See VrCapabilities|
|`audioPassThruCapabilities`|False|See AudioPassThruCapability|
|`pcmStreamCapabilities`|False|See AudioPassThruCapability|
|`vehicleType`|False|Specifies the vehicle's type. See VehicleType.|
|`supportedDiagModes`|False|Specifies the white-list of supported diagnostic modes (0x00-0xFF) capable for DiagnosticMessage requests.                If a mode outside this list is requested, it will be rejected.            |
|`hmiCapabilities`|False|Specifies the HMIÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s capabilities. See HMICapabilities.|
|`sdlVersion`|False|The SmartDeviceLink version.|
|`systemSoftwareVersion`|False|The software version of the system that implements the SmartDeviceLink core.|


### UnregisterAppInterface
Message Type: **request**

Closes an interface from a mobile application.
            After unregisterAppInterface, no commands other than registerAppInterface will be accepted/executed.
            Will fail, if no registerAppInterface was completed successfully before.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|


### UnregisterAppInterface
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### SetGlobalProperties
Message Type: **request**

Allows setting global properties.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`helpPrompt`|False|The help prompt.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`timeoutPrompt`|False|Help text for a wait timeout.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`vrHelpTitle`|False|VR Help Title text.                If omitted on supported displays, the default module help title shall be used.                If omitted and one or more vrHelp items are provided, the request will be rejected.            |
|`vrHelp`|False|VR Help Items.                If omitted on supported displays, the default AppLink VR help / What Can I Say? screen shall be used.                If the list of VR Help Items contains nonsequential positions (e.g. [1,2,4]), the RPC shall be rejected.                If omitted and a vrHelpTitle is provided, the request will be rejected.            |
|`menuTitle`|False|Optional text to label an app menu button (for certain touchscreen platforms).|
|`menuIcon`|False|>Optional icon to draw on an app menu button (for certain touchscreen platforms).|
|`keyboardProperties`|False|On-screen keybaord configuration (if available).|


### SetGlobalProperties
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### ResetGlobalProperties
Message Type: **request**

Allows resetting global properties.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`properties`|True|Contains the names of all global properties (like timeoutPrompt) that should be unset. Resetting means, that they have the same value as at start up (default)|


### ResetGlobalProperties
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### AddCommand
Message Type: **request**

Adds a command to the in application menu.
            Either menuParams or vrCommands must be provided.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`cmdID`|True|unique ID of the command to add.|
|`menuParams`|False|Optional sub value containing menu parameters|
|`vrCommands`|False|An array of strings to be used as VR synonyms for this command.                If this array is provided, it may not be empty.            |
|`cmdIcon`|False|Image struct determining whether static or dynamic icon.                If omitted on supported displays, no (or the default if applicable) icon shall be displayed.            |


### AddCommand
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### DeleteCommand
Message Type: **request**

Deletes all commands from the in-application menu with the specified command id.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`cmdID`|True|ID of the command(s) to delete.|


### DeleteCommand
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### AddSubMenu
Message Type: **request**

Adds a sub menu to the in-application menu.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`menuID`|True|unique ID of the sub menu to add.|
|`position`|False|Position within the items that are are at top level of the in application menu.                0 will insert at the front.                1 will insert at the second position.                If position is greater or equal than the number of items on top level, the sub menu will be appended to the end.                Position of any submenu will always be located before the return and exit options                If this param was omitted the entry will be added at the end.            |
|`menuName`|True|Text to show in the menu for this sub menu.|


### AddSubMenu
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### DeleteSubMenu
Message Type: **request**

Deletes a submenu from the in-application menu.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`menuID`|True|The "menuID" of the submenu to delete. (See addSubMenu.menuID)|


### DeleteSubMenu
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### CreateInteractionChoiceSet
Message Type: **request**

creates interaction choice set to be used later by performInteraction

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`interactionChoiceSetID`|True|Unique ID used for this interaction choice set.|
|`choiceSet`|True||


### CreateInteractionChoiceSet
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### PerformInteraction
Message Type: **request**

Triggers an interaction (e.g. "Permit GPS?" - Yes, no, Always Allow).

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`initialText`|True|Text to be displayed first.            |
|`initialPrompt`|False|This is the intial prompt spoken to the user at the start of an interaction.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`interactionMode`|True|See InteractionMode.|
|`interactionChoiceSetIDList`|True|List of interaction choice set IDs to use with an interaction.|
|`helpPrompt`|False|Help text. This is the spoken string when a user speaks "help" when the interaction is occuring.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`timeoutPrompt`|False|Timeout text. This text is spoken when a VR interaction times out.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`timeout`|False|Timeout in milliseconds.                If omitted a standard value of 10000 milliseconds is used.                Applies only to the menu portion of the interaction. The VR timeout will be handled by the platform.            |
|`vrHelp`|False|Ability to send suggested VR Help Items to display on-screen during Perform Interaction.                If omitted on supported displays, the default generated list of suggested choices shall be displayed.            |
|`interactionLayout`|False|See LayoutMode.|


### PerformInteraction
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|
|`choiceID`|False|ID of the choice that was selected in response to PerformInteraction.                Only is valid if general result is "success:true".            |
|`manualTextEntry`|False|Manually entered text selection, e.g. through keyboard                Can be returned in lieu of choiceID, depending on trigger source            |
|`triggerSource`|False|See TriggerSource                Only is valid if resultCode is SUCCESS.            |


### DeleteInteractionChoiceSet
Message Type: **request**

Deletes interaction choice set that has been created with "CreateInteractionChoiceSet".

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`interactionChoiceSetID`|True|ID of the interaction choice set to delete.|


### DeleteInteractionChoiceSet
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### Alert
Message Type: **request**

Shows an alert which typically consists of text-to-speech message and text on the display. At least either alertText1, alertText2 or TTSChunks need to be provided.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`alertText1`|False|The first line of the alert text field|
|`alertText2`|False|The second line of the alert text field|
|`alertText3`|False|The optional third line of the alert text field|
|`ttsChunks`|False|An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`duration`|False|Timeout in milliseconds.                Typical timeouts are 3-5 seconds.                If omitted, timeout is set to 5s.            |
|`playTone`|False|Defines if tone should be played. Tone is played before TTS.                If omitted, no tone is played.            |
|`progressIndicator`|False|If supported on the given platform, the alert GUI will include some sort of animation indicating that loading of a feature is progressing.  e.g. a spinning wheel or hourglass, etc.            |
|`softButtons`|False|App defined SoftButtons.                If omitted on supported displays, the displayed alert shall not have any SoftButtons.            |


### Alert
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|
|`tryAgainTime`|False|Amount of time (in seconds) that an app must wait before resending an alert.                If provided, another system event or overlay currently has a higher priority than this alert.                An app must not send an alert without waiting at least the amount of time dictated.            |


### Show
Message Type: **request**

Updates the persistent display. Supported fields depend on display capabilities.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`mainField1`|False|The text that should be displayed in a single or upper display line.                If this text is not set, the text of mainField1 stays unchanged.                If this text is empty "", the field will be cleared.            |
|`mainField2`|False|The text that should be displayed on the second display line.                If this text is not set, the text of mainField2 stays unchanged.                If this text is empty "", the field will be cleared.            |
|`mainField3`|False|The text that should be displayed on the second "page" first display line.                If this text is not set, the text of mainField3 stays unchanged.                If this text is empty "", the field will be cleared.            |
|`mainField4`|False|The text that should be displayed on the second "page" second display line.                If this text is not set, the text of mainField4 stays unchanged.                If this text is empty "", the field will be cleared.            |
|`alignment`|False|Specifies how mainField1 and mainField2 texts should be aligned on display.                If omitted, texts will be centered.            |
|`statusBar`|False|Requires investigation regarding the nav display capabilities. Potentially lower lowerStatusBar, upperStatusBar, titleBar, etc.|
|`mediaClock`|False|Text value for MediaClock field. Has to be properly formatted by Mobile App according to the module's capabilities.                If this text is set, any automatic media clock updates previously set with SetMediaClockTimer will be stopped.            |
|`mediaTrack`|False|The text that should be displayed in the track field.                If this text is not set, the text of mediaTrack stays unchanged.                If this text is empty "", the field will be cleared.            |
|`graphic`|False|Image struct determining whether static or dynamic image to display in app.                If omitted on supported displays, the displayed graphic shall not change.            |
|`secondaryGraphic`|False|Image struct determining whether static or dynamic secondary image to display in app.                If omitted on supported displays, the displayed secondary graphic shall not change.            |
|`softButtons`|False|App defined SoftButtons.                If omitted on supported displays, the currently displayed SoftButton values will not change.            |
|`customPresets`|False|App labeled on-screen presets (i.e. on-screen media presets or dynamic search suggestions).                If omitted on supported displays, the presets will be shown as not defined.            |
|`textFieldMetadata`|False|App defined metadata information. See MetadataStruct. Uses mainField1, mainField2, mainField3, mainField4.                If omitted on supported displays, the currently set metadata tags will not change.                If any text field contains no tags or the none tag, the metadata tag for that textfield should be removed.|


### Show
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### Speak
Message Type: **request**

Speaks a text.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`ttsChunks`|True|An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |


### Speak
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### SetMediaClockTimer
Message Type: **request**

Sets the initial media clock value and automatic update method.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`startTime`|False|See StartTime.                startTime must be provided for "COUNTUP" and "COUNTDOWN".                startTime will be ignored for "RESUME", and "CLEAR"                startTime can be sent for "PAUSE", in which case it will update the paused startTime            |
|`endTime`|False|See StartTime.                endTime can be provided for "COUNTUP" and "COUNTDOWN"; to be used to calculate any visual progress bar (if not provided, this feature is ignored)                If endTime is greater then startTime for COUNTDOWN or less than startTime for COUNTUP, then the request will return an INVALID_DATA.                endTime will be ignored for "RESUME", and "CLEAR"                endTime can be sent for "PAUSE", in which case it will update the paused endTime            |
|`updateMode`|True|Enumeration to control the media clock.                In case of pause, resume, or clear, the start time value is ignored and shall be left out.  For resume, the time continues with the same value as it was when paused.            |


### SetMediaClockTimer
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### PerformAudioPassThru
Message Type: **request**

Starts audio pass thru session 

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`initialPrompt`|False|The module will speak this prompt before opening the audio pass thru session.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.                If omitted, then no initial prompt is spoken.            |
|`audioPassThruDisplayText1`|False|First line of text displayed during audio capture.|
|`audioPassThruDisplayText2`|False|Second line of text displayed during audio capture.|
|`samplingRate`|True|This value shall be allowed at 8 khz or 16 or 22 or 44 khz.|
|`maxDuration`|True|The maximum duration of audio recording in milliseconds. |
|`bitsPerSample`|True|Specifies the quality the audio is recorded. Currently 8 bit or 16 bit.|
|`audioType`|True|Specifies the type of audio data being requested.|
|`muteAudio`|False|Defines if the current audio source should be muted during the APT session.  If not, the audio source will play without interruption.                If omitted, the value is set to true.            |


### PerformAudioPassThru
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### EndAudioPassThru
Message Type: **request**

When this request is invoked, the audio capture stops.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|


### EndAudioPassThru
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### SubscribeButton
Message Type: **request**

Subscribes to built-in HMI buttons.
            The application will be notified by the OnButtonEvent and OnButtonPress.
            To unsubscribe the notifications, use unsubscribeButton.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`buttonName`|True|Name of the button to subscribe.|


### SubscribeButton
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### UnsubscribeButton
Message Type: **request**

Unsubscribes from built-in HMI buttons.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`buttonName`|True|Name of the button to unsubscribe.|


### UnsubscribeButton
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### SubscribeVehicleData
Message Type: **request**

Subscribes for specific published data items.
            The data will be only sent if it has changed.
            The application will be notified by the onVehicleData notification whenever new data is available.
            To unsubscribe the notifications, use unsubscribe with the same subscriptionType.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`gps`|False|See GPSData|
|`speed`|False|The vehicle speed in kilometers per hour|
|`rpm`|False|The number of revolutions per minute of the engine|
|`fuelLevel`|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|False|The fuel level state|
|`instantFuelConsumption`|False|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|False|The external temperature in degrees celsius|
|`prndl`|False|See PRNDL|
|`tirePressure`|False|See TireStatus|
|`odometer`|False|Odometer in km|
|`beltStatus`|False|The status of the seat belts|
|`bodyInformation`|False|The body information including power modes|
|`deviceStatus`|False|The device status including signal and battery strength|
|`driverBraking`|False|The status of the brake pedal|
|`wiperStatus`|False|The status of the wipers|
|`headLampStatus`|False|Status of the head lamps|
|`engineTorque`|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|False|Current angle of the steering wheel (in deg)|
|`eCallInfo`|False|Emergency Call notification and confirmation data|
|`airbagStatus`|False|The status of the air bags|
|`emergencyEvent`|False|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|False|The status modes of the cluster|
|`myKey`|False|Information related to the MyKey feature|


### SubscribeVehicleData
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|
|`gps`|False|See GPSData|
|`speed`|False|The vehicle speed in kilometers per hour|
|`rpm`|False|The number of revolutions per minute of the engine|
|`fuelLevel`|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|False|The fuel level state|
|`instantFuelConsumption`|False|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|False|The external temperature in degrees celsius.|
|`prndl`|False|See PRNDL|
|`tirePressure`|False|See TireStatus|
|`odometer`|False|Odometer in km|
|`beltStatus`|False|The status of the seat belts|
|`bodyInformation`|False|The body information including power modes|
|`deviceStatus`|False|The device status including signal and battery strength|
|`driverBraking`|False|The status of the brake pedal|
|`wiperStatus`|False|The status of the wipers|
|`headLampStatus`|False|Status of the head lamps|
|`engineTorque`|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|False|Current angle of the steering wheel (in deg)|
|`eCallInfo`|False|Emergency Call notification and confirmation data|
|`airbagStatus`|False|The status of the air bags|
|`emergencyEvent`|False|Information related to an emergency event (and if it occurred)|
|`clusterModes`|False|The status modes of the cluster|
|`myKey`|False|Information related to the MyKey feature|


### UnsubscribeVehicleData
Message Type: **request**

This function is used to unsubscribe the notifications from the subscribeVehicleData function.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`gps`|False|See GPSData|
|`speed`|False|The vehicle speed in kilometers per hour|
|`rpm`|False|The number of revolutions per minute of the engine|
|`fuelLevel`|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|False|The fuel level state|
|`instantFuelConsumption`|False|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|False|The external temperature in degrees celsius.|
|`prndl`|False|See PRNDL|
|`tirePressure`|False|See TireStatus|
|`odometer`|False|Odometer in km|
|`beltStatus`|False|The status of the seat belts|
|`bodyInformation`|False|The body information including power modes|
|`deviceStatus`|False|The device status including signal and battery strength|
|`driverBraking`|False|The status of the brake pedal|
|`wiperStatus`|False|The status of the wipers|
|`headLampStatus`|False|Status of the head lamps|
|`engineTorque`|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|False|Current angle of the steering wheel (in deg)|
|`eCallInfo`|False|Emergency Call notification and confirmation data|
|`airbagStatus`|False|The status of the air bags|
|`emergencyEvent`|False|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|False|The status modes of the cluster|
|`myKey`|False|Information related to the MyKey feature|


### UnsubscribeVehicleData
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|
|`gps`|False|See GPSData|
|`speed`|False|The vehicle speed in kilometers per hour|
|`rpm`|False|The number of revolutions per minute of the engine|
|`fuelLevel`|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|False|The fuel level state|
|`instantFuelConsumption`|False|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|False|The external temperature in degrees celsius|
|`prndl`|False|See PRNDL|
|`tirePressure`|False|See TireStatus|
|`odometer`|False|Odometer in km|
|`beltStatus`|False|The status of the seat belts|
|`bodyInformation`|False|The body information including power modes|
|`deviceStatus`|False|The device status including signal and battery strength|
|`driverBraking`|False|The status of the brake pedal|
|`wiperStatus`|False|The status of the wipers|
|`headLampStatus`|False|Status of the head lamps|
|`engineTorque`|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|False|Current angle of the steering wheel (in deg)|
|`eCallInfo`|False|Emergency Call notification and confirmation data|
|`airbagStatus`|False|The status of the air bags|
|`emergencyEvent`|False|Information related to an emergency event (and if it occurred)|
|`clusterModes`|False|The status modes of the cluster|
|`myKey`|False|Information related to the MyKey feature|


### GetVehicleData
Message Type: **request**

Non periodic vehicle data read request.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`gps`|False|See GPSData|
|`speed`|False|The vehicle speed in kilometers per hour|
|`rpm`|False|The number of revolutions per minute of the engine|
|`fuelLevel`|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|False|The fuel level state|
|`instantFuelConsumption`|False|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|False|The external temperature in degrees celsius|
|`vin`|False|Vehicle identification number|
|`prndl`|False|See PRNDL|
|`tirePressure`|False|See TireStatus|
|`odometer`|False|Odometer in km|
|`beltStatus`|False|The status of the seat belts|
|`bodyInformation`|False|The body information including ignition status and internal temp|
|`deviceStatus`|False|The device status including signal and battery strength|
|`driverBraking`|False|The status of the brake pedal|
|`wiperStatus`|False|The status of the wipers|
|`headLampStatus`|False|Status of the head lamps|
|`engineTorque`|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|False|Current angle of the steering wheel (in deg)|
|`eCallInfo`|False|Emergency Call notification and confirmation data|
|`airbagStatus`|False|The status of the air bags|
|`emergencyEvent`|False|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|False|The status modes of the cluster|
|`myKey`|False|Information related to the MyKey feature|


### GetVehicleData
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|
|`gps`|False|See GPSData|
|`speed`|False|The vehicle speed in kilometers per hour|
|`rpm`|False|The number of revolutions per minute of the engine|
|`fuelLevel`|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|False|The fuel level state|
|`instantFuelConsumption`|False|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|False|The external temperature in degrees celsius|
|`vin`|False|Vehicle identification number|
|`prndl`|False|See PRNDL|
|`tirePressure`|False|See TireStatus|
|`odometer`|False|Odometer in km|
|`beltStatus`|False|The status of the seat belts|
|`bodyInformation`|False|The body information including power modes|
|`deviceStatus`|False|The device status including signal and battery strength|
|`driverBraking`|False|The status of the brake pedal|
|`wiperStatus`|False|The status of the wipers|
|`headLampStatus`|False|Status of the head lamps|
|`engineTorque`|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|False|Current angle of the steering wheel (in deg)|
|`eCallInfo`|False|Emergency Call notification and confirmation data|
|`airbagStatus`|False|The status of the air bags|
|`emergencyEvent`|False|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|False|The status modes of the cluster|
|`myKey`|False|Information related to the MyKey feature|


### ReadDID
Message Type: **request**

Non periodic vehicle data read request

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`ecuName`|True|Name of ECU.|
|`didLocation`|True|Get raw data from vehicle data DID location(s)|


### ReadDID
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|
|`didResult`|False|Array of requested DID results (with data if available).|


### GetDTCs
Message Type: **request**

Vehicle module diagnostic trouble code request.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`ecuName`|True|Name of ECU.|
|`dtcMask`|False|DTC Mask Byte to be sent in diagnostic request to module .|


### GetDTCs
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|
|`ecuHeader`|True|2 byte ECU Header for DTC response (as defined in VHR_Layout_Specification_DTCs.pdf)|
|`dtc`|False|Array of all reported DTCs on module (ecuHeader contains information if list is truncated).                Each DTC is represented by 4 bytes (3 bytes of data and 1 byte status as defined in VHR_Layout_Specification_DTCs.pdf).            |


### DiagnosticMessage
Message Type: **request**

Non periodic vehicle diagnostic request

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`targetID`|True|Name of target ECU.|
|`messageLength`|True|Length of message (in bytes).|
|`messageData`|True|Array of bytes comprising CAN message.            |


### DiagnosticMessage
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|
|`messageDataResult`|True|Array of bytes comprising CAN message result.            |


### ScrollableMessage
Message Type: **request**

Creates a full screen overlay containing a large block of formatted text that can be scrolled with up to 8 SoftButtons defined

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`scrollableMessageBody`|True|Body of text that can include newlines and tabs.|
|`timeout`|False|App defined timeout.  Indicates how long of a timeout from the last action (i.e. scrolling message resets timeout).|
|`softButtons`|False|App defined SoftButtons.                If omitted on supported displays, only the system defined "Close" SoftButton will be displayed.            |


### ScrollableMessage
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### Slider
Message Type: **request**

Creates a full screen or pop-up overlay (depending on platform) with a single user controlled slider.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`numTicks`|True|Number of selectable items on a horizontal axis|
|`position`|True|Initial position of slider control (cannot exceed numTicks)|
|`sliderHeader`|True|Text header to display|
|`sliderFooter`|False|Text footer to display (meant to display min/max threshold descriptors).                For a static text footer, only one footer string shall be provided in the array.                For a dynamic text footer, the number of footer text string in the array must match the numTicks value.                For a dynamic text footer, text array string should correlate with potential slider position index.                If omitted on supported displays, no footer text shall be displayed.            |
|`timeout`|False|App defined timeout.  Indicates how long of a timeout from the last action (i.e. sliding control resets timeout).                If omitted, the value is set to 10000.            |


### Slider
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|
|`sliderPosition`|False|Current slider value returned when saved or canceled (aborted)                This value is only returned for resultCodes "SAVED" or "ABORTED"            |


### ShowConstantTBT
Message Type: **request**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`navigationText1`|False||
|`navigationText2`|False||
|`eta`|False||
|`timeToDestination`|False||
|`totalDistance`|False||
|`turnIcon`|False||
|`nextTurnIcon`|False||
|`distanceToManeuver`|False|Fraction of distance till next maneuver (starting from when AlertManeuver is triggered).                Used to calculate progress bar.            |
|`distanceToManeuverScale`|False|Distance till next maneuver (starting from) from previous maneuver.                Used to calculate progress bar.            |
|`maneuverComplete`|False|If and when a maneuver has completed while an AlertManeuver is active, the app must send this value set to TRUE in order to clear the AlertManeuver overlay.                If omitted the value will be assumed as FALSE.            |
|`softButtons`|False|Three dynamic SoftButtons available (first SoftButton is fixed to "Turns").                If omitted on supported displays, the currently displayed SoftButton values will not change.            |


### ShowConstantTBT
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### AlertManeuver
Message Type: **request**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`ttsChunks`|False|An array of text chunks of type TTSChunk. See TTSChunk|
|`softButtons`|False|If omitted on supported displays, only the system defined "Close" SoftButton shall be displayed.|


### AlertManeuver
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### UpdateTurnList
Message Type: **request**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`turnList`|False||
|`softButtons`|False|If omitted on supported displays, app-defined SoftButton will be left blank.|


### UpdateTurnList
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### ChangeRegistration
Message Type: **request**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`language`|True|Requested voice engine (VR+TTS) language registration|
|`hmiDisplayLanguage`|True|Request display language registration|
|`appName`|False|Request new app name registration|
|`ttsName`|False|Request new ttsName registration|
|`ngnMediaScreenAppName`|False|Request new app short name registration|
|`vrSynonyms`|False|Request new VR synonyms registration|


### ChangeRegistration
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful                false, if failed            |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### GenericResponse
Message Type: **response**

Generic Response is sent, when the name of a received msg cannot be retrieved. Only used in case of an error.
            Currently, only resultCode INVALID_DATA is used.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### PutFile
Message Type: **request**

Used to push a binary data onto the module from a mobile device, such as icons and album art
            Not supported on first generation of SDL enabled modules.
            Binary data is in binary part of hybrid msg.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`syncFileName`|True|File reference name.|
|`fileType`|True|Selected file type.|
|`persistentFile`|False|Indicates if the file is meant to persist between sessions / ignition cycles.                If set to TRUE, then the system will aim to persist this file through session / cycles.                While files with this designation will have priority over others, they are subject to deletion by the system at any time.                In the event of automatic deletion by the system, the app will receive a rejection and have to resend the file.                If omitted, the value will be set to false.            |
|`systemFile`|False|Indicates if the file is meant to be passed thru core to elsewhere on the system.                If set to TRUE, then the system will instead pass the data thru as it arrives to a predetermined area outside of core.                If omitted, the value will be set to false.            |
|`offset`|False|Optional offset in bytes for resuming partial data chunks|
|`length`|False|Optional length in bytes for resuming partial data chunks                If offset is set to 0, then length is the total length of the file to be downloaded            |


### PutFile
Message Type: **response**

Response is sent, when the file data was copied (success case). Or when an error occured.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`spaceAvailable`|True|Provides the total local space available in SDL Core for the registered app.                If the transfer has systemFile enabled, then the value will be set to 0 automatically.            |
|`info`|False|Provides additional human readable info regarding the result.|


### DeleteFile
Message Type: **request**

Used to delete a file resident on the module in the app's local cache.
            Not supported on first generation SDL enabled vehicles.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`syncFileName`|True|File reference name.|


### DeleteFile
Message Type: **response**

Response is sent, when the file data was deleted (success case). Or when an error occured.
            Not supported on First generation SDL enabled vehicles.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true if successful; false, if failed |
|`resultCode`|True|See Result|
|`spaceAvailable`|True|Provides the total local space available on the module for the registered app.|
|`info`|False|Provides additional human readable info regarding the result.|


### ListFiles
Message Type: **request**

Requests the current list of resident filenames for the registered app.
            Not supported on first generation SDL enabled vehicles.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|


### ListFiles
Message Type: **response**

Returns the current list of resident filenames for the registered app along with the current space available
            Not supported on First generation SDL enabled vehicles.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`filenames`|False|An array of all filenames resident on the module for the given registered app.                If omitted, then no files currently reside on the system.            |
|`spaceAvailable`|True|Provides the total local space available on the module for the registered app.|
|`info`|False|Provides additional human readable info regarding the result.|


### SetAppIcon
Message Type: **request**

Used to set existing local file on the module as the app's icon
            Not supported on first generation SDL enabled vehicles.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`syncFileName`|True|File reference name.|


### SetAppIcon
Message Type: **response**

Response is sent, when the file data was copied (success case). Or when an error occured.
            Not supported on First generation SDL enabled vehicles.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### SetDisplayLayout
Message Type: **request**

Used to set an alternate display layout.
            If not sent, default screen for given platform will be shown
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`displayLayout`|True|Predefined or dynamically created screen layout.                Currently only predefined screen layouts are defined.            |


### SetDisplayLayout
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`displayCapabilities`|False|See DisplayCapabilities|
|`buttonCapabilities`|False|See ButtonCapabilities|
|`softButtonCapabilities`|False|If returned, the platform supports on-screen SoftButtons; see SoftButtonCapabilities.|
|`presetBankCapabilities`|False|If returned, the platform supports custom on-screen Presets; see PresetBankCapabilities.|
|`info`|False|Provides additional human readable info regarding the result.|


### SystemRequest
Message Type: **request**

An asynchronous request from the device; binary data can be included in hybrid part of message for some requests (such as HTTP, Proprietary, or Authentication requests)

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`requestType`|True|The type of system request.                Note that Proprietary requests should forward the binary data to the known proprietary module on the system.            |
|`fileName`|False|Filename of HTTP data to store in predefined system staging area.                Mandatory if requestType is HTTP.                PROPRIETARY requestType should ignore this parameter.            |


### SystemRequest
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|


### SendLocation
Message Type: **request**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`longitudeDegrees`|False||
|`latitudeDegrees`|False||
|`locationName`|False|Name / title of intended location            |
|`locationDescription`|False|Description intended location / establishment (if applicable)            |
|`addressLines`|False|Location address (if applicable)            |
|`phoneNumber`|False|Phone number of intended location / establishment (if applicable)            |
|`locationImage`|False|Image / icon of intended location (if applicable and supported)            |
|`timeStamp`|False|timestamp in ISO 8601 format            |
|`address`|False|Address to be used for setting destination|
|`deliveryMode`|False|Defines the mode of prompt for user|


### SendLocation
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### DialNumber
Message Type: **request**

Dials a phone number and switches to phone application.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`number`|True|Phone number is a string, which can be up to 40 chars.                All characters shall be stripped from string except digits 0-9 and * # , ; +            |


### DialNumber
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful|
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### SubscribeWayPoints
Message Type: **request**

To subscribe in getting changes for Waypoints/destinations

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|


### SubscribeWayPoints
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### GetWayPoints
Message Type: **request**

Request for getting waypoint/destination data.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`wayPointType`|True|To request for either the destination only or for all waypoints including destination|


### GetWayPoints
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|
|`wayPoints`|False|See LocationDetails|


### UnsubscribeWayPoints
Message Type: **request**

Request to unsubscribe from WayPoints and Destination

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|


### UnsubscribeWayPoints
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|
|`wayPoints`|False|See LocationDetails|


### GetSystemCapability
Message Type: **request**

Request for expanded information about a supported system/HMI capability

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`systemCapabilityType`|True|The type of system capability to get more information on|


### GetSystemCapability
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`systemCapability`|True||
|`resultCode`|True|See Result|
|`info`|False||
|`success`|True|true if successful; false, if failed |


### ButtonPress
Message Type: **request**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`moduleType`|The module where the button should be pressed|
|`buttonName`|The name of supported RC climate or radio button.|
|`buttonPressMode`|Indicates whether this is a LONG or SHORT button press event.|


### ButtonPress
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`resultCode`|See Result|
|`info`|False||
|`success`|true if successful; false, if failed |


### GetInteriorVehicleData
Message Type: **request**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`moduleType`|The type of a RC module to retrieve module data from the vehicle.        In the future, this should be the Identification of a module.      |
|`subscribe`|False|If subscribe is true, the head unit will register onInteriorVehicleData notifications for the requested moduelType.        If subscribe is false, the head unit will unregister onInteriorVehicleData notifications for the requested moduelType.      |


### GetInteriorVehicleData
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`moduleData`||
|`resultCode`|See Result|
|`info`|False||
|`success`|true if successful; false, if failed |
|`isSubscribed`|False|It is a conditional-mandatory parameter: must be returned in case "subscribe" parameter was present in the related request.       if "true" - the "moduleType" from request is successfully subscribed and the head unit will send onInteriorVehicleData notifications for the moduleType.       if "false" - the "moduleType" from request is either unsubscribed or failed to subscribe.     |


### SetInteriorVehicleData
Message Type: **request**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`moduleData`|The module data to set for the requested RC module.|


### SetInteriorVehicleData
Message Type: **response**

Used to set the values of one remote control module 

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`moduleData`||
|`resultCode`|See Result|
|`info`|False||
|`success`|true if successful; false, if failed |


### SendHapticData
Message Type: **request**

Send the spatial data gathered from SDLCarWindow or VirtualDisplayEncoder to the HMI. This data will be utilized by the HMI to determine how and when haptic events should occur

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`HapticSpatialData`|False|Array of spatial data structures that represent the locations of all user controls present on the HMI. This data should be updated if/when the application presents a new screen. When a request is sent, if successful, it will replace all spatial data previously sent through RPC. If an empty array is sent, the existing spatial data will be cleared|


### SendHapticData
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|true if successful; false if failed |
|`resultCode`|See Result|


### OnHMIStatus
Message Type: **notification**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`hmiLevel`|True|See HMILevel|
|`audioStreamingState`|True|See AudioStreamingState|
|`systemContext`|True|See SystemContext|


### OnAppInterfaceUnregistered
Message Type: **notification**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`reason`|True|See AppInterfaceUnregisteredReason|


### OnButtonEvent
Message Type: **notification**

Notifies application of UP/DOWN events for buttons to which the application is subscribed.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`buttonName`|True||
|`buttonEventMode`|True|Indicates whether this is an UP or DOWN event.|
|`customButtonID`|False|If ButtonName is "CUSTOM_BUTTON", this references the integer ID passed by a custom button. (e.g. softButton ID)|


### OnButtonPress
Message Type: **notification**

Notifies application of LONG/SHORT press events for buttons to which the application is subscribed.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`buttonName`|True||
|`buttonPressMode`|True|Indicates whether this is a LONG or SHORT button press event.|
|`customButtonID`|False|If ButtonName is "CUSTOM_BUTTON", this references the integer ID passed by a custom button. (e.g. softButton ID)|


### OnVehicleData
Message Type: **notification**

Callback for the periodic and non periodic vehicle data read function.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`gps`|False|See GPSData|
|`speed`|False|The vehicle speed in kilometers per hour|
|`rpm`|False|The number of revolutions per minute of the engine|
|`fuelLevel`|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|False|The fuel level state|
|`instantFuelConsumption`|False|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|False|The external temperature in degrees celsius|
|`vin`|False|Vehicle identification number.|
|`prndl`|False|See PRNDL|
|`tirePressure`|False|See TireStatus|
|`odometer`|False|Odometer in km|
|`beltStatus`|False|The status of the seat belts|
|`bodyInformation`|False|The body information including power modes|
|`deviceStatus`|False|The device status including signal and battery strength|
|`driverBraking`|False|The status of the brake pedal|
|`wiperStatus`|False|The status of the wipers|
|`headLampStatus`|False|Status of the head lamps|
|`engineTorque`|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|False|Current angle of the steering wheel (in deg)|
|`eCallInfo`|False|Emergency Call notification and confirmation data|
|`airbagStatus`|False|The status of the air bags|
|`emergencyEvent`|False|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|False|The status modes of the cluster|
|`myKey`|False|Information related to the MyKey feature|


### OnCommand
Message Type: **notification**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`cmdID`|True|Command ID, which is related to a specific menu entry|
|`triggerSource`|True|See TriggerSource|


### OnTBTClientState
Message Type: **notification**

Provides applications with notifications specific to the current TBT client status on the module

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`state`|True|Current State of TBT client|


### OnDriverDistraction
Message Type: **notification**

Provides driver distraction state to mobile applications

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`state`|True|Current State of Driver Distraction|


### OnPermissionsChange
Message Type: **notification**

Provides update to app of which policy-table-enabled functions are available

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`permissionItem`|True|Change in permissions for a given set of RPCs|


### OnAudioPassThru
Message Type: **notification**

Binary data is in binary part of hybrid msg

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|


### OnLanguageChange
Message Type: **notification**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`language`|True|Current SDL voice engine (VR+TTS) language|
|`hmiDisplayLanguage`|True|Current display language|


### OnKeyboardInput
Message Type: **notification**

On-screen keyboard event.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`event`|True|On-screen keyboard input data.|
|`data`|False|On-screen keyboard input data.|


### OnTouchEvent
Message Type: **notification**

Notifies about touch events on the screen's prescribed area

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`type`|True|The type of touch event.|
|`event`|True|List of all individual touches involved in this event.|


### OnSystemRequest
Message Type: **notification**

An asynchronous request from the system for specific data from the device or the cloud or response to a request from the device or cloud
            Binary data can be included in hybrid part of message for some requests (such as Authentication request responses)
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`requestType`|True|The type of system request.|
|`url`|False|Optional URL for HTTP requests.                If blank, the binary data shall be forwarded to the app.                If not blank, the binary data shall be forwarded to the url with a provided timeout in seconds.            |
|`timeout`|False|Optional timeout for HTTP requests                Required if a URL is provided            |
|`fileType`|False|Optional file type (meant for HTTP file requests).|
|`offset`|False|Optional offset in bytes for resuming partial data chunks|
|`length`|False|Optional length in bytes for resuming partial data chunks|


### OnHashChange
Message Type: **notification**

Notification containing an updated hashID which can be used over connection cycles (i.e. loss of connection, ignition cycles, etc.).
            Sent after initial registration and subsequently after any change in the calculated hash of all persisted app data.
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`hashID`|True|Calculated hash ID to be referenced during RegisterAppInterface.|


### OnWayPointChange
Message Type: **notification**

Notification which provides the entire LocationDetails when there is a change to any waypoints or destination.

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`wayPoints`|True|See LocationDetails|


### OnInteriorVehicleData
Message Type: **notification**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`moduleData`|True||


### EncodedSyncPData
Message Type: **request**

Allows encoded data in the form of SyncP packets to be sent to the SYNC module.
            Legacy / v1 Protocol implementation; use SyncPData instead.
            *** DEPRECATED ***
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`data`|True|Contains base64 encoded string of SyncP packets.|


### EncodedSyncPData
Message Type: **response**

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`success`|True|true, if successful; false, if failed |
|`resultCode`|True|See Result|
|`info`|False|Provides additional human readable info regarding the result.|


### OnEncodedSyncPData
Message Type: **notification**

Callback including encoded data of any SyncP packets that SYNC needs to send back to the mobile device.
            Legacy / v1 Protocol implementation; responds to EncodedSyncPData.
            *** DEPRECATED ***
        

##### Parameters

| Value | Mandatory | Description | 
| ---------- |:-----------: |:-----------:|
|`data`|True|Contains base64 encoded string of SyncP packets.|
|`URL`|False|If blank, the SyncP data shall be forwarded to the app.                If not blank, the SyncP data shall be forwarded to the provided URL.            |
|`Timeout`|False|If blank, the SyncP data shall be forwarded to the app.                If not blank, the SyncP data shall be forwarded with the provided timeout in seconds.            |


