# Copyright 2021 Opener B.V. <stefan@opener.amsterdam>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo.tests.common import SavepointCase, tagged


@tagged('post_install', '-at_install')
class TestAccountMoveLineDrilldown(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.journal = cls.env["account.journal"].search(
            [("company_id", "=", cls.env.user.company_id.id)], limit=1)
        cls.accounts = cls.env["account.account"].search(
            [("company_id", "=", cls.env.user.company_id.id)], limit=3)

    def test_account_move_line_drilldown(self):
        """Fields from this module are computed as expected"""
        move = self.env['account.move'].create({
            'journal_id': self.journal.id,
            'line_ids': [
                (0, 0, {'debit': 100.0, 'account_id': self.accounts[0].id}),
                (0, 0, {'credit': 100.0, 'account_id': self.accounts[1].id}),
            ],
        })
        move_line = move.line_ids[0]
        self.assertEqual(
            move_line.account_root_code, move_line.account_id.code[0])
        self.assertEqual(
            move_line.account_sub_code, move_line.account_id.code[:2])
        move_line.account_id.code = "89" + move_line.account_id.code
        self.assertEqual(move_line.account_root_code, "8")
        self.assertEqual(move_line.account_sub_code, "89")
