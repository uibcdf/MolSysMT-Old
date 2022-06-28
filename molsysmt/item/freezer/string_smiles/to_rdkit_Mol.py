def to_rdkit_Mol(item, selection='all', structure_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.string_smiles import is_string_smiles
    from molsysmt.basic import convert

    if not is_string_smiles(item):
        raise ValueError

    tmp_item = convert(item, to_form='rdkit.Mol', selection=selection, structure_indices=structure_indices, syntaxis=syntaxis)

    return tmp_item

