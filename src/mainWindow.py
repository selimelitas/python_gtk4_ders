# Load Gtk
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

# ==SETUPS==

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self,app):
        super().__init__(application=app)
        self.setup_window()
        self.setup_ui()

    def setup_window(self):
        self.set_default_size(400,300)
        self.set_title("USB_Creator")
    def setup_headerbar(self):
        pass
    def setup_ui(self):
        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=50
        )
        label = Gtk.Label(
            label="Select USB")

        btn=Gtk.Button(
            label="Create"
        )
        btn.connect("clicked",self.on_btn_create_clicked)

        box.append(label)
        box.append(btn)

        self.set_child(box)
# ==FUNCTIONS==


# ==CALLBACKS==

    def on_btn_create_clicked (self,btn):
        print("Butona bastınız")
