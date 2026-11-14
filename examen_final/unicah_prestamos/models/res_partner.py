from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    prestamo_ids = fields.One2many(
        "unicah.prestamo",
        "estudiante_id",
        string="Préstamos",
    )
    prestamo_count = fields.Integer(
        string="Total de préstamos",
        compute="_compute_prestamo_count",
    )

    @api.depends("prestamo_ids")
    def _compute_prestamo_count(self):
        for partner in self:
            partner.prestamo_count = len(partner.prestamo_ids)
            