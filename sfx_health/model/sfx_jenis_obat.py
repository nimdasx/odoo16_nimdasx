from odoo import models, fields, api


class SfxJenisObat(models.Model):
    _name = 'sfx_jenis_obat'
    _description = 'Iki data jenisobat'

    # urutan
    _order = "name asc"

    name = fields.Char(
        string="Nama Jenis Obat",
        required=True,
        help="Isikan nama jenis obat di sini")

    # ini gak ada di dabase, adanya di related tabelnya
    # daftar obat yang jenisnya ini
    obat_ids = fields.One2many("sfx_obat", "jenis_obat_id", string="BUD Lines")

    # jumlah obat per jenis obat ini
    obat_count = fields.Integer(string='Number of Obat', compute='_compute_obat_count')

    @api.depends('obat_ids')
    def _compute_obat_count(self):
        for record in self:
            record.obat_count = len(record.obat_ids)
