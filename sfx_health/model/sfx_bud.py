from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class SfxBud(models.Model):
    _name = 'sfx_bud'
    _description = 'Iki data Beyond Usage Date'

    obat_id = fields.Many2one("sfx_obat", required=True, ondelete='cascade')
    dicampur_dengan = fields.Char()
    expired_setelah = fields.Integer(
        help="Dalam satuan hari",
        default=7
    )
    expired_date = fields.Date(
        compute="_compute_expired_date",
        # inverse="_inverse_expired_setelah_date"
    )

    @api.depends("expired_setelah")
    def _compute_expired_date(self):
        for record in self:
            if not record.create_date:
                record.create_date = fields.datetime.now()
            record.expired_date = record.create_date + relativedelta(days=record.expired_setelah)

    # def _inverse_expired_setelah_date(self):
    #     for record in self:
    #         record.expired_setelah = 89
