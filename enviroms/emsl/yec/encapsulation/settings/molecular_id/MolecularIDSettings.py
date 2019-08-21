class MoleculaLookupTableSettings:
    
    # C, H, N, O, S and P atoms are ALWAYS needed at usedAtoms
    # if you don't want to include one of thoses atoms set the max and min at 0
    # you can include any atom listed at Atoms class inside Constants module
    # make sure to include the selected valence at the used_atoms_valences when adding atoms 
    # to the usedAtoms dicts 
    # NOTE : Adducts atoms have zero valence
    used_atom_valences = {'C': 4,
                            'H': 1,
                            'O': 2,
                            'N': 3,
                            'S': 2,
                            'P': 3,
                            }

    def __init__(self):
        
        self.usedAtoms = {'C': (1, 100),
                    'H': (4, 200),
                    'O': (0, 20),
                    'N': (0, 0),
                    'S': (0, 0),
                    'P': (0, 0),
                    }
        

        #min_mz changes automatically with mass spectrum
        self.min_mz = 100

        #max_mz changes automatically with mass spectrum
        self.max_mz = 800

        self.min_dbe = 0

        self.max_dbe = 50

        #overwrites the dbe limits above to DBE = (C + heteroatoms) * 0.9
        self.use_pah_line_rule = True
        
        self.isRadical = True

        self.isProtonated = True

        self.ionization_type = "ESI"

        #ionCharge changes automatically with mass spectrum
        self.ionCharge = -1

        self.hc_filter = 0.3

        self.oc_filter = 1.2

class MoleculaSearchSettings:
    
    #needs to be enabled at the class MoleculaLookupTableSettings
    isRadical = False
    
    #needs to be enabled at the class MoleculaLookupTableSettings
    isProtonated = True

    #empirically set / needs optimization
    min_mz_error = -2 #ppm

    #empirically set / needs optimization    
    max_mz_error = 1 #ppm

    #empirically set / needs optimization
    min_abun_error = -30 # percentage 
    
    #empirically set / needs optimization
    max_abun_error = 70 # percentage 

    #empirically set / needs optimization
    mz_error_range = 1.5

    #'distance', 'lowest', 'symmetrical','average' 'None'
    error_method = 'average'

    mz_error_average = 0