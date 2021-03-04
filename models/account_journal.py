# Copyright 2017 Tecnativa.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    check_print_auto = fields.Boolean(
        string='Impresión automática de cheques',
        help='El cheque predeterminado de la empresa se imprime automáticamente cuando '
             'el pago de la factura está validado',
    )
    check_layout_id = fields.Many2one(
        comodel_name='account.payment.check.report',
        string="Formato Cheque")
