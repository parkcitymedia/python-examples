from gi.repository import Gtk
gi.require_version('Gtk', '3.0')

class MainWindow(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title="Button window")

            self.button = Gtk.Button(label="Hey, click me!")

window = MainWindow()
# window.connect("delete-event", Gtk.main_quit)
# window.show_all()
# Gtk.main()