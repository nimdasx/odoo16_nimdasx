from odoo import models, fields, api, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    # ingat, one2many virtual field, dia tidak ada ada di database
    # kenapa domain state new gak jalan???? ada tanda petik dua domain="[('state','=','new')]"
    # petik dua tak hilangkan berhasil, tapi di contoh codingya odoo ada yang tetap pakai petik dua
    obat_ids = fields.One2many(
        'sfx_obat',
        'create_uid',
        string='Obats',
        domain=[('state','=','new')]
    )
