from os.path import basename as _basename
from molsysmt._private.exceptions import *
from molsysmt.api_forms.common_gets import *
import numpy as np
from MDAnalysis.topology import PDBParser as _mdanalysis_topology_PDBParser

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _mdanalysis_topology_PDBParser : form_name,
    'mdanalysis.topology.PDBParser' : form_name
        }

info=["",""]
with_topology=True
with_coordinates=False
with_box=False
with_parameters=False

def to_mdanalysis_Topology(item, atom_indices='all', structure_indices='all',
                           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from .api_mdanalysis_Topology import extract as extract_mdanalysis_Topology

    tmp_item = item.parse()
    tmp_item = extract_mdanalysis_Topology(tmp_item, atom_indices=atom_indices, structure_indices=structure_indices)
    return tmp_item

def select_with_Amber(item, selection):

    raise NotImplementedError

def select_with_MDAnalysis(item, selection):

    raise NotImplementedError

def select_with_MDTraj(item, selection):

    raise NotImplementedError

def select_with_MolSysMT(item, selection):

    raise NotImplementedError

def extract(item, atom_indices='all', structure_indices='all'):

    if (atom_indices is 'all') and (structure_indices is 'all'):
        return item
    else:
        raise NotImplementedError

def copy(item):

    raise NotImplementedError

def merge(list_items, list_atom_indices, list_structure_indices):

    raise NotImplementedError

def concatenate(list_items, list_atom_indices, list_structure_indices):

    raise NotImplementedError

def add(item, list_items, list_atom_indices, list_structure_indices):

    raise NotImplementedError

def append(item, list_items, list_atom_indices, list_structure_indices):

    raise NotImplementedError

###### Get

## atom

def get_atom_id_from_atom(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_atom_name_from_atom(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_atom_type_from_atom(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_group_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_component_index_from_atom (item, indices='all', structure_indices='all'):

    from molsysmt.elements.component import get_component_index_from_atom as _get
    return _get(item, indices=indices)

def get_chain_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_molecule_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_entity_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_bonded_atoms_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_bond_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_n_bonds_from_atom (item, indices='all', structure_indices='all'):

    if indices is 'all':
        return get_n_bonds_from_system (item)
    else:
        raise NotImplementedError

def get_inner_bond_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_inner_bonded_atoms_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_n_inner_bonds_from_atom (item, indices='all', structure_indices='all'):

    if indices is 'all':
        return get_n_inner_bonds_from_system (item)
    else:
        raise NotImplementedError

def get_coordinates_from_atom(item, indices='all', structure_indices='all'):

    raise NotImplementedError

## group

def get_group_id_from_group(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_group_name_from_group(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_group_type_from_group(item, indices='all', structure_indices='all'):

    raise NotImplementedError

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

    raise NotImplementedError

def get_molecule_name_from_molecule (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_molecule_type_from_molecule (item, indices='all', structure_indices='all'):

    raise NotImplementedError

## chain

def get_chain_id_from_chain (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_chain_name_from_chain (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_chain_type_from_chain (item, indices='all', structure_indices='all'):

    raise NotImplementedError

## entity

def get_entity_id_from_entity (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_entity_name_from_entity (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_entity_type_from_entity (item, indices='all', structure_indices='all'):

    raise NotImplementedError

## system

def get_n_atoms_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_n_groups_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_n_components_from_system(item, indices='all', structure_indices='all'):

    output = get_component_index_from_atom(item, indices='all')
    output = np.unique(output)
    return output.shape[0]

def get_n_chains_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_n_molecules_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_n_entities_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_n_bonds_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_coordinates_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_box_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_box_shape_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_box_lengths_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_box_angles_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_time_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_step_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_n_structures_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_bonded_atoms_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_form_from_system(item, indices='all', structure_indices='all'):

    return form_name

def get_has_topology_from_system(item, indices='all', structure_indices='all'):

    return with_topology

def get_has_parameters_from_system(item, indices='all', structure_indices='all'):

    return with_parameters

def get_has_coordinates_from_system(item, indices='all', structure_indices='all'):

    return with_coordinates

def get_has_box_from_system(item, indices='all', structure_indices='all'):

    output = False

    if with_box:
        tmp_box = get_box_from_system(item, indices=indices, structure_indices=structure_indices)
        if tmp_box[0] is not None:
            output = True

    return output

def get_has_bonds_from_system(item, indices='all', structure_indices='all'):

    output = False

    if with_topology:
        if get_n_bonds_from_system(item, indices=indices, structure_indices=structure_indices):
            output = True

    return output

## bond

def get_bond_order_from_bond(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_bond_type_from_bond(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_atom_index_from_bond(item, indices='all', structure_indices='all'):

    raise NotImplementedError

###### Set

def set_box_to_system(item, indices='all', structure_indices='all', value=None):

    raise NotImplementedError

def set_coordinates_to_system(item, indices='all', structure_indices='all', value=None):

    raise NotImplementedError

