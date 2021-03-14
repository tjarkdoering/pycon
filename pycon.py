#!/usr/bin/python3

__version__ = 'v0.4'
avail_formats = 'F, in, psi, oz'

# ---
# setup

import sys

# need help?

def help() :
    print('This is pycon', __version__)
    print('The following unit conversions are supported:', avail_formats)
    print('\nUsage:\n pycon [-v] N U')
    print('\nOptions:')
    print(' -v          Verbose output')
    print(' -h, --help  Shows this help message and quits') 
    print('\nArguments:')
    print(' N           A number to convert')
    print(' U           The corresponding unit')
    quit()

# were no arguments given? print help.

if len(sys.argv) < 2 :
    help()

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    help()


# is verbose mode on?
verb = None
if sys.argv[1] == '-v' :
    verb = True
    if len(sys.argv) < 4 :
         help()
    else :
        print('Using pycon', __version__,'\n')
        arg_pos = 2
else :
    verb = False
    arg_pos = 1

# define functions for checking types
def is_intstring(i) :
    try :
        float(i)
        return True
    except ValueError :
        return False

def is_charstring(s) :
    try :
        str.isalpha(s)
        return True
    except ValueError :
        return False

# validate input and set conversion variables

short_help = 'The first argument must be a number, the second the unit.'

stupid_value = None
stupid_unit = None

if is_intstring(sys.argv[arg_pos]) :
    stupid_value = float(sys.argv[arg_pos])
else :
    print(short_help)

if is_charstring(sys.argv[arg_pos+1]) :
    stupid_unit = sys.argv[arg_pos+1]
else :
    print(short_help)


# ---
# case management as if-else-if ladder because I don't know better yet

metric_value = None
metric_unit  = None
additional_output = ''

if stupid_unit == 'F' : # Convert Fahrenheit
    metric_value = (5/9)*(stupid_value - 32)
    metric_unit = '°C'
    kelvin = metric_value + 273.15
    additional_output = str(format(kelvin, '.2f')) + ' K'

elif stupid_unit == 'in' : # Convert inches:
    metric_value = stupid_value * 0.0254
    metric_unit = 'm'
    milim = metric_value * 1000
    additional_output = str(format(milim, '.2f')) + ' mm'

elif stupid_unit == 'psi' : # Convert psi
    metric_value = stupid_value * 6.894757
    metric_unit = 'kPa'
    bar = metric_value / 100
    additional_output = str(format(bar, '.2f')) + ' bar'


elif stupid_unit == 'oz' : # Convert oz
    metric_value = stupid_value * 0.0283495
    metric_unit = 'kg'


else :
    print('This conversion is not supported yet.\n You can only convert:', avail_formats)
    quit()


# ---
# printing results

# mind the verbose option
if verb == True :
    print('You want to convert', stupid_value, stupid_unit, 'to metric.\nYour result is ')
    print( format(metric_value, '.2f') , metric_unit )
    if additional_output != '' :
        print(additional_output)
        
    print('\nThank you for converting to the metric system.')
else :
    print( format(metric_value, '.2f') , metric_unit )
    if additional_output != '' :
        print(additional_output)
        

quit()
