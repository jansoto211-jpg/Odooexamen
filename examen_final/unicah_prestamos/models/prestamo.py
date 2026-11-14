from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Prestamo(models.Model):

    _name = "unicah.prestamo"
    _description = "Préstamo de equipos universitarios"

    name = fields.Char(
        string="Código",
        required=True
    )

    estudiante_id = fields.Many2one(
        "res.partner",
        string="Estudiante",
        required=True
    )

    equipo = fields.Char(
        string="Equipo",
        required=True
    )

    fecha_prestamo = fields.Date(
        string="Fecha de préstamo",
        default=fields.Date.context_today,
        required=True
    )

    fecha_devolucion = fields.Date(
        string="Fecha de devolución",
        required=True
    )

    estado = fields.Selection(
        [
            ("pendiente", "Pendiente"),
            ("prestado", "Prestado"),
            ("devuelto", "Devuelto"),
        ],
        string="Estado",
        default="pendiente",
        required=True
    )

    dias_prestamo = fields.Integer(
        string="Días de préstamo",
        compute="_compute_dias",
        store=True
    )

    @api.depends("fecha_prestamo", "fecha_devolucion")
    def _compute_dias(self):

        for record in self:

            if record.fecha_prestamo and record.fecha_devolucion:
                record.dias_prestamo = (
                    record.fecha_devolucion - record.fecha_prestamo
                ).days
            else:
                record.dias_prestamo = 0

    @api.constrains("fecha_prestamo", "fecha_devolucion")
    def _check_fechas(self):

        for record in self:

            if record.fecha_devolucion < record.fecha_prestamo:
                raise ValidationError(
                    "La fecha de devolución no puede ser anterior al préstamo."
                )