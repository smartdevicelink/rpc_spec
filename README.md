# SmartDeviceLink
# RPC Spec

###### Version: 5.1.0

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
|`TOO_MANY_PENDING_REQUESTS`|There are too many requests pending (means, that the response has not been delivered, yet).There may be a maximum of 1000 pending requests at a time.|
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
|`DATA_NOT_AVAILABLE`|The requested information is currently not available. This is different than UNSUPPORTED_RESOURCE because it implies the data is at some point available. |
|`READ_ONLY`|The value being set is read only|
|`CORRUPTED_DATA`|The data sent failed to pass CRC check in receiver end|


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
|`BOTH`|This mode causes both a VR and display selection option for an interaction. The user will first be asked via Voice Interaction (if available). If this is unsuccessful, the system will switch to manual input.|


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
Enumeration that describes current levels of HMI.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`FULL`||
|`LIMITED`||
|`BACKGROUND`||
|`NONE`||


### AudioStreamingState
Enumeration that describes possible states of audio streaming.

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


### VideoStreamingState
Enumeration that describes possible states of video streaming. 

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`STREAMABLE`||
|`NOT_STREAMABLE`||


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
|`FILE`||


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
|`8KHZ`|Sampling rate of 8000 Hz.|
|`16KHZ`|Sampling rate of 16000 Hz.|
|`22KHZ`|Sampling rate of 22050 Hz.|
|`44KHZ`|Sampling rate of 44100 Hz.|


### BitsPerSample
Describes different quality options for PerformAudioPassThru.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`8_BIT`|Audio sample is 8 bits wide, unsigned.|
|`16_BIT`|Audio sample is 16 bits wide, signed, and in little endian.|


### AudioType
Describes different audio type options for PerformAudioPassThru.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`PCM`|Linear PCM.|


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
|`VEHICLEDATA_TURNSIGNAL`||
|`VEHICLEDATA_FUELRANGE`||
|`VEHICLEDATA_ENGINEOILLIFE`||
|`VEHICLEDATA_ELECTRONICPARKBRAKESTATUS`||
|`VEHICLEDATA_CLOUDAPPVEHICLEID`||
|`VEHICLEDATA_OEM_CUSTOM_DATA`||


### HybridAppPreference
Enumeration for the user's preference of which app type to use when both are available

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`MOBILE`||
|`CLOUD`||
|`BOTH`||


### ButtonName
Defines the hard (physical) and soft (touchscreen) buttons available from the module

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`OK`||
|`PLAY_PAUSE`|The button name for the physical Play/Pause              toggle that can be used by media apps.            |
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


### DisplayType

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
|`templateTitle`|The title of the new template that will be displayed; applies to "Show"|
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
|`graphic`|The primary image field for Show|
|`secondaryGraphic`|The secondary image field for Show|
|`showConstantTBTIcon`|The primary image field for ShowConstantTBT|
|`showConstantTBTNextTurnIcon`|The secondary image field for ShowConstantTBT|
|`locationImage`|The optional image of a destination / location|
|`alertIcon`|The image field for Alert|


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
Enumeration that describes possible states of turn-by-turn client or SmartDeviceLink app.

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


### AudioStreamingIndicator
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`PLAY_PAUSE`|Default playback indicator.                By default the playback indicator should be PLAY_PAUSE when:                    - the media app is newly registered on the head unit (after RegisterAppInterface)                    - the media app was closed by the user (App enters HMI_NONE)                    - the app sends SetMediaClockTimer with audioStreamingIndicator not set to any value            |
|`PLAY`|Indicates that a button press of the Play/Pause button starts the audio playback.|
|`PAUSE`|Indicates that a button press of the Play/Pause button pauses the current audio playback.|
|`STOP`|Indicates that a button press of the Play/Pause button stops the current audio playback.|


### GlobalProperty
The different global properties.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`USER_LOCATION`|Location of the user's seat of setGlobalProperties|
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
|`2D`|Longitude and latitude|
|`3D`|Longitude and latitude and altitude|


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


### TPMS
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`UNKNOWN`|If set the status of the tire is not known.|
|`SYSTEM_FAULT`|TPMS does not function.|
|`SENSOR_FAULT`|The sensor of the tire does not function.|
|`LOW`|TPMS is reporting a low tire pressure for the tire.|
|`SYSTEM_ACTIVE`|TPMS is active and the tire pressure is monitored.|
|`TRAIN`|TPMS is reporting that the tire must be trained.|
|`TRAINING_COMPLETE`|TPMS reports the training for the tire is completed.|
|`NOT_TRAINED`|TPMS reports the tire is not trained.|


### FuelType
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`GASOLINE`||
|`DIESEL`||
|`CNG`|For vehicles using compressed natural gas.            |
|`LPG`|For vehicles using liquefied petroleum gas.            |
|`HYDROGEN`|For FCEV (fuel cell electric vehicle).|
|`BATTERY`|For BEV (Battery Electric Vehicle), PHEV (Plug-in Hybrid Electric Vehicle), solar vehicles and other vehicles which run on a battery.|


### ElectronicParkBrakeStatus
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`CLOSED`|Park brake actuators have been fully applied.        |
|`TRANSITION`|Park brake actuators are transitioning to either Apply/Closed or Release/Open state.        |
|`OPEN`|Park brake actuators are released.        |
|`DRIVE_ACTIVE`|When driver pulls the Electronic Park Brake switch while driving "at speed".        |
|`FAULT`|When system has a fault or is under maintenance.        |


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
|`CD`||
|`USB`||
|`USB2`||
|`BLUETOOTH_STEREO_BTST`||
|`LINE_IN`||
|`IPOD`||
|`MOBILE_APP`||
|`AM`||
|`FM`||
|`XM`||
|`DAB`||


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


### ModuleType
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`CLIMATE`||
|`RADIO`||
|`SEAT`||
|`AUDIO`||
|`LIGHT`||
|`HMI_SETTINGS`||


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


### TurnSignal
Enumeration that describes the status of the turn light indicator.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`OFF`|Turn signal is OFF|
|`LEFT`|Left turn signal is on|
|`RIGHT`|Right turn signal is on|
|`BOTH`|Both signals (left and right) are on.|


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
|`OEM_SPECIFIC`||
|`ICON_URL`||


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
|`DEFAULT`|Default media / non-media screen.                Can be set as a root screen.            |
|`MEDIA`|Default Media screen.                Can be set as a root screen.            |
|`NON-MEDIA`|Default Non-media screen.                Can be set as a root screen.            |
|`ONSCREEN_PRESETS`|Custom root media screen containing app-defined onscreen presets.                Can be set as a root screen.            |
|`NAV_FULLSCREEN_MAP`|Custom root template screen containing full screen map with navigation controls.                Can be set as a root screen.            |
|`NAV_LIST`|Custom root template screen containing video represented list.                Can be set as a root screen.            |
|`NAV_KEYBOARD`|Custom root template screen containing video represented keyboard.                Can be set as a root screen.            |
|`GRAPHIC_WITH_TEXT`|Custom root template screen containing half-screen graphic with lines of text.                Can be set as a root screen.            |
|`TEXT_WITH_GRAPHIC`|Custom root template screen containing lines of text with half-screen graphic.                Can be set as a root screen.            |
|`TILES_ONLY`|Custom root template screen containing only tiled SoftButtons.                Can be set as a root screen.            |
|`TEXTBUTTONS_ONLY`|Custom root template screen containing only text SoftButtons.                Can be set as a root screen.            |
|`GRAPHIC_WITH_TILES`|Custom root template screen containing half-screen graphic with tiled SoftButtons.                Can be set as a root screen.            |
|`TILES_WITH_GRAPHIC`|Custom root template screen containing tiled SoftButtons with half-screen graphic.                Can be set as a root screen.            |
|`GRAPHIC_WITH_TEXT_AND_SOFTBUTTONS`|Custom root template screen containing half-screen graphic with text and SoftButtons.                Can be set as a root screen.            |
|`TEXT_AND_SOFTBUTTONS_WITH_GRAPHIC`|Custom root template screen containing text and SoftButtons with half-screen graphic.                Can be set as a root screen.            |
|`GRAPHIC_WITH_TEXTBUTTONS`|Custom root template screen containing half-screen graphic with text only SoftButtons.                Can be set as a root screen.            |
|`TEXTBUTTONS_WITH_GRAPHIC`|Custom root template screen containing text only SoftButtons with half-screen graphic.                Can be set as a root screen.            |
|`LARGE_GRAPHIC_WITH_SOFTBUTTONS`|Custom root template screen containing a large graphic and SoftButtons.                Can be set as a root screen.            |
|`DOUBLE_GRAPHIC_WITH_SOFTBUTTONS`|Custom root template screen containing two graphics and SoftButtons.                Can be set as a root screen.            |
|`LARGE_GRAPHIC_ONLY`|Custom root template screen containing only a large graphic.                Can be set as a root screen.            |


### WindowType
Enumeration listing possible window types.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`MAIN`|This window type describes the main screen on a display.|
|`WIDGET`|A widget is a small window that the app can create to provide information and softbuttons for a quick app control.|

### PredefinedWindows

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`DEFAULT_WINDOW`|The default window is a main window pre-created on behalf of the app.|
|`PRIMARY_WIDGET`|The primary widget of the app.|

### FunctionID
Enumeration linking function names with function IDs in SmartDeviceLink protocol. Assumes enumeration starts at value 0.

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
|`SetCloudAppPropertiesID`||
|`GetCloudAppPropertiesID`||
|`PublishAppServiceID`||
|`GetAppServiceDataID`||
|`GetFileID`||
|`PerformAppServiceInteractionID`||
|`CloseApplicationID`||
|`CancelInteractionID`||
|`ShowAppMenuID`||
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
|`OnRCStatusID`||
|`OnAppServiceDataID`||
|`OnSystemCapabilityUpdatedID`||
|`EncodedSyncPDataID`||
|`SyncPDataID`||
|`OnEncodedSyncPDataID`||
|`OnSyncPDataID`||
|`CreateWindowID`||
|`DeleteWindowID`||
|`GetInteriorVehicleDataConsentID`||
|`ReleaseInteriorVehicleDataModuleID`||

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
|`APP_SERVICES`||
|`DISPLAYS`||


### MassageZone
List possible zones of a multi-contour massage seat.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`LUMBAR`|The back of a multi-contour massage seat. or SEAT_BACK|
|`SEAT_CUSHION`|The bottom a multi-contour massage seat. or SEAT_BOTTOM |


### MassageMode
List possible modes of a massage zone.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`OFF`||
|`LOW`||
|`HIGH`||


### MassageCushion
List possible cushions of a multi-contour massage seat.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`TOP_LUMBAR`||
|`MIDDLE_LUMBAR`||
|`BOTTOM_LUMBAR`||
|`BACK_BOLSTERS`||
|`SEAT_BOLSTERS`||


### SeatMemoryActionType
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`SAVE`|Save current seat postions and settings to seat memory.|
|`RESTORE`|Restore / apply the seat memory settings to the current seat. |
|`NONE`|No action to be performed.|


### SupportedSeat
List possible seats that is a remote controllable seat.

##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`DRIVER`||
|`FRONT_PASSENGER`||


### LightName
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`FRONT_LEFT_HIGH_BEAM`||
|`FRONT_RIGHT_HIGH_BEAM`||
|`FRONT_LEFT_LOW_BEAM`||
|`FRONT_RIGHT_LOW_BEAM`||
|`FRONT_LEFT_PARKING_LIGHT`||
|`FRONT_RIGHT_PARKING_LIGHT`||
|`FRONT_LEFT_FOG_LIGHT`||
|`FRONT_RIGHT_FOG_LIGHT`||
|`FRONT_LEFT_DAYTIME_RUNNING_LIGHT`||
|`FRONT_RIGHT_DAYTIME_RUNNING_LIGHT`||
|`FRONT_LEFT_TURN_LIGHT`||
|`FRONT_RIGHT_TURN_LIGHT`||
|`REAR_LEFT_FOG_LIGHT`||
|`REAR_RIGHT_FOG_LIGHT`||
|`REAR_LEFT_TAIL_LIGHT`||
|`REAR_RIGHT_TAIL_LIGHT`||
|`REAR_LEFT_BRAKE_LIGHT`||
|`REAR_RIGHT_BRAKE_LIGHT`||
|`REAR_LEFT_TURN_LIGHT`||
|`REAR_RIGHT_TURN_LIGHT`||
|`REAR_REGISTRATION_PLATE_LIGHT`||
|`HIGH_BEAMS`|Include all high beam lights: front_left and front_right.|
|`LOW_BEAMS`|Include all low beam lights: front_left and front_right.|
|`FOG_LIGHTS`|Include all fog lights: front_left, front_right, rear_left and rear_right.|
|`RUNNING_LIGHTS`|Include all daytime running lights: front_left and front_right.|
|`PARKING_LIGHTS`|Include all parking lights: front_left and front_right.|
|`BRAKE_LIGHTS`|Include all brake lights: rear_left and rear_right.|
|`REAR_REVERSING_LIGHTS`||
|`SIDE_MARKER_LIGHTS`||
|`LEFT_TURN_LIGHTS`|Include all left turn signal lights: front_left, rear_left, left_side and mirror_mounted.|
|`RIGHT_TURN_LIGHTS`|Include all right turn signal lights: front_right, rear_right, right_side and mirror_mounted.|
|`HAZARD_LIGHTS`|Include all hazard lights: front_left, front_right, rear_left and rear_right.|
|`REAR_CARGO_LIGHTS`|Cargo lamps illuminate the cargo area.|
|`REAR_TRUCK_BED_LIGHTS`|Truck bed lamps light up the bed of the truck.|
|`REAR_TRAILER_LIGHTS`|Trailer lights are lamps mounted on a trailer hitch.|
|`LEFT_SPOT_LIGHTS`|It is the spotlights mounted on the left side of a vehicle.|
|`RIGHT_SPOT_LIGHTS`|It is the spotlights mounted on the right side of a vehicle.|
|`LEFT_PUDDLE_LIGHTS`|Puddle lamps illuminate the ground beside the door as the customer is opening or approaching the door.|
|`RIGHT_PUDDLE_LIGHTS`|Puddle lamps illuminate the ground beside the door as the customer is opening or approaching the door.|
|`AMBIENT_LIGHTS`||
|`OVERHEAD_LIGHTS`||
|`READING_LIGHTS`||
|`TRUNK_LIGHTS`||
|`EXTERIOR_FRONT_LIGHTS`|Include exterior lights located in front of the vehicle. For example, fog lights and low beams.|
|`EXTERIOR_REAR_LIGHTS`|Include exterior lights located at the back of the vehicle. For example, license plate lights, reverse lights, cargo lights, bed lights and trailer assist lights.|
|`EXTERIOR_LEFT_LIGHTS`|Include exterior lights located at the left side of the vehicle. For example, left puddle lights and spot lights.|
|`EXTERIOR_RIGHT_LIGHTS`|Include exterior lights located at the right side of the vehicle. For example, right puddle lights and spot lights.|
|`EXTERIOR_ALL_LIGHTS`|Include all exterior lights around the vehicle.|


### LightStatus
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`ON`||
|`OFF`||
|`RAMP_UP`||
|`RAMP_DOWN`||
|`UNKNOWN`||
|`INVALID`||


### DisplayMode
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`DAY`||
|`NIGHT`||
|`AUTO`||


### DistanceUnit
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`MILES`||
|`KILOMETERS`||


### MetadataType
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


### AppServiceType
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`MEDIA`||
|`WEATHER`||
|`NAVIGATION`||


### MediaType
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`MUSIC`||
|`PODCAST`||
|`AUDIOBOOK`||
|`OTHER`||


### NavigationAction
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`TURN`|Using this action plus a supplied direction can give the type of turn. |
|`EXIT`||
|`STAY`||
|`MERGE`||
|`FERRY`||
|`CAR_SHUTTLE_TRAIN`||
|`WAYPOINT`||


### NavigationJunction
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`REGULAR`|A junction that represents a standard intersection with a single road crossing another. |
|`BIFURCATION`|A junction where the road splits off into two paths; a fork in the road. |
|`MULTI_CARRIAGEWAY`|A junction that has multiple intersections and paths. |
|`ROUNDABOUT`|A junction where traffic moves in a single direction around a central, non-traversable point to reach one of the connecting roads. |
|`TRAVERSABLE_ROUNDABOUT`|Similar to a roundabout, however the center of the roundabout is fully traversable. Also known as a mini-roundabout. |
|`JUGHANDLE`|A junction where lefts diverge to the right, then curve to the left, converting a left turn to a crossing maneuver. |
|`ALL_WAY_YIELD`|Multiple way intersection that allows traffic to flow based on priority; most commonly right of way and first in, first out. |
|`TURN_AROUND`|A junction designated for traffic turn arounds. |


### Direction
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`LEFT`||
|`RIGHT`||


### ServiceUpdateReason
##### Elements

