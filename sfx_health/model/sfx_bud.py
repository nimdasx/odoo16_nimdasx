from odoo import models, fields


class SfxBud(models.Model):
    _name = 'sfx_bud'
    _description = 'Iki data Beyond Usage Date'

    dicampur_dengan = fields.Char()
    expired_setelah = fields.Integer(
        help="Dalam satuan jam"
    )
    obat_id = fields.Many2one("sfx_obat", required=True,ondelete='cascade')
