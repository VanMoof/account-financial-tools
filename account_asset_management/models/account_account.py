# -*- coding: utf-8 -*-
# Copyright 2009-2017 Noviat
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models, _
from openerp.exceptions import ValidationError


class AccountAccount(models.Model):
    _inherit = 'account.account'

    asset_category_id = fields.Many2one(
        comodel_name='account.asset.category',
        string='Asset Category',
        help="Default Asset Category when creating invoice lines "
             "with this account.")

    @api.multi
    @api.constrains('asset_category_id')
    def _check_asset_profile(self):
        for account in self:
            if account.asset_category_id and \
                    account.asset_category_id.account_asset_id != account:
                raise ValidationError(_(
                    "The Asset Account defined in the Asset Category "
                    "must be equal to the account."))