| Value | Description | 
| ---------- |:-----------:|
|`PUBLISHED`|The service has just been published with the module and once activated to the primary service of its type, it will be ready for possible consumption.|
|`REMOVED`|The service has just been unpublished with the module and is no longer accessible|
|`ACTIVATED`|The service is activated as the primary service of this type. All requests dealing with this service type will be handled by this service.|
|`DEACTIVATED`|The service has been deactivated as the primary service of its type|
|`MANIFEST_UPDATE`|The service has updated its manifest. This could imply updated capabilities|



<div style="page-break-after: always;"></div>

## Structs

### AudioPassThruCapabilities
Describes different audio type configurations for PerformAudioPassThru.
            e.g. {8kHz,8-bit,PCM}
            The audio is recorded in monaural.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`samplingRate`|SamplingRate|True||
|`bitsPerSample`|BitsPerSample|True||
|`audioType`|AudioType|True||


### CloudAppProperties
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`nicknames`|String[]|False|An array of app names a cloud app is allowed to register with. If included in a SetCloudAppProperties request, this value will overwrite the existing "nicknames" field in the app policies section of the policy table.|
|`appID`|String|True||
|`enabled`|Boolean|False|If true, cloud app will be included in HMI RPC UpdateAppList|
|`authToken`|String|False|Used to authenticate websocket connection on app activation|
|`cloudTransportType`|String|False|Specifies the connection type Core should use|
|`hybridAppPreference`|HybridAppPreference|False|Specifies the user preference to use the cloud app version or mobile app version when both are available|
|`endpoint`|String|False|Specifies the endpoint which Core will attempt to connect to when this app is selected|


### Image
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`value`|String|True|Either the static hex icon value or the binary image file name identifier (sent by PutFile).|
|`imageType`|ImageType|True|Describes, whether it is a static or dynamic image.|
|`isTemplate`|Boolean|False|If true, the image is a template image and can be recolored by the HMI|


### SoftButton
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`type`|SoftButtonType|True|Describes, whether it is text, highlighted text, icon, or dynamic image. See softButtonType|
|`text`|String|False|Optional text to display (if defined as TEXT or BOTH)|
|`image`|Image|False|Optional image struct for SoftButton (if defined as IMAGE or BOTH)|
|`isHighlighted`|Boolean|False|True, if highlighted                False, if not highlighted            |
|`softButtonID`|Integer|True|Value which is returned via OnButtonPress / OnButtonEvent|
|`systemAction`|SystemAction|False|Parameter indicating whether selecting a SoftButton shall call a specific system action.  This is intended to allow Notifications to bring the callee into full / focus; or in the case of persistent overlays, the overlay can persist when a SoftButton is pressed.|


### Choice
A choice is an option given to the user, which can be selected either by menu, or through voice recognition system.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`choiceID`|Integer|True||
|`menuName`|String|True||
|`vrCommands`|String[]|False||
|`image`|Image|False||
|`secondaryText`|String|False|Optional secondary text to display; e.g. address of POI in a search result entry|
|`tertiaryText`|String|False|Optional tertiary text to display; e.g. distance to POI for a search result entry|
|`secondaryImage`|Image|False|Optional secondary image struct for choice|


### VrHelpItem
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`text`|String|True|Text to display for VR Help item|
|`image`|Image|False|Image struct for VR Help item|
|`position`|Integer|True|Position to display item in VR Help list|


### SyncMsgVersion
Specifies the version number of the SmartDeviceLink protocol that is supported by the mobile application

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`majorVersion`|Integer|True|The major version indicates versions that is not-compatible to previous versions.|
|`minorVersion`|Integer|True|The minor version indicates a change to a previous version that should still allow to be run on an older version (with limited functionality)|
|`patchVersion`|Integer|False|The patch version indicates a fix to existing functionality in a previous version that should still be able to be run on an older version |


### FuelRange
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`type`|FuelType|False||
|`range`|Float|False|The estimate range in KM the vehicle can travel based on fuel level and consumption.            |


### SingleTireStatus
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`status`|ComponentVolumeStatus|True|See ComponentVolumeStatus.|
|`tpms`|TPMS|False|The status of TPMS according to the particular tire.            |
|`pressure`|Float|False|The pressure value of the particular tire in kilo pascal.|


### BeltStatus
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`driverBeltDeployed`|VehicleDataEventStatus|True|References signal "VedsDrvBelt_D_Ltchd". See VehicleDataEventStatus.|
|`passengerBeltDeployed`|VehicleDataEventStatus|True|References signal "VedsPasBelt_D_Ltchd". See VehicleDataEventStatus.|
|`passengerBuckleBelted`|VehicleDataEventStatus|True|References signal "VedsRw1PasBckl_D_Ltchd". See VehicleDataEventStatus.|
|`driverBuckleBelted`|VehicleDataEventStatus|True|References signal "VedsRw1DrvBckl_D_Ltchd". See VehicleDataEventStatus.|
|`leftRow2BuckleBelted`|VehicleDataEventStatus|True|References signal "VedsRw2lBckl_D_Ltchd". See VehicleDataEventStatus.|
|`passengerChildDetected`|VehicleDataEventStatus|True|References signal "VedsRw1PasChld_D_Ltchd". See VehicleDataEventStatus.|
|`rightRow2BuckleBelted`|VehicleDataEventStatus|True|References signal "VedsRw2rBckl_D_Ltchd". See VehicleDataEventStatus.|
|`middleRow2BuckleBelted`|VehicleDataEventStatus|True|References signal "VedsRw2mBckl_D_Ltchd". See VehicleDataEventStatus.|
|`middleRow3BuckleBelted`|VehicleDataEventStatus|True|References signal "VedsRw3mBckl_D_Ltchd". See VehicleDataEventStatus.|
|`leftRow3BuckleBelted`|VehicleDataEventStatus|True|References signal "VedsRw3lBckl_D_Ltchd". See VehicleDataEventStatus.|
|`rightRow3BuckleBelted`|VehicleDataEventStatus|True|References signal "VedsRw3rBckl_D_Ltchd". See VehicleDataEventStatus.|
|`leftRearInflatableBelted`|VehicleDataEventStatus|True|References signal "VedsRw2lRib_D_Ltchd". See VehicleDataEventStatus.|
|`rightRearInflatableBelted`|VehicleDataEventStatus|True|References signal "VedsRw2rRib_D_Ltchd". See VehicleDataEventStatus.|
|`middleRow1BeltDeployed`|VehicleDataEventStatus|True|References signal "VedsRw1mBelt_D_Ltchd". See VehicleDataEventStatus.|
|`middleRow1BuckleBelted`|VehicleDataEventStatus|True|References signal "VedsRw1mBckl_D_Ltchd". See VehicleDataEventStatus.|


### BodyInformation
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`parkBrakeActive`|Boolean|True|References signal "PrkBrkActv_B_Actl".|
|`ignitionStableStatus`|IgnitionStableStatus|True|References signal "Ignition_Switch_Stable". See IgnitionStableStatus.|
|`ignitionStatus`|IgnitionStatus|True|References signal "Ignition_status". See IgnitionStatus.|
|`driverDoorAjar`|Boolean|False|References signal "DrStatDrv_B_Actl".|
|`passengerDoorAjar`|Boolean|False|References signal "DrStatPsngr_B_Actl".|
|`rearLeftDoorAjar`|Boolean|False|References signal "DrStatRl_B_Actl".|
|`rearRightDoorAjar`|Boolean|False|References signal "DrStatRr_B_Actl".|


### DeviceStatus
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`voiceRecOn`|Boolean|True|References signal "CPM_VoiceRec_STAT".|
|`btIconOn`|Boolean|True|References signal "BT_ICON".|
|`callActive`|Boolean|True|References signal "CPM_Call_Active_STAT".|
|`phoneRoaming`|Boolean|True|References signal "CPM_Phone_Roaming_STAT".|
|`textMsgAvailable`|Boolean|True|References signal "CPM_TextMsg_AVAL".|
|`battLevelStatus`|DeviceLevelStatus|True|Device battery level status.  References signal "CPM_Batt_Level_STAT". See DeviceLevelStatus.|
|`stereoAudioOutputMuted`|Boolean|True|References signal "CPM_Stereo_Audio_Output".|
|`monoAudioOutputMuted`|Boolean|True|References signal "CPM_Mono_Audio_Output".|
|`signalLevelStatus`|DeviceLevelStatus|True|Device signal level status.  References signal "CPM_Signal_Strength_STAT". See DeviceLevelStatus.|
|`primaryAudioSource`|PrimaryAudioSource|True|References signal "CPM_Stereo_PAS_Source". See PrimaryAudioSource.|
|`eCallEventActive`|Boolean|True|References signal "eCall_Event".|


### HeadLampStatus
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`lowBeamsOn`|Boolean|True|Status of the low beam lamps.  References signal "HeadLampLoActv_B_Stat".|
|`highBeamsOn`|Boolean|True|Status of the high beam lamps.  References signal "HeadLghtHiOn_B_Stat".|
|`ambientLightSensorStatus`|AmbientLightStatus|False|Status of the ambient light sensor.|


### AppInfo
Contains detailed information about the registered application.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`appDisplayName`|String|True|The name displayed for the mobile application on the mobile device (can differ from the app name set in the initial RAI request).|
|`appBundleID`|String|True|The AppBundleID of an iOS application or package name of the Android application. This supports App Launch strategies for each platform.|
|`appVersion`|String|True|Represents the build version number of this particular mobile app.|
|`appIcon`|String|False|A file reference to the icon utilized by this app (simplifies the process of setting an app icon during app registration).|


### ECallInfo
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`eCallNotificationStatus`|VehicleDataNotificationStatus|True|References signal "eCallNotification_4A". See VehicleDataNotificationStatus.|
|`auxECallNotificationStatus`|VehicleDataNotificationStatus|True|References signal "eCallNotification". See VehicleDataNotificationStatus.|
|`eCallConfirmationStatus`|ECallConfirmationStatus|True|References signal "eCallConfirmation". See ECallConfirmationStatus.|


### AirbagStatus
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`driverAirbagDeployed`|VehicleDataEventStatus|True|References signal "VedsDrvBag_D_Ltchd". See VehicleDataEventStatus.|
|`driverSideAirbagDeployed`|VehicleDataEventStatus|True|References signal "VedsDrvSideBag_D_Ltchd". See VehicleDataEventStatus.|
|`driverCurtainAirbagDeployed`|VehicleDataEventStatus|True|References signal "VedsDrvCrtnBag_D_Ltchd". See VehicleDataEventStatus.|
|`passengerAirbagDeployed`|VehicleDataEventStatus|True|References signal "VedsPasBag_D_Ltchd". See VehicleDataEventStatus.|
|`passengerCurtainAirbagDeployed`|VehicleDataEventStatus|True|References signal "VedsPasCrtnBag_D_Ltchd". See VehicleDataEventStatus.|
|`driverKneeAirbagDeployed`|VehicleDataEventStatus|True|References signal "VedsKneeDrvBag_D_Ltchd". See VehicleDataEventStatus.|
|`passengerSideAirbagDeployed`|VehicleDataEventStatus|True|References signal "VedsPasSideBag_D_Ltchd". See VehicleDataEventStatus.|
|`passengerKneeAirbagDeployed`|VehicleDataEventStatus|True|References signal "VedsKneePasBag_D_Ltchd". See VehicleDataEventStatus.|


### EmergencyEvent
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`emergencyEventType`|EmergencyEventType|True|References signal "VedsEvntType_D_Ltchd". See EmergencyEventType.|
|`fuelCutoffStatus`|FuelCutoffStatus|True|References signal "RCM_FuelCutoff". See FuelCutoffStatus.|
|`rolloverEvent`|VehicleDataEventStatus|True|References signal "VedsEvntRoll_D_Ltchd". See VehicleDataEventStatus.|
|`maximumChangeVelocity`|Integer|True|References signal "VedsMaxDeltaV_D_Ltchd". Change in velocity in KPH.  Additional reserved values:                0x00 No event                0xFE Not supported                0xFF Fault            |
|`multipleEvents`|VehicleDataEventStatus|True|References signal "VedsMultiEvnt_D_Ltchd". See VehicleDataEventStatus.|


### ClusterModeStatus
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`powerModeActive`|Boolean|True|References signal "PowerMode_UB".|
|`powerModeQualificationStatus`|PowerModeQualificationStatus|True|References signal "PowerModeQF". See PowerModeQualificationStatus.|
|`carModeStatus`|CarModeStatus|True|References signal "CarMode". See CarMode.|
|`powerModeStatus`|PowerModeStatus|True|References signal "PowerMode". See PowerMode.|


### MyKey
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`e911Override`|VehicleDataStatus|True|Indicates whether e911 override is on.  References signal "MyKey_e911Override_St". See VehicleDataStatus.|


### TireStatus
The status and pressure of the tires.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`pressureTelltale`|WarningLightStatus|True|Status of the Tire Pressure Telltale. See WarningLightStatus.|
|`leftFront`|SingleTireStatus|True|The status of the left front tire.|
|`rightFront`|SingleTireStatus|True|The status of the right front tire.|
|`leftRear`|SingleTireStatus|True|The status of the left rear tire.|
|`rightRear`|SingleTireStatus|True|The status of the right rear tire.|
|`innerLeftRear`|SingleTireStatus|True|The status of the inner left rear.|
|`innerRightRear`|SingleTireStatus|True|The status of the inner right rear.|


### GPSData
Struct with the GPS data.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`longitudeDegrees`|Float|True||
|`latitudeDegrees`|Float|True||
|`utcYear`|Integer|False|The current UTC year.|
|`utcMonth`|Integer|False|The current UTC month.|
|`utcDay`|Integer|False|The current UTC day.|
|`utcHours`|Integer|False|The current UTC hour.|
|`utcMinutes`|Integer|False|The current UTC minute.|
|`utcSeconds`|Integer|False|The current UTC second.|
|`compassDirection`|CompassDirection|False|See CompassDirection.|
|`pdop`|Float|False|PDOP.  If undefined or unavailable, then value shall be set to 0.|
|`hdop`|Float|False|HDOP.  If value is unknown, value shall be set to 0.|
|`vdop`|Float|False|VDOP.  If value is unknown, value shall be set to 0.|
|`actual`|Boolean|False|True, if actual.                False, if inferred.            |
|`satellites`|Integer|False|Number of satellites in view|
|`dimension`|Dimension|False|See Dimension|
|`altitude`|Float|False|Altitude in meters|
|`heading`|Float|False|The heading. North is 0. Resolution is 0.01|
|`speed`|Float|False|The speed in KPH|
|`shifted`|Boolean|False|True, if GPS lat/long, time, and altitude have been purposefully shifted (requires a proprietary algorithm to unshift).                False, if the GPS data is raw and un-shifted.                If not provided, then value is assumed False.            |


### VehicleDataResult
Individual published data request result

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`dataType`|VehicleDataType|True|Defined published data element type.|
|`resultCode`|VehicleDataResultCode|True|Published data result code.|
|`oemCustomDataType`|String|False|Type of requested oem specific parameter |


### DIDResult
Individual requested DID result and data

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`resultCode`|VehicleDataResultCode|True|Individual DID result code.|
|`didLocation`|Integer|True|Location of raw data from vehicle data DID|
|`data`|String|False|Raw DID-based data returned for requested element.|


### StartTime
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`hours`|Integer|True|The hour of the media clock.                Some radios only support a max of 19 hours. If out of range, it will be rejected.            |
|`minutes`|Integer|True||
|`seconds`|Integer|True||


### TextField
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`name`|TextFieldName|True|The name that identifies the field. See TextFieldName.|
|`characterSet`|CharacterSet|True|The character set that is supported in this field. See CharacterSet.|
|`width`|Integer|True|The number of characters in one row of this field.|
|`rows`|Integer|True|The number of rows of this field.|


### ImageResolution
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`resolutionWidth`|Integer|True|The image resolution width.|
|`resolutionHeight`|Integer|True|The image resolution height.|


### ImageField
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`name`|ImageFieldName|True|The name that identifies the field. See ImageFieldName.|
|`imageTypeSupported`|FileType[]|True|The image types that are supported in this field. See FileType.|
|`imageResolution`|ImageResolution|False|The image resolution of this field.|


### TouchCoord
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`x`|Integer|True|The x coordinate of the touch.|
|`y`|Integer|True|The y coordinate of the touch.|


### TouchEvent
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`id`|Integer|True|A touch's unique identifier.  The application can track the current touch events by id.                If a touch event has type begin, the id should be added to the set of touches.                If a touch event has type end, the id should be removed from the set of touches.            |
|`ts`|Integer[]|True|The time that the touch was recorded.  This number can the time since the beginning of the session or something else as long as the units are in milliseconds.                The timestamp is used to determined the rate of change of position of a touch.                The application also uses the time to verify whether two touches, with different ids, are part of a single action by the user.                If there is only a single timestamp in this array, it is the same for every coordinate in the coordinates array.            |
|`c`|TouchCoord[]|True||


### TouchEventCapabilities
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`pressAvailable`|Boolean|True||
|`multiTouchAvailable`|Boolean|True||
|`doublePressAvailable`|Boolean|True||


