# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_account_user = fields.Boolean('Show Full Accounting Features', implied_group='account.group_account_user')
