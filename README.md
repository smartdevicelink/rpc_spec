# SmartDeviceLink
# RPC Spec

###### Version: 4.5.0

## Enumerations

### Result
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`SUCCESS`|The request succeeded|
|`UNSUPPORTED_REQUEST`|The request is not supported by Sync|
|`UNSUPPORTED_RESOURCE`|A button that was requested for subscription is not supported under the current system.                NOTE: could become a more generic UNSUPPORTED_RESOURCE by merging with VEHICLE_DATA_NOT_AVAILABLE.            |
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
|`WRONG_LANGUAGE`|The requested language is currently not supported.                Might be because of a mismatch of the currently active language on Sync and the requested language            |
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
|`FILE_NOT_FOUND`|A specified file could not be found on Sync.|
|`CANCEL_ROUTE`|User selected to Cancel Route.|
|`SAVED`|The RPC (e.g. Slider) executed successfully and the user elected to save the current position / value.|
|`INVALID_CERT`|The certificate provided during authentication is invalid.|
|`EXPIRED_CERT`|The certificate provided during authentication is expired.|
|`RESUME_FAILED`|The provided hash ID does not match the hash of the current set of registered data or the core could not resume the previous data.|


### ButtonPressMode
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`LONG`|A button was released, after it was pressed for a long time                Actual timing is defined by Sync and may vary            |
|`SHORT`|A button was released, after it was pressed for a short time                Actual timing is defined by Sync and may vary            |


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
|`MANUAL_ONLY`|This mode causes the interaction to only occur on the display, meaning the choices are provided only via the display.Selections are made with the OK and Seek Right and Left, Tune Up and Down buttons.|
|`VR_ONLY`|This mode causes the interaction to only occur using V4. Selections are made by saying the command.|
|`BOTH`|This mode causes both a VR and display selection option for an interaction. Selections can be made either from the menu display or by speaking the command.|


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
Error code, which comes from sync side.

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
Defines the hard (physical) and soft (touchscreen) buttons available from SYNC

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
|`GetWayPointsID`||
|`SubscribeWayPointsID`||
|`UnsubscribeWayPointsID`||
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



<div style="page-break-after: always;"></div>

## Structs

### AudioPassThruCapabilities
Describes different audio type configurations for PerformAudioPassThru.
            e.g. {8kHz,8-bit,PCM}
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`samplingRate`||
|`bitsPerSample`||
|`audioType`||


### Image
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`value`|Either the static hex icon value or the binary image file name identifier (sent by PutFile).|
|`imageType`|Describes, whether it is a static or dynamic image.|


### SoftButton
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`type`|Describes, whether it is text, highlighted text, icon, or dynamic image. See softButtonType|
|`text`|Optional text to display (if defined as TEXT or BOTH)|
|`image`|Optional image struct for SoftButton (if defined as IMAGE or BOTH)|
|`isHighlighted`|True, if highlighted                False, if not highlighted            |
|`softButtonID`|Value which is returned via OnButtonPress / OnButtonEvent|
|`systemAction`|Parameter indicating whether selecting a SoftButton shall call a specific system action.  This is intended to allow Notifications to bring the callee into full / focus; or in the case of persistent overlays, the overlay can persist when a SoftButton is pressed.|


### Choice
A choice is an option given to the user, which can be selected either by menu, or through voice recognition system.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`choiceID`||
|`menuName`||
|`vrCommands`||
|`image`||
|`secondaryText`|Optional secondary text to display; e.g. address of POI in a search result entry|
|`tertiaryText`|Optional tertiary text to display; e.g. distance to POI for a search result entry|
|`secondaryImage`|Optional secondary image struct for choice|


### VrHelpItem
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`text`|Text to display for VR Help item|
|`image`|Image struct for VR Help item|
|`position`|Position to display item in VR Help list|


### SyncMsgVersion
Specifies the version number of the SYNC V4 protocol, that is supported by the mobile application

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`majorVersion`|The major version indicates versions that is not-compatible to previous versions.|
|`minorVersion`|The minor version indicates a change to a previous version that should still allow to be run on an older version (with limited functionality)|
|`patchVersion`|The patch version indicates a fix to existing functionality in a previous version that should still be able to be run on an older version |


### SingleTireStatus
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`status`|See ComponentVolumeStatus.|


### BeltStatus
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`driverBeltDeployed`|References signal "VedsDrvBelt_D_Ltchd". See VehicleDataEventStatus.|
|`passengerBeltDeployed`|References signal "VedsPasBelt_D_Ltchd". See VehicleDataEventStatus.|
|`passengerBuckleBelted`|References signal "VedsRw1PasBckl_D_Ltchd". See VehicleDataEventStatus.|
|`driverBuckleBelted`|References signal "VedsRw1DrvBckl_D_Ltchd". See VehicleDataEventStatus.|
|`leftRow2BuckleBelted`|References signal "VedsRw2lBckl_D_Ltchd". See VehicleDataEventStatus.|
|`passengerChildDetected`|References signal "VedsRw1PasChld_D_Ltchd". See VehicleDataEventStatus.|
|`rightRow2BuckleBelted`|References signal "VedsRw2rBckl_D_Ltchd". See VehicleDataEventStatus.|
|`middleRow2BuckleBelted`|References signal "VedsRw2mBckl_D_Ltchd". See VehicleDataEventStatus.|
|`middleRow3BuckleBelted`|References signal "VedsRw3mBckl_D_Ltchd". See VehicleDataEventStatus.|
|`leftRow3BuckleBelted`|References signal "VedsRw3lBckl_D_Ltchd". See VehicleDataEventStatus.|
|`rightRow3BuckleBelted`|References signal "VedsRw3rBckl_D_Ltchd". See VehicleDataEventStatus.|
|`leftRearInflatableBelted`|References signal "VedsRw2lRib_D_Ltchd". See VehicleDataEventStatus.|
|`rightRearInflatableBelted`|References signal "VedsRw2rRib_D_Ltchd". See VehicleDataEventStatus.|
|`middleRow1BeltDeployed`|References signal "VedsRw1mBelt_D_Ltchd". See VehicleDataEventStatus.|
|`middleRow1BuckleBelted`|References signal "VedsRw1mBckl_D_Ltchd". See VehicleDataEventStatus.|


### BodyInformation
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`parkBrakeActive`|References signal "PrkBrkActv_B_Actl".|
|`ignitionStableStatus`|References signal "Ignition_Switch_Stable". See IgnitionStableStatus.|
|`ignitionStatus`|References signal "Ignition_status". See IgnitionStatus.|
|`driverDoorAjar`|References signal "DrStatDrv_B_Actl".|
|`passengerDoorAjar`|References signal "DrStatPsngr_B_Actl".|
|`rearLeftDoorAjar`|References signal "DrStatRl_B_Actl".|
|`rearRightDoorAjar`|References signal "DrStatRr_B_Actl".|


