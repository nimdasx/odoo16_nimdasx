from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class SfxBud(models.Model):
    _name = 'sfx_bud'
    _description = 'Iki data Beyond Usage Date'

    obat_id = fields.Many2one("sfx_obat", required=True, ondelete='cascade')
    dicampur_dengan = fields.Char()
    expired_setelah = fields.Integer(
        help="Dalam satuan jam",
        default=7
    )
    expired_datetime = fields.Datetime(
        compute="_compute_expired_datetime",
        inverse="_inverse_expired_datetime"
    )

    @api.depends("expired_setelah")
    def _compute_expired_datetime(self):
        for record in self:
            if not record.create_date:
                record.create_date = fields.datetime.now()
            record.expired_datetime = record.create_date + relativedelta(hours=record.expired_setelah)

    def _inverse_expired_datetime(self):
        for record in self:
            delta = record.expired_datetime - record.create_date
            record.expired_setelah = delta.total_seconds() / 3600

    # nyobo action accepting
    state = fields.Selection(
        selection=[
            ('new', 'Baru'),
            ('accepted', 'Diterima'),
            ('refused', 'Ditolak')
        ],
        default="new")

    def action_accepting(self):
        for baris in self:
            baris.state = "accepted"
            baris.obat_id.embuh = baris.dicampur_dengan
        return True

    def action_refusing(self):
        for baris in self:
            baris.state = "refused"
        return True

    # relasi ke sfx_jenis_obat via sfx_obat, ini dipakai untuk oe_stat_button di form sfx_jenis_obat
    jenis_obat_id = fields.Many2one('sfx_jenis_obat', related="obat_id.jenis_obat_id", store=True)
    # nampilke nama obat neng table sfx_bud
    obat_name = fields.Char(related="obat_id.name")

    # inherit on create
    @api.model
    def create(self, vals):

        # ngene yo iso
        self.env['sfx_obat'].browse(vals['obat_id']).state = 'received'

        # golei record obat dan ganti value-nya
        # obat = self.env['sfx_obat'].browse(vals['obat_id'])

        # ngene yo iso
        # obat.state = 'received'

        # ngene yo iso
        # obat.write({'state': 'received'})

        # Then call super to execute the parent method
        return super().create(vals)

    # dilinkke ke partner, go nyobo gawe invoice
    res_partner_id = fields.Many2one("res.partner", string="Buyer")

    # Konstrain SQL untuk membuat partner_id unik untuk setiap obat
    _sql_constraints = [
        ('unique_partner_per_obat', 'UNIQUE(obat_id, res_partner_id)', 'Partner must be unique per obat!'),
    ]
