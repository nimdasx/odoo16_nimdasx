from odoo import models, fields, api, _

class ResUsers(models.Model):
    _inherit = 'res.users'

    # ingat one2many virtual field, dia tidak ada ada di database
    obat_ids = fields.One2many(
        'sfx_obat',
        'create_uid',
        domain="[('state','=','new')]"
    )