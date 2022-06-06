from odoo import models, fields, api


class PaymentMethod(models.Model):
    _name = "crud.create"
    _description = "Create crud"

    name = fields.Char(string='Name', track_visibility='onchange')
    email = fields.Char(string='Email',track_visibility='onchange')
    cell = fields.Char(string='Cell',track_visibility='onchange')