### DeviceStatus
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`voiceRecOn`|References signal "CPM_VoiceRec_STAT".|
|`btIconOn`|References signal "BT_ICON".|
|`callActive`|References signal "CPM_Call_Active_STAT".|
|`phoneRoaming`|References signal "CPM_Phone_Roaming_STAT".|
|`textMsgAvailable`|References signal "CPM_TextMsg_AVAL".|
|`battLevelStatus`|Device battery level status.  References signal "CPM_Batt_Level_STAT". See DeviceLevelStatus.|
|`stereoAudioOutputMuted`|References signal "CPM_Stereo_Audio_Output".|
|`monoAudioOutputMuted`|References signal "CPM_Mono_Audio_Output".|
|`signalLevelStatus`|Device signal level status.  References signal "CPM_Signal_Strength_STAT". See DeviceLevelStatus.|
|`primaryAudioSource`|References signal "CPM_Stereo_PAS_Source". See PrimaryAudioSource.|
|`eCallEventActive`|References signal "eCall_Event".|


### HeadLampStatus
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`lowBeamsOn`|Status of the low beam lamps.  References signal "HeadLampLoActv_B_Stat".|
|`highBeamsOn`|Status of the high beam lamps.  References signal "HeadLghtHiOn_B_Stat".|
|`ambientLightSensorStatus`|Status of the ambient light sensor.|


### AppInfo
Contains detailed information about the registered application.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`appDisplayName`|The name displayed for the mobile application on the mobile device (can differ from the app name set in the initial RAI request).|
|`appBundleID`|The AppBundleID of an iOS application or package name of the Android application. This supports App Launch strategies for each platform.|
|`appVersion`|Represents the build version number of this particular mobile app.|
|`appIcon`|A file reference to the icon utilized by this app (simplifies the process of setting an app icon during app registration).|


### ECallInfo
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`eCallNotificationStatus`|References signal "eCallNotification_4A". See VehicleDataNotificationStatus.|
|`auxECallNotificationStatus`|References signal "eCallNotification". See VehicleDataNotificationStatus.|
|`eCallConfirmationStatus`|References signal "eCallConfirmation". See ECallConfirmationStatus.|


### AirbagStatus
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`driverAirbagDeployed`|References signal "VedsDrvBag_D_Ltchd". See VehicleDataEventStatus.|
|`driverSideAirbagDeployed`|References signal "VedsDrvSideBag_D_Ltchd". See VehicleDataEventStatus.|
|`driverCurtainAirbagDeployed`|References signal "VedsDrvCrtnBag_D_Ltchd". See VehicleDataEventStatus.|
|`passengerAirbagDeployed`|References signal "VedsPasBag_D_Ltchd". See VehicleDataEventStatus.|
|`passengerCurtainAirbagDeployed`|References signal "VedsPasCrtnBag_D_Ltchd". See VehicleDataEventStatus.|
|`driverKneeAirbagDeployed`|References signal "VedsKneeDrvBag_D_Ltchd". See VehicleDataEventStatus.|
|`passengerSideAirbagDeployed`|References signal "VedsPasSideBag_D_Ltchd". See VehicleDataEventStatus.|
|`passengerKneeAirbagDeployed`|References signal "VedsKneePasBag_D_Ltchd". See VehicleDataEventStatus.|


### EmergencyEvent
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`emergencyEventType`|References signal "VedsEvntType_D_Ltchd". See EmergencyEventType.|
|`fuelCutoffStatus`|References signal "RCM_FuelCutoff". See FuelCutoffStatus.|
|`rolloverEvent`|References signal "VedsEvntRoll_D_Ltchd". See VehicleDataEventStatus.|
|`maximumChangeVelocity`|References signal "VedsMaxDeltaV_D_Ltchd". Change in velocity in KPH.  Additional reserved values:                0x00 No event                0xFE Not supported                0xFF Fault            |
|`multipleEvents`|References signal "VedsMultiEvnt_D_Ltchd". See VehicleDataEventStatus.|


### ClusterModeStatus
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`powerModeActive`|References signal "PowerMode_UB".|
|`powerModeQualificationStatus`|References signal "PowerModeQF". See PowerModeQualificationStatus.|
|`carModeStatus`|References signal "CarMode". See CarMode.|
|`powerModeStatus`|References signal "PowerMode". See PowerMode.|


### MyKey
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`e911Override`|Indicates whether e911 override is on.  References signal "MyKey_e911Override_St". See VehicleDataStatus.|


### TireStatus
The status and pressure of the tires.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`pressureTelltale`|Status of the Tire Pressure Telltale. See WarningLightStatus.|
|`leftFront`|The status of the left front tire.|
|`rightFront`|The status of the right front tire.|
|`leftRear`|The status of the left rear tire.|
|`rightRear`|The status of the right rear tire.|
|`innerLeftRear`|The status of the inner left rear.|
|`innerRightRear`|The status of the inner right rear.|


### GPSData
Struct with the GPS data.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`longitudeDegrees`||
|`latitudeDegrees`||
|`utcYear`|The current UTC year.|
|`utcMonth`|The current UTC month.|
|`utcDay`|The current UTC day.|
|`utcHours`|The current UTC hour.|
|`utcMinutes`|The current UTC minute.|
|`utcSeconds`|The current UTC second.|
|`compassDirection`|See CompassDirection.|
|`pdop`|PDOP.  If undefined or unavailable, then value shall be set to 0.|
|`hdop`|HDOP.  If value is unknown, value shall be set to 0.|
|`vdop`|VDOP.  If value is unknown, value shall be set to 0.|
|`actual`|True, if actual.                False, if infered.            |
|`satellites`|Number of satellites in view|
|`dimension`|See Dimension|
|`altitude`|Altitude in meters|
|`heading`|The heading. North is 0. Resolution is 0.01|
|`speed`|The speed in KPH|


### VehicleDataResult
Individual published data request result

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`dataType`|Defined published data element type.|
|`resultCode`|Published data result code.|


### DIDResult
Individual requested DID result and data

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`resultCode`|Individual DID result code.|
|`didLocation`|Location of raw data from vehicle data DID|
|`data`|Raw DID-based data returned for requested element.|


### StartTime
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`hours`|The hour of the media clock.                Some radios only support a max of 19 hours. If out of range, it will be rejected.            |
|`minutes`||
|`seconds`||


### TextField
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`name`|The name that identifies the field. See TextFieldName.|
|`characterSet`|The character set that is supported in this field. See CharacterSet.|
|`width`|The number of characters in one row of this field.|
|`rows`|The number of rows of this field.|


### ImageResolution
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`resolutionWidth`|The image resolution width.|
|`resolutionHeight`|The image resolution height.|


### ImageField
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`name`|The name that identifies the field. See ImageFieldName.|
|`imageTypeSupported`|The image types that are supported in this field. See FileType.|
|`imageResolution`|The image resolution of this field.|


### TouchCoord
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`x`|The x coordinate of the touch.|
|`y`|The y coordinate of the touch.|


### TouchEvent
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`id`|A touch's unique identifier.  The application can track the current touch events by id.                If a touch event has type begin, the id should be added to the set of touches.                If a touch event has type end, the id should be removed from the set of touches.            |
|`ts`|The time that the touch was recorded.  This number can the time since the beginning of the session or something else as long as the units are in milliseconds.                The timestamp is used to determined the rate of change of position of a touch.                The application also uses the time to verify whether two touches, with different ids, are part of a single action by the user.                If there is only a single timestamp in this array, it is the same for every coordinate in the coordinates array.            |
|`c`||


### TouchEventCapabilities
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`pressAvailable`||
|`multiTouchAvailable`||
|`doublePressAvailable`||


### ScreenParams
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`resolution`|The resolution of the prescribed screen area.|
|`touchEventAvailable`|Types of screen touch events available in screen area.|


