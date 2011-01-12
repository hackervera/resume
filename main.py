import pygtk
pygtk.require('2.0')
import gtk
import subprocess
import gst
import os

class GTKizzle:
  def delete_event(self, widget,event, data=None):
    return False

  def destroy(self,widget,data=None):
    gtk.main_quit()
    
  
  def __init__(self):
    #subprocess.Popen(['xdg-open','music.mp3'])
    self.player = gst.element_factory_make("playbin2", "player")
    self.player.set_property("uri", "file://"+os.path.abspath('music.ogg'))
    self.player.set_state(gst.STATE_PLAYING)
    self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window.connect("delete_event", self.delete_event)
    self.window.connect("destroy", self.destroy)
    self.window.set_border_width(10)
    self.window.set_title("Tyler Gillies")
    self.button = gtk.Button("Hello world")
    self.hbox = gtk.HBox()
    self.vbox1 = gtk.VBox()
    self.vbox2 = gtk.VBox()
    self.hbox2 = gtk.HBox()
    self.tyler_image = gtk.Image()
    self.tyler_image.set_from_file("tyler.jpg")
    self.label = gtk.Label("My name is Tyler Gillies. \nI was born in Portland Oregon. \nI code.")
    self.linkbutton = gtk.LinkButton("http://www.github.com/tjgillies", "GitHub profile")
    self.twitter = gtk.LinkButton("http://www.twitter.com/tylergillies", "Twitter")
    self.vbox1.pack_start(self.tyler_image)
    self.vbox2.pack_start(self.label, False,False,10)
    self.hbox2.pack_start(self.linkbutton, False)
    self.hbox2.pack_start(self.twitter, False)
    
    #self.button.connect("clicked", self.hello, None)
    self.hbox.pack_start(self.vbox1)
    self.hbox.pack_start(self.vbox2,False, False,20)
    self.vbox2.pack_start(self.hbox2, False)
    #self.window.add(self.tyler_image)
    self.window.add(self.hbox)
    #self.button.show()
    self.window.show()
    self.hbox.show()
    self.hbox2.show()
    self.vbox1.show()
    self.vbox2.show()
    self.linkbutton.show()
    self.tyler_image.show()
    self.label.show()
    self.twitter.show()
    
  def main(self):
    gtk.main()
  
if __name__ == "__main__":
  hello = GTKizzle()
  hello.main()
