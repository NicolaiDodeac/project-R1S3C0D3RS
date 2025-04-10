from datetime import datetime

class Note:
    def __init__(self, name_note, body_note, tag_note = None):
        self.name_note = name_note
        self.body_note = body_note
        self.tag_note = tag_note
        self.date_created = datetime.now()

    def __str__(self):
        if self.tag_note is None:
            return f"Нотатка {self.name_note}, створена {self.date_created.strftime('%d.%m.%Y')} - {self.body_note}"
        else:
            return f"Нотатка {self.name_note}  і тегом {self.tag_note}, створена {self.date_created.strftime('%d.%m.%Y')} - {self.body_note}"
    

    
if __name__ == "__main__":
  pass