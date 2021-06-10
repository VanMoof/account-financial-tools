Go to Invoicing -> Reporting -> Management -> Journal Item Drilldown to browse
journal items in the pseudo hierarchy that this module provides.

By default, you will get a pivot view with the three levels expanded:

  .. figure:: https://raw.githubusercontent.com/OCA/account-financial-tools/12.0/account_move_line_drilldown/static/description/drilldown_pivot.png
     :scale: 80 %
     :alt: journal Item Drilldown pivot view

The three levels are: the account root code (first digit of the account code),
the account sub code (first two digits of the account code) and the account
itself. You can easily collapse a level by deselecting them in the `Group By`
dropdown in the search bar.

You can also browse the journal items by switching to the tree view and click
through the grouping levels in that view.

  .. figure:: https://raw.githubusercontent.com/OCA/account-financial-tools/12.0/account_move_line_drilldown/static/description/drilldown_tree.png
     :scale: 80 %
     :alt: journal Item Drilldown tree view