### ScreenParams
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`resolution`|ImageResolution|True|The resolution of the prescribed screen area.|
|`touchEventAvailable`|TouchEventCapabilities|False|Types of screen touch events available in screen area.|


### HMIPermissions
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`allowed`|HMILevel[]|True|A set of all HMI levels that are permitted for this given RPC.|
|`userDisallowed`|HMILevel[]|True|A set of all HMI levels that are prohibited for this given RPC.|


### ParameterPermissions
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`allowed`|String[]|True|A set of all parameters that are permitted for this given RPC.|
|`userDisallowed`|String[]|True|A set of all parameters that are prohibited for this given RPC.|


### PermissionItem
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`rpcName`|String|True|Name of the individual RPC in the policy table.|
|`hmiPermissions`|HMIPermissions|True||
|`parameterPermissions`|ParameterPermissions|True||


### DisplayCapabilities
Contains information about the display capabilities.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`displayType`|DisplayType|True|The type of the display. See DisplayType|
|`displayName`|String|False|The name of the display the app is connected to.|
|`textFields`|TextField[]|True|A set of all fields that support text data. See TextField|
|`imageFields`|ImageField[]|False|A set of all fields that support images. See ImageField|
|`mediaClockFormats`|MediaClockFormat[]|True|A set of all supported formats of the media clock. See MediaClockFormat|
|`graphicSupported`|Boolean|True|The display's persistent screen supports referencing a static or dynamic image.|
|`templatesAvailable`|String[]|False|A set of all predefined persistent display templates available on headunit.  To be referenced in SetDisplayLayout.|
|`screenParams`|ScreenParams|False|A set of all parameters related to a prescribed screen area (e.g. for video / touch input).|
|`numCustomPresetsAvailable`|Integer|False|The number of on-screen custom presets available (if any); otherwise omitted.|

### Grid
Describes a location (origin coordinates and span) of a vehicle component.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`col`|Integer|True|
|`row`|Integer|True|
|`level`|Integer|False|
|`colspan`|Integer|False|
|`rowspan`|Integer|False|
|`levelspan`|Integer|False|

### ModuleInfo
Information about a RC module.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleId`|String|True|uuid of a module. "moduleId + moduleType" uniquely identify a module.|
|`location`|Grid|False|Location of a module.|
|`serviceArea`|Grid|False|Service area of a module.|
|`allowMultipleAccess`|Boolean|False|allow multiple users/apps to access the module or not. |


### ButtonCapabilities
Contains information about a button's capabilities.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`name`|ButtonName|True|The name of the button. See ButtonName.|
|`moduleInfo`|ModuleInfo|False|Information about a RC module, including its id. See ModuleInfo.|
|`shortPressAvailable`|Boolean|True|The button supports a short press.                Whenever the button is pressed short, onButtonPressed( SHORT) will be invoked.            |
|`longPressAvailable`|Boolean|True|The button supports a LONG press.                Whenever the button is pressed long, onButtonPressed( LONG) will be invoked.            |
|`upDownAvailable`|Boolean|True|The button supports "button down" and "button up".                Whenever the button is pressed, onButtonEvent( DOWN) will be invoked.                Whenever the button is released, onButtonEvent( UP) will be invoked.            |


### SoftButtonCapabilities
Contains information about a SoftButton's capabilities.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`shortPressAvailable`|Boolean|True|The button supports a short press.                Whenever the button is pressed short, onButtonPressed( SHORT) will be invoked.            |
|`longPressAvailable`|Boolean|True|The button supports a LONG press.                Whenever the button is pressed long, onButtonPressed( LONG) will be invoked.            |
|`upDownAvailable`|Boolean|True|The button supports "button down" and "button up".                Whenever the button is pressed, onButtonEvent( DOWN) will be invoked.                Whenever the button is released, onButtonEvent( UP) will be invoked.            |
|`imageSupported`|Boolean|True|The button supports referencing a static or dynamic image.|
|`textSupported`|Boolean|False|he button supports the use of text. If not included, the default value should be considered true that the button will support text.|

### PresetBankCapabilities
Contains information about on-screen preset capabilities.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`onScreenPresetsAvailable`|Boolean|True|Onscreen custom presets are available.|


### HMICapabilities
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`navigation`|Boolean|False|Availability of build in Nav. True: Available, False: Not Available|
|`phoneCall`|Boolean|False|Availability of build in phone. True: Available, False: Not Available |
|`videoStreaming`|Boolean|False|Availability of video streaming. |
|`remoteControl`|Boolean|False|Availability of remote control feature. True: Available, False: Not Available|


### MenuParams
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`parentID`|Integer|False|unique ID of the sub menu, the command will be added to.                If not provided, it will be provided to the top level of the in application menu.            |
|`position`|Integer|False|Position within the items that are are at top level of the in application menu.                0 will insert at the front.                1 will insert at the second position.                if position is greater or equal than the number of items on top level, the sub menu will be appended to the end.                If this param was omitted the entry will be added at the end.            |
|`menuName`|String|True|Text to show in the menu for this sub menu.|


### TTSChunk
A TTS chunk, that consists of text/phonemes to speak or the name of a file to play, and a TTS type (like text or SAPI)

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`text`|String|True|The text or phonemes to speak, or the name of the audio file to play.                May not be empty.            |
|`type`|SpeechCapabilities|True|Describes whether the TTS chunk is plain text, a specific phoneme set, or an audio file. See SpeechCapabilities|


### Turn
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`navigationText`|String|False|Individual turn text.  Must provide at least text or icon for a given turn.|
|`turnIcon`|Image|False|Individual turn icon.  Must provide at least text or icon for a given turn.|


### VehicleType
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`make`|String|False|Make of the vehicle, e.g. Ford|
|`model`|String|False|Model of the vehicle, e.g. Fiesta|
|`modelYear`|String|False|Model Year of the vehicle, e.g. 2013|
|`trim`|String|False|Trim of the vehicle, e.g. SE|


### KeyboardProperties
Configuration of on-screen keyboard (if available).

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`language`|Language|False|The keyboard language.|
|`keyboardLayout`|KeyboardLayout|False|Desired keyboard layout.|
|`keypressMode`|KeypressMode|False|Desired keypress mode.                If omitted, this value will be set to RESEND_CURRENT_ENTRY.            |
|`limitedCharacterList`|String[]|False|Array of keyboard characters to enable.|
|`autoCompleteText`|String|False|Deprecated, use autoCompleteList instead.|
|`autoCompleteList`|String[]|False|Allows an app to prepopulate the text field with a list of suggested or completed entries as the user types.                 If empty, the auto-complete list will be removed from the screen.            |


### DeviceInfo
Various information about connecting device.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`hardware`|String|False|Device model|
|`firmwareRev`|String|False|Device firmware revision|
|`os`|String|False|Device OS|
|`osVersion`|String|False|Device OS version|
|`carrier`|String|False|Device mobile carrier (if applicable)|
|`maxNumberRFCOMMPorts`|Integer|False|Omitted if connected not via BT.|


### DateTime
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`millisecond`|Integer|False|Milliseconds |
|`second`|Integer|False|Seconds part of time|
|`minute`|Integer|False|Minutes part of time|
|`hour`|Integer|False|Hours part of time. Note that this structure accepts time only in 24 Hr format|
|`day`|Integer|False|Day of the month|
|`month`|Integer|False|Month of the year|
|`year`|Integer|False|The year in YYYY format|
|`tz_hour`|Integer|False|Time zone offset in Hours wrt UTC.|
|`tz_minute`|Integer|False|Time zone offset in Min wrt UTC.|


### Coordinate
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`latitudeDegrees`|Float|True|Latitude of the location.|
|`longitudeDegrees`|Float|True|Longitude of the location.|


### OASISAddress
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`countryName`|String|False|Name of the country (localized)|
|`countryCode`|String|False|Name of country (ISO 3166-2)|
|`postalCode`|String|False|(PLZ, ZIP, PIN, CAP etc.)|
|`administrativeArea`|String|False|Portion of country (e.g. state)|
|`subAdministrativeArea`|String|False|Portion of e.g. state (e.g. county)|
|`locality`|String|False|Hypernym for e.g. city/village|
|`subLocality`|String|False|Hypernym for e.g. district|
|`thoroughfare`|String|False|Hypernym for street, road etc.|
|`subThoroughfare`|String|False|Portion of thoroughfare e.g. house number|


### LocationDetails
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`coordinate`|Coordinate|False|Latitude/Longitude of the location.|
|`locationName`|String|False|Name of location.|
|`addressLines`|String[]|False|Location address for display purposes only|
|`locationDescription`|String|False|Description intended location / establishment (if applicable)|
|`phoneNumber`|String|False|Phone number of location / establishment.|
|`locationImage`|Image|False|Image / icon of intended location.|
|`searchAddress`|OASISAddress|False|Address to be used by navigation engines for search|


### NavigationCapability
Extended capabilities for an onboard navigation system

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`sendLocationEnabled`|Boolean|False|If the module has the ability to add locations to the onboard nav|
|`getWayPointsEnabled`|Boolean|False|If the module has the ability to return way points from onboard nav|


### PhoneCapability
Extended capabilities of the module's phone feature

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`dialNumberEnabled`|Boolean|False|If the module has the ability to perform dial number|


### VideoStreamingFormat
Video streaming formats and their specifications.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`protocol`|VideoStreamingProtocol|True|Protocol type, see VideoStreamingProtocol|
|`codec`|VideoStreamingCodec|True|Codec type, see VideoStreamingCodec|


### VideoStreamingCapability
Contains information about this system's video streaming capabilities.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`preferredResolution`|ImageResolution|False|The preferred resolution of a video stream for decoding and rendering on HMI.|
|`maxBitrate`|Integer|False|The maximum bitrate of video stream that is supported, in kbps.|
|`supportedFormats`|VideoStreamingFormat[]|False|Detailed information on each format supported by this system, in its preferred order (i.e. the first element in the array is most preferable to the system). Each object will contain a VideoStreamingFormat that describes what can be expected.|
|`hapticSpatialDataSupported`|Boolean|False|True if the system can utilize the haptic spatial data from the source being streamed. If not included, it can be assumed the module doesn't support haptic spatial data'. |


### RGBColor
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`red`|Integer|True||
|`green`|Integer|True||
|`blue`|Integer|True||


### TemplateColorScheme
A color scheme for all display layout templates.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`primaryColor`|RGBColor|False|The primary "accent" color|
|`secondaryColor`|RGBColor|False|The secondary "accent" color|
|`backgroundColor`|RGBColor|False|The color of the background|


### MassageModeData
Specify the mode of a massage zone.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`massageZone`|MassageZone|True||
|`massageMode`|MassageMode|True||


### MassageCushionFirmness
The intensity or firmness of a cushion.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`cushion`|MassageCushion|True||
|`firmness`|Integer|True||


### SeatMemoryAction
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`id`|Integer|True||
|`label`|String|False||
|`action`|SeatMemoryActionType|True||

### SeatLocation
Describes the location of a seat.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`grid`|Grid|False||


### SeatLocationCapability
Contains information about the locations of each seat

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`rows`|Integer|False||
|`columns`|Integer|False||
|`levels`|Integer|False||
|`seats`|SeatLocation[]|False|Contains a list of SeatLocation in the vehicle. |

### SeatControlData
Seat control data corresponds to "SEAT" ModuleType. 

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`id`|SupportedSeat|True||
|`heatingEnabled`|Boolean|False||
|`coolingEnabled`|Boolean|False||
|`heatingLevel`|Integer|False||
|`coolingLevel`|Integer|False||
|`horizontalPosition`|Integer|False||
|`verticalPosition`|Integer|False||
|`frontVerticalPosition`|Integer|False||
|`backVerticalPosition`|Integer|False||
|`backTiltAngle`|Integer|False||
|`headSupportHorizontalPosition`|Integer|False||
|`headSupportVerticalPosition`|Integer|False||
|`massageEnabled`|Boolean|False||
|`massageMode`|MassageModeData[]|False||
|`massageCushionFirmness`|MassageCushionFirmness[]|False||
|`memory`|SeatMemoryAction|False||


### SeatControlCapabilities
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleName`|String|True|The short friendly name of the light control module.            It should not be used to identify a module by mobile application.            |
|`moduleInfo`|ModuleInfo|False|Information about a RC module, including its id.|
|`heatingEnabledAvailable`|Boolean|False||
|`coolingEnabledAvailable`|Boolean|False||
|`heatingLevelAvailable`|Boolean|False||
|`coolingLevelAvailable`|Boolean|False||
|`horizontalPositionAvailable`|Boolean|False||
|`verticalPositionAvailable`|Boolean|False||
|`frontVerticalPositionAvailable`|Boolean|False||
|`backVerticalPositionAvailable`|Boolean|False||
|`backTiltAngleAvailable`|Boolean|False||
|`headSupportHorizontalPositionAvailable`|Boolean|False||
|`headSupportVerticalPositionAvailable`|Boolean|False||
|`massageEnabledAvailable`|Boolean|False||
|`massageModeAvailable`|Boolean|False||
|`massageCushionFirmnessAvailable`|Boolean|False||
|`memoryAvailable`|Boolean|False||


### Temperature
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`unit`|TemperatureUnit|True|Temperature Unit|
|`value`|Float|True|Temperature Value in TemperatureUnit specified unit. Range depends on OEM and is not checked by SDL.|


### RdsData
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`PS`|String|False|Program Service Name|
|`RT`|String|False|Radio Text|
|`CT`|String|False|The clock text in UTC format as YYYY-MM-DDThh:mm:ss.sTZD|
|`PI`|String|False|Program Identification - the call sign for the radio station|
|`PTY`|Integer|False|The program type - The region should be used to differentiate between EU and North America program types|
|`TP`|Boolean|False|Traffic Program Identification - Identifies a station that offers traffic|
|`TA`|Boolean|False|Traffic Announcement Identification - Indicates an ongoing traffic announcement|
|`REG`|String|False|Region|


### StationIDNumber
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`countryCode`|Integer|False|Binary Representation of ITU Country Code. USA Code is 001.|
|`fccFacilityId`|Integer|False|Binary representation  of unique facility ID assigned by the FCC; FCC controlled for U.S. territory|


### SisData
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`stationShortName`|String|False|Identifies the 4-alpha-character station call sign plus an optional (-FM) extension|
|`stationIDNumber`|StationIDNumber|False|Used for network Application. Consists of Country Code and FCC Facility ID.|
|`stationLongName`|String|False|Identifies the station call sign or other identifying information in the long format.|
|`stationLocation`|GPSData|False|Provides the 3-dimensional geographic station location.|
|`stationMessage`|String|False|May be used to convey textual information of general interest to the consumer such as weather forecasts or public service announcements. Includes a high priority delivery feature to convey emergencies that may be in the listening area.|


### RadioControlData
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`frequencyInteger`|Integer|False|The integer part of the frequency ie for 101.7 this value should be 101|
|`frequencyFraction`|Integer|False|The fractional part of the frequency for 101.7 is 7|
|`band`|RadioBand|False||
|`rdsData`|RdsData|False||
|`hdRadioEnable`|Boolean|False|True if the hd radio is on, false if the radio is off|
|`availableHDs`|Integer|False|number of HD sub-channels if available|
|`hdChannel`|Integer|False|Current HD sub-channel if available|
|`signalStrength`|Integer|False||
|`signalChangeThreshold`|Integer|False|If the signal strength falls below the set value for this parameter, the radio will tune to an alternative frequency|
|`radioEnable`|Boolean|False|True if the radio is on, false if the radio is off. If set to false, no other data will be included.|
|`state`|RadioState|False||
|`sisData`|SisData|False|Read-only Station Information Service (SIS) data provides basic information about the station such as call sign, as well as information not displayable to the consumer such as the station identification number|


### ClimateControlData
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`fanSpeed`|Integer|False||
|`currentTemperature`|Temperature|False||
|`desiredTemperature`|Temperature|False||
|`acEnable`|Boolean|False||
|`circulateAirEnable`|Boolean|False||
|`autoModeEnable`|Boolean|False||
|`defrostZone`|DefrostZone|False||
|`dualModeEnable`|Boolean|False||
|`acMaxEnable`|Boolean|False||
|`ventilationMode`|VentilationMode|False||
|`heatedSteeringWheelEnable`|Boolean|False|value false means disabled/turn off, value true means enabled/turn on.|
|`heatedWindshieldEnable`|Boolean|False|value false means disabled, value true means enabled.|
|`heatedRearWindowEnable`|Boolean|False|value false means disabled, value true means enabled.|
|`heatedMirrorsEnable`|Boolean|False|value false means disabled, value true means enabled.|


