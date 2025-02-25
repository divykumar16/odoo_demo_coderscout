from odoo import api, models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    coder_scout_api_key = fields.Char(string="CoderScout API Key", config_parameter='coder_scout_api_key',
                                      help="API Key for connecting to the CoderScout service.", )
