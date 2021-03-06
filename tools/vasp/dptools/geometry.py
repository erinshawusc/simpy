############################################################################
# Representation of a geometry
############################################################################

"""
@log: 2014_06_15 Tao add volume calculation

"""
import numpy as np
import numpy.linalg as la

__all__ = [ "Geometry", ]

class Geometry:
    """Atomic geometry representation.

    Attributes:
        specienames: Name of atomtypes which can be found in the geometry.
        nspecie: Number of species.
        indexes: For each atom the index of the corresponding specie
            in specienames.
        natom: Number of atoms.
        coords: xyz coordinates of the atoms.
        origin: Origin.
        periodic: True if the structure is periodic.
        latvecs: Lattice vectors (None for non-periodic structures).
        relcoords: Relative lattice coordinates (None if non-periodic).
    """
  
    def __init__(self, specienames, indexes, coords, latvecs=None, origin=None,
                 relcoords=False):
        """Initializes a geometry object.

        Args:
            specienames: Names of the species occuring in the geometry.
            indexes: Species index for every atom. Shape (natom,)
            coords: Coordinates of the atoms.
            latvecs: Lattice vectors (default: None, non-periodic modell). 
            origin: Origin of the primitive cell (default (0.0, 0.0, 0.0))
            relcoords: If set to yes, coordinates are assumed to be relative
                coordinates specified as multiples of the lattice vectors.
        """
        self.specienames = list(specienames)
        self.nspecie = len(self.specienames)
        self.indexes = np.array(indexes)
        self.natom = len(self.indexes)
        self.coords = np.array(coords)
        if origin is None:
            self.origin = np.array((0, 0, 0), dtype=float)
        else:
            self.origin = np.array(origin, dtype=float)
        self.periodic = latvecs is not None
        if self.periodic:
            self.latvecs = np.array(latvecs, dtype=float)
            a = self.latvecs[0]
            b = self.latvecs[1]
            c = self.latvecs[2]
            volume = a[0]*b[1]*c[2]-a[0]*b[2]*c[1]+a[1]*b[2]*c[0]-a[1]*b[0]*c[2]+a[2]*b[0]*c[1]-a[2]*b[1]*c[0]
            self.volume = volume
            self._invlatvecs = la.inv(self.latvecs)
            if relcoords:
                self.relcoords = coords
                self.coords = np.dot(self.relcoords, self.latvecs) + self.origin
            else:
                self.coords = coords
                self.relcoords = np.dot(self.coords - self.origin,
                                        self._invlatvecs)
        else:
            self.latvecs = None
            self.volume = None
            self._invlatvecs = None
            self.relcoords = None

    
    def setlattice(self, latvecs, origin=None):
        """Makes geometry periodic or changes supercell vectors.

        Args:
            latvecs: Periodicity defined by lattice vectors.
            origin: Origin (default: 0, 0, 0)
        """
        self.latvecs = np.array(latvecs, dtype=float)
        self._invlatvecs = la.inv(self.latvecs)
        if origin is None:
            self.origin = np.array((0, 0, 0), dtype=float)
        else:
            self.origin = np.array(origin, dtype=float)
        self.relcoords = np.dot(self.coords - self.origin, self._invlatvecs)
        self.periodic = True
