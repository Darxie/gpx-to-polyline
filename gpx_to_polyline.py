import gpxpy
import polyline

def gpx_to_google_polyline(gpx_file):
    with open(gpx_file, 'r') as file:
        gpx = gpxpy.parse(file)
    
    track_points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                track_points.append((point.latitude, point.longitude))

    google_polyline = polyline.encode(track_points)
    return google_polyline

gpx_file = 'slovakia.gpx'
google_polyline = gpx_to_google_polyline(gpx_file)
print("---------------")
print(google_polyline)
print("---------------")