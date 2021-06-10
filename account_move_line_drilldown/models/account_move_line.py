# Copyright 2021 Opener B.V. <stefan@opener.amsterdam>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    account_root_code = fields.Char(
        compute="_compute_account_codes", index=True, store=True)
    account_sub_code = fields.Char(
        compute="_compute_account_codes", index=True, store=True)

    @api.depends("account_id.code")
    def _compute_account_codes(self):
        """Provide the root and sub account codes for each move line"""
        for aml in self:
            aml.account_root_code = aml.account_id.code[:1]
            aml.account_sub_code = aml.account_id.code[:2]
