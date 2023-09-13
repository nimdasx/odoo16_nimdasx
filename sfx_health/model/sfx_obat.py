from odoo import models, fields


class SfxObat(models.Model):
    _name = 'sfx_obat'
    _description = 'Iki data obat'

    nama = fields.Char(string="Nama Obat", required=True, help="Isikan nama obat di sini")
    tanggal = fields.Date()
    deskripsi = fields.Text()
    harga = fields.Float()
    area = fields.Integer()
    garasi = fields.Boolean()
    tipe_gundul = fields.Selection(
        string='Tipe Gundulnya',
        selection=[('lead', 'Lead'), ('opportunity', 'Opportunity')],
        help="Type is used to separate Leads and Opportunities")