### HMIPermissions
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`allowed`|A set of all HMI levels that are permitted for this given RPC.|
|`userDisallowed`|A set of all HMI levels that are prohibited for this given RPC.|


### ParameterPermissions
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`allowed`|A set of all parameters that are permitted for this given RPC.|
|`userDisallowed`|A set of all parameters that are prohibited for this given RPC.|


### PermissionItem
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`rpcName`|Name of the individual RPC in the policy table.|
|`hmiPermissions`||
|`parameterPermissions`||


### DisplayCapabilities
Contains information about the display capabilities.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`displayType`|The type of the display. See DisplayType|
|`textFields`|A set of all fields that support text data. See TextField|
|`imageFields`|A set of all fields that support images. See ImageField|
|`mediaClockFormats`|A set of all supported formats of the media clock. See MediaClockFormat|
|`graphicSupported`|The display's persistent screen supports referencing a static or dynamic image.|
|`templatesAvailable`|A set of all predefined persistent display templates available on headunit.  To be referenced in SetDisplayLayout.|
|`screenParams`|A set of all parameters related to a prescribed screen area (e.g. for video / touch input).|
|`numCustomPresetsAvailable`|The number of on-screen custom presets available (if any); otherwise omitted.|


### ButtonCapabilities
Contains information about a button's capabilities.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`name`|The name of the button. See ButtonName.|
|`shortPressAvailable`|The button supports a short press.         Whenever the button is pressed short, onButtonPressed( SHORT) will be invoked.         |
|`longPressAvailable`|The button supports a LONG press.         Whenever the button is pressed long, onButtonPressed( LONG) will be invoked.         |
|`upDownAvailable`|The button supports "button down" and "button up".         Whenever the button is pressed, onButtonEvent( DOWN) will be invoked.         Whenever the button is released, onButtonEvent( UP) will be invoked.         |


### SoftButtonCapabilities
Contains information about a SoftButton's capabilities.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`shortPressAvailable`|The button supports a short press.         Whenever the button is pressed short, onButtonPressed( SHORT) will be invoked.         |
|`longPressAvailable`|The button supports a LONG press.         Whenever the button is pressed long, onButtonPressed( LONG) will be invoked.         |
|`upDownAvailable`|The button supports "button down" and "button up".         Whenever the button is pressed, onButtonEvent( DOWN) will be invoked.         Whenever the button is released, onButtonEvent( UP) will be invoked.         |
|`imageSupported`|The button supports referencing a static or dynamic image.|


### PresetBankCapabilities
Contains information about on-screen preset capabilities.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`onScreenPresetsAvailable`|Onscreen custom presets are available.|


### HMICapabilities
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`navigation`|Availability of build in Nav. True: Available, False: Not Available|
|`phoneCall`|Availability of build in phone. True: Available, False: Not Available |


### MenuParams
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`parentID`|unique ID of the sub menu, the command will be added to.         If not provided, it will be provided to the top level of the in application menu.         |
|`position`|Position within the items that are are at top level of the in application menu.         0 will insert at the front.         1 will insert at the second position.         if position is greater or equal than the number of items on top level, the sub menu will be appended to the end.         If this param was omitted the entry will be added at the end.         |
|`menuName`|Text to show in the menu for this sub menu.|


### TTSChunk
A TTS chunk, that consists of the text/phonemes to speak and the type (like text or SAPI)

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`text`|The text or phonemes to speak.         May not be empty.         |
|`type`|Describes, whether it is text or a specific phoneme set. See SpeechCapabilities|


### Turn
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`navigationText`|Individual turn text.  Must provide at least text or icon for a given turn.|
|`turnIcon`|Individual turn icon.  Must provide at least text or icon for a given turn.|


### VehicleType
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`make`|Make of the vehicle, e.g. Ford|
|`model`|Model of the vehicle, e.g. Fiesta|
|`modelYear`|Model Year of the vehicle, e.g. 2013|
|`trim`|Trim of the vehicle, e.g. SE|


### KeyboardProperties
Configuration of on-screen keyboard (if available).

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`language`|The keyboard language.|
|`keyboardLayout`|Desired keyboard layout.|
|`keypressMode`|Desired keypress mode.         If omitted, this value will be set to RESEND_CURRENT_ENTRY.         |
|`limitedCharacterList`|Array of keyboard characters to enable.|
|`autoCompleteText`|Allows an app to prepopulate the text field with a suggested or completed entry as the user types|


### DeviceInfo
Various information abount connecting device.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`hardware`|Device model|
|`firmwareRev`|Device firmware revision|
|`os`|Device OS|
|`osVersion`|Device OS version|
|`carrier`|Device mobile carrier (if applicable)|
|`maxNumberRFCOMMPorts`|Omitted if connected not via BT.|


### DateTime
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`millisecond`|Milliseconds |
|`second`|Seconds part of time|
|`minute`|Minutes part of time|
|`hour`|Hours part of time. Note that this structure accepts time only in 24 Hr format|
|`day`|Day of the month|
|`month`|Month of the year|
|`year`|The year in YYYY format|
|`tz_hour`|Time zone offset in Hours wrt UTC.|
|`tz_minute`|Time zone offset in Min wrt UTC.|


### Coordinate
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`latitudeDegrees`|Latitude of the location.|
|`longitudeDegrees`|Longitude of the location.|


### OASISAddress
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`countryName`|Name of the country (localized)|
|`countryCode`|Name of country (ISO 3166-2)|
|`postalCode`|(PLZ, ZIP, PIN, CAP etc.)|
|`administrativeArea`|Portion of country (e.g. state)|
|`subAdministrativeArea`|Portion of e.g. state (e.g. county)|
|`locality`|Hypernym for e.g. city/village|
|`subLocality`|Hypernym for e.g. district|
|`thoroughfare`|Hypernym for street, road etc.|
|`subThoroughfare`|Portion of thoroughfare e.g. house number|


### LocationDetails
##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`coordinate`|Latitude/Longitude of the location.|
|`locationName`|Name of location.|
|`addressLines`|Location address for display purposes only|
|`locationDescription`|Description intended location / establishment (if applicable)|
|`phoneNumber`|Phone number of location / establishment.|
|`locationImage`|Image / icon of intended location.|
|`searchAddress`|Address to be used by navigation engines for search|



<div style="page-break-after: always;"></div>


## Remote Procedure Calls

### RegisterAppInterface
Message Type: **request**

Establishes an interface with a mobile application.
            Before registerAppInterface no other commands will be accepted/executed.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`syncMsgVersion`|See SyncMsgVersion|
