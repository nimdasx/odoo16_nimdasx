from odoo import models, fields


class SfxTag(models.Model):
    _name = 'sfx_tag'
    _description = 'Iki data tag'

    name = fields.Char(
        string="Nama Tag",
        required=True,
        help="Isikan nama tag")
