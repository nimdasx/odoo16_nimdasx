{
    'name': 'Health SFX',
    'author': "Nimda SX",
    'website': "https://sofy.web.id",
    'summary': 'Health Information System SFX',
    'version': '1.0',
    'application': True,
    'category': 'Productivity',
    'license': 'Other proprietary',
    'depends': ['base'],

    # always loaded
    'data': [
        'data/sfx_jenis_obat.csv',
        'data/sfx_tag.csv',
        'data/sfx_obat.csv',
        'keamanan/ir.model.access.csv',
        'tampilan/tampilan_sfx_jenis_obat.xml',
        'tampilan/tampilan_sfx_tag.xml',
        'tampilan/tampilan_sfx_obat.xml',
        'tampilan/tampilan_sfx_bud.xml',
        'tampilan/menu.xml',
    ],

}
