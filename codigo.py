# -*- coding: utf-8 -*-
#from odoo import models, api, fields
import logging

from openerp import api, fields, models, _ 
from openerp.exceptions import UserError, ValidationError
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT as DF


# Este lo usamos para realizar las pruebas
_logger = logging.getLogger(__name__)

class saleOrder(models.Model):
	_name = 'sale.order'
	_inherit = 'sale.order'

	consignacion = fields.Boolean('Consignación')