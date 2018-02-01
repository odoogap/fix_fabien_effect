# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_mrp_routings = fields.Selection([
        (0, "Manage production by manufacturing orders"),
        (1, "Manage production by work orders")], "Routings & Planning",
        implied_group='mrp.group_mrp_routings',
        help='Work Order Operations allow you to create and manage the manufacturing operations that should be followed '
             'within your work centers in order to produce a product. They are attached to bills of materials '
             'that will define the required raw materials.')
