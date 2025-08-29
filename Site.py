class Site:
    # A site has a defined position (errors not implemented) and can contain multiple atoms
    def __init__(self):
        self.atoms = []
        self.site_label = ""
        self.multiplicity = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def add_atom(self, atom):
        self.atoms.append(atom)

    @property
    def header(self):
        text ="site_label\tmultiplicity\tx\ty\tz\t"
        for i in range(0, len(self.atoms)):
            text += "ATOM" + str(i + 1) + "\t"
            text += self.atoms[i].header + "\t"

        return text

    @property
    def data(self):
        return self.site_label + "\t" + str(self.multiplicity) + "\t" + str(self.x) + "\t" + str(self.y) + "\t" + str(
            self.z)

    @property
    def atom_data(self):
        text = ""
        for i in range(0, len(self.atoms)):
            text += "ATOM" + str(i + 1) + "\t"
            text += self.atoms[i].data + "\t"

        return text
