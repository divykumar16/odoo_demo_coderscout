from odoo import api, models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    coderscout_api_key = fields.Char(
        string="CoderScout API Key",
        config_parameter='coderscout.api_key',
        help="API Key for connecting to the CoderScout service.",
    )