### RadioControlCapabilities
Contains information about a radio control module's capabilities.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleName`|String|True|The short friendly name of the climate control module.                It should not be used to identify a module by mobile application.            |
|`moduleInfo`|ModuleInfo|False|Information about a RC module, including its id.|
|`radioEnableAvailable`|Boolean|False|Availability of the control of enable/disable radio.                True: Available, False: Not Available, Not present: Not Available.            |
|`radioBandAvailable`|Boolean|False|Availability of the control of radio band.                True: Available, False: Not Available, Not present: Not Available.            |
|`radioFrequencyAvailable`|Boolean|False|Availability of the control of radio frequency.                True: Available, False: Not Available, Not present: Not Available.            |
|`hdChannelAvailable`|Boolean|False|Availability of the control of HD radio channel.                True: Available, False: Not Available, Not present: Not Available.            |
|`rdsDataAvailable`|Boolean|False|Availability of the getting Radio Data System (RDS) data.                True: Available, False: Not Available, Not present: Not Available.            |
|`availableHDsAvailable`|Boolean|False|Availability of the getting the number of available HD channels.                True: Available, False: Not Available, Not present: Not Available.            |
|`stateAvailable`|Boolean|False|Availability of the getting the Radio state.                True: Available, False: Not Available, Not present: Not Available.            |
|`signalStrengthAvailable`|Boolean|False|Availability of the getting the signal strength.                True: Available, False: Not Available, Not present: Not Available.            |
|`signalChangeThresholdAvailable`|Boolean|False|Availability of the getting the signal Change Threshold.                True: Available, False: Not Available, Not present: Not Available.            |
|`sisDataAvailable`|Boolean|False|Availability of the getting HD radio Station Information Service (SIS) data.                True: Available, False: Not Available, Not present: Not Available.            |
|`hdRadioEnableAvailable`|Boolean|False|Availability of the control of enable/disable HD radio.                True: Available, False: Not Available, Not present: Not Available.            |
|`siriusxmRadioAvailable`|Boolean|False|Availability of sirius XM radio.                True: Available, False: Not Available, Not present: Not Available.            |


### ClimateControlCapabilities
Contains information about a climate control module's capabilities.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleName`|String|True|The short friendly name of the climate control module.                It should not be used to identify a module by mobile application.|
|`moduleInfo`|ModuleInfo|False|Information about a RC module, including its id.|
|`currentTemperatureAvailable`|Boolean|False|Availability of the reading of current temperature.                True: Available, False: Not Available, Not present: Not Available.            |
|`fanSpeedAvailable`|Boolean|False|Availability of the control of fan speed.                True: Available, False: Not Available, Not present: Not Available.            |
|`desiredTemperatureAvailable`|Boolean|False|Availability of the control of desired temperature.                True: Available, False: Not Available, Not present: Not Available.            |
|`acEnableAvailable`|Boolean|False|Availability of the control of turn on/off AC.                True: Available, False: Not Available, Not present: Not Available.            |
|`acMaxEnableAvailable`|Boolean|False|Availability of the control of enable/disable air conditioning is ON on the maximum level.                True: Available, False: Not Available, Not present: Not Available.            |
|`circulateAirEnableAvailable`|Boolean|False|Availability of the control of enable/disable circulate Air mode.                True: Available, False: Not Available, Not present: Not Available.            |
|`autoModeEnableAvailable`|Boolean|False|Availability of the control of enable/disable auto mode.                True: Available, False: Not Available, Not present: Not Available.            |
|`dualModeEnableAvailable`|Boolean|False|Availability of the control of enable/disable dual mode.                True: Available, False: Not Available, Not present: Not Available.            |
|`defrostZoneAvailable`|Boolean|False|Availability of the control of defrost zones.                True: Available, False: Not Available, Not present: Not Available.            |
|`defrostZone`|DefrostZone[]|False|A set of all defrost zones that are controllable.            |
|`ventilationModeAvailable`|Boolean|False|Availability of the control of air ventilation mode.                True: Available, False: Not Available, Not present: Not Available.            |
|`ventilationMode`|VentilationMode[]|False|A set of all ventilation modes that are controllable.            |
|`heatedSteeringWheelAvailable`|Boolean|False|Availability of the control (enable/disable) of heated Steering Wheel.                True: Available, False: Not Available, Not present: Not Available.            |
|`heatedWindshieldAvailable`|Boolean|False|Availability of the control (enable/disable) of heated Windshield.                True: Available, False: Not Available, Not present: Not Available.            |
|`heatedRearWindowAvailable`|Boolean|False|Availability of the control (enable/disable) of heated Rear Window.                True: Available, False: Not Available, Not present: Not Available.            |
|`heatedMirrorsAvailable`|Boolean|False|Availability of the control (enable/disable) of heated Mirrors.                True: Available, False: Not Available, Not present: Not Available.            |


### EqualizerSettings
Defines the each Equalizer channel settings.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`channelId`|Integer|True||
|`channelName`|String|False|read-only channel / frequency name (e.i. "Treble, Midrange, Bass" or "125 Hz")|
|`channelSetting`|Integer|True|Reflects the setting, from 0%-100%.|


### AudioControlData
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`source`|PrimaryAudioSource|False|In a getter response or a notification, it is the current primary audio source of the system.                In a setter request, it is the target audio source that the system shall switch to.                If the value is MOBILE_APP, the system shall switch to the mobile media app that issues the setter RPC.            |
|`keepContext`|Boolean|False|This parameter shall not be present in any getter responses or notifications.                This parameter is optional in a setter request. The default value is false if it is not included.                If it is false, the system not only changes the audio source but also brings the default application or                 system UI associated with the audio source to foreground.                If it is true, the system only changes the audio source, but keeps the current application in foreground.            |
|`volume`|Integer|False|Reflects the volume of audio, from 0%-100%.|
|`equalizerSettings`|EqualizerSettings[]|False|Defines the list of supported channels (band) and their current/desired settings on HMI|


### AudioControlCapabilities
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleName`|String|True|The short friendly name of the light control module.                It should not be used to identify a module by mobile application.            |
|`moduleInfo`|ModuleInfo|False|Information about a RC module, including its id.|
|`sourceAvailable`|Boolean|False|Availability of the control of audio source. |
|`keepContextAvailable`|Boolean|False|Availability of the keepContext parameter. |
|`volumeAvailable`|Boolean|False|Availability of the control of audio volume.|
|`equalizerAvailable`|Boolean|False|Availability of the control of Equalizer Settings.|
|`equalizerMaxChannelId`|Integer|False|Must be included if equalizerAvailable=true, and assume all IDs starting from 1 to this value are valid|


### LightCapabilities
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`name`|LightName|True||
|`statusAvailable`|Boolean|False|Indicates if the status (ON/OFF) can be set remotely. App shall not use read-only values (RAMP_UP/RAMP_DOWN/UNKNOWN/INVALID) in a setInteriorVehicleData request.          |
|`densityAvailable`|Boolean|False|Indicates if the light's density can be set remotely (similar to a dimmer).            |
|`rgbColorSpaceAvailable`|Boolean|False|Indicates if the light's color can be set remotely by using the sRGB color space.            |


### LightControlCapabilities
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleName`|String|True|The short friendly name of the light control module.                It should not be used to identify a module by mobile application.            |
|`moduleInfo`|ModuleInfo|False|Information about a RC module, including its id.|
|`supportedLights`|LightCapabilities[]|True|An array of available LightCapabilities that are controllable. |


### LightState
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`id`|LightName|True|The name of a light or a group of lights. |
|`status`|LightStatus|True||
|`density`|Float|False||
|`color`|RGBColor|False||


### LightControlData
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`lightState`|LightState[]|True|An array of LightNames and their current or desired status. No change to the status of the LightNames that are not listed in the array.|


### HMISettingsControlData
Corresponds to "HMI_SETTINGS" ModuleType

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`displayMode`|DisplayMode|False||
|`temperatureUnit`|TemperatureUnit|False||
|`distanceUnit`|DistanceUnit|False||


### HMISettingsControlCapabilities
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleName`|String|True|The short friendly name of the hmi setting module.              It should not be used to identify a module by mobile application.            |
|`moduleInfo`|ModuleInfo|False|Information about a RC module, including its id.|
|`distanceUnitAvailable`|Boolean|False|Availability of the control of distance unit. |
|`temperatureUnitAvailable`|Boolean|False|Availability of the control of temperature unit. |
|`displayModeUnitAvailable`|Boolean|False|Availability of the control of HMI display mode. |


### ModuleData
The moduleType indicates which type of data should be changed and identifies which data object exists in this struct. For example, if the moduleType is CLIMATE then a "climateControlData" should exist

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleType`|ModuleType|True||
|`moduleId`|String|False|Id of a module, published by System Capability.|
|`radioControlData`|RadioControlData|False||
|`climateControlData`|ClimateControlData|False||
|`seatControlData`|SeatControlData|False||
|`audioControlData`|AudioControlData|False||
|`lightControlData`|LightControlData|False||
|`hmiSettingsControlData`|HMISettingsControlData|False||


### RemoteControlCapabilities
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`climateControlCapabilities`|ClimateControlCapabilities[]|False|If included, the platform supports RC climate controls. For this baseline version, maxsize=1. i.e. only one climate control module is supported.|
|`radioControlCapabilities`|RadioControlCapabilities[]|False|If included, the platform supports RC radio controls.For this baseline version, maxsize=1. i.e. only one radio control module is supported.|
|`buttonCapabilities`|ButtonCapabilities[]|False|If included, the platform supports RC button controls with the included button names.|
|`audioControlCapabilities`|AudioControlCapabilities[]|False|If included, the platform supports audio controls.|
|`hmiSettingsControlCapabilities`|HMISettingsControlCapabilities|False|If included, the platform supports hmi setting controls.|
|`lightControlCapabilities`|LightControlCapabilities|False|If included, the platform supports light controls.|
|`seatControlCapabilities`|SeatControlCapabilities[]|False|If included, the platform supports seat controls.|


### MetadataTags
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`mainField1`|MetadataType[]|False|The type of data contained in the "mainField1" text field.|
|`mainField2`|MetadataType[]|False|The type of data contained in the "mainField2" text field.|
|`mainField3`|MetadataType[]|False|The type of data contained in the "mainField3" text field.|
|`mainField4`|MetadataType[]|False|The type of data contained in the "mainField4" text field.|


### Rectangle
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`x`|Float|True|The upper left X-coordinate of the rectangle|
|`y`|Float|True|The upper left Y-coordinate of the rectangle|
|`width`|Float|True|The width of the rectangle|
|`height`|Float|True|The height of the rectangle|


### HapticRect
Defines haptic data for each user control object for video streaming application

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`id`|Integer|True|A user control spatial identifier|
|`rect`|Rectangle|True|The position of the haptic rectangle to be highlighted. The center of this rectangle will be "touched" when a press occurs.|


### MediaServiceManifest

### MediaServiceData
This data is related to what a media service should provide

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`mediaType`|MediaType|False|The type of the currently playing or paused track.|
|`mediaTitle`|String|False|Music: The name of the current track                Podcast: The name of the current episode                Audiobook: The name of the current chapter            |
|`mediaArtist`|String|False|Music: The name of the current album artist                Podcast: The provider of the podcast (hosts, network, company)                Audiobook: The book author's name            |
|`mediaAlbum`|String|False|Music: The name of the current album                Podcast: The name of the current podcast show                Audiobook: The name of the current book            |
|`playlistName`|String|False|Music: The name of the playlist or radio station, if the user is playing from a playlist, otherwise, Null                Podcast: The name of the playlist, if the user is playing from a playlist, otherwise, Null                Audiobook: Likely not applicable, possibly a collection or "playlist" of books            |
|`isExplicit`|Boolean|False|Whether or not the content currently playing (e.g. the track, episode, or book) contains explicit content|
|`trackPlaybackProgress`|Integer|False|Music: The current progress of the track in seconds                Podcast: The current progress of the episode in seconds                Audiobook: The current progress of the current segment (e.g. the chapter) in seconds            |
|`trackPlaybackDuration`|Integer|False|Music: The total duration of the track in seconds                Podcast: The total duration of the episode in seconds                Audiobook: The total duration of the current segment (e.g. the chapter) in seconds            |
|`queuePlaybackProgress`|Integer|False|Music: The current progress of the playback queue in seconds                Podcast: The current progress of the playback queue in seconds                Audiobook: The current progress of the playback queue (e.g. the book) in seconds            |
|`queuePlaybackDuration`|Integer|False|Music: The total duration of the playback queue in seconds                Podcast: The total duration of the playback queue in seconds                Audiobook: The total duration of the playback queue (e.g. the book) in seconds            |
|`queueCurrentTrackNumber`|Integer|False|Music: The current number (1 based) of the track in the playback queue                Podcast: The current number (1 based) of the episode in the playback queue                Audiobook: The current number (1 based) of the episode in the playback queue (e.g. the chapter number in the book)            |
|`queueTotalTrackCount`|Integer|False|Music: The total number of tracks in the playback queue                Podcast: The total number of episodes in the playback queue                Audiobook: The total number of sections in the playback queue (e.g. the number of chapters in the book)            |


### WeatherServiceManifest
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`currentForecastSupported`|Boolean|False||
|`maxMultidayForecastAmount`|Integer|False||
|`maxHourlyForecastAmount`|Integer|False||
|`maxMinutelyForecastAmount`|Integer|False||
|`weatherForLocationSupported`|Boolean|False||


### WeatherAlert
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`title`|String|False||
|`summary`|String|False||
|`expires`|DateTime|False||
|`regions`|String[]|False||
|`severity`|String|False||
|`timeIssued`|DateTime|False||


### WeatherData
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`currentTemperature`|Temperature|False||
|`temperatureHigh`|Temperature|False||
|`temperatureLow`|Temperature|False||
|`apparentTemperature`|Temperature|False||
|`apparentTemperatureHigh`|Temperature|False||
|`apparentTemperatureLow`|Temperature|False||
|`weatherSummary`|String|False||
|`time`|DateTime|False||
|`humidity`|Float|False|0 to 1, percentage humidity |
|`cloudCover`|Float|False|0 to 1, percentage cloud cover |
|`moonPhase`|Float|False|0 to 1, percentage of the moon seen, e.g. 0 = no moon, 0.25 = quarter moon |
|`windBearing`|Integer|False|In degrees, true north at 0 degrees |
|`windGust`|Float|False|km/hr |
|`windSpeed`|Float|False|km/hr |
|`nearestStormBearing`|Integer|False|In degrees, true north at 0 degrees |
|`nearestStormDistance`|Integer|False|In km |
|`precipAccumulation`|Float|False|cm |
|`precipIntensity`|Float|False|cm of water per hour |
|`precipProbability`|Float|False|0 to 1, percentage chance |
|`precipType`|String|False|e.g. "rain", "snow", "sleet", "hail" |
|`visibility`|Float|False|In km |
|`weatherIcon`|Image|False||


### WeatherServiceData
This data is related to what a weather service would provide

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`location`|LocationDetails|True||
|`currentForecast`|WeatherData|False||
|`minuteForecast`|WeatherData[]|False||
|`hourlyForecast`|WeatherData[]|False||
|`multidayForecast`|WeatherData[]|False||
|`alerts`|WeatherAlert[]|False|This array should be ordered with the first object being the current day|


### NavigationServiceManifest
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`acceptsWayPoints`|Boolean|False|Informs the subscriber if this service can actually accept way points. |


### NavigationInstruction
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`locationDetails`|LocationDetails|True||
|`action`|NavigationAction|True||
|`eta`|DateTime|False||
|`bearing`|Integer|False|The angle at which this instruction takes place. For example, 0 would mean straight, less than 45 is bearing right, greater than 135 is sharp right, between 45 and 135 is a regular right, and 180 is a U-Turn, etc. |
|`junctionType`|NavigationJunction|False||
|`drivingSide`|Direction|False|Used to infer which side of the road this instruction takes place. For a U-Turn (action=TURN, bearing=180) this will determine which direction the turn should take place. |
|`details`|String|False|This is a string representation of this instruction, used to display instructions to the users. This is not intended to be read aloud to the users, see the param prompt in NavigationServiceData for that. |
|`image`|Image|False|An image representation of this instruction. |


### NavigationServiceData
This data is related to what a navigation service would provide.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`timeStamp`|DateTime|True|This is the timestamp of when the data was generated. This is to ensure any time or distance given in the data can accurately be adjusted if necessary. |
|`origin`|LocationDetails|False||
|`destination`|LocationDetails|False||
|`destinationETA`|DateTime|False||
|`instructions`|NavigationInstruction[]|False|This array should be ordered with all remaining instructions. The start of this array should always contain the next instruction.|
|`nextInstructionETA`|DateTime|False||
|`nextInstructionDistance`|Float|False|The distance to this instruction from current location. This should only be updated ever .1 unit of distance. For more accuracy the consumer can use the GPS location of itself and the next instruction. |
|`nextInstructionDistanceScale`|Float|False|Distance till next maneuver (starting from) from previous maneuver.|
|`prompt`|String|False|This is a prompt message that should be conveyed to the user through either display or voice (TTS). This param will change often as it should represent the following: approaching instruction, post instruction, alerts that affect the current navigation session, etc.|


