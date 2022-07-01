class linked_list():
    def __init__(self, name):
        self.links=[]
        self.name = name
    def add_child(self, link):
        self.links.append(link)
