import math
def dms_to_dd(dms):
    """This function converts coordinates in degrees minutes seconds into decimal degrees format."""
    separated = dms.split(" ")
    dd = float(separated[0]) + (float(separated[1]) / 60) + (float(separated[2]) / 3600)
    return dd
    
def vert_sep():
    """This function collects all of the coordinates and elevations necessary to calculate the vertical separation between a drone being flown under
    an established approach path, runs all of the calculations, and prints the separation in feet. All coordinates are entered by the user in degrees
    minutes seconds format with no special characters. Degrees minutes and seconds are separated with spaces. All elevations and altitudes are entered
    in feet. The approach path glide slope angle is entered in degrees."""
    drone_northing_dms = raw_input("Enter the northing of the location that the drone will fly in DMS format. ex. 34 14 21.25 :")
    drone_northing_dd = dms_to_dd(drone_northing_dms)
    drone_easting_dms = raw_input("Enter the easting of the location that the drone will fly in DMS format. ex. 83 52 1.75 :")
    drone_easting_dd = dms_to_dd(drone_easting_dms)
    iaf_northing_dms = raw_input("Enter the northing of the initial approach fix in DMS format. ex. 34 12 12.11 :")
    iaf_northing_dd = dms_to_dd(iaf_northing_dms)
    iaf_easting_dms = raw_input("Enter the easting of the initial approach fix in DMS format. ex. 83 54 22.74 :")
    iaf_easting_dd = dms_to_dd(iaf_easting_dms)
    
    long_degree_dist_ft = (math.cos(math.radians(float(drone_northing_dd))) * 69.172) * 5280
    easting_distance_ft = (abs(float(iaf_easting_dd)) - float(drone_easting_dd)) * float(long_degree_dist_ft)
    northing_distance_ft = (abs(float(iaf_northing_dd) - float(drone_northing_dd))) * 364320
    distance_ft = ((float(easting_distance_ft) ** 2.0) + (float(northing_distance_ft) ** 2.0)) ** (1/2.0)
    tdze = raw_input("Enter the elevation of the touch down zone in feet. ex 1276 :")
    iaf_alt = raw_input("Enter the altitude of the initial approach fix in feet. ex 3100 :")
    gsa = raw_input("Enter the glide slope angle in degrees. ex 3.00 :")
    study_area_elevation = raw_input("Enter the elevation of the location that the drone will fly in feet. ex. 1162 :")
    drone_alt = raw_input("Enter the altitude that the drone will fly in feet. ex 270 :")
    adjactnt_side = float(iaf_alt) - float(tdze)
    alt_above_tdze = (math.tan(math.radians(float(gsa)))) * float(distance_ft)
    elevation_diff = float(tdze) - float(study_area_elevation)
    approach_path_alt = float(alt_above_tdze) + float(elevation_diff)
    vert_sep = float(approach_path_alt) - float(drone_alt)
    print ("There will be {} feet of vertical separation between the drone and the approach path.").format(round(vert_sep, 1))
