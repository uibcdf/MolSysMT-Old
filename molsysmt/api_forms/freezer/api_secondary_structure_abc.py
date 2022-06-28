from os.path import basename as _basename

form_name=_basename(__file__).split('.')[0].replace('api_','')+':seq'

is_form={
    'secondary_structure_abc:seq' : form_name
}

info=["",""]
with_topology=False
with_trajectory=False

def select_with_MDTraj(item, selection):
    raise NotImplementedError

def extract(item, atom_indices='all', structure_indices='all'):

    if (atom_indices is 'all') and (structure_indices is 'all'):
        return item
    else:
        raise NotImplementedError


def copy(item):

    raise NotImplementedError


###### Get

## system

def get_form_from_system(item, indices='all', structure_indices='all'):

    return form_name

