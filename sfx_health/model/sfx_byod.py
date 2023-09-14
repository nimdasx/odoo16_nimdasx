from odoo import models, fields
from dateutil.relativedelta import relativedelta


class SfxByod(models.Model):
    _name = 'sfx_byod'
    _description = 'Iki data byod'

    dicampur_dengan = fields.Char()
    expired_setelah = fields.Integer(
        help="Dalam satuan jam"
    )
