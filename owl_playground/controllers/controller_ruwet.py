from odoo import http
from odoo.http import request, route


class OwlControllerRuwet(http.Controller):
    @http.route(['/owl_plastik/kresek'], type='http', auth='public')
    def owl_plastik_kresek(self):
        """
        Renders the owl playground page
        """
        return request.render('owl_playground.semprotan')
        # return "fadhli daswir"
