class Kool:
    def __init__(self, nimi):
        self.nimi = nimi
        self.õpilased = []

    def kas_saab_registreerida_kooli(self, õpilane):
        if õpilane not in self.õpilased:
            return True
        else:
            return False

    def registreeri_kooli(self, õpilane):
        if self.kas_saab_registreerida_kooli(õpilane):
            self.õpilased.append(õpilane)