### AppServiceManifest
This manifest contains all the information necessary for the service to be published, activated, and consumers able to interact with it 

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`serviceName`|String|False|Unique name of this service |
|`serviceType`|String|True|The type of service that is to be offered by this app. See AppServiceType for known enum equivalent types. Parameter is a string to allow for new service types to be used by apps on older versions of SDL Core. |
|`serviceIcon`|Image|False|The icon to be associated with this service. Most likely the same as the appIcon.|
|`allowAppConsumers`|Boolean|False|If true, app service consumers beyond the IVI system will be able to access this service. If false, only the IVI system will be able consume the service. If not provided, it is assumed to be false. |
|`rpcSpecVersion`|SyncMsgVersion|False|This is the max RPC Spec version the app service understands. This is important during the RPC passthrough functionality. If not included, it is assumed the max version of the module is acceptable. |
|`handledRPCs`|Integer[]|False|This field contains the Function IDs for the RPCs that this service intends to handle correctly. This means the service will provide meaningful responses. |
|`mediaServiceManifest`|MediaServiceManifest|False||
|`weatherServiceManifest`|WeatherServiceManifest|False||
|`navigationServiceManifest`|NavigationServiceManifest|False||


### AppServiceRecord
This is the record of an app service publisher that the module has. It should contain the most up to date information including the service's active state

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`serviceID`|String|True|A unique ID tied to this specific service record. The ID is supplied by the module that services publish themselves. |
|`serviceManifest`|AppServiceManifest|True|Manifest for the service that this record is for.|
|`servicePublished`|Boolean|True|If true, the service is published and available. If false, the service has likely just been unpublished, and should be considered unavailable.|
|`serviceActive`|Boolean|True|If true, the service is the active primary service of the supplied service type. It will receive all potential RPCs that are passed through to that service type. If false, it is not the primary service of the supplied type. See servicePublished for its availability. |


### AppServiceData
Contains all the current data of the app service. The serviceType will link to which of the service data objects are included in this object (e.g. if the service type is MEDIA, the mediaServiceData param should be included).

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`serviceType`|String|True|The type of service that is to be offered by this app. See AppServiceType for known enum equivalent types. Parameter is a string to allow for new service types to be used by apps on older versions of SDL Core.|
|`serviceID`|String|True||
|`mediaServiceData`|MediaServiceData|False||
|`weatherServiceData`|WeatherServiceData|False||
|`navigationServiceData`|NavigationServiceData|False||


### AppServiceCapability
##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`updateReason`|ServiceUpdateReason|False|Only included in OnSystemCapabilityUpdated. Update reason for service record.|
|`updatedAppServiceRecord`|AppServiceRecord|True|Service record for a specific app service provider|


### AppServicesCapabilities
Capabilities of app services including what service types are supported and the current state of services.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`appServices`|AppServiceCapability[]|False|An array of currently available services. If this is an update to the capability the affected services will include an update reason in that item|


### SystemCapability
The systemCapabilityType identifies which data object exists in this struct. For example, if the SystemCapability Type is NAVIGATION then a "navigationCapability" should exist

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`systemCapabilityType`|SystemCapabilityType|True|Used as a descriptor of what data to expect in this struct. The corresponding param to this enum should be included and the only other param included.|
|`navigationCapability`|NavigationCapability|False|Describes extended capabilities for onboard navigation system |
|`phoneCapability`|PhoneCapability|False|Describes extended capabilities of the module's phone feature|
|`videoStreamingCapability`|VideoStreamingCapability|False|Describes extended capabilities of the module's phone feature|
|`remoteControlCapability`|RemoteControlCapabilities|False|Describes extended capabilities of the module's phone feature|
|`appServicesCapabilities`|AppServicesCapabilities|False|An array of currently available services. If this is an update to the capability the affected services will include an update reason in that item|
|`seatLocationCapability`|SeatLocationCapability|False|Contains information about the locations of each seat|
|`displayCapabilities`|DisplayCapability[]|False||

### WindowCapability

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`windowID`|Integer|False|The specified ID of the window. Can be set to a predefined window, or omitted for the main window on the main display.|
|`textFields`|TextField[]|False|A set of all fields that support text data. See TextField|
|`imageFields`|ImageField[]|False|A set of all fields that support images. See ImageField.|
|`imageTypeSupported`|ImageType[]|False|Provides information about image types supported by the system.|
|`templatesAvailable`|String[]|False|A set of all window templates available on the head unit.|
|`numCustomPresetsAvailable`|Integer[]|False|The number of on-window custom presets available (if any); otherwise omitted.|
|`buttonCapabilities`|ButtonCapabilities[]|False|The number of buttons and the capabilities of each on-window button.|
|`softButtonCapabilities`|SoftButtonCapabilities[]|False|The number of soft buttons available on-window and the capabilities for each button.|

### WindowTypeCapabilities

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`type`|WindowType|True||
|`maximumNumberOfWindows`|Integer|True||

### DisplayCapability

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`displayName`|String|False||
|`windowTypeSupported`|WindowTypeCapabilities[]|False|Informs the application how many windows the app is allowed to create per type.|
|`windowCapabilities`|WindowCapability[]|False|Contains a list of capabilities of all windows related to the app.
Once the app has registered the capabilities of all windows are provided. GetSystemCapability still allows requesting window capabilities of all windows.
After registration, only windows with capabilities changed willincluded. Following cases will cause only affected windows toincluded:
1. App creates a new window. After the window is created, a syscapability notification will be sent related only to the created window.
2. App sets a new layout to the window. The new layout changes wincapabilties. The notification will reflect those changes to the sinwindow.|

### TemplateConfiguration

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`template`|String|True|Predefined or dynamically created window template. Currently only predefined window template layouts are defined.|
|`dayColorScheme`|TemplateColorScheme|False||
|`nightColorScheme`|TemplateColorScheme|False||

<div style="page-break-after: always;"></div>


## Remote Procedure Calls

### RegisterAppInterface
Message Type: **request**

Establishes an interface with a mobile application.
            Before registerAppInterface no other commands will be accepted/executed.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`syncMsgVersion`|SyncMsgVersion|True|See SyncMsgVersion|
|`appName`|String|True|The mobile application name, e.g. "Ford Drive Green".                Needs to be unique over all applications.                May not be empty.                May not start with a new line character.                May not interfere with any name or synonym of previously registered applications and any predefined blacklist of words (global commands)                Needs to be unique over all applications. Applications with the same name will be rejected.                Only characters from char set [@TODO: Create char set (character/hex value) for each ACM and refer to] are supported.            |
|`ttsName`|TTSChunk[]|False|TTS string for VR recognition of the mobile application name, e.g. "Ford Drive Green".                Meant to overcome any failing on speech engine in properly pronouncing / understanding app name.                Needs to be unique over all applications.                May not be empty.                May not start with a new line character.                Only characters from char set [@TODO: Create char set (character/hex value) for each ACM and refer to] are supported.            |
|`ngnMediaScreenAppName`|String|False|Provides an abbreviated version of the app name (if needed), that will be displayed on the NGN media screen.                If not provided, the appName is used instead (and will be truncated if too long)                Only characters from char set [@TODO: Create char set (character/hex value) for each ACM and refer to] are supported.            |
|`vrSynonyms`|String[]|False|Defines an additional voice recognition command.                May not interfere with any app name of previously registered applications and any predefined blacklist of words (global commands)                Only characters from char set [@TODO: Create char set (character/hex value) for each ACM and refer to] are supported.            |
|`isMediaApplication`|Boolean|True|Indicates if the application is a media or a non-media application.                Only media applications will be able to stream audio to the module that is audible outside of the BT media source.            |
|`languageDesired`|Language|True|See Language                Current app's expected VR+TTS language                If there is a mismatch with the module, the app will be able to change this registration with changeRegistration prior to app being brought into focus.            |
|`hmiDisplayLanguageDesired`|Language|True|See Language                Current app's expected display language                If there is a mismatch with the module, the app will be able to change this registration with changeRegistration prior to app being brought into focus.            |
|`appHMIType`|AppHMIType[]|False|See AppHMIType                List of all applicable app HMI types stating which HMI classifications to be given to the app.            |
|`hashID`|String|False|ID used to uniquely identify current state of all app data that can persist through connection cycles (e.g. ignition cycles).                This registered data (commands, submenus, choice sets, etc.) can be reestablished without needing to explicitly reregister each piece.                If omitted, then the previous state of an app's commands, etc. will not be restored.                When sending hashID, all RegisterAppInterface parameters should still be provided (e.g. ttsName, etc.).            |
|`deviceInfo`|DeviceInfo|False|See DeviceInfo.            |
|`appID`|String|True|ID used to validate app with policy table entries|
|`fullAppID`|String|False|ID used to validate app with policy table entries|
|`appInfo`|AppInfo|False|See AppInfo.            |
|`dayColorScheme`|TemplateColorScheme|False||
|`nightColorScheme`|TemplateColorScheme|False||


### RegisterAppInterface
Message Type: **response**

The response to registerAppInterface

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`syncMsgVersion`|SyncMsgVersion|False|See SyncMsgVersion|
|`language`|Language|False|The currently active VR+TTS language on the module. See "Language" for options.|
|`hmiDisplayLanguage`|Language|False|The currently active display language on the module. See "Language" for options.|
|`displayCapabilities`|DisplayCapabilities|False|See DisplayCapabilities|
|`buttonCapabilities`|ButtonCapabilities[]|False|See ButtonCapabilities|
|`softButtonCapabilities`|SoftButtonCapabilities[]|False|If returned, the platform supports on-screen SoftButtons; see SoftButtonCapabilities.|
|`presetBankCapabilities`|PresetBankCapabilities|False|If returned, the platform supports custom on-screen Presets; see PresetBankCapabilities.|
|`hmiZoneCapabilities`|HmiZoneCapabilities[]|False|See HmiZoneCapabilities|
|`speechCapabilities`|SpeechCapabilities[]|False|See SpeechCapabilities|
|`prerecordedSpeech`|PrerecordedSpeech[]|False|See PrerecordedSpeech|
|`vrCapabilities`|VrCapabilities[]|False|See VrCapabilities|
|`audioPassThruCapabilities`|AudioPassThruCapabilities[]|False|See AudioPassThruCapability|
|`pcmStreamCapabilities`|AudioPassThruCapabilities[]|False|See AudioPassThruCapability|
|`vehicleType`|VehicleType|False|Specifies the vehicle's type. See VehicleType.|
|`supportedDiagModes`|Integer[]|False|Specifies the white-list of supported diagnostic modes (0x00-0xFF) capable for DiagnosticMessage requests.                If a mode outside this list is requested, it will be rejected.            |
|`hmiCapabilities`|HMICapabilities|False|Specifies the HMIÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s capabilities. See HMICapabilities.|
|`sdlVersion`|String|False|The SmartDeviceLink version.|
|`systemSoftwareVersion`|String|False|The software version of the system that implements the SmartDeviceLink core.|
|`iconResumed`|Boolean|False|Existence of apps icon at system. If true, apps icon                was resumed at system. If false, apps icon is not resumed at system            |


### UnregisterAppInterface
Message Type: **request**

Closes an interface from a mobile application.
            After unregisterAppInterface, no commands other than registerAppInterface will be accepted/executed.
            Will fail, if no registerAppInterface was completed successfully before.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|


### UnregisterAppInterface
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### SetGlobalProperties
Message Type: **request**

Allows setting global properties.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`userLocation`|SeatLocation|False|Location of the user's seat. Default is driver's seat location if it is not set yet.|
|`helpPrompt`|TTSChunk[]|False|The help prompt.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`timeoutPrompt`|TTSChunk[]|False|Help text for a wait timeout.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`vrHelpTitle`|String|False|VR Help Title text.                If omitted on supported displays, the default module help title shall be used.                If omitted and one or more vrHelp items are provided, the request will be rejected.            |
|`vrHelp`|VrHelpItem[]|False|VR Help Items.                If omitted on supported displays, the default SmartDeviceLink VR help / What Can I Say? screen shall be used.                If the list of VR Help Items contains nonsequential positions (e.g. [1,2,4]), the RPC shall be rejected.                If omitted and a vrHelpTitle is provided, the request will be rejected.            |
|`menuTitle`|String|False|Optional text to label an app menu button (for certain touchscreen platforms).|
|`menuIcon`|Image|False|Optional icon to draw on an app menu button (for certain touchscreen platforms).|
|`keyboardProperties`|KeyboardProperties|False|On-screen keyboard configuration (if available).|


### SetGlobalProperties
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### ResetGlobalProperties
Message Type: **request**

Allows resetting global properties.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`properties`|GlobalProperty[]|True|Contains the names of all global properties (like timeoutPrompt) that should be unset. Resetting means, that they have the same value as at start up (default)|


### ResetGlobalProperties
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### AddCommand
Message Type: **request**

Adds a command to the in application menu.
            Either menuParams or vrCommands must be provided.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`cmdID`|Integer|True|unique ID of the command to add.|
|`menuParams`|MenuParams|False|Optional sub value containing menu parameters|
|`vrCommands`|String[]|False|An array of strings to be used as VR synonyms for this command.                If this array is provided, it may not be empty.            |
|`cmdIcon`|Image|False|Image struct determining whether static or dynamic icon.                If omitted on supported displays, no (or the default if applicable) icon shall be displayed.            |


### AddCommand
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### DeleteCommand
Message Type: **request**

Deletes all commands from the in-application menu with the specified command id.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`cmdID`|Integer|True|ID of the command(s) to delete.|


### DeleteCommand
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### AddSubMenu
Message Type: **request**

Adds a sub menu to the in-application menu.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`menuID`|Integer|True|unique ID of the sub menu to add.|
|`position`|Integer|False|Position within the items that are are at top level of the in application menu.                0 will insert at the front.                1 will insert at the second position.                If position is greater or equal than the number of items on top level, the sub menu will be appended to the end.                Position of any submenu will always be located before the return and exit options                If this param was omitted the entry will be added at the end.            |
|`menuName`|String|True|Text to show in the menu for this sub menu.|
|`menuIcon`|Image|False|The image field for AddSubMenu|


### AddSubMenu
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### DeleteSubMenu
Message Type: **request**

Deletes a submenu from the in-application menu.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`menuID`|Integer|True|The "menuID" of the submenu to delete. (See addSubMenu.menuID)|


### DeleteSubMenu
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### ShowAppMenu
Message Type: **request**

Shows the built in menu view

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`menuID`|Integer|False|If omitted the HMI opens the app's menu.<br>If set to a sub-menu ID the HMI opens the corresponding sub-menu previously added using `AddSubMenu`.|


### ShowAppMenu
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### CreateInteractionChoiceSet
Message Type: **request**

creates interaction choice set to be used later by performInteraction

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`interactionChoiceSetID`|Integer|True|Unique ID used for this interaction choice set.|
|`choiceSet`|Choice[]|True||


### CreateInteractionChoiceSet
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### PerformInteraction
Message Type: **request**

Triggers an interaction (e.g. "Permit GPS?" - Yes, no, Always Allow).

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`initialText`|String|True|Text to be displayed first.            |
|`initialPrompt`|TTSChunk[]|False|This is the initial prompt spoken to the user at the start of an interaction.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`interactionMode`|InteractionMode|True|See InteractionMode.|
|`interactionChoiceSetIDList`|Integer[]|True|List of interaction choice set IDs to use with an interaction.|
|`helpPrompt`|TTSChunk[]|False|Help text. This is the spoken string when a user speaks "help" when the interaction is occurring.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`timeoutPrompt`|TTSChunk[]|False|Timeout text. This text is spoken when a VR interaction times out.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`timeout`|Integer|False|Timeout in milliseconds.                If omitted a standard value of 10000 milliseconds is used.                Applies only to the menu portion of the interaction. The VR timeout will be handled by the platform.            |
|`vrHelp`|VrHelpItem[]|False|Ability to send suggested VR Help Items to display on-screen during Perform Interaction.                If omitted on supported displays, the default generated list of suggested choices shall be displayed.            |
|`interactionLayout`|LayoutMode|False|See LayoutMode.|


### PerformInteraction
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`choiceID`|Integer|False|ID of the choice that was selected in response to PerformInteraction.                Only is valid if general result is "success:true".            |
|`manualTextEntry`|String|False|Manually entered text selection, e.g. through keyboard                Can be returned in lieu of choiceID, depending on trigger source            |
|`triggerSource`|TriggerSource|False|See TriggerSource                Only is valid if resultCode is SUCCESS.            |


### DeleteInteractionChoiceSet
Message Type: **request**

Deletes interaction choice set that has been created with "CreateInteractionChoiceSet".

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`interactionChoiceSetID`|Integer|True|ID of the interaction choice set to delete.|


### DeleteInteractionChoiceSet
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### Alert
Message Type: **request**

Shows an alert which typically consists of text-to-speech message and text on the display. At least either alertText1, alertText2 or TTSChunks need to be provided.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`alertText1`|String|False|The first line of the alert text field|
|`alertText2`|String|False|The second line of the alert text field|
|`alertText3`|String|False|The optional third line of the alert text field|
|`ttsChunks`|TTSChunk[]|False|An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |
|`duration`|Integer|False|Timeout in milliseconds.                Typical timeouts are 3-5 seconds.                If omitted, timeout is set to 5s.            |
|`playTone`|Boolean|False|Defines if tone should be played. Tone is played before TTS.                If omitted, no tone is played.            |
|`progressIndicator`|Boolean|False|If supported on the given platform, the alert GUI will include some sort of animation indicating that loading of a feature is progressing.  e.g. a spinning wheel or hourglass, etc.            |
|`softButtons`|SoftButton[]|False|App defined SoftButtons.                If omitted on supported displays, the displayed alert shall not have any SoftButtons.            |
|`alertIcon`|Image|False|Image struct determining whether static or dynamic icon.                If omitted on supported displays, no (or the default if applicable) icon should be displayed.            |


