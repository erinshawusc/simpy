"""constants
"""

# Atom number - Atom name map
ELEMENT = {1:"H", 3:"Li", 6:"C", 7:"N",  8:"O", 9:"F", 12: "Mg", 13: "Al", 14:"Si", 
            15:"P", 16:"S", 17:"Cl", 20:"Ca", 22:"Ti", 28:"Ni", 31:"Ga", 32:"Ge"}
# Atom name - Atom number map
ELEMENT2ATN = {"H":1, "Li":3, "C":6, "N":7,  "O":8, 9:"F", "Na":11, 12: "Mg", "Al":13, "Si":14, 
            "P":15, "S":16, "Cl":17, "Ca":20, "Ti":22, "V":23,"Ni":28, "Pt":78, 32:"Ge", "MO":42, "Mo":42,
            "NB": 41, "Nb":41, "TE":52, "Te":52, "Ga": 31, "Co":27, "D":1, "Ar":18,
               "Ba": 56, "Y":39, "Zr": 40, "Cu": 29, "K":19, "Br":35, "Cs":55}

# Atom name - Atom mass map
ELEMENT2MASS = {"H": 1.0079, "O": 15.999, "N": 14.007, "Li":6.941, "LI":6.941, "Al": 26.982, "AL": 26.982, 
                "Ca": 40.078, "CA": 40.078, "Ti":47.867, "TI":47.867, "Si": 28.086, "SI": 28.086, 
                "Mg": 24.305, "Mg": 24.305, "C":12.011, "Cl":35.453, "CL":35.453, "P":30.974, "S":32.065, 
                "Ge":72.64, "GE":72.64, "B": 10.811, "ZR":91.224, "V": 50.942, "Mo":95.94, 
                "MO": 95.94, "Te": 127.6, "TE": 127.6, "Nb":92.906, "NB":92.906, "Cu":63.546, 
                "Ni": 58.693, "NI": 58.693, "Pt": 195.08, "PT":195.08, "F":18.998, "Na":22.990, "NA":22.990, 
                "Be":9.0122, "BE":9.0122, "Zr":91.224, "ZR":91.224, "Au": 196.97, "AU":196.97,
                "Bi": 208.98, "BI": 208.98, "Ga": 69.723, "X":99999.99, "Co":58.933, "D":1.0079,
                "Ar":39.948, "AR":39.948, "Ba":137.327, "BA":137.327, "Zr":91.224, "ZR":91.224, "Y":88.906,
                "I":126.90, "K":39.098, "Br":79.904, "Cs":132.905, "Fe":55.845}
# Atom name - Atom mass map
MASS2ELMENT = {1: "H",12: "C", 14:"N", 16: "O", 24: "Mg",  27: "Al", 28:"Si", 32: "S", 35: "Cl",
                40:"Ca", 48: "Ti", 64: "Cu",
               195: "Pt"}

ATOMIC_MASS_CONSTANT = 1.6605389e-27 #kg
KG2G = 1000

A2Bohr = 1.88973

