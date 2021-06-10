# Copyright 2021 Opener B.V. <stefan@opener.amsterdam>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


def pre_init_hook(cr):
    """Populate the stored computed fields from this module"""
    cr.execute(
        """alter table account_move_line
        add column if not exists account_root_code varchar,
        add column if not exists account_sub_code varchar;
        update account_move_line aml
        set account_root_code = substring(aa.code from 1 for 1),
            account_sub_code = substring(aa.code from 1 for 2)
        from account_account aa
        where aa.id = aml.account_id;
        """)