### Alert
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`tryAgainTime`|Integer|False|Amount of time (in seconds) that an app must wait before resending an alert.                If provided, another system event or overlay currently has a higher priority than this alert.                An app must not send an alert without waiting at least the amount of time dictated.            |


### Show
Message Type: **request**

Updates the persistent display. Supported fields depend on display capabilities.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`mainField1`|String|False|The text that should be displayed in a single or upper display line.                If this text is not set, the text of mainField1 stays unchanged.                If this text is empty "", the field will be cleared.            |
|`mainField2`|String|False|The text that should be displayed on the second display line.                If this text is not set, the text of mainField2 stays unchanged.                If this text is empty "", the field will be cleared.            |
|`mainField3`|String|False|The text that should be displayed on the second "page" first display line.                If this text is not set, the text of mainField3 stays unchanged.                If this text is empty "", the field will be cleared.            |
|`mainField4`|String|False|The text that should be displayed on the second "page" second display line.                If this text is not set, the text of mainField4 stays unchanged.                If this text is empty "", the field will be cleared.            |
|`alignment`|TextAlignment|False|Specifies how mainField1 and mainField2 texts should be aligned on display.                If omitted, texts will be centered.            |
|`statusBar`|String|False|Requires investigation regarding the nav display capabilities. Potentially lower lowerStatusBar, upperStatusBar, titleBar, etc.|
|`mediaClock`|String|False|Text value for MediaClock field. Has to be properly formatted by Mobile App according to the module's capabilities.                If this text is set, any automatic media clock updates previously set with SetMediaClockTimer will be stopped.            |
|`mediaTrack`|String|False|The text that should be displayed in the track field.                If this text is not set, the text of mediaTrack stays unchanged.                If this text is empty "", the field will be cleared.            |
|`graphic`|Image|False|Image struct determining whether static or dynamic image to display in app.                If omitted on supported displays, the displayed graphic shall not change.            |
|`secondaryGraphic`|Image|False|Image struct determining whether static or dynamic secondary image to display in app.                If omitted on supported displays, the displayed secondary graphic shall not change.            |
|`softButtons`|SoftButton[]|False|App defined SoftButtons.                If omitted on supported displays, the currently displayed SoftButton values will not change.            |
|`customPresets`|String[]|False|App labeled on-screen presets (i.e. on-screen media presets or dynamic search suggestions).                If omitted on supported displays, the presets will be shown as not defined.            |
|`metadataTags`|MetadataTags|False|App defined metadata information. See MetadataStruct. Uses mainField1, mainField2, mainField3, mainField4.                If omitted on supported displays, the currently set metadata tags will not change.                If any text field contains no tags or the none tag, the metadata tag for that textfield should be removed.|
|`templateTitle`|String|False|The title of the new template that will be displayed.<br>How this will be displayed is dependent on the OEM design and implementation of the template.|
|`windowID`|Integer|False|This is the unique ID assigned to the window that this RPC is intended. If this param is not included, it will be assumed that this request is specifically for the main window on the main display. See PredefinedWindows enum.|
|`templateConfiguration`|TemplateConfiguration|False|Used to set an alternate template layout to a window.|

### Show
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### Speak
Message Type: **request**

Speaks a text.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`ttsChunks`|TTSChunk[]|True|An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.            |


### Speak
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### SetMediaClockTimer
Message Type: **request**

Sets the initial media clock value and automatic update method.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`startTime`|StartTime|False|See StartTime.                startTime must be provided for "COUNTUP" and "COUNTDOWN".                startTime will be ignored for "RESUME", and "CLEAR"                startTime can be sent for "PAUSE", in which case it will update the paused startTime            |
|`endTime`|StartTime|False|See StartTime.                endTime can be provided for "COUNTUP" and "COUNTDOWN"; to be used to calculate any visual progress bar (if not provided, this feature is ignored)                If endTime is greater then startTime for COUNTDOWN or less than startTime for COUNTUP, then the request will return an INVALID_DATA.                endTime will be ignored for "RESUME", and "CLEAR"                endTime can be sent for "PAUSE", in which case it will update the paused endTime            |
|`updateMode`|UpdateMode|True|Enumeration to control the media clock.                In case of pause, resume, or clear, the start time value is ignored and shall be left out.  For resume, the time continues with the same value as it was when paused.            |
|`audioStreamingIndicator`|AudioStreamingIndicator|False|Enumeration for the indicator icon on a play/pause button. see AudioStreamingIndicator.            |


### SetMediaClockTimer
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### PerformAudioPassThru
Message Type: **request**

Starts audio pass thru session 

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`initialPrompt`|TTSChunk[]|False|The module will speak this prompt before opening the audio pass thru session.                An array of text chunks of type TTSChunk. See TTSChunk.                The array must have at least one item.                If omitted, then no initial prompt is spoken.            |
|`audioPassThruDisplayText1`|String|False|First line of text displayed during audio capture.|
|`audioPassThruDisplayText2`|String|False|Second line of text displayed during audio capture.|
|`samplingRate`|SamplingRate|True|This value shall be allowed at 8 kHz or 16 or 22 or 44 kHz.|
|`maxDuration`|Integer|True|The maximum duration of audio recording in milliseconds. |
|`bitsPerSample`|BitsPerSample|True|Specifies the quality the audio is recorded. Currently 8 bit or 16 bit.|
|`audioType`|AudioType|True|Specifies the type of audio data being requested.|
|`muteAudio`|Boolean|False|Defines if the current audio source should be muted during the APT session.  If not, the audio source will play without interruption.                If omitted, the value is set to true.            |


### PerformAudioPassThru
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### EndAudioPassThru
Message Type: **request**

When this request is invoked, the audio capture stops.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|


### EndAudioPassThru
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### SubscribeButton
Message Type: **request**

Subscribes to built-in HMI buttons.
            The application will be notified by the OnButtonEvent and OnButtonPress.
            To unsubscribe the notifications, use unsubscribeButton.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`buttonName`|ButtonName|True|Name of the button to subscribe.|


### SubscribeButton
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### UnsubscribeButton
Message Type: **request**

Unsubscribes from built-in HMI buttons.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`buttonName`|ButtonName|True|Name of the button to unsubscribe.|


### UnsubscribeButton
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### SubscribeVehicleData
Message Type: **request**

Subscribes for specific published data items.
            The data will be only sent if it has changed.
            The application will be notified by the onVehicleData notification whenever new data is available.
            To unsubscribe the notifications, use unsubscribe with the same subscriptionType.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`gps`|Boolean|False|See GPSData|
|`speed`|Boolean|False|The vehicle speed in kilometers per hour|
|`rpm`|Boolean|False|The number of revolutions per minute of the engine|
|`fuelLevel`|Boolean|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|Boolean|False|The fuel level state|
|`instantFuelConsumption`|Boolean|False|The instantaneous fuel consumption in microlitres|
|`fuelRange`|Boolean|False|The estimate range in KM the vehicle can travel based on fuel level and consumption|
|`externalTemperature`|Boolean|False|The external temperature in degrees celsius|
|`turnSignal`|Boolean|False|See TurnSignal|
|`prndl`|Boolean|False|See PRNDL|
|`tirePressure`|Boolean|False|See TireStatus|
|`odometer`|Boolean|False|Odometer in km|
|`beltStatus`|Boolean|False|The status of the seat belts|
|`bodyInformation`|Boolean|False|The body information including power modes|
|`deviceStatus`|Boolean|False|The device status including signal and battery strength|
|`driverBraking`|Boolean|False|The status of the brake pedal|
|`wiperStatus`|Boolean|False|The status of the wipers|
|`headLampStatus`|Boolean|False|Status of the head lamps|
|`engineTorque`|Boolean|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|Boolean|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|Boolean|False|Current angle of the steering wheel (in deg)|
|`engineOilLife`|Boolean|False|The estimated percentage of remaining oil life of the engine.|
|`electronicParkBrakeStatus`|Boolean|False|The status of the park brake as provided by Electric Park Brake (EPB) system.|
|`cloudAppVehicleID`|Boolean|False|Parameter used by cloud apps to identify a head unit|
|`eCallInfo`|Boolean|False|Emergency Call notification and confirmation data|
|`airbagStatus`|Boolean|False|The status of the air bags|
|`emergencyEvent`|Boolean|False|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|Boolean|False|The status modes of the cluster|
|`myKey`|Boolean|False|Information related to the MyKey feature|


### SubscribeVehicleData
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`gps`|VehicleDataResult|False|See GPSData|
|`speed`|VehicleDataResult|False|The vehicle speed in kilometers per hour|
|`rpm`|VehicleDataResult|False|The number of revolutions per minute of the engine|
|`fuelLevel`|VehicleDataResult|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|VehicleDataResult|False|The fuel level state|
|`instantFuelConsumption`|VehicleDataResult|False|The instantaneous fuel consumption in microlitres|
|`fuelRange`|VehicleDataResult|False|The estimate range in KM the vehicle can travel based on fuel level and consumption|
|`externalTemperature`|VehicleDataResult|False|The external temperature in degrees celsius.|
|`turnSignal`|VehicleDataResult|False|See TurnSignal|
|`prndl`|VehicleDataResult|False|See PRNDL|
|`tirePressure`|VehicleDataResult|False|See TireStatus|
|`odometer`|VehicleDataResult|False|Odometer in km|
|`beltStatus`|VehicleDataResult|False|The status of the seat belts|
|`bodyInformation`|VehicleDataResult|False|The body information including power modes|
|`deviceStatus`|VehicleDataResult|False|The device status including signal and battery strength|
|`driverBraking`|VehicleDataResult|False|The status of the brake pedal|
|`wiperStatus`|VehicleDataResult|False|The status of the wipers|
|`headLampStatus`|VehicleDataResult|False|Status of the head lamps|
|`engineTorque`|VehicleDataResult|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|VehicleDataResult|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|VehicleDataResult|False|Current angle of the steering wheel (in deg)|
|`engineOilLife`|VehicleDataResult|False|The estimated percentage of remaining oil life of the engine.|
|`electronicParkBrakeStatus`|VehicleDataResult|False|The status of the park brake as provided by Electric Park Brake (EPB) system.|
|`cloudAppVehicleID`|VehicleDataResult|False|Parameter used by cloud apps to identify a head unit|
|`eCallInfo`|VehicleDataResult|False|Emergency Call notification and confirmation data|
|`airbagStatus`|VehicleDataResult|False|The status of the air bags|
|`emergencyEvent`|VehicleDataResult|False|Information related to an emergency event (and if it occurred)|
|`clusterModes`|VehicleDataResult|False|The status modes of the cluster|
|`myKey`|VehicleDataResult|False|Information related to the MyKey feature|


### UnsubscribeVehicleData
Message Type: **request**

This function is used to unsubscribe the notifications from the subscribeVehicleData function.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`gps`|Boolean|False|See GPSData|
|`speed`|Boolean|False|The vehicle speed in kilometers per hour|
|`rpm`|Boolean|False|The number of revolutions per minute of the engine|
|`fuelLevel`|Boolean|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|Boolean|False|The fuel level state|
|`instantFuelConsumption`|Boolean|False|The instantaneous fuel consumption in microlitres|
|`fuelRange`|Boolean|False|The estimate range in KM the vehicle can travel based on fuel level and consumption|
|`externalTemperature`|Boolean|False|The external temperature in degrees celsius.|
|`turnSignal`|Boolean|False|See TurnSignal|
|`prndl`|Boolean|False|See PRNDL|
|`tirePressure`|Boolean|False|See TireStatus|
|`odometer`|Boolean|False|Odometer in km|
|`beltStatus`|Boolean|False|The status of the seat belts|
|`bodyInformation`|Boolean|False|The body information including power modes|
|`deviceStatus`|Boolean|False|The device status including signal and battery strength|
|`driverBraking`|Boolean|False|The status of the brake pedal|
|`wiperStatus`|Boolean|False|The status of the wipers|
|`headLampStatus`|Boolean|False|Status of the head lamps|
|`engineTorque`|Boolean|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|Boolean|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|Boolean|False|Current angle of the steering wheel (in deg)|
|`engineOilLife`|Boolean|False|The estimated percentage of remaining oil life of the engine.|
|`electronicParkBrakeStatus`|Boolean|False|The status of the park brake as provided by Electric Park Brake (EPB) system.|
|`cloudAppVehicleID`|Boolean|False|Parameter used by cloud apps to identify a head unit|
|`eCallInfo`|Boolean|False|Emergency Call notification and confirmation data|
|`airbagStatus`|Boolean|False|The status of the air bags|
|`emergencyEvent`|Boolean|False|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|Boolean|False|The status modes of the cluster|
|`myKey`|Boolean|False|Information related to the MyKey feature|


### UnsubscribeVehicleData
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`gps`|VehicleDataResult|False|See GPSData|
|`speed`|VehicleDataResult|False|The vehicle speed in kilometers per hour|
|`rpm`|VehicleDataResult|False|The number of revolutions per minute of the engine|
|`fuelLevel`|VehicleDataResult|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|VehicleDataResult|False|The fuel level state|
|`instantFuelConsumption`|VehicleDataResult|False|The instantaneous fuel consumption in microlitres|
|`fuelRange`|VehicleDataResult|False|The estimate range in KM the vehicle can travel based on fuel level and consumption|
|`externalTemperature`|VehicleDataResult|False|The external temperature in degrees celsius|
|`turnSignal`|VehicleDataResult|False|See TurnSignal|
|`prndl`|VehicleDataResult|False|See PRNDL|
|`tirePressure`|VehicleDataResult|False|See TireStatus|
|`odometer`|VehicleDataResult|False|Odometer in km|
|`beltStatus`|VehicleDataResult|False|The status of the seat belts|
|`bodyInformation`|VehicleDataResult|False|The body information including power modes|
|`deviceStatus`|VehicleDataResult|False|The device status including signal and battery strength|
|`driverBraking`|VehicleDataResult|False|The status of the brake pedal|
|`wiperStatus`|VehicleDataResult|False|The status of the wipers|
|`headLampStatus`|VehicleDataResult|False|Status of the head lamps|
|`engineTorque`|VehicleDataResult|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|VehicleDataResult|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|VehicleDataResult|False|Current angle of the steering wheel (in deg)|
|`engineOilLife`|VehicleDataResult|False|The estimated percentage of remaining oil life of the engine.|
|`electronicParkBrakeStatus`|VehicleDataResult|False|The status of the park brake as provided by Electric Park Brake (EPB) system.|
|`cloudAppVehicleID`|VehicleDataResult|False|Parameter used by cloud apps to identify a head unit|
|`eCallInfo`|VehicleDataResult|False|Emergency Call notification and confirmation data|
|`airbagStatus`|VehicleDataResult|False|The status of the air bags|
|`emergencyEvent`|VehicleDataResult|False|Information related to an emergency event (and if it occurred)|
|`clusterModes`|VehicleDataResult|False|The status modes of the cluster|
|`myKey`|VehicleDataResult|False|Information related to the MyKey feature|


### GetVehicleData
Message Type: **request**

Non periodic vehicle data read request.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`gps`|Boolean|False|See GPSData|
|`speed`|Boolean|False|The vehicle speed in kilometers per hour|
|`rpm`|Boolean|False|The number of revolutions per minute of the engine|
|`fuelLevel`|Boolean|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|Boolean|False|The fuel level state|
|`instantFuelConsumption`|Boolean|False|The instantaneous fuel consumption in microlitres|
|`fuelRange`|Boolean|False|The estimate range in KM the vehicle can travel based on fuel level and consumption|
|`externalTemperature`|Boolean|False|The external temperature in degrees celsius|
|`turnSignal`|Boolean|False|See TurnSignal|
|`vin`|Boolean|False|Vehicle identification number|
|`prndl`|Boolean|False|See PRNDL|
|`tirePressure`|Boolean|False|See TireStatus|
|`odometer`|Boolean|False|Odometer in km|
|`beltStatus`|Boolean|False|The status of the seat belts|
|`bodyInformation`|Boolean|False|The body information including ignition status and internal temp|
|`deviceStatus`|Boolean|False|The device status including signal and battery strength|
|`driverBraking`|Boolean|False|The status of the brake pedal|
|`wiperStatus`|Boolean|False|The status of the wipers|
|`headLampStatus`|Boolean|False|Status of the head lamps|
|`engineTorque`|Boolean|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|Boolean|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|Boolean|False|Current angle of the steering wheel (in deg)|
|`engineOilLife`|Boolean|False|The estimated percentage of remaining oil life of the engine.|
|`electronicParkBrakeStatus`|Boolean|False|The status of the park brake as provided by Electric Park Brake (EPB) system.|
|`cloudAppVehicleID`|Boolean|False|Parameter used by cloud apps to identify a head unit|
|`eCallInfo`|Boolean|False|Emergency Call notification and confirmation data|
|`airbagStatus`|Boolean|False|The status of the air bags|
|`emergencyEvent`|Boolean|False|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|Boolean|False|The status modes of the cluster|
|`myKey`|Boolean|False|Information related to the MyKey feature|


