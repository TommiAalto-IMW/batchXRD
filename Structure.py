class Structure:
    # A Structure has properties like space group, lattice parameters ... and contains various sites.
    def __init__(self):
        self.sites = []
        self.space_group = ""
        self.a = 0
        self.a_error = 0
        self.b = 0
        self.b_error = 0
        self.c = 0
        self.c_error = 0
        self.al = 90
        self.al_error = 0
        self.be = 90
        self.be_error = 0
        self.ga = 90
        self.ga_error = 0
        self.crystallite_size = 0
        self.crystallite_size_error = 0
        self.strain = 0
        self.strain_error = 0
        self.r_bragg = 0
        self.phase_name = ""
        self.unit_cell_mass = 0
        self.unit_cell_volume = 0
        self.unit_cell_volume_error = 0
        self.weight_fraction_percent = 0
        self.weight_fraction_percent_error = 0
        self.scale = 0
        self.scale_error = 0
        self.density = 0

    def add_site(self, site):
        self.sites.append(site)

    @property
    def header(self):
        """
        :return: returns a string with all the names of the data types of the structure returned by data()
        """
        text = "space_group\ta\ta_er\tb\tb_er\tc\tc_er\talpha\t_alpha_er\tbeta\tbeta_error\tgamma\tgamma_error\tcrystallite_size\tcrys_error\tstrain\tstrain_error\tr_bragg\tphase_name\t" \
               "unit_cell_mass\tunit_cell_volume\tvolume_error\tweight_fraction_weight_percent\tweight_error\tscale\tscale_error\tdensity\t"
        for i in range(0, len(self.sites)):
            text += "SITE" + str(i + 1) + "\t"
            text += self.sites[i].header + "\t"
        return text

    @property
    def data(self):
        """
        :return: returns a string with all the data of the structure
        """
        return self.space_group + "\t" + str(self.a) + "\t" + str(self.a_error) + "\t" + str(self.b)+ "\t" + str(self.b_error) + "\t" + str(
            self.c)+ "\t" + str(self.c_error) + "\t" + str(self.al)+ "\t" + str(self.al_error) + "\t" + str(self.be)+ "\t" + str(self.be_error) + "\t" + str(self.ga)+ "\t" + str(self.ga_error) + "\t" + str(
            self.crystallite_size)+ "\t" + str(self.crystallite_size_error) + "\t" + str(self.strain)+ "\t" + str(self.strain_error) + "\t" + str(self.r_bragg) + "\t" + str(
            self.phase_name) + "\t" + str(self.unit_cell_mass) + "\t" + str(self.unit_cell_volume)+ "\t" + str(self.unit_cell_volume_error) + "\t" + str(
            self.weight_fraction_percent)+ "\t" + str(self.weight_fraction_percent_error) + "\t" + str(self.scale)+ "\t" + str(self.scale_error) + "\t" + str(self.density)

    @property
    def site_data(self):
        """
        :return: returns a string with all the data of all sites in the structure
        """
        text = ""
        for i in range(0, len(self.sites)):
            text += "SITE" + str(i + 1) + "\t"
            text += self.sites[i].data + "\t"
            text += self.sites[i].atom_data + "\t"

        return text
