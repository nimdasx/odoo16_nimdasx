from odoo import models, fields
class obat(models.Model):
    _name = 'sfx.obat'
    _description = 'Iki data obat'

    name = fields.Char()