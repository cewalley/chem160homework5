def molemass(compound):
    # dictionary to associate atomic symbols with their masses.
    atomic_mass = {'H' : 1.0079, 'C' : 12.0107, 'N' : 14.0067, 'O' : 15.99944,
                   'P' : 30.9738, 'S' : 32.0660, 'K' : 39.0983, 'F' : 18.9984}

    # initialize molemass as 0.
    molemass = 0

    # Using for loop to iterate over the atoms in the given compund.
    # This for loop iterate over each letter in the compound.
    for atom in compound:
        # add the atomic mass of the atom to the molemass.
        # atomic_mass[atom] gives the atomic mass of the atom from the
        # atomic_mass dictionary.
        molemass += atomic_mass[atom]

    # return molemass.
    return molemass