|`appName`|The mobile application name, e.g. "Ford Drive Green".                Needs to be unique over all applications.                May not be empty.                May not start with a new line character.                May not interfere with any name or synonym of previously registered applications and any predefined blacklist of words (global commands)                Needs to be unique over all applications. Applications with the same name will be rejected.                Only characters from char set [@TODO: Create char set (character/hex value) for each ACM and refer to] are supported.            |
|`ttsName`|TTS string for VR recognition of the mobile application name, e.g. "Ford Drive Green".                Meant to overcome any failing on speech engine in properly pronouncing / understanding app name.                Needs to be unique over all applications.                May not be empty.                May not start with a new line character.                Only characters from char set [@TODO: Create char set (character/hex value) for each ACM and refer to] are supported.            |
|`ngnMediaScreenAppName`|Provides an abbreviated version of the app name (if needed), that will be displayed on the NGN media screen.                If not provided, the appName is used instead (and will be truncated if too long)                Only characters from char set [@TODO: Create char set (character/hex value) for each ACM and refer to] are supported.            |
|`vrSynonyms`|Defines an additional voice recognition command.                May not interfere with any app name of previously registered applications and any predefined blacklist of words (global commands)                Only characters from char set [@TODO: Create char set (character/hex value) for each ACM and refer to] are supported.            |
|`isMediaApplication`|Indicates if the application is a media or a non-media application.                Only media applications will be able to stream audio to Sync that is audible outside of the BT media source.            |
|`languageDesired`|See Language                Current app's expected VR+TTS language                If there is a mismatch with SYNC, the app will be able to change this registration with changeRegistration prior to app being brought into focus.            |
|`hmiDisplayLanguageDesired`|See Language                Current app's expected display language                If there is a mismatch with SYNC, the app will be able to change this registration with changeRegistration prior to app being brought into focus.            |
|`appHMIType`|See AppHMIType                List of all applicable app HMI types stating which HMI classifications to be given to the app.            |
|`hashID`|ID used to uniquely identify current state of all app data that can persist through connection cycles (e.g. ignition cycles).                This registered data (commands, submenus, choice sets, etc.) can be reestablished without needing to explicitly reregister each piece.                If omitted, then the previous state of an app's commands, etc. will not be restored.                When sending hashID, all RegisterAppInterface parameters should still be provided (e.g. ttsName, etc.).            |
|`deviceInfo`|See DeviceInfo.            |
|`appID`|ID used to validate app with policy table entries|
|`appInfo`|See AppInfo.            |


### RegisterAppInterface
Message Type: **response**

The response to registerAppInterface

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|
|`syncMsgVersion`|See SyncMsgVersion|
|`language`|The currently active VR+TTS language on Sync. See "Language" for options.|
|`hmiDisplayLanguage`|The currently active display language on Sync. See "Language" for options.|
|`displayCapabilities`|See DisplayCapabilities|
|`buttonCapabilities`|See ButtonCapabilities|
|`softButtonCapabilities`|If returned, the platform supports on-screen SoftButtons; see SoftButtonCapabilities.|
|`presetBankCapabilities`|If returned, the platform supports custom on-screen Presets; see PresetBankCapabilities.|
|`hmiZoneCapabilities`|See HmiZoneCapabilities|
|`speechCapabilities`|See SpeechCapabilities|
|`prerecordedSpeech`|See PrerecordedSpeech|
|`vrCapabilities`|See VrCapabilities|
|`audioPassThruCapabilities`|See AudioPassThruCapability|
|`pcmStreamCapabilities`|See AudioPassThruCapability|
|`vehicleType`|Specifies the vehicle's type. See VehicleType.|
|`supportedDiagModes`|Specifies the white-list of supported diagnostic modes (0x00-0xFF) capable for DiagnosticMessage requests.                If a mode outside this list is requested, it will be rejected.            |
|`hmiCapabilities`|Specifies the HMIÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s capabilities. See HMICapabilities.|
|`sdlVersion`|The SmartDeviceLink version.|
|`systemSoftwareVersion`|The software version of the system that implements the SmartDeviceLink core.|


### UnregisterAppInterface
Message Type: **request**

Closes an interface from a mobile application.
            After unregisterAppInterface, no commands other than registerAppInterface will be accepted/executed.
            Will fail, if no registerAppInterface was completed successfully before.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|


### UnregisterAppInterface
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### SetGlobalProperties
Message Type: **request**

Allows setting global properties.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`helpPrompt`|The help prompt.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`timeoutPrompt`|Help text for a wait timeout.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`vrHelpTitle`|VR Help Title text.                If omitted on supported displays, the default SYNC help title shall be used.                If omitted and one or more vrHelp items are provided, the request will be rejected.            |
|`vrHelp`|VR Help Items.                If omitted on supported displays, the default AppLink VR help / What Can I Say? screen shall be used.                If the list of VR Help Items contains nonsequential positions (e.g. [1,2,4]), the RPC shall be rejected.                If omitted and a vrHelpTitle is provided, the request will be rejected.            |
|`menuTitle`|Optional text to label an app menu button (for certain touchscreen platforms).|
|`menuIcon`|>Optional icon to draw on an app menu button (for certain touchscreen platforms).|
|`keyboardProperties`|On-screen keybaord configuration (if available).|


### SetGlobalProperties
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### ResetGlobalProperties
Message Type: **request**

Allows resetting global properties.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`properties`|Contains the names of all global properties (like timeoutPrompt) that should be unset. Resetting means, that they have the same value as at start up (default)|


### ResetGlobalProperties
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### AddCommand
Message Type: **request**

Adds a command to the in application menu.
            Either menuParams or vrCommands must be provided.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`cmdID`|unique ID of the command to add.|
|`menuParams`|Optional sub value containing menu parameters|
|`vrCommands`|An array of strings to be used as VR synonyms for this command.                If this array is provided, it may not be empty.            |
|`cmdIcon`|Image struct determining whether static or dynamic icon.                If omitted on supported displays, no (or the default if applicable) icon shall be displayed.            |


### AddCommand
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### DeleteCommand
Message Type: **request**

Deletes all commands from the in-application menu with the specified command id.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`cmdID`|ID of the command(s) to delete.|


### DeleteCommand
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### AddSubMenu
Message Type: **request**

Adds a sub menu to the in-application menu.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`menuID`|unique ID of the sub menu to add.|
|`position`|Position within the items that are are at top level of the in application menu.                0 will insert at the front.                1 will insert at the second position.                If position is greater or equal than the number of items on top level, the sub menu will be appended to the end.                Position of any submenu will always be located before the return and exit options                If this param was omitted the entry will be added at the end.            |
|`menuName`|Text to show in the menu for this sub menu.|


### AddSubMenu
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### DeleteSubMenu
Message Type: **request**

Deletes a submenu from the in-application menu.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`menuID`|The "menuID" of the submenu to delete. (See addSubMenu.menuID)|


### DeleteSubMenu
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### CreateInteractionChoiceSet
Message Type: **request**

creates interaction choice set to be used later by performInteraction

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`interactionChoiceSetID`|Unique ID used for this interaction choice set.|
|`choiceSet`||


### CreateInteractionChoiceSet
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### PerformInteraction
Message Type: **request**

Triggers an interaction (e.g. "Permit GPS?" - Yes, no, Always Allow).

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`initialText`|Text to be displayed first.            |
|`initialPrompt`|This is the intial prompt spoken to the user at the start of an interaction.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`interactionMode`|See InteractionMode.|
|`interactionChoiceSetIDList`|List of interaction choice set IDs to use with an interaction.|
|`helpPrompt`|Help text. This is the spoken string when a user speaks "help" when the interaction is occuring.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`timeoutPrompt`|Timeout text. This text is spoken when a VR interaction times out.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`timeout`|Timeout in milliseconds.                If omitted a standard value of 10000 milliseconds is used.                Applies only to the menu portion of the interaction. The VR timeout will be handled by the platform.            |
|`vrHelp`|Ability to send suggested VR Help Items to display on-screen during Perform Interaction.                If omitted on supported displays, the default SYNC generated list of suggested choices shall be displayed.            |
|`interactionLayout`|See LayoutMode.|


