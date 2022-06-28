from molsysmt._private.exceptions import *
import numpy as np
from molsysmt.api_forms.common_gets import *
from molsysmt.native.molecular_system import molecular_system_components

form_name='openff.Topology'
from_type='class'

is_form={
    'openff.toolkit.topology.Topology' : form_name,
}

info=["",""]

has = molecular_system_components.copy()
for ii in ['elements', 'bonds', 'coordinates']:
    has[ii]=True

def to_molsysmt_Topology(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from molsysmt.native.io.topology import from_openff_Topology as openff_Topology_to_molsysmt_Topology

    tmp_item, tmp_molecular_system = openff_Topology_to_molsysmt_Topology(item,
            molecular_system=molecular_system, atom_indices='all', structure_indices='all')

    return tmp_item, tmp_molecular_system

def to_molsysmt_MolSys(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from molsysmt.native.io.topology import from_openff_Topology as openff_Topology_to_molsysmt_MolSys

    tmp_item, tmp_molecular_system = openff_Topology_to_molsysmt_MolSys(item,
            molecular_system=molecular_system, atom_indices='all', structure_indices='all')

    return tmp_item, tmp_molecular_system

def to_openmm_Topology(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from .api_openmm_Topology import to_openmm_Topology as openmm_Topology_to_openmm_Topology

    tmp_item = item.to_openmm()

    if molecular_system is None:
                tmp_molecular_system = molecular_system.combine_with_items(tmp_item)
    else:
        tmp_molecular_system = None

    tmp_item, tmp_molecular_system = openmm_Topology_to_openmm_Topology(tmp_item,
            molecular_system=tmp_molecular_system, atom_indices='all',
            structure_indices='all')

    return tmp_item, tmp_molecular_system

def to_openff_Topology(item, molecular_system=None, atom_indices='all', structure_indices='all', copy_if_all=True):

    tmp_molecular_system = None

    if (atom_indices is 'all') and (structure_indices is 'all'):
        if copy_if_all:
            tmp_item = extract(item)
            if molecular_system is not None:
                tmp_molecular_system = molecular_system.combine_with_items(tmp_item)
        else:
            tmp_item = item
            if molecular_system is not None:
                tmp_molecular_system = molecular_system
    else:
        tmp_item = extract(item, atom_indices=atom_indices, structure_indices=structure_indices)
        if molecular_system is not None:
            tmp_molecular_system = molecular_system.combine_with_items(tmp_item, atom_indices=atom_indices, structure_indices=structure_indices)

    return tmp_item, tmp_molecular_system

def extract(item, atom_indices='all', structure_indices='all'):

    if (atom_indices is 'all') and (structure_indices is 'all'):
        tmp_item = openff_Topology(item)
    else:
        raise NotImplementedError()

    return tmp_item

def merge(item_1, item_2):

    raise NotImplementedError

def add(to_item, item):

    raise NotImplementedError

def append_structures(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError()

def concatenate_structures(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError()


###### Get

## atom

def get_atom_id_from_atom(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_atom_name_from_atom(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_atom_type_from_atom(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_group_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_component_index_from_atom (item, indices='all', structure_indices='all'):

    from molsysmt.elements.component import get_component_index_from_atom as _get
    return _get(item, indices=indices)

def get_chain_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_molecule_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_entity_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_bonded_atoms_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_bond_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_n_bonds_from_atom (item, indices='all', structure_indices='all'):

    if indices is 'all':
        return get_n_bonds_from_system (item)
    else:
        raise NotImplementedError()

def get_inner_bond_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_inner_bonded_atoms_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_n_inner_bonds_from_atom (item, indices='all', structure_indices='all'):

    if indices is 'all':
        return get_n_inner_bonds_from_system (item)
    else:
        raise NotImplementedError()

def get_coordinates_from_atom(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

## group

def get_group_id_from_group(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_group_name_from_group(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_group_type_from_group(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

## component

def get_component_id_from_component (item, indices='all', structure_indices='all'):

    from molsysmt.elements.component import get_component_id_from_component as get
    return get(item, indices)

def get_component_name_from_component (item, indices='all', structure_indices='all'):

    from molsysmt.elements.component import get_component_name_from_component as get
    return get(item, indices)

def get_component_type_from_component (item, indices='all', structure_indices='all'):

    from molsysmt.elements.component import get_component_type_from_component as get
    return get(item, indices)

## molecule

def get_molecule_id_from_molecule (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_molecule_name_from_molecule (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_molecule_type_from_molecule (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

## chain

def get_chain_id_from_chain (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_chain_name_from_chain (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_chain_type_from_chain (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

## entity

def get_entity_id_from_entity (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_entity_name_from_entity (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_entity_type_from_entity (item, indices='all', structure_indices='all'):

    raise NotImplementedError()

## system

def get_n_atoms_from_system(item, indices='all', structure_indices='all'):

    return item.n_atoms

def get_n_groups_from_system(item, indices='all', structure_indices='all'):

    return 1

def get_n_components_from_system(item, indices='all', structure_indices='all'):

    return 1

def get_n_chains_from_system(item, indices='all', structure_indices='all'):

    raise 1

def get_n_molecules_from_system(item, indices='all', structure_indices='all'):

    raise 1

def get_n_entities_from_system(item, indices='all', structure_indices='all'):

    raise 1

def get_n_bonds_from_system(item, indices='all', structure_indices='all'):

    return item.n_bonds

def get_coordinates_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_box_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_box_shape_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_box_lengths_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_box_angles_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_time_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_step_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_n_structures_from_system(item, indices='all', structure_indices='all'):

    return None

def get_bonded_atoms_from_system(item, indices='all', structure_indices='all'):

    return NotImplementedError()

## bond

def get_bond_order_from_bond(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_bond_type_from_bond(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

def get_atom_index_from_bond(item, indices='all', structure_indices='all'):

    raise NotImplementedError()

###### Set

def set_box_to_system(item, indices='all', structure_indices='all', value=None):

    raise NotImplementedError()

def set_coordinates_to_system(item, indices='all', structure_indices='all', value=None):

    raise NotImplementedError()

