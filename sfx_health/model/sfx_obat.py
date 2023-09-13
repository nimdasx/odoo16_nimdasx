from odoo import models, fields


class SfxObat(models.Model):
    _name = 'sfx_obat'
    _description = 'Iki data obat'

    name = fields.Char(
        string="Nama Obat",
        required=True,
        help="Isikan nama obat di sini")
    tanggal = fields.Date(
        "Last Seen",
        default=lambda self: fields.Date.today())
    deskripsi = fields.Text(default="Baceman Teklek")
    harga = fields.Float(readonly=True)
    area = fields.Integer(copy=False)
    garasi = fields.Boolean()
    tipe_gundul = fields.Selection(
        string='Tipe Gundulnya',
        selection=[('lead', 'Lead'), ('opportunity', 'Opportunity')],
        help="Type is used to separate Leads and Opportunities")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[('new', 'Baru'), ('received', 'Offer Received')],
        default="new")