### PerformInteraction
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|
|`choiceID`|ID of the choice that was selected in response to PerformInteraction.                Only is valid if general result is "success:true".            |
|`manualTextEntry`|Manually entered text selection, e.g. through keyboard                Can be returned in lieu of choiceID, depending on trigger source            |
|`triggerSource`|See TriggerSource                Only is valid if resultCode is SUCCESS.            |


### DeleteInteractionChoiceSet
Message Type: **request**

Deletes interaction choice set that has been created with "CreateInteractionChoiceSet".

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`interactionChoiceSetID`|ID of the interaction choice set to delete.|


### DeleteInteractionChoiceSet
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### Alert
Message Type: **request**

Shows an alert which typically consists of text-to-speech message and text on the display. At least either alertText1, alertText2 or TTSChunks need to be provided.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`alertText1`|The first line of the alert text field|
|`alertText2`|The second line of the alert text field|
|`alertText3`|The optional third line of the alert text field|
|`ttsChunks`|An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`duration`|Timeout in milliseconds.                Typical timeouts are 3-5 seconds.                If omitted, timeout is set to 5s.            |
|`playTone`|Defines if tone should be played. Tone is played before TTS.                If omitted, no tone is played.            |
|`progressIndicator`|If supported on the given platform, the alert GUI will include some sort of animation indicating that loading of a feature is progressing.  e.g. a spinning wheel or hourglass, etc.            |
|`softButtons`|App defined SoftButtons.                If omitted on supported displays, the displayed alert shall not have any SoftButtons.            |


### Alert
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|
|`tryAgainTime`|Amount of time (in seconds) that an app must wait before resending an alert.                If provided, another system event or overlay currently has a higher priority than this alert.                An app must not send an alert without waiting at least the amount of time dictated.            |


### Show
Message Type: **request**

Updates the persistent display. Supported fields depend on display capabilities.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`mainField1`|The text that should be displayed in a single or upper display line.                If this text is not set, the text of mainField1 stays unchanged.                If this text is empty "", the field will be cleared.            |
|`mainField2`|The text that should be displayed on the second display line.                If this text is not set, the text of mainField2 stays unchanged.                If this text is empty "", the field will be cleared.            |
|`mainField3`|The text that should be displayed on the second "page" first display line.                If this text is not set, the text of mainField3 stays unchanged.                If this text is empty "", the field will be cleared.            |
|`mainField4`|The text that should be displayed on the second "page" second display line.                If this text is not set, the text of mainField4 stays unchanged.                If this text is empty "", the field will be cleared.            |
|`alignment`|Specifies how mainField1 and mainField2 texts should be aligned on display.                If omitted, texts will be centered.            |
|`statusBar`|Requires investigation regarding the nav display capabilities. Potentially lower lowerStatusBar, upperStatusBar, titleBar, etc.|
|`mediaClock`|Text value for MediaClock field. Has to be properly formatted by Mobile App according to Sync capabilities.                If this text is set, any automatic media clock updates previously set with SetMediaClockTimer will be stopped.            |
|`mediaTrack`|The text that should be displayed in the track field.                If this text is not set, the text of mediaTrack stays unchanged.                If this text is empty "", the field will be cleared.            |
|`graphic`|Image struct determining whether static or dynamic image to display in app.                If omitted on supported displays, the displayed graphic shall not change.            |
|`secondaryGraphic`|Image struct determining whether static or dynamic secondary image to display in app.                If omitted on supported displays, the displayed secondary graphic shall not change.            |
|`softButtons`|App defined SoftButtons.                If omitted on supported displays, the currently displayed SoftButton values will not change.            |
|`customPresets`|App labeled on-screen presets (i.e. on-screen media presets or dynamic search suggestions).                If omitted on supported displays, the presets will be shown as not defined.            |


### Show
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### Speak
Message Type: **request**

Speaks a text.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`ttsChunks`|An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |


### Speak
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### SetMediaClockTimer
Message Type: **request**

Sets the initial media clock value and automatic update method.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`startTime`|See StartTime.                startTime must be provided for "COUNTUP" and "COUNTDOWN".                startTime will be ignored for "RESUME", and "CLEAR"                startTime can be sent for "PAUSE", in which case it will update the paused startTime            |
|`endTime`|See StartTime.                endTime can be provided for "COUNTUP" and "COUNTDOWN"; to be used to calculate any visual progress bar (if not provided, this feature is ignored)                If endTime is greater then startTime for COUNTDOWN or less than startTime for COUNTUP, then the request will return an INVALID_DATA.                endTime will be ignored for "RESUME", and "CLEAR"                endTime can be sent for "PAUSE", in which case it will update the paused endTime            |
|`updateMode`|Enumeration to control the media clock.                In case of pause, resume, or clear, the start time value is ignored and shall be left out.  For resume, the time continues with the same value as it was when paused.            |


### SetMediaClockTimer
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### PerformAudioPassThru
Message Type: **request**

Starts audio pass thru session 

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`initialPrompt`|SYNC will speak this prompt before opening the audio pass thru session.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.                If omitted, then no initial prompt is spoken.            |
|`audioPassThruDisplayText1`|First line of text displayed during audio capture.|
|`audioPassThruDisplayText2`|Second line of text displayed during audio capture.|
|`samplingRate`|This value shall be allowed at 8 khz or 16 or 22 or 44 khz.|
|`maxDuration`|The maximum duration of audio recording in milliseconds. |
|`bitsPerSample`|Specifies the quality the audio is recorded. Currently 8 bit or 16 bit.|
|`audioType`|Specifies the type of audio data being requested.|
|`muteAudio`|Defines if the current audio source should be muted during the APT session.  If not, the audio source will play without interruption.                If omitted, the value is set to true.            |


### PerformAudioPassThru
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### EndAudioPassThru
Message Type: **request**

When this request is invoked, the audio capture stops.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|


### EndAudioPassThru
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### SubscribeButton
Message Type: **request**

Subscribes to built-in HMI buttons.
            The application will be notified by the OnButtonEvent and OnButtonPress.
            To unsubscribe the notifications, use unsubscribeButton.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`buttonName`|Name of the button to subscribe.|


### SubscribeButton
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### UnsubscribeButton
Message Type: **request**

Unsubscribes from built-in HMI buttons.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`buttonName`|Name of the button to unsubscribe.|


### UnsubscribeButton
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### SubscribeVehicleData
Message Type: **request**

Subscribes for specific published data items.
            The data will be only sent if it has changed.
            The application will be notified by the onVehicleData notification whenever new data is available.
            To unsubscribe the notifications, use unsubscribe with the same subscriptionType.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`gps`|See GPSData|
|`speed`|The vehicle speed in kilometers per hour|
|`rpm`|The number of revolutions per minute of the engine|
|`fuelLevel`|The fuel level in the tank (percentage)|
|`fuelLevel_State`|The fuel level state|
|`instantFuelConsumption`|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|The external temperature in degrees celsius|
|`prndl`|See PRNDL|
|`tirePressure`|See TireStatus|
|`odometer`|Odometer in km|
|`beltStatus`|The status of the seat belts|
|`bodyInformation`|The body information including power modes|
|`deviceStatus`|The device status including signal and battery strength|
|`driverBraking`|The status of the brake pedal|
|`wiperStatus`|The status of the wipers|
|`headLampStatus`|Status of the head lamps|
|`engineTorque`|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|Current angle of the steering wheel (in deg)|
|`eCallInfo`|Emergency Call notification and confirmation data|
|`airbagStatus`|The status of the air bags|
|`emergencyEvent`|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|The status modes of the cluster|
|`myKey`|Information related to the MyKey feature|


