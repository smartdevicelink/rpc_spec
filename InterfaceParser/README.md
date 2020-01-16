# Parser types
Different parser types implemented in Interface Parser for parsing different types of source XML and generating the code in SDL_core project.
| Parser | Source file |
| sdlrpcv1 | sdl_core/src/components/interfaces/v4_protocol_v1_2_no_extra.xml |
| sdlrpcv2 | sdl_core/src/components/interfaces/MOBILE_API.xml |
| jsonrpc | sdl_core/src/components/interfaces/HMI_API.xml |
| mobile-policy-types | sdl_core/src/components/interfaces/MOBILE_API.xml |
| hmi-policy-types | sdl_core/src/components/interfaces/HMI_API.xml |

# `MOBILE_RPC.xml` structure

## Overview
This document contains the description of the `MOBILE_API.xml` structure in order of preparation specification and transformation rules for Proxy Library RPC Generation. This is not a full XML specification and only elements and attributes required for the code generation are described here. For the full specification see MOBILE_API.xsd.

## `<interface>`
The root element is the `<interface>`. The `<interface>` contains any number of `<enum>`, `<struct>` and `<function>`.

Example:
```xml
<interface name="string" version="string" minVersion="string" date="string">
  <!--Zero or more repetitions:-->
  <enum/>
  <!--Zero or more repetitions:-->
  <struct/>
  <!--Zero or more repetitions:-->
  <function/>
</interface>
```

## `<enum>`
The `<enum>` element contains any number of `<element>` that represents a set of possible values. The `<enum>` has a required `"name"` attribute.

Example:
```xml
<enum deprecated="boolean" internal_scope="string" name="string" platform="string" since="string" until="string">
  <!--Zero or more repetitions:-->
  <description>string</description>
  <!--Zero or more repetitions:-->
 <element hexvalue="string" internal_name="string" name="string" rootscreen="boolean" since="string" value="integer">
    <!--Zero or more repetitions:-->
    <description>string</description>
    <!--Zero or more repetitions:-->
    <warning>string</warning>
  </element>
  <!--Optional:-->
  <history>
    <enum/>
  </history>
</enum>
```
SDL has two different enum types: `string` and `integer`. If `"hexvalue"` or `"value"` attribute exists, the enum type is `integer`, otherwise the enum type is `string`.

The `<element>` has a required `"name"` attribute. For `string` enums, the value of `"name"` attribute will be one of the possible values of the particular `<enum>`.  For `integer` enums, the value of `"value"` attribute will be one of the possible values, the `"hexvalue"` is just a hexadecimal representation of the `"value"` attribute, any of them could be used but `"hexvalue"` is preferred if exist.

Additionally, `<element>` could have an `"internal_name"` attribute. This helper attribute is not used in communication with SDL Core and describes the `<element>` name for SDL libraries. The actual naming of `<element>` in libraries is per the following rationale: If the `<element>` has an `"internal_name"` attribute, all libraries should name the `<element>` based on this attribute. If `"internal_name"` is not specified, the libraries should name the `<element>` based on the `"name"` attribute. There are possible additional rules, e.g., for `internal_name="SamplingRate_8KHZ"` to cut the leading `<enum>` name, but those rules must be individually specified per each library.

## `<struct>`
The `<struct>` is a complex data type. The `<struct>` contains any number of `<param>`. The `<struct>` has a required `"name"` attribute.

Example:
```xml
<struct deprecated="boolean" name="string" since="string" until="string">
  <!--Optional:-->
  <history>
    <struct/>
  </history>
  <!--Zero or more repetitions:-->
  <description>string</description>
  <!--Zero or more repetitions:-->
  <param array="boolean" defvalue="integer|decimal|boolean|string" deprecated="boolean" mandatory="boolean" maxlength="integer" maxsize="integer" maxvalue="decimal" minlength="integer" minsize="integer" minvalue="decimal" name="string" since="string" type="string" until="string">
    <!--Zero or more repetitions:-->
    <description>string</description>
    <!--Optional:-->
    <history>
      <param/>
    </history>
  </param>
</struct>
```
Each `<param>` requires `"name"`, `"type"` and `"mandatory"` attributes. The `"type"` attribute value should be one of `"Boolean"`, `"Float"`, `"Integer"`, `"String"` or the one of `<enum>`, `<struct>` name specified in the Mobile API.

Additionally, `<param>` could have `"array"` attribute to represent an array of values or objects of the described type. Attributes `"maxsize"` and `"minsize"` provide additional restrictions to an array.

Numeric types can be restricted using `"minvalue"` and `"maxvalue"`. The `"defvalue"` attribute contains default value with different type, depends on `<param>` type, note: this attribute is not allowed for `<struct>` type.

## `<function>`
The `<function>` element represents a specific RPC and message type of the Mobile API. It contains any number of `<param>`. The `<function>` has a required `"name"`, `"messagetype"`, `"functionID"` attributes.

Example:
```xml

<function deprecated="boolean" functionID="string" messagetype="string" name="string" since="string" until="string">
  <!--Optional:-->
  <history>
    <function/>
  </history>
  <!--Zero or more repetitions:-->
  <description>string</description>
  <!--Zero or more repetitions:-->
  <param array="boolean" defvalue="integer|decimal|boolean|string" deprecated="boolean" mandatory="boolean" maxlength="integer" maxsize="integer" maxvalue="decimal" minlength="integer" minsize="integer" minvalue="decimal" name="string" platform="string" since="string" type="string" until="string">
    <!--Zero or more repetitions:-->
    <description>string</description>
    <!--Optional:-->
    <history>
      <param/>
    </history>
    <!--Zero or more repetitions:-->
    <todo>string</todo>
    <!--Zero or more repetitions:-->
    <element name="string">
      <!--Optional:-->
      <description>string</description>
    </element>
  </param>
</function>
```
The `"messagetype"` attribute value should be one of `"request"`, `"response"`, or `"notification"`. The `"functionID"` attribute value should match the `"name`" attribute of one `<element>` of the `<enum>` named `"FunctionID"`.

Just like `<param>` elements in `<struct>`, each `<param>` has required `"name"`, `"type"`, and `"mandatory"` attributes. The `"type"` attribute value should be one of `"Boolean"`, `"Float"`, `"Integer"`, `"String"` or the one of `<enum>`, `<struct>` name exists in XML.

Additionally, `<param>` could have `"array"` attribute which means the param represents array of described types. Attributes `"max*"` and `"min*"` provide additional restrictions. The `"defvalue"` attribute contains default value with different type, depends on `<param>` type, note: this attribute is not allowed for `<struct>` type.

The `<param>` with `<enum>` type could additionally contain any number of `<element>` (but not more than the number of `<element>` in the related `<enum>`). The `<element>` has required `"name"` attribute and this should match the one of `<element>`'s `"name"` or `"internal_name"` attribute in the related `<enum>`. This restricts the represented value by the defined list of `<element>` instead of the full list of `<element>` in the related `<enum>`.
