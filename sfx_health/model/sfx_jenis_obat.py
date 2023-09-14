from odoo import models, fields


class SfxJenisObat(models.Model):
    _name = 'sfx_jenis_obat'
    _description = 'Iki data jenisobat'

    name = fields.Char(
        string="Nama Jenis Obat",
        required=True,
        help="Isikan nama jenis obat di sini")