### SubscribeVehicleData
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|
|`gps`|See GPSData|
|`speed`|The vehicle speed in kilometers per hour|
|`rpm`|The number of revolutions per minute of the engine|
|`fuelLevel`|The fuel level in the tank (percentage)|
|`fuelLevel_State`|The fuel level state|
|`instantFuelConsumption`|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|The external temperature in degrees celsius.|
|`prndl`|See PRNDL|
|`tirePressure`|See TireStatus|
|`odometer`|Odometer in km|
|`beltStatus`|The status of the seat belts|
|`bodyInformation`|The body information including power modes|
|`deviceStatus`|The device status including signal and battery strength|
|`driverBraking`|The status of the brake pedal|
|`wiperStatus`|The status of the wipers|
|`headLampStatus`|Status of the head lamps|
|`engineTorque`|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|Current angle of the steering wheel (in deg)|
|`eCallInfo`|Emergency Call notification and confirmation data|
|`airbagStatus`|The status of the air bags|
|`emergencyEvent`|Information related to an emergency event (and if it occurred)|
|`clusterModes`|The status modes of the cluster|
|`myKey`|Information related to the MyKey feature|


### UnsubscribeVehicleData
Message Type: **request**

This function is used to unsubscribe the notifications from the subscribeVehicleData function.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`gps`|See GPSData|
|`speed`|The vehicle speed in kilometers per hour|
|`rpm`|The number of revolutions per minute of the engine|
|`fuelLevel`|The fuel level in the tank (percentage)|
|`fuelLevel_State`|The fuel level state|
|`instantFuelConsumption`|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|The external temperature in degrees celsius.|
|`prndl`|See PRNDL|
|`tirePressure`|See TireStatus|
|`odometer`|Odometer in km|
|`beltStatus`|The status of the seat belts|
|`bodyInformation`|The body information including power modes|
|`deviceStatus`|The device status including signal and battery strength|
|`driverBraking`|The status of the brake pedal|
|`wiperStatus`|The status of the wipers|
|`headLampStatus`|Status of the head lamps|
|`engineTorque`|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|Current angle of the steering wheel (in deg)|
|`eCallInfo`|Emergency Call notification and confirmation data|
|`airbagStatus`|The status of the air bags|
|`emergencyEvent`|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|The status modes of the cluster|
|`myKey`|Information related to the MyKey feature|


### UnsubscribeVehicleData
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|
|`gps`|See GPSData|
|`speed`|The vehicle speed in kilometers per hour|
|`rpm`|The number of revolutions per minute of the engine|
|`fuelLevel`|The fuel level in the tank (percentage)|
|`fuelLevel_State`|The fuel level state|
|`instantFuelConsumption`|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|The external temperature in degrees celsius|
|`prndl`|See PRNDL|
|`tirePressure`|See TireStatus|
|`odometer`|Odometer in km|
|`beltStatus`|The status of the seat belts|
|`bodyInformation`|The body information including power modes|
|`deviceStatus`|The device status including signal and battery strength|
|`driverBraking`|The status of the brake pedal|
|`wiperStatus`|The status of the wipers|
|`headLampStatus`|Status of the head lamps|
|`engineTorque`|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|Current angle of the steering wheel (in deg)|
|`eCallInfo`|Emergency Call notification and confirmation data|
|`airbagStatus`|The status of the air bags|
|`emergencyEvent`|Information related to an emergency event (and if it occurred)|
|`clusterModes`|The status modes of the cluster|
|`myKey`|Information related to the MyKey feature|


### GetVehicleData
Message Type: **request**

Non periodic vehicle data read request.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`gps`|See GPSData|
|`speed`|The vehicle speed in kilometers per hour|
|`rpm`|The number of revolutions per minute of the engine|
|`fuelLevel`|The fuel level in the tank (percentage)|
|`fuelLevel_State`|The fuel level state|
|`instantFuelConsumption`|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|The external temperature in degrees celsius|
|`vin`|Vehicle identification number|
|`prndl`|See PRNDL|
|`tirePressure`|See TireStatus|
|`odometer`|Odometer in km|
|`beltStatus`|The status of the seat belts|
|`bodyInformation`|The body information including ignition status and internal temp|
|`deviceStatus`|The device status including signal and battery strength|
|`driverBraking`|The status of the brake pedal|
|`wiperStatus`|The status of the wipers|
|`headLampStatus`|Status of the head lamps|
|`engineTorque`|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|Current angle of the steering wheel (in deg)|
|`eCallInfo`|Emergency Call notification and confirmation data|
|`airbagStatus`|The status of the air bags|
|`emergencyEvent`|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|The status modes of the cluster|
|`myKey`|Information related to the MyKey feature|


### GetVehicleData
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|
|`gps`|See GPSData|
|`speed`|The vehicle speed in kilometers per hour|
|`rpm`|The number of revolutions per minute of the engine|
|`fuelLevel`|The fuel level in the tank (percentage)|
|`fuelLevel_State`|The fuel level state|
|`instantFuelConsumption`|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|The external temperature in degrees celsius|
|`vin`|Vehicle identification number|
|`prndl`|See PRNDL|
|`tirePressure`|See TireStatus|
|`odometer`|Odometer in km|
|`beltStatus`|The status of the seat belts|
|`bodyInformation`|The body information including power modes|
|`deviceStatus`|The device status including signal and battery strength|
|`driverBraking`|The status of the brake pedal|
|`wiperStatus`|The status of the wipers|
|`headLampStatus`|Status of the head lamps|
|`engineTorque`|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|Current angle of the steering wheel (in deg)|
|`eCallInfo`|Emergency Call notification and confirmation data|
|`airbagStatus`|The status of the air bags|
|`emergencyEvent`|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|The status modes of the cluster|
|`myKey`|Information related to the MyKey feature|


### ReadDID
Message Type: **request**

Non periodic vehicle data read request

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`ecuName`|Name of ECU.|
|`didLocation`|Get raw data from vehicle data DID location(s)|


### ReadDID
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|
|`didResult`|Array of requested DID results (with data if available).|


### GetDTCs
Message Type: **request**

Vehicle module diagnostic trouble code request.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`ecuName`|Name of ECU.|
|`dtcMask`|DTC Mask Byte to be sent in diagnostic request to module .|


### GetDTCs
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|
|`ecuHeader`|2 byte ECU Header for DTC response (as defined in VHR_Layout_Specification_DTCs.pdf)|
|`dtc`|Array of all reported DTCs on module (ecuHeader contains information if list is truncated).                Each DTC is represented by 4 bytes (3 bytes of data and 1 byte status as defined in VHR_Layout_Specification_DTCs.pdf).            |


### DiagnosticMessage
Message Type: **request**

Non periodic vehicle diagnostic request

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`targetID`|Name of target ECU.|
|`messageLength`|Length of message (in bytes).|
|`messageData`|Array of bytes comprising CAN message.            |


### DiagnosticMessage
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|
|`messageDataResult`|Array of bytes comprising CAN message result.            |


### ScrollableMessage
Message Type: **request**

