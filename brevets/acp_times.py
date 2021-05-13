"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km> 1.2*brevet_dist_km:
        return "the control point is over 20% longer than the theoretical distance"
    if control_dist_km<0:
        return "unrecognized control point measurement"
    elif control_dist_km==0:
        time=0
    elif 0<control_dist_km<=200:
        time= control_dist_km/34
    elif 200<control_dist_km<=400:
        time= 200/34 + (control_dist_km-200)/32

    elif 400<control_dist_km<=600:
        time= 200/34 + 200/32 + (control_dist_km-400)/30
    elif 600<control_dist_km<=1000:
        time= 200/34 + 200/32 + 200/30+ (control_dist_km-600)/28
    hrs=time//1
    mins=round((time-hrs)*60)
    return brevet_start_time.shift(hours=hrs,minutes=mins)



def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km> 1.2*brevet_dist_km:
        return "the control point is over 20% longer than the theoretical distance"
    if control_dist_km<0:
        return "unrecognized control point measurement"
    elif control_dist_km==0:
        time=1
    elif 0<control_dist_km<=600:
        if control_dist_km==200:
            time=13.5
        elif control_dist_km==300:
            time=20
        elif control_dist_km==400:
            time=27
        elif control_dist_km==600:
            time=40
        else:
            time=control_dist_km/15
    elif 600<control_dist_km<=1000:
        if control_dist_km==1000:
            time=75
        else:
            time=600/15+(control_dist_km-600)/11.428
    hrs=time//1
    mins=round((time-hrs)*60)
    return brevet_start_time.shift(hours=hrs,minutes=mins)
