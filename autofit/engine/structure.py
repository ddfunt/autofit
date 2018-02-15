import numpy as np

class Atom:

    def __init__(self, mass, x, y, z):
        self.mass = mass
        self.x = x
        self.y = y
        self.z = z

    @property
    def point(self):
        return [self.x, self.y, self.z]

    def skew(self,):
        v = np.array([self.x, self.y, self.z])
        skv = np.roll(np.roll(np.diag(v.flatten()), 1, 1), -1, 0)
        return skv - skv.T

    @property
    def intertia_matrix(self):
        return -1 * np.dot(self.skew(), self.skew())

    @property
    def tensor_product(self):
        return self.mass * self.intertia_matrix

    def __repr__(self):
        return 'Atom(mass:{mass}, x,y,z:{x},{y},{z})'.format(mass=self.mass,
                                                            x=self.x,
                                                            y=self.y,
                                                            z=self.z
                                                            )

class Structure:
    atoms = []

    def __init__(self, input_array, mass_col=0):

        for atom in input_array:
            atom = atom.tolist()
            mass = atom.pop(mass_col)
            self.atoms.append(Atom(mass, *atom))

    @property
    def position_matrix(self):
        return np.array([x.point for x in self.atoms])

    @property
    def mass_vector(self):
        return np.array([x.mass for x in self.atoms])


    def calc_constants(self):
        inertia_list = [atom.tensor_product for atom in self.atoms]
        tensor_sum = np.sum(inertia_list, 0)
        consants, _ = np.linalg.eig(tensor_sum)
        return np.sort(consants)[::-1]


if __name__ == '__main__':

    test = np.array([[1,2,3,4], [2,4,5,6]])
    s = Structure(test)
    print(s.mass_vector)
    print(s.position_matrix)
    print(s.calc_constants())