Creates a full screen overlay containing a large block of formatted text that can be scrolled with up to 8 SoftButtons defined

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`scrollableMessageBody`|Body of text that can include newlines and tabs.|
|`timeout`|App defined timeout.  Indicates how long of a timeout from the last action (i.e. scrolling message resets timeout).|
|`softButtons`|App defined SoftButtons.                If omitted on supported displays, only the system defined "Close" SoftButton will be displayed.            |


### ScrollableMessage
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### Slider
Message Type: **request**

Creates a full screen or pop-up overlay (depending on platform) with a single user controlled slider.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`numTicks`|Number of selectable items on a horizontal axis|
|`position`|Initial position of slider control (cannot exceed numTicks)|
|`sliderHeader`|Text header to display|
|`sliderFooter`|Text footer to display (meant to display min/max threshold descriptors).                For a static text footer, only one footer string shall be provided in the array.                For a dynamic text footer, the number of footer text string in the array must match the numTicks value.                For a dynamic text footer, text array string should correlate with potential slider position index.                If omitted on supported displays, no footer text shall be displayed.            |
|`timeout`|App defined timeout.  Indicates how long of a timeout from the last action (i.e. sliding control resets timeout).                If omitted, the value is set to 10000.            |


### Slider
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|
|`sliderPosition`|Current slider value returned when saved or canceled (aborted)                This value is only returned for resultCodes "SAVED" or "ABORTED"            |


### ShowConstantTBT
Message Type: **request**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`navigationText1`||
|`navigationText2`||
|`eta`||
|`timeToDestination`||
|`totalDistance`||
|`turnIcon`||
|`nextTurnIcon`||
|`distanceToManeuver`|Fraction of distance till next maneuver (starting from when AlertManeuver is triggered).                Used to calculate progress bar.            |
|`distanceToManeuverScale`|Distance till next maneuver (starting from) from previous maneuver.                Used to calculate progress bar.            |
|`maneuverComplete`|If and when a maneuver has completed while an AlertManeuver is active, the app must send this value set to TRUE in order to clear the AlertManeuver overlay.                If omitted the value will be assumed as FALSE.            |
|`softButtons`|Three dynamic SoftButtons available (first SoftButton is fixed to "Turns").                If omitted on supported displays, the currently displayed SoftButton values will not change.            |


### ShowConstantTBT
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### AlertManeuver
Message Type: **request**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`ttsChunks`|An array of text chunks of type TTSChunk. See TTSChunk|
|`softButtons`|If omitted on supported displays, only the system defined "Close" SoftButton shall be displayed.|


### AlertManeuver
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### UpdateTurnList
Message Type: **request**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`turnList`||
|`softButtons`|If omitted on supported displays, app-defined SoftButton will be left blank.|


### UpdateTurnList
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### ChangeRegistration
Message Type: **request**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`language`|Requested voice engine (VR+TTS) language registration|
|`hmiDisplayLanguage`|Request display language registration|
|`appName`|Request new app name registration|
|`ttsName`|Request new ttsName registration|
|`ngnMediaScreenAppName`|Request new app short name registration|
|`vrSynonyms`|Request new VR synonyms registration|


### ChangeRegistration
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful                false, if failed            |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### GenericResponse
Message Type: **response**

Generic Response is sent, when the name of a received msg cannot be retrieved. Only used in case of an error.
            Currently, only resultCode INVALID_DATA is used.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### PutFile
Message Type: **request**

Used to push a binary data onto the SYNC module from a mobile device, such as icons and album art
            Not supported on first generation SYNC vehicles.
            Binary data is in binary part of hybrid msg.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`syncFileName`|File reference name.|
|`fileType`|Selected file type.|
|`persistentFile`|Indicates if the file is meant to persist between sessions / ignition cycles.                If set to TRUE, then the system will aim to persist this file through session / cycles.                While files with this designation will have priority over others, they are subject to deletion by the system at any time.                In the event of automatic deletion by the system, the app will receive a rejection and have to resend the file.                If omitted, the value will be set to false.            |
|`systemFile`|Indicates if the file is meant to be passed thru core to elsewhere on the system.                If set to TRUE, then the system will instead pass the data thru as it arrives to a predetermined area outside of core.                If omitted, the value will be set to false.            |
|`offset`|Optional offset in bytes for resuming partial data chunks|
|`length`|Optional length in bytes for resuming partial data chunks                If offset is set to 0, then length is the total length of the file to be downloaded            |


### PutFile
Message Type: **response**

Response is sent, when the file data was copied (success case). Or when an error occured.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`spaceAvailable`|Provides the total local space available in SDL Core for the registered app.                If the transfer has systemFile enabled, then the value will be set to 0 automatically.            |
|`info`|Provides additional human readable info regarding the result.|


### DeleteFile
Message Type: **request**

Used to delete a file resident on the SYNC module in the app's local cache.
            Not supported on first generation SYNC vehicles.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`syncFileName`|File reference name.|


### DeleteFile
Message Type: **response**

Response is sent, when the file data was deleted (success case). Or when an error occured.
            Not supported on First generation SYNC vehicles.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true if successful; false, if failed |
|`resultCode`|See Result|
|`spaceAvailable`|Provides the total local space available on SYNC for the registered app.|
|`info`|Provides additional human readable info regarding the result.|


### ListFiles
Message Type: **request**

Requests the current list of resident filenames for the registered app.
            Not supported on first generation SYNC vehicles.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|


### ListFiles
Message Type: **response**

Returns the current list of resident filenames for the registered app along with the current space available
            Not supported on First generation SYNC vehicles.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`filenames`|An array of all filenames resident on SYNC for the given registered app.                If omitted, then no files currently reside on the system.            |
|`spaceAvailable`|Provides the total local space available on SYNC for the registered app.|
|`info`|Provides additional human readable info regarding the result.|


### SetAppIcon
Message Type: **request**

Used to set existing local file on SYNC as the app's icon
            Not supported on first generation SYNC vehicles.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`syncFileName`|File reference name.|


### SetAppIcon
Message Type: **response**

Response is sent, when the file data was copied (success case). Or when an error occured.
            Not supported on First generation SYNC vehicles.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### SetDisplayLayout
Message Type: **request**

Used to set an alternate display layout.
            If not sent, default screen for given platform will be shown
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`displayLayout`|Predefined or dynamically created screen layout.                Currently only predefined screen layouts are defined.            |


### SetDisplayLayout
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`displayCapabilities`|See DisplayCapabilities|
|`buttonCapabilities`|See ButtonCapabilities|
|`softButtonCapabilities`|If returned, the platform supports on-screen SoftButtons; see SoftButtonCapabilities.|
|`presetBankCapabilities`|If returned, the platform supports custom on-screen Presets; see PresetBankCapabilities.|
|`info`|Provides additional human readable info regarding the result.|


### SystemRequest
Message Type: **request**

An asynchronous request from the device; binary data can be included in hybrid part of message for some requests (such as HTTP, Proprietary, or Authentication requests)

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`requestType`|The type of system request.                Note that Proprietary requests should forward the binary data to the known proprietary module on the system.            |
|`fileName`|Filename of HTTP data to store in predefined system staging area.                Mandatory if requestType is HTTP.                PROPRIETARY requestType should ignore this parameter.            |


### SystemRequest
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|


