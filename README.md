# UOCIS322 - Project 4 #
Brevet time calculator.

## Overview

Reimplement the RUSA ACP controle time calculator with Flask and AJAX.

### ACP controle times

Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location. In other words, essentially replacing the calculator here [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html).   

###

## Algorithm description

###Open time
For open time, there's not randonneuring events, all of output time follow the rule:
control distance(referred to as cd then) equals 0, time=0; 0<cd<=200, time=cd/34; 200<cd<=400,because in distances 0-200, moving speed is 15 km/h, so time= 200/34 + (cd-200)/32; and for range in 400-600, 600-1000, maximun speed respectively are 30 and 28, by the same piecewise calculation, can get open time.
And if control dist over brevet distance less than 20%(over will be illegal), the open time of control distance will just equals open time of brevet distance.


## Testing



## Identifying Information
Author: Haoran Zhang, hzhang9@uoregon.edu
