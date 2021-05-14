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
    if brevet_dist_km<control_dist_km<=1.2*brevet_dist_km:
    #if cd>bd,and also doesn't over 20% of bd, time will equals in bd,so
    #call open_time to get time for bd.
        return open_time(brevet_dist_km,brevet_dist_km,brevet_start_time)
    else:
        if control_dist_km==0:
        #cd=0, open time should =0
            time=0
        elif 0<control_dist_km<=200:
        #else, piecewise calculate time cost base on different speed in each distance
            time= control_dist_km/34
        elif 200<control_dist_km<=400:
            time= 200/34 + (control_dist_km-200)/32
        elif 400<control_dist_km<=600:
            time= 200/34 + 200/32 + (control_dist_km-400)/30
        elif 600<control_dist_km<=1000:
            time= 200/34 + 200/32 + 200/30+ (control_dist_km-600)/28
        hrs=time//1 #get integet of hours
        mins=round((time-hrs)*60) #get minutes,don't need second so use round
        result=brevet_start_time.shift(hours=hrs,minutes=mins)
        #shift arrow brevet_start_time hrs hours and mins minutes
        return result

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
    if brevet_dist_km<control_dist_km<=1.2*brevet_dist_km:
    #if cd>bd,and also doesn't over 20% of bd, time will equals in bd,so
    #call close_time to get time for bd.
        return close_time(brevet_dist_km,brevet_dist_km,brevet_start_time)
    else:
    #else 0<=cd<=bd
        if control_dist_km==0:
        #cd=0, close_time should = 1
            time=1
        elif 0<control_dist_km<=60:
        #time cost in cd is 1+cd* speed 20
            time=1+control_dist_km/20
        elif 60<control_dist_km<=600:
            #if cd exactly equals 200,300,400,600 or 1000,time will be a fixed value
            if control_dist_km==200:
                if brevet_dist_km==200:
                    time=13.5
                else:
                    time=control_dist_km/15
            elif control_dist_km==300:
                time=20
            elif control_dist_km==400:
                if brevet_dist_km==400:
                    time=27
                else:
                    time=control_dist_km/15
            elif control_dist_km==600:
                time=40
            else:
            #else get time cost
                time=control_dist_km/15
        elif 600<control_dist_km<=1000:
            if control_dist_km==1000:
                time=75
            else:
            #0-600 speed is 15, the rest time 600-1000 speed is 11.428
                time=600/15+(control_dist_km-600)/11.428
        hrs=time//1#get integer of hours
        mins=round((time-hrs)*60)#get minutes, don't need seconds so use round
        result=brevet_start_time.shift(hours=hrs,minutes=mins)
        #shift arrow brevet_start_time hrs hours and mins minutes
        return result
