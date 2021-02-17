# pycon
A conversion tool. To convert to a reasonable sysem of units (aka. the metric system). Written in python3.

It only converts to metric as other conversions should not be done anyway.
Thank you for converting to the metric system.


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


## ToDo

Oh so much:
* Make it more resilient to user input error
  * Add exceptions for empty arguments
  * Ignore upper/lower case differences
* add more conversions
* improve overall code quality
  * use `argpars`?
