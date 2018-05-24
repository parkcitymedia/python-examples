from gi.repository import Gtk

window = Gtk.Window()

label = Gtk.Label()
label.set_label("Label function text")
label.set_angle(180)
label.set_halign(Gtk.Align.END)
window.add(label)

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()

#from gi.repository import Gtk
#
#class MainWindow(Gtk.Window):
#        def __init__(self):
#            Gtk.Window.__init__(self, title="Button window")
#            self.button = Gtk.Button(label="Hey, click me!")
#            self.button.connect("clicked", self.button_clicked)
#            self.add(self.button)
#
#        def button_clicked(self, widget):
#            print("Hey! did you ask before touching me there?")
#
#
#
#window = MainWindow()
#window.connect("delete-event", Gtk.main_quit)
#window.show_all()
#Gtk.main()