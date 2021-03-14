# pycon

Have a badge here...

A conversion tool. To convert to a reasonable sysem of units (aka. the metric system). Written in python3.

It only converts to metric as other conversions should not be done anyway.
Thank you for converting to the metric system.  


## Supported conversions

The amount of supported units is embarrassingly low. New units come when I need them. Or someone suggests them. Here are the currently supported ones.

| From           | To                       |
| -------------- | ------------------------ |
| `F` Fahrenheit | `°C` Celsius, `K` Kelvin |
| `in` inch      | `mm` Millimeter, `m` Meter |
| `psi` Pounds per squre inch | `kPa` Kilopascal, `bar` Bar |
| `oz` Ounces (mass) | `kg` Kilogram |


## Setup

1. Have `python3` installed.
2. Copy `pycon` to any of your local `bin` paths.
3. Make `pycon` executable.
3. Convert to the metric system.


## Usage

    pycon [-v] N U
    
    Options:
     -v          Verbose output
     -h, --help  Shows this help message

    Arguments:
     N           A number to convert
     U           The corresponding unit

### Example

    $ pycon 40 F
    4.44 °C
    277.59 K
