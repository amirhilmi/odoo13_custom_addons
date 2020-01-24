# _*_ coding: utf-8 _*_

from odoo import models, fields


class SchoolStudent(models.Model):
    _name = 'school.student2'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Student Table"
    # _rec_name = "analytic_id"
    # _order = "sequence"

    name = fields.Char(string="Name", required=True)
