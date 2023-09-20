from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


def tigabulanlagi():
    return fields.Date.today() + relativedelta(months=3)


class SfxObat(models.Model):
    _name = 'sfx_obat'
    _description = 'Iki data obat'

    name = fields.Char(
        string="Nama Obat",
        required=True,
        help="Isikan nama obat di sini")
    tanggal = fields.Date(
        "Last Seen",
        default=lambda aku_parameter_ora_kanggo: (fields.Date.today() + relativedelta(months=3))
        # default=tigabulanlagi()
    )
    embuh = fields.Char(
        string="Embuh Ramudeng"
    )
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
    jenis_obat_id = fields.Many2one("sfx_jenis_obat")
    tag_ids = fields.Many2many("sfx_tag", string="Tag Tak Ketak")
    bud_ids = fields.One2many("sfx_bud", "obat_id", string="BUD Lines")
    tanggal_embuh = fields.Date(compute="_compute_tanggal_embuh")
    expired_paling_lama = fields.Integer(compute="_compute_expired_paling_lama")
    paling_lama_dicampur_dengan = fields.Char(compute="_compute_paling_lama_dicampur_dengan")

    @api.depends("tanggal")
    def _compute_tanggal_embuh(ucuppppp):
        for ngorok in ucuppppp:
            ngorok.tanggal_embuh = ngorok.tanggal + relativedelta(months=3)

    @api.depends("bud_ids.expired_setelah")
    def _compute_expired_paling_lama(self):
        for turu in self:
            turu.expired_paling_lama = max(turu.bud_ids.mapped('expired_setelah'))

    @api.depends('bud_ids.expired_setelah')
    def _compute_paling_lama_dicampur_dengan(self):
        for obat in self:

            def sorting_key(record):
                return record.expired_setelah

            # buds = obat.bud_ids.sorted(key=lambda roramudeng: roramudeng.expired_setelah, reverse=True)
            buds = obat.bud_ids.sorted(key=sorting_key, reverse=True)
            if buds:
                obat.paling_lama_dicampur_dengan = buds[0].dicampur_dengan
            else:
                obat.paling_lama_dicampur_dengan = 'tidak ada'

    # nyobo inverse function
    # di database tidak akan ada field total ini
    total = fields.Float(
        compute="_compute_total",
        inverse="_inverse_total"
    )
    amount = fields.Float()

    @api.depends("amount")
    def _compute_total(self):
        for record in self:
            record.total = 2.0 * record.amount

    def _inverse_total(self):
        for record in self:
            record.amount = record.total / 2.0

    # nyobo on change
    # ini hanya terjadi di form view sehingga tidak butuh di for record in self (loop)
    is_garden = fields.Boolean(
        string="Garden"
    )
    garden_area = fields.Integer(
        string="Garden Area"
    )
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[('north', 'North'), ('south', 'Selatan Orientation')]
    )

    @api.onchange("is_garden")
    def _onchange_is_gardern(self):
        if not self.is_garden:
            self.garden_area = False
            self.garden_orientation = False
        else:
            self.garden_area = 23
            self.garden_orientation = "south"
