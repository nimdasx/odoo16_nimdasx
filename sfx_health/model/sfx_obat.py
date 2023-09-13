from odoo import models, fields


class SfxObat(models.Model):
    _name = 'sfx_obat'
    _description = 'Iki data obat'

    name = fields.Char(string="Nama Obat", required=True, help="Isikan nama obat di sini")
    tanggal = fields.Date()
