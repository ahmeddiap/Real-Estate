from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'
    _description = 'Property'


    name = fields.Char(required=1, default='New', size=10)
    description = fields.Text()
    postcode = fields.Char(required=1)
    date_availability = fields.Date()
    expected_Price = fields.Float(digits=(0, 2))
    selling_Price = fields.Float()
    diff = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], default='north')
    owner_id = fields.Many2one('owner')

    @api.constrains('bedrooms')
    def check_bedrooms(self):
        for rec in self:
            if rec.bedrooms <= 0:
                raise ValidationError('Please add valid number of bedrooms!')

    @api.model_create_multi
    def create(self, vals):
        res = super(Property, self).create(vals)
        # print(f"self: {self}, vals: {vals}, res: {res}")
        return res

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        res = super(Property, self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
        # print(f"self: {self}\n domain: {domain}\n offset: {offset}\n limit: {limit}\n order: {order}\n access_rights_uid: {access_rights_uid}")
        return res





