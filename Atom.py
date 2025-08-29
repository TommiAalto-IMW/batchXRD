class Atom:
    def __init__(self):
        self.formfactor = ""
        self.occupation = 0
        self.beq = 0

    @property
    def data(self):
        """
        :return: returns a string with all the data of the atom
        """
        return self.formfactor + "\t" + str(self.occupation) + "\t" + str(self.beq)

    @property
    def header(self):
        return "formfactor\toccupation\tbeq"
