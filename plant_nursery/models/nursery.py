from odoo import models, fields

class Plants(models.Model):
    _name = 'nursery.plant'

    name = fields.Char(string="Plant Name")
    price = fields.Float()