### GetVehicleData
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`gps`|GPSData|False|See GPSData|
|`speed`|Float|False|The vehicle speed in kilometers per hour|
|`rpm`|Integer|False|The number of revolutions per minute of the engine|
|`fuelLevel`|Float|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|ComponentVolumeStatus|False|The fuel level state|
|`instantFuelConsumption`|Float|False|The instantaneous fuel consumption in microlitres|
|`fuelRange`|FuelRange[]|False|The estimate range in KM the vehicle can travel based on fuel level and consumption|
|`externalTemperature`|Float|False|The external temperature in degrees celsius|
|`turnSignal`|TurnSignal|False|See TurnSignal|
|`vin`|String|False|Vehicle identification number|
|`prndl`|PRNDL|False|See PRNDL|
|`tirePressure`|TireStatus|False|See TireStatus|
|`odometer`|Integer|False|Odometer in km|
|`beltStatus`|BeltStatus|False|The status of the seat belts|
|`bodyInformation`|BodyInformation|False|The body information including power modes|
|`deviceStatus`|DeviceStatus|False|The device status including signal and battery strength|
|`driverBraking`|VehicleDataEventStatus|False|The status of the brake pedal|
|`wiperStatus`|WiperStatus|False|The status of the wipers|
|`headLampStatus`|HeadLampStatus|False|Status of the head lamps|
|`engineTorque`|Float|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|Float|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|Float|False|Current angle of the steering wheel (in deg)|
|`engineOilLife`|Float|False|The estimated percentage of remaining oil life of the engine.|
|`electronicParkBrakeStatus`|ElectronicParkBrakeStatus|False|The status of the park brake as provided by Electric Park Brake (EPB) system.|
|`cloudAppVehicleID`|String|False|Parameter used by cloud apps to identify a head unit|
|`eCallInfo`|ECallInfo|False|Emergency Call notification and confirmation data|
|`airbagStatus`|AirbagStatus|False|The status of the air bags|
|`emergencyEvent`|EmergencyEvent|False|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|ClusterModeStatus|False|The status modes of the cluster|
|`myKey`|MyKey|False|Information related to the MyKey feature|


### ReadDID
Message Type: **request**

Non periodic vehicle data read request

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`ecuName`|Integer|True|Name of ECU.|
|`didLocation`|Integer[]|True|Get raw data from vehicle data DID location(s)|


### ReadDID
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`didResult`|DIDResult[]|False|Array of requested DID results (with data if available).|


### GetDTCs
Message Type: **request**

Vehicle module diagnostic trouble code request.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`ecuName`|Integer|True|Name of ECU.|
|`dtcMask`|Integer|False|DTC Mask Byte to be sent in diagnostic request to module .|


### GetDTCs
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`ecuHeader`|Integer|False|2 byte ECU Header for DTC response (as defined in VHR_Layout_Specification_DTCs.pdf)|
|`dtc`|String[]|False|Array of all reported DTCs on module (ecuHeader contains information if list is truncated).                Each DTC is represented by 4 bytes (3 bytes of data and 1 byte status as defined in VHR_Layout_Specification_DTCs.pdf).            |


### DiagnosticMessage
Message Type: **request**

Non periodic vehicle diagnostic request

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`targetID`|Integer|True|Name of target ECU.|
|`messageLength`|Integer|True|Length of message (in bytes).|
|`messageData`|Integer[]|True|Array of bytes comprising CAN message.            |


### DiagnosticMessage
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`messageDataResult`|Integer[]|False|Array of bytes comprising CAN message result.            |


### ScrollableMessage
Message Type: **request**

Creates a full screen overlay containing a large block of formatted text that can be scrolled with up to 8 SoftButtons defined

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`scrollableMessageBody`|String|True|Body of text that can include newlines and tabs.|
|`timeout`|Integer|False|App defined timeout.  Indicates how long of a timeout from the last action (i.e. scrolling message resets timeout).|
|`softButtons`|SoftButton[]|False|App defined SoftButtons.                If omitted on supported displays, only the system defined "Close" SoftButton will be displayed.            |


### ScrollableMessage
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### Slider
Message Type: **request**

Creates a full screen or pop-up overlay (depending on platform) with a single user controlled slider.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`numTicks`|Integer|True|Number of selectable items on a horizontal axis|
|`position`|Integer|True|Initial position of slider control (cannot exceed numTicks)|
|`sliderHeader`|String|True|Text header to display|
|`sliderFooter`|String[]|False|Text footer to display (meant to display min/max threshold descriptors).                For a static text footer, only one footer string shall be provided in the array.                For a dynamic text footer, the number of footer text string in the array must match the numTicks value.                For a dynamic text footer, text array string should correlate with potential slider position index.                If omitted on supported displays, no footer text shall be displayed.            |
|`timeout`|Integer|False|App defined timeout.  Indicates how long of a timeout from the last action (i.e. sliding control resets timeout).                If omitted, the value is set to 10000.            |


### Slider
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`sliderPosition`|Integer|False|Current slider value returned when saved or canceled (aborted)                This value is only returned for resultCodes "SAVED" or "ABORTED"            |


### ShowConstantTBT
Message Type: **request**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`navigationText1`|String|False||
|`navigationText2`|String|False||
|`eta`|String|False||
|`timeToDestination`|String|False||
|`totalDistance`|String|False||
|`turnIcon`|Image|False||
|`nextTurnIcon`|Image|False||
|`distanceToManeuver`|Float|False|Fraction of distance till next maneuver (starting from when AlertManeuver is triggered).                Used to calculate progress bar.            |
|`distanceToManeuverScale`|Float|False|Distance till next maneuver (starting from) from previous maneuver.                Used to calculate progress bar.            |
|`maneuverComplete`|Boolean|False|If and when a maneuver has completed while an AlertManeuver is active, the app must send this value set to TRUE in order to clear the AlertManeuver overlay.                If omitted the value will be assumed as FALSE.            |
|`softButtons`|SoftButton[]|False|Three dynamic SoftButtons available (first SoftButton is fixed to "Turns").                If omitted on supported displays, the currently displayed SoftButton values will not change.            |


### ShowConstantTBT
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### AlertManeuver
Message Type: **request**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`ttsChunks`|TTSChunk[]|False|An array of text chunks of type TTSChunk. See TTSChunk|
|`softButtons`|SoftButton[]|False|If omitted on supported displays, only the system defined "Close" SoftButton shall be displayed.|


### AlertManeuver
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### UpdateTurnList
Message Type: **request**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`turnList`|Turn[]|False||
|`softButtons`|SoftButton[]|False|If omitted on supported displays, app-defined SoftButton will be left blank.|


### UpdateTurnList
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### ChangeRegistration
Message Type: **request**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`language`|Language|True|Requested voice engine (VR+TTS) language registration|
|`hmiDisplayLanguage`|Language|True|Request display language registration|
|`appName`|String|False|Request new app name registration|
|`ttsName`|TTSChunk[]|False|Request new ttsName registration|
|`ngnMediaScreenAppName`|String|False|Request new app short name registration|
|`vrSynonyms`|String[]|False|Request new VR synonyms registration|


### ChangeRegistration
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful                false, if failed            |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### GenericResponse
Message Type: **response**

Generic Response is sent, when the name of a received msg cannot be retrieved. Only used in case of an error.
            Currently, only resultCode INVALID_DATA is used.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### PutFile
Message Type: **request**

Used to push a binary data onto the module from a mobile device, such as icons and album art
            Not supported on first generation of SDL enabled modules.
            Binary data is in binary part of hybrid msg.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`syncFileName`|String|True|File reference name.|
|`fileType`|FileType|True|Selected file type.|
|`persistentFile`|Boolean|False|Indicates if the file is meant to persist between sessions / ignition cycles.                If set to TRUE, then the system will aim to persist this file through session / cycles.                While files with this designation will have priority over others, they are subject to deletion by the system at any time.                In the event of automatic deletion by the system, the app will receive a rejection and have to resend the file.                If omitted, the value will be set to false.            |
|`systemFile`|Boolean|False|Indicates if the file is meant to be passed thru core to elsewhere on the system.                If set to TRUE, then the system will instead pass the data thru as it arrives to a predetermined area outside of core.                If omitted, the value will be set to false.            |
|`offset`|Integer|False|Optional offset in bytes for resuming partial data chunks|
|`length`|Integer|False|Optional length in bytes for resuming partial data chunks                If offset is set to 0, then length is the total length of the file to be downloaded            |
|`crc`|Integer|False|Additional CRC32 checksum to protect data integrity up to 512 Mbits |


### PutFile
Message Type: **response**

Response is sent, when the file data was copied (success case). Or when an error occurred.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`spaceAvailable`|Integer|False|Provides the total local space available in SDL Core for the registered app.                If the transfer has systemFile enabled, then the value will be set to 0 automatically.            |
|`info`|String|False|Provides additional human readable info regarding the result.|


### GetFile
Message Type: **request**

This request is sent to the module to retrieve a file

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`fileName`|String|True|File name that should be retrieved|
|`appServiceId`|String|False|ID of the service that should have uploaded the requested file.|
|`fileType`|FileType|False|Selected file type.|
|`offset`|Integer|False|Optional offset in bytes for resuming partial data chunks|
|`length`|Integer|False|Optional length in bytes for resuming partial data chunks                If offset is set to 0, then length is the total length of the file to be retrieved            |


### GetFile
Message Type: **response**

This response includes the data that is requested from the specific service

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`offset`|Integer|False|Optional offset in bytes for resuming partial data chunks|
|`length`|Integer|False|Optional length in bytes for resuming partial data chunks if offset is set to 0, then length is the total length of the file to be downloaded|
|`fileType`|FileType|False|File type that is being sent in response.|
|`crc`|Integer|False|Additional CRC32 checksum to protect data integrity up to 512 Mbits|


### DeleteFile
Message Type: **request**

Used to delete a file resident on the module in the app's local cache.
            Not supported on first generation SDL enabled vehicles.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`syncFileName`|String|True|File reference name.|


### DeleteFile
Message Type: **response**

Response is sent, when the file data was deleted (success case). Or when an error occurred.
            Not supported on First generation SDL enabled vehicles.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`spaceAvailable`|Integer|False|Provides the total local space available on the module for the registered app.|
|`info`|String|False|Provides additional human readable info regarding the result.|


### ListFiles
Message Type: **request**

Requests the current list of resident filenames for the registered app.
            Not supported on first generation SDL enabled vehicles.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|


### ListFiles
Message Type: **response**

Returns the current list of resident filenames for the registered app along with the current space available
            Not supported on First generation SDL enabled vehicles.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`filenames`|String[]|False|An array of all filenames resident on the module for the given registered app.                If omitted, then no files currently reside on the system.            |
|`spaceAvailable`|Integer|False|Provides the total local space available on the module for the registered app.|
|`info`|String|False|Provides additional human readable info regarding the result.|


### SetAppIcon
Message Type: **request**

Used to set existing local file on the module as the app's icon
            Not supported on first generation SDL enabled vehicles.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`syncFileName`|String|True|File reference name.|


### SetAppIcon
Message Type: **response**

Response is sent, when the file data was copied (success case). Or when an error occurred.
            Not supported on First generation SDL enabled vehicles.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### SetDisplayLayout
Message Type: **request**

This RPC is deprecated. Use Show RPC to change layout.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`displayLayout`|String|True|Predefined or dynamically created screen layout.                Currently only predefined screen layouts are defined.            |
|`dayColorScheme`|TemplateColorScheme|False||
|`nightColorScheme`|TemplateColorScheme|False||


### SetDisplayLayout
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`displayCapabilities`|DisplayCapabilities|False|See DisplayCapabilities|
|`buttonCapabilities`|ButtonCapabilities[]|False|See ButtonCapabilities|
|`softButtonCapabilities`|SoftButtonCapabilities[]|False|If returned, the platform supports on-screen SoftButtons; see SoftButtonCapabilities.|
|`presetBankCapabilities`|PresetBankCapabilities|False|If returned, the platform supports custom on-screen Presets; see PresetBankCapabilities.|
|`info`|String|False|Provides additional human readable info regarding the result.|


### SystemRequest
Message Type: **request**

An asynchronous request from the device; binary data can be included in hybrid part of message for some requests (such as HTTP, Proprietary, or Authentication requests)

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`requestType`|RequestType|True|The type of system request.                Note that Proprietary requests should forward the binary data to the known proprietary module on the system.            |
|`requestSubType`|String|False|This parameter is filled for supporting OEM proprietary data exchanges.            |
|`fileName`|String|False|Filename of HTTP data to store in predefined system staging area.                Mandatory if requestType is HTTP.                PROPRIETARY requestType should ignore this parameter.            |


### SystemRequest
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|


### SendLocation
Message Type: **request**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`longitudeDegrees`|Float|False||
|`latitudeDegrees`|Float|False||
|`locationName`|String|False|Name / title of intended location            |
|`locationDescription`|String|False|Description intended location / establishment (if applicable)            |
|`addressLines`|String[]|False|Location address (if applicable)            |
|`phoneNumber`|String|False|Phone number of intended location / establishment (if applicable)            |
|`locationImage`|Image|False|Image / icon of intended location (if applicable and supported)            |
|`timeStamp`|DateTime|False|timestamp in ISO 8601 format            |
|`address`|OASISAddress|False|Address to be used for setting destination|
|`deliveryMode`|DeliveryMode|False|Defines the mode of prompt for user|


### SendLocation
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### DialNumber
Message Type: **request**

Dials a phone number and switches to phone application.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`number`|String|True|Phone number is a string, which can be up to 40 chars.                All characters shall be stripped from string except digits 0-9 and * # , ; +            |


### DialNumber
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful|
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### ButtonPress
Message Type: **request**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleType`|ModuleType|True|The module where the button should be pressed|
|`moduleId`|String|False|Id of a module, published by System Capability.|
|`buttonName`|ButtonName|True|The name of supported RC climate or radio button.|
|`buttonPressMode`|ButtonPressMode|True|Indicates whether this is a LONG or SHORT button press event.|


### ButtonPress
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`resultCode`|Result|True|See Result|
|`info`|String|False||
|`success`|Boolean|True|true if successful; false, if failed |


### GetInteriorVehicleData
Message Type: **request**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleType`|ModuleType|True|The type of a RC module to retrieve module data from the vehicle.                In the future, this should be the Identification of a module.            |
|`moduleId`|String|False|Id of a module, published by System Capability.|
|`subscribe`|Boolean|False| If subscribe is true, the head unit will register OnInteriorVehicleData notifications for the requested module (moduleId and moduleType).
If subscribe is false, the head unit will unregister OnInteriorVehicleData notifications for the requested module (moduleId and moduleType).
If subscribe is not included, the subscription status of the app for the requested module (moduleId and moduleType) will remain unchanged.|


### GetInteriorVehicleData
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleData`|ModuleData|False||
|`resultCode`|Result|True|See Result|
|`info`|String|False||
|`success`|Boolean|True|true if successful; false, if failed |
|`isSubscribed`|Boolean|False|It is a conditional-mandatory parameter: must be returned in case "subscribe" parameter was present in the related request.                if "true" - the "moduleType" from request is successfully subscribed and the head unit will send onInteriorVehicleData notifications for the moduleType.                if "false" - the "moduleType" from request is either unsubscribed or failed to subscribe.            |

### GetInteriorVehicleDataConsent
Message Type: **request**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleType`|ModuleType|True|The module type that the app requests to control.    |
|`moduleIds`|String[]|True|Ids of a module of same type, published by System Capability. |


### GetInteriorVehicleDataConsent
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`allowed`|Boolean[]|True|This array has the same size as "moduleIds" in the request; each element corresponding to one moduleId  
"true" - if SDL grants the permission for the requested module;
"false" - SDL denies the permission for the requested module.|
|`resultCode`|Result|True|See Result|
|`info`|String|False||
|`success`|Boolean|True|true if successful; false, if failed |


### ReleaseInteriorVehicleDataModule
Message Type: **request**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleType`|ModuleType|True||
|`moduleId`|String|False|Id of a module, published by System Capability.|


### ReleaseInteriorVehicleDataModule
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`resultCode`|Result|True|See Result|
|`info`|String|False||
|`success`|Boolean|True|true if successful; false, if failed |


### SetInteriorVehicleData
Message Type: **request**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleData`|ModuleData|True|The module data to set for the requested RC module.|


### SetInteriorVehicleData
Message Type: **response**

Used to set the values of one remote control module 

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleData`|ModuleData|False||
|`resultCode`|Result|True|See Result|
|`info`|String|False||
|`success`|Boolean|True|true if successful; false, if failed |


### SubscribeWayPoints
Message Type: **request**

To subscribe in getting changes for Waypoints/destinations

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|


### SubscribeWayPoints
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### GetWayPoints
Message Type: **request**

Request for getting waypoint/destination data.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`wayPointType`|WayPointType|True|To request for either the destination only or for all waypoints including destination|


### GetWayPoints
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`wayPoints`|LocationDetails[]|False|See LocationDetails|


### UnsubscribeWayPoints
Message Type: **request**

Request to unsubscribe from WayPoints and Destination

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|


### UnsubscribeWayPoints
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`wayPoints`|LocationDetails[]|False|See LocationDetails|


### GetSystemCapability
Message Type: **request**

Request for expanded information about a supported system/HMI capability

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`systemCapabilityType`|SystemCapabilityType|True|The type of system capability to get more information on|
|`subscribe`|Boolean|False|Flag to subscribe to updates of the supplied service capability type. If true, the requester will be subscribed. If false, the requester will not be subscribed and be removed as a subscriber if it was previously subscribed.|


### GetSystemCapability
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`systemCapability`|SystemCapability|False||
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`success`|Boolean|True|true if successful; false, if failed |


### SendHapticData
Message Type: **request**

Send the spatial data gathered from SDLCarWindow or VirtualDisplayEncoder to the HMI. This data will be utilized by the HMI to determine how and when haptic events should occur

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`hapticRectData`|HapticRect[]|False|Array of spatial data structures that represent the locations of all user controls present on the HMI. This data should be updated if/when the application presents a new screen. When a request is sent, if successful, it will replace all spatial data previously sent through RPC. If an empty array is sent, the existing spatial data will be cleared|


### SendHapticData
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false if failed |
|`info`|String|False|Provides additional human readable info regarding the result.|
|`resultCode`|Result|True|See Result|


### SetCloudAppProperties
Message Type: **request**

RPC used to enable/disable a cloud application and set its cloud-related policy properties
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`properties`|CloudAppProperties|True|The new cloud application properties |


### SetCloudAppProperties
Message Type: **response**

The response to SetCloudAppProperties

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### GetCloudAppProperties
Message Type: **request**

RPC used to get the current properties of a cloud application
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`appID`|String|True||


### GetCloudAppProperties
Message Type: **response**

The response to GetCloudAppProperties

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`properties`|CloudAppProperties|False|The requested cloud application properties |
|`success`|Boolean|True|true if successful; false if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### PublishAppService
Message Type: **request**

Registers a service offered by this app on the module

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`appServiceManifest`|AppServiceManifest|True|The manifest of the service that wishes to be published.|


### PublishAppService
Message Type: **response**

Response to the request to register a service offered by this app on the module

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`appServiceRecord`|AppServiceRecord|False|If the request was successful, this object will be the current status of the service record for the published service. This will include the Core supplied service ID.|


### GetAppServiceData
Message Type: **request**

This request asks the module for current data related to the specific service. It also includes an option to subscribe to that service for future updates

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`serviceType`|String|True|The type of service that is to be offered by this app. See AppServiceType for known enum equivalent types. Parameter is a string to allow for new service types to be used by apps on older versions of SDL Core.|
|`subscribe`|Boolean|False|If true, the consumer is requesting to subscribe to all future updates from the service publisher. If false, the consumer doesn't wish to subscribe and should be unsubscribed if it was previously subscribed.|


### GetAppServiceData
Message Type: **response**

This response includes the data that was requested from the specific service

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`serviceData`|AppServiceData|False||


### PerformAppServiceInteraction
Message Type: **request**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`serviceUri`|String|True|Fully qualified URI based on a predetermined scheme provided by the app service. SDL makes no guarantee that this URI is correct.|
|`serviceID`|String|True|The service ID that the app consumer wishes to send this URI.|
|`originApp`|String|True|This string is the appID of the app requesting the app service provider take the specific action.|
|`requestServiceActive`|Boolean|False|This flag signals the requesting consumer would like this service to become the active primary service of the destination's type.|


### PerformAppServiceInteraction
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result. All results will be available for this response.|
|`info`|String|False|Provides additional human readable info regarding the result.|
|`serviceSpecificResult`|String|False|The service can provide specific result strings to the consumer through this param.|


### CloseApplication
Message Type: **request**

Request from the application to exit the foreground and enter HMI_NONE.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|


### CloseApplication
Message Type: **response**

|`cancelID`|Integer|False|The ID of the specific interaction you want to dismiss. If not set, the most recent of the RPC type set in functionID will be dismissed.|
|`functionID`|Integer|True|The ID of the type of interaction the developer wants to dismiss. Only values 10, (PerformInteractionID), 12 (AlertID), 25 (ScrollableMessageID), and 26 (SliderID) are permitted.|

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True||
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### CancelInteraction
Message Type: **request**

Close an active interaction on the HMI.


##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|

|`cancelID`|Integer|False|The ID of the specific interaction you want to dismiss. If not set, the most recent of the RPC type set in functionID will be dismissed.|
|`functionID`|Integer|True|The ID of the type of interaction the developer wants to dismiss. Only values 10, (PerformInteractionID), 12 (AlertID), 25 (ScrollableMessageID), and 26 (SliderID) are permitted.|


### CancelInteraction
Message Type: **response**

If no applicable request can be dismissed, the result will be IGNORED.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true if successful; false, if failed |
|`resultCode`|Result|True||
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### OnHMIStatus
Message Type: **notification**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`hmiLevel`|HMILevel|True|See HMILevel|
|`audioStreamingState`|AudioStreamingState|True|See AudioStreamingState|
|`systemContext`|SystemContext|True|See SystemContext|
|`videoStreamingState`|VideoStreamingState|False|See VideoStreamingState.                 If it is NOT_STREAMABLE, the app must stop streaming video to SDL Core(stop service).            |
|`windowID`|Integer|False|This is the unique ID assigned to the window that this RPC is intended. If this param is not included, it will be assumed that this request is specifically for the main window on the main display. See PredefinedWindows enum.|


### OnAppInterfaceUnregistered
Message Type: **notification**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`reason`|AppInterfaceUnregisteredReason|True|See AppInterfaceUnregisteredReason|


### OnButtonEvent
Message Type: **notification**

Notifies application of UP/DOWN events for buttons to which the application is subscribed.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`buttonName`|ButtonName|True||
|`buttonEventMode`|ButtonEventMode|True|Indicates whether this is an UP or DOWN event.|
|`customButtonID`|Integer|False|If ButtonName is "CUSTOM_BUTTON", this references the integer ID passed by a custom button. (e.g. softButton ID)|


### OnButtonPress
Message Type: **notification**

Notifies application of LONG/SHORT press events for buttons to which the application is subscribed.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`buttonName`|ButtonName|True||
|`buttonPressMode`|ButtonPressMode|True|Indicates whether this is a LONG or SHORT button press event.|
|`customButtonID`|Integer|False|If ButtonName is "CUSTOM_BUTTON", this references the integer ID passed by a custom button. (e.g. softButton ID)|


### OnVehicleData
Message Type: **notification**

Callback for the periodic and non periodic vehicle data read function.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`gps`|GPSData|False|See GPSData|
|`speed`|Float|False|The vehicle speed in kilometers per hour|
|`rpm`|Integer|False|The number of revolutions per minute of the engine|
|`fuelLevel`|Float|False|The fuel level in the tank (percentage)|
|`fuelLevel_State`|ComponentVolumeStatus|False|The fuel level state|
|`instantFuelConsumption`|Float|False|The instantaneous fuel consumption in microlitres|
|`fuelRange`|FuelRange[]|False|The estimate range in KM the vehicle can travel based on fuel level and consumption|
|`externalTemperature`|Float|False|The external temperature in degrees celsius|
|`turnSignal`|TurnSignal|False|See TurnSignal|
|`vin`|String|False|Vehicle identification number.|
|`prndl`|PRNDL|False|See PRNDL|
|`tirePressure`|TireStatus|False|See TireStatus|
|`odometer`|Integer|False|Odometer in km|
|`beltStatus`|BeltStatus|False|The status of the seat belts|
|`bodyInformation`|BodyInformation|False|The body information including power modes|
|`deviceStatus`|DeviceStatus|False|The device status including signal and battery strength|
|`driverBraking`|VehicleDataEventStatus|False|The status of the brake pedal|
|`wiperStatus`|WiperStatus|False|The status of the wipers|
|`headLampStatus`|HeadLampStatus|False|Status of the head lamps|
|`engineTorque`|Float|False|Torque value for engine (in Nm) on non-diesel variants|
|`accPedalPosition`|Float|False|Accelerator pedal position (percentage depressed)|
|`steeringWheelAngle`|Float|False|Current angle of the steering wheel (in deg)|
|`engineOilLife`|Float|False|The estimated percentage of remaining oil life of the engine.|
|`electronicParkBrakeStatus`|ElectronicParkBrakeStatus|False|The status of the park brake as provided by Electric Park Brake (EPB) system.|
|`cloudAppVehicleID`|String|False|Parameter used by cloud apps to identify a head unit|
|`eCallInfo`|ECallInfo|False|Emergency Call notification and confirmation data|
|`airbagStatus`|AirbagStatus|False|The status of the air bags|
|`emergencyEvent`|EmergencyEvent|False|Information related to an emergency event (and if it occurred)|
|`clusterModeStatus`|ClusterModeStatus|False|The status modes of the cluster|
|`myKey`|MyKey|False|Information related to the MyKey feature|


### OnCommand
Message Type: **notification**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`cmdID`|Integer|True|Command ID, which is related to a specific menu entry|
|`triggerSource`|TriggerSource|True|See TriggerSource|


### OnTBTClientState
Message Type: **notification**

Provides applications with notifications specific to the current TBT client status on the module

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`state`|TBTState|True|Current State of TBT client|


### OnDriverDistraction
Message Type: **notification**

Provides driver distraction state to mobile applications

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`state`|DriverDistractionState|True|Current State of Driver Distraction|
|`lockScreenDismissalEnabled`|Boolean|False|If enabled, the lock screen will be able to be dismissed while connected to SDL, allowing users                 the ability to interact with the app. Dismissals should include a warning to the user and ensure                 that they are not the driver.            |
|`lockScreenDismissalWarning`|String|False|Warning message to be displayed on the lock screen when dismissal is enabled.                This warning should be used to ensure that the user is not the driver of the vehicle,                 ex. `Swipe down to dismiss, acknowledging that you are not the driver.`.                This parameter must be present if "lockScreenDismissalEnabled" is set to true.            |


### OnPermissionsChange
Message Type: **notification**

Provides update to app of which policy-table-enabled functions are available

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`permissionItem`|PermissionItem[]|True|Change in permissions for a given set of RPCs|


### OnAudioPassThru
Message Type: **notification**

Binary data is in binary part of hybrid msg

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|


### OnLanguageChange
Message Type: **notification**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`language`|Language|True|Current SDL voice engine (VR+TTS) language|
|`hmiDisplayLanguage`|Language|True|Current display language|


### OnKeyboardInput
Message Type: **notification**

On-screen keyboard event.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`event`|KeyboardEvent|True|On-screen keyboard input data.|
|`data`|String|False|On-screen keyboard input data.|


### OnTouchEvent
Message Type: **notification**

Notifies about touch events on the screen's prescribed area

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`type`|TouchType|True|The type of touch event.|
|`event`|TouchEvent[]|True|List of all individual touches involved in this event.|


### OnSystemRequest
Message Type: **notification**

An asynchronous request from the system for specific data from the device or the cloud or response to a request from the device or cloud
            Binary data can be included in hybrid part of message for some requests (such as Authentication request responses)
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`requestType`|RequestType|True|The type of system request.|
|`requestSubType`|String|False|This parameter is filled for supporting OEM proprietary data exchanges.            |
|`url`|String|False|Optional URL for HTTP requests.                If blank, the binary data shall be forwarded to the app.                If not blank, the binary data shall be forwarded to the url with a provided timeout in seconds.            |
|`timeout`|Integer|False|Optional timeout for HTTP requests                Required if a URL is provided            |
|`fileType`|FileType|False|Optional file type (meant for HTTP file requests).|
|`offset`|Integer|False|Optional offset in bytes for resuming partial data chunks|
|`length`|Integer|False|Optional length in bytes for resuming partial data chunks|


### OnHashChange
Message Type: **notification**

Notification containing an updated hashID which can be used over connection cycles (i.e. loss of connection, ignition cycles, etc.).
            Sent after initial registration and subsequently after any change in the calculated hash of all persisted app data.
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`hashID`|String|True|Calculated hash ID to be referenced during RegisterAppInterface.|


### OnWayPointChange
Message Type: **notification**

Notification which provides the entire LocationDetails when there is a change to any waypoints or destination.

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`wayPoints`|LocationDetails[]|True|See LocationDetails|


### OnInteriorVehicleData
Message Type: **notification**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`moduleData`|ModuleData|True||


### OnRCStatus
Message Type: **notification**

Issued by SDL to notify the application about remote control status change on SDL

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`allowed`|Boolean|False|If "true" - RC is allowed; if "false" - RC is disallowed.|
|`allocatedModules`|ModuleData[]|True|Contains a list (zero or more) of module types that are allocated to the application.|
|`freeModules`|ModuleData[]|True|Contains a list (zero or more) of module types that are free to access for the application.|


### OnAppServiceData
Message Type: **notification**

This notification includes the data that is updated from the specific service

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`serviceData`|AppServiceData|True||


### OnSystemCapabilityUpdated
Message Type: **notification**

A notification between HMI and SDL that a specific system capability has been changed. It can be sent in both directions SDL to HMI and HMI to SDL. Direction is dependent on the point where capabilities have been changed

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`systemCapability`|SystemCapability|True|The system capability that has been updated|
|`appID`|Integer|False|ID of application that is related to this RPC.|


### EncodedSyncPData
Message Type: **request**

Allows encoded data in the form of SyncP packets to be sent to the SYNC module.
            Legacy / v1 Protocol implementation; use SyncPData instead.
            *** DEPRECATED ***
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`data`|String[]|True|Contains base64 encoded string of SyncP packets.|


### EncodedSyncPData
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`resultCode`|Result|True|See Result|
|`info`|String|False|Provides additional human readable info regarding the result.|


### OnEncodedSyncPData
Message Type: **notification**

Callback including encoded data of any SyncP packets that SYNC needs to send back to the mobile device.
            Legacy / v1 Protocol implementation; responds to EncodedSyncPData.
            *** DEPRECATED ***
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`data`|String[]|True|Contains base64 encoded string of SyncP packets.|
|`URL`|String|False|If blank, the SyncP data shall be forwarded to the app.                If not blank, the SyncP data shall be forwarded to the provided URL.            |
|`Timeout`|Integer|False|If blank, the SyncP data shall be forwarded to the app.                If not blank, the SyncP data shall be forwarded with the provided timeout in seconds.            |

### CreateWindow
Message Type: **request**

Create a new window on the display with the specified window type.
            
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`windowID`|Integer|A unique ID to identify the window. The value of '0' will always be the default main window on the main display and should not be used in this context as it will already be created for the app. See PredefinedWindows enum. Creating a window with an ID that is already in use will be rejected with `INVALID_ID`..|
|`windowName`|String[]|True|The window name to be used by the HMI. The name of the pre-created default window will match the app name. Multiple apps can share the same window name except for the default main window. Creating a window with a name which is already in use by the app will result in `DUPLICATE_NAME`..|
|`type`|WindowType|True|The type of the window to be created. Main window or widget.|
|`associatedServiceType`|String[]|False|Allows an app to create a widget related to a specific service type.As an example if a `MEDIA` app becomes active, this app becomes audible and is allowed to play audio. Actions such as skip or play/pause will be directed to this active media app. In case of widgets, the system can provide a single "media" widget which will act as a placeholder for the active media app.

It is only allowed to have one window per service type. This means that a media app can only have a single MEDIA widget. Still the app can create widgets omitting this parameter. Those widgets would be available as app specific widgets that are permanently included in the HMI.

This parameter is related to widgets only. The default main windwhich is pre-created during app registration, will be created basedthe HMI types specified in the app registration request.|
|`duplicateUpdatesFromWindowID`|Integer|False|Optional parameter. Specify whether the content sent to an existing window should be duplicated to the created window.
If there isn't a window with the ID, the request will be rejected with `INVALID_DATA`.|



### CreateWindow
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`info`|String|False|Provides additional human readable info regarding the result.|
|`resultCode`|Result|True|See Result|

### DeleteWindow
Message Type: **request**

Deletes previously created window of the SDL application.
            
        

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`windowID`|Integer|A unique ID to identify the window. The value of '0' will always be the default main window on the main display and should not be used in this context as it will already be created for the app. See PredefinedWindows enum. Creating a window with an ID that is already in use will be rejected with `INVALID_ID`..|


### DeleteWindow
Message Type: **response**

##### Parameters

| Value |  Type | Mandatory | Description | 
| ---------- | ---------- |:-----------: |:-----------:|
|`success`|Boolean|True|true, if successful; false, if failed |
|`info`|String|False|Provides additional human readable info regarding the result.|
|`resultCode`|Result|True|See Result|
https://github.com/mked-luxoft/rpc_spec.git