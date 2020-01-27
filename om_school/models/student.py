# _*_ coding: utf-8 _*_

from odoo import models, fields


class SchoolStudent(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Student Table"

    # charity_amount = fields.Integer(string="Amount of Charity Received",  required=True)
    
    charity_amount = fields.Float(string="Amount of Charity Received (RM)", digits=(16, 2), required=True)
#     name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    personInCharge = fields.Char(string="Person In Charge")
    charity_channel = fields.Selection(
        [
            ('moneyBox_friday', 'Moneybox - Friday'),
            ('moneyBox_orphan', 'Moneybox - Orphan'),
            ('moneyBox_1', 'Moneybox - 1'),
            ('other', 'Other'),
        ], 
        string='Charity Channel', default='moneyBox_1')

    date_of_collection = fields.Datetime(string="Date Of Collection", default=fields.Datetime.now)
    # admission_date = fields.Datetime(string='Init Date', default=fields.Datetime.now)

    note = fields.Text(string="Notes")  
    image = fields.Binary(string="Receipt")