### SendLocation
Message Type: **request**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`longitudeDegrees`||
|`latitudeDegrees`||
|`locationName`|Name / title of intended location            |
|`locationDescription`|Description intended location / establishment (if applicable)            |
|`addressLines`|Location address (if applicable)            |
|`phoneNumber`|Phone number of intended location / establishment (if applicable)            |
|`locationImage`|Image / icon of intended location (if applicable and supported)            |
|`timeStamp`|timestamp in ISO 8601 format            |
|`address`|Address to be used for setting destination|
|`deliveryMode`|Defines the mode of prompt for user|


### SendLocation
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### DialNumber
Message Type: **request**

Dials a phone number and switches to phone application.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`number`|Phone number is a string, which can be up to 40 chars.                All characters shall be stripped from string except digits 0-9 and * # , ; +            |


### DialNumber
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful|
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### SubscribeWayPoints
Message Type: **request**

To subscribe in getting changes for Waypoints/destinations

##### Parameters

| Value | Description | 
| ---------- |:-----------:|


### SubscribeWayPoints
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### GetWayPoints
Message Type: **request**

Request for getting waypoint/destination data.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`wayPointType`|To request for either the destination only or for all waypoints including destination|


### GetWayPoints
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|
|`wayPoints`|See LocationDetails|


### UnsubscribeWayPoints
Message Type: **request**

Request to unsubscribe from WayPoints and Destination

##### Parameters

| Value | Description | 
| ---------- |:-----------:|


### UnsubscribeWayPoints
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|
|`wayPoints`|See LocationDetails|


### OnHMIStatus
Message Type: **notification**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`hmiLevel`|See HMILevel|
|`audioStreamingState`|See AudioStreamingState|
|`systemContext`|See SystemContext|


### OnAppInterfaceUnregistered
Message Type: **notification**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`reason`|See AppInterfaceUnregisteredReason|


### OnButtonEvent
Message Type: **notification**

Notifies application of UP/DOWN events for buttons to which the application is subscribed.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`buttonName`||
|`buttonEventMode`|Indicates whether this is an UP or DOWN event.|
|`customButtonID`|If ButtonName is "CUSTOM_BUTTON", this references the integer ID passed by a custom button. (e.g. softButton ID)|


### OnButtonPress
Message Type: **notification**

Notifies application of LONG/SHORT press events for buttons to which the application is subscribed.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`buttonName`||
|`buttonPressMode`|Indicates whether this is a LONG or SHORT button press event.|
|`customButtonID`|If ButtonName is "CUSTOM_BUTTON", this references the integer ID passed by a custom button. (e.g. softButton ID)|


### OnVehicleData
Message Type: **notification**

Callback for the periodic and non periodic vehicle data read function.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`gps`|See GPSData|
|`speed`|The vehicle speed in kilometers per hour|
|`rpm`|The number of revolutions per minute of the engine|
|`fuelLevel`|The fuel level in the tank (percentage)|
|`fuelLevel_State`|The fuel level state|
|`instantFuelConsumption`|The instantaneous fuel consumption in microlitres|
|`externalTemperature`|The external temperature in degrees celsius|
|`vin`|Vehicle identification number.|
|`prndl`|See PRNDL|
|`tirePressure`|See TireStatus|
|`odometer`|Odometer in km|
|`beltStatus`|The status of the seat belts|
|`bodyInformation`|The body information including power modes|
|`deviceStatus`|The device status including signal and battery strength|
|`driverBraking`|The status of the brake pedal|
|`wiperStatus`|The status of the wipers|
|`headLampStatus`|Status of the head lamps|
|`engineTorque`|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|Current angle of the steering wheel (in deg)|
|`eCallInfo`|Emergency Call notification and confirmation data|
|`airbagStatus`|The status of the air bags|
|`emergencyEvent`|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|The status modes of the cluster|
|`myKey`|Information related to the MyKey feature|


### OnCommand
Message Type: **notification**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`cmdID`|Command ID, which is related to a specific menu entry|
|`triggerSource`|See TriggerSource|


### OnTBTClientState
Message Type: **notification**

Provides applications with notifications specific to the current TBT client status on the module

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`state`|Current State of TBT client|


### OnDriverDistraction
Message Type: **notification**

Provides driver distraction state to mobile applications

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`state`|Current State of Driver Distraction|


### OnPermissionsChange
Message Type: **notification**

Provides update to app of which policy-table-enabled functions are available

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`permissionItem`|Change in permissions for a given set of RPCs|


### OnAudioPassThru
Message Type: **notification**

Binary data is in binary part of hybrid msg

##### Parameters

| Value | Description | 
| ---------- |:-----------:|


### OnLanguageChange
Message Type: **notification**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`language`|Current SYNC voice engine (VR+TTS) language|
|`hmiDisplayLanguage`|Current display language|


### OnKeyboardInput
Message Type: **notification**

On-screen keyboard event.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`event`|On-screen keyboard input data.|
|`data`|On-screen keyboard input data.|


### OnTouchEvent
Message Type: **notification**

Notifies about touch events on the screen's prescribed area

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`type`|The type of touch event.|
|`event`|List of all individual touches involved in this event.|


### OnSystemRequest
Message Type: **notification**

An asynchronous request from the system for specific data from the device or the cloud or response to a request from the device or cloud
            Binary data can be included in hybrid part of message for some requests (such as Authentication request responses)
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`requestType`|The type of system request.|
|`url`|Optional URL for HTTP requests.                If blank, the binary data shall be forwarded to the app.                If not blank, the binary data shall be forwarded to the url with a provided timeout in seconds.            |
|`timeout`|Optional timeout for HTTP requests                Required if a URL is provided            |
|`fileType`|Optional file type (meant for HTTP file requests).|
|`offset`|Optional offset in bytes for resuming partial data chunks|
|`length`|Optional length in bytes for resuming partial data chunks|


### OnHashChange
Message Type: **notification**

Notification containing an updated hashID which can be used over connection cycles (i.e. loss of connection, ignition cycles, etc.).
            Sent after initial registration and subsequently after any change in the calculated hash of all persisted app data.
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`hashID`|Calculated hash ID to be referenced during RegisterAppInterface.|


### OnWayPointChange
Message Type: **notification**

Notification which provides the entire LocationDetails when there is a change to any waypoints or destination.

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`wayPoints`|See LocationDetails|


### EncodedSyncPData
Message Type: **request**

Allows encoded data in the form of SyncP packets to be sent to the SYNC module.
            Legacy / v1 Protocol implementation; use SyncPData instead.
            *** DEPRECATED ***
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`data`|Contains base64 encoded string of SyncP packets.|


### EncodedSyncPData
Message Type: **response**

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`success`|true, if successful; false, if failed |
|`resultCode`|See Result|
|`info`|Provides additional human readable info regarding the result.|


### OnEncodedSyncPData
Message Type: **notification**

Callback including encoded data of any SyncP packets that SYNC needs to send back to the mobile device.
            Legacy / v1 Protocol implementation; responds to EncodedSyncPData.
            *** DEPRECATED ***
        

##### Parameters

| Value | Description | 
| ---------- |:-----------:|
|`data`|Contains base64 encoded string of SyncP packets.|
|`URL`|If blank, the SyncP data shall be forwarded to the app.                If not blank, the SyncP data shall be forwarded to the provided URL.            |
|`Timeout`|If blank, the SyncP data shall be forwarded to the app.                If not blank, the SyncP data shall be forwarded with the provided timeout in seconds.            |


