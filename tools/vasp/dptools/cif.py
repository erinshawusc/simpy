############################################################################
# Information in CIF-files (only basic informations)
############################################################################

"""
@log: 2014_06_15 Tao add volume output
"""
import numpy as np
from dptools.common import openfile

__all__ = [ "CIF", ]

class CIF:
    """Representation of a CIF file.

    Attributes:
        geometry: Geometry object with atom positions and lattice vectors.
        celllengths: Length of the 3 cell vectors.
        cellangles: Angles between the cell vectors in radian.
    """

    def __init__(self, geometry):
        """Initializes a CIF instance.

        Args:
            geometry: geometry object with atom positions and lattice vectors.
        """
        self.geometry = geometry
        self.celllengths = np.array([ np.sqrt(np.sum(vv**2))
                                      for vv in geometry.latvecs ], dtype=float)
        # cellangles in radians (alpha, beta and gamma as in crystallography)
        self.cellangles = np.empty(3, dtype=float)
        for ii in range(3):
            i1 = (ii + 1) % 3
            i2 = (ii + 2) % 3
            v1 = geometry.latvecs[i1]
            v2 = geometry.latvecs[i2]
            dot = np.dot(v1, v2) / (self.celllengths[i1] * self.celllengths[i2])
            self.cellangles[ii] = np.arccos(dot)
        self.volume = geometry.volume

    def tofile(self, fobj):
        geo = self.geometry
        fp = openfile(fobj, "w")
        fp.write("data_global\n")
        for name, value in zip(["a", "b", "c"], self.celllengths):
            fp.write("_cell_length_{0:s} {1:.10f}\n".format(name, value))
        # cell angles are needed in degrees
        for name, value in zip(["alpha", "beta", "gamma"],
                               self.cellangles * 180.0 / np.pi):
            fp.write("_cell_angle_{0:s} {1:.10f}\n".format(name, value))
        if self.volume:
            fp.write("_cell_volume    " + str(self.volume)+"\n")
        fp.write("_symmetry_space_group_name_H-M 'P 1'\n")
        fp.write("loop_\n_atom_site_label\n_atom_site_fract_x\n"
                 "_atom_site_fract_y\n_atom_site_fract_z\n")
        for ii in range(geo.natom):
            fp.write("{0:3s} {1:.10f} {2:.10f} {3:.10f}\n".format(
                geo.specienames[geo.indexes[ii]], *geo.relcoords[ii]))
        fp.close()
