class Volume:
    chapter = 1
    def __init__(self, paragraph):
        self.paragraph = paragraph
        Volume.chapter +=1
    def remove(self):
        del self.paragraph

edition = Volume(1)
print(edition.__dict__)
edition.remove()
print(edition.__dict__)
print(Volume.__dict__)