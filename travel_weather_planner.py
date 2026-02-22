

distance_mi = 0
is_raining = False
has_bike = False
has_car = False
has_ride_share_app = False
final = None
    
if distance_mi <= 1:
    final = not is_raining
    print(final)
elif distance_mi > 1 and distance_mi <= 6:
    if has_bike == True:
        if is_raining == False:
            final = True
            print(final)
        else:
            final = False
            print(final)
    else:
        final = False
        print(final)
elif distance_mi > 6:
    if has_car == True or has_ride_share_app == True:
        final = True
    else:
        final = False
    print(final)