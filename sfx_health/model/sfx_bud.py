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
        return True
