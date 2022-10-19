import cdsapi

c = cdsapi.Client()

c.retrieve(
    'cams-global-emission-inventories',
    {
        'version': 'latest',
        'format': 'tgz',
        'source': 'anthropogenic',
        'variable': [
            'acetylene', 'acids', 'alcohols',
            'ammonia', 'benzene', 'black_carbon',
            'butanes', 'carbon_dioxide', 'carbon_dioxide_excl_short_cycle',
            'carbon_monoxide', 'chlorinated_hydrocarbons', 'esters',
            'ethane', 'ethene', 'ethers',
            'formaldehyde', 'hexanes', 'isoprene',
            'ketones', 'methane', 'monoterpenes',
            'nitrogen_oxides', 'non_methane_vocs', 'organic_carbon',
            'other_aldehydes', 'other_alkenes_alkynes', 'other_aromatics',
            'other_vocs', 'pentanes', 'propane',
            'propene', 'sulphur_dioxide', 'toluene',
            'trimethylbenzenes', 'xylenes',
        ],
        'year': '2019',
    },
    '../data/emi/cams_global_2019.gz')
