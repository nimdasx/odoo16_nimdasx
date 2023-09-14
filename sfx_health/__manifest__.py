{
    'name': 'Health SFX',
    'author': "Sofyan & Shofia",
    'website': "https://sofy.web.id",
    'summary': 'Health Information System SFX',
    'version': '1.0',
    'application': True,
    'category': 'Productivity',
    'license': 'Other proprietary',
    'depends': ['base'],

    # always loaded
    'data': [
        'data/sfx_obat.csv',
        'data/sfx_jenis_obat.csv',
        'data/sfx_tag.csv',
        'keamanan/ir.model.access.csv',
        'tampilan/tampilan_sfx_obat.xml',
        'tampilan/tampilan_sfx_jenis_obat.xml',
        'tampilan/tampilan_sfx_tag.xml',
        'tampilan/menu.xml',
    ],

}
