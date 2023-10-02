from odoo import http
from odoo.http import request, route


class OwlControllerOwel(http.Controller):

    @http.route(['/owel_dolanan/mendem'], type='http', auth='public')
    def show_ngantuk(self):
        return request.render('owl_playground.lele')
