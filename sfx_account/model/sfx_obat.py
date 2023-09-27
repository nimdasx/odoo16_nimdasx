from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SfxObat(models.Model):
    _inherit = 'sfx_obat'

    def action_sold(self):

        # Memastikan bahwa hanya ada satu rekaman yang sesuai dengan kriteria
        self.ensure_one()

        # nek wis canceled raoleh diapak-apakke
        if self.state != "received":
            raise UserError("kudu received sik lagi iso dijual yo")

        # cek ada gak bud yang statusnya
        # raise UserError(f"nek wis canceled raiso diapak-apakke {baris.state}")
        buds = self.bud_ids
        if not buds:
            raise UserError("tidak ada bud sama sekali")

        for bud in buds:
            print(f"{bud.dicampur_dengan} {bud.state}")
            if bud.state == 'accepted' and bud.res_partner_id:
                budvalid = bud
                print(f"ini juaranya : {budvalid.dicampur_dengan}")
                break
        else:
            raise UserError("tidak ditemukan bud dengan status accepted dan partner terisi")

        if not budvalid:
            raise UserError("tidak ditemukan bud valid kok ngeyel")

        # kalau pakai ini akan search ke semua record di model buds, tidak hanya yang berelasi
        # budvalid = buds.search([('state', '=', 'accepted')], limit=1)
        # if not budvalid:
        #     raise UserError("tidak ditemukan bud yang state-nya diterima")
        # else:
        #     raise UserError(f"{budvalid.dicampur_dengan}")

        # raise UserError(f"{budvalid.dicampur_dengan}  {budvalid.res_partner_id.id}")

        # buat invoice, jurnal_id gak perlu soale wis ono move_type out_invoice jarene chatgpt
        invoice_vals = {
            'partner_id': budvalid.res_partner_id.id,
            'move_type': 'out_invoice',
            # 'journal_id' : 'asdasdasd'
        }
        invoice = self.env['account.move'].create(invoice_vals)
        print(invoice)
        # end of buat invoice

        # buat invoice line
        invoice_line_vals = {
            'move_id': invoice.id,
            'name': 'telo',
            'quantity': 34,
            'price_unit': 3432478
        }
        invoice_line = self.env['account.move.line'].create(invoice_line_vals)
        # end buat invoice line

        # post invoice
        invoice.action_post()

        # nek wis rampung urusane, lagi statuse di sold
        res = super().action_sold()
        print("gila")
        return res
