#!/usr/bin/python3

# Load Gtk
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
from mainWindow import MainWindow


# When the application is launched…
def on_activate(app):
    # … create a new window…
    win = MainWindow(app)
    
    # … with a button in it…
    #btn = Gtk.Button(label='Hello, World!')
    # … which closes the window when clicked
    #btn.connect('clicked', lambda x: win.close())
    #win.set_child(btn)
    win.present()

# Create a new application
app = Gtk.Application(application_id='tr.org.pardus.GtkApplication')
app.connect('activate', on_activate)



# Run the application
app.run(None)
