class Õpilane:
    def __init__(self, nimi, klass):
        self.nimi = nimi
        self.klass = klass
        self.keskmine_hinne = 0.0
        self.ained = []

    def __repr__(self):
        return self.nimi