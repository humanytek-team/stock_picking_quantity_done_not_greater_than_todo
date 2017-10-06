# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, models
from openerp.exceptions import ValidationError
from openerp.tools.translate import _


class StockPackOperation(models.Model):
    _inherit = 'stock.pack.operation'

    @api.constrains('qty_done')
    def _check_qty_done(self):
        if not self.user_has_groups('stock.group_stock_manager'):
            for record in self:
                if record.qty_done > record.product_qty:
                    raise ValidationError(
                        _('The quantity done should not be greater than quantity to do')
                        )
