import gpxpy
import polyline
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


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

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("GPX Files", "*.gpx")])
    if file_path:
        try:
            polyline = gpx_to_google_polyline(file_path)
            polyline_text.delete(1.0, tk.END)
            polyline_text.insert(tk.END, polyline)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()
window.title("GPX to Polyline Converter")

# Create a button to open the file dialog
open_button = tk.Button(window, text="Open GPX File", command=open_file_dialog)
open_button.pack(pady=20)

# Create a text widget to display the polyline
polyline_text = tk.Text(window, height=20, width=50)
polyline_text.pack(padx=20, pady=20)

# Create a scrollbar for the text widget
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
polyline_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=polyline_text.yview)

# Run the GUI
window.mainloop()