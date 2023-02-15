import Note
import View
import Workwithnote

class Controller:
    view = View.Print
    work = Workwithnote.Work

    def write_note(self):
        note = self.view.input_text(self)
        self.work.write_notes(self, note)
    
    def read_notes(self):
        self.work.read_notes(self)
    
    def read_note(self, name):
        self.work.read_note(self, name)

    def del_note(self, name):
        self.work.del_note(self, name)