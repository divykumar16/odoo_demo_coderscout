from email.policy import default

import requests
from odoo import api, models, fields
from odoo.exceptions import UserError


class CoderScoutAssessment(models.Model):
    _name = 'coder_scout.assessment'
    _description = "Candidate Assessment Details"

    candidate_id = fields.Many2one('hr.candidate', string="Candidate", required=True)
    candidate_id_number = fields.Integer(related="candidate_id.id", string="Candidate ID", readonly=True)
    coderScout_assessment_name = fields.Selection(
        selection=lambda self: self._get_coderscout_assessments(),
        string="CoderScout Assessment Name", required=True,
    )
    job_opening = fields.Many2one('hr.job', string="Odoo Job Opening", required=True)
    test_start_time = fields.Datetime(string="Assessment Start Time", required=True)
    score = fields.Integer(string="Score")
    assessment_report_url = fields.Char(string="Assessment Report URL")
    feedback = fields.Text(string="Feedback")

    @api.constrains('test_start_time')
    def _check_start_time(self):
        for record in self:
            if record.test_start_time and record.test_start_time < fields.Datetime.now():
                raise UserError('The Assessment Start Time must be in the future.')

    @api.model
    def _get_coderscout_assessments(self):
        api_key = self.env['ir.config_parameter'].sudo().get_param('coderscout.api_key')
        if not api_key:
            raise UserError(
                'CoderScout API key is missing.\n'
                'Please contact your administrator to add the CoderScout API key in Recruitment Settings.'
            )

        url = 'https://api.coderscout.io/api/contests/assessment-list'
        headers = {
            'x-api-key': api_key
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            assessments = response.json()

            if not assessments:
                raise UserError(
                    'No assessments found from the CoderScout API.\n'
                    'Please check the API key and ensure assessments exist in your account.'
                )

            assessment_choices = [(str(assessment['id']), assessment['name']) for assessment in assessments]
            return assessment_choices
        except requests.exceptions.RequestException as e:
            raise UserError(
                'CoderScout API key issue detected.\n'
                'Please contact your administrator to verify the API key and try again.'
            )

    def display_notification(self, title, msg_type, message):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': title,
                'type': msg_type,
                'message': message,
                'sticky': False,
                'next': {'type': 'ir.actions.act_window_close'},
            }
        }

    def action_submit(self):
        for record in self:
            if record.test_start_time:
                test_start_time_str = record.test_start_time.strftime(
                    '%Y-%m-%dT%H:%M:%S') + f".{int(record.test_start_time.microsecond / 1000):03d}Z"
            else:
                test_start_time_str = None

            # Prepare API data
            database_name = self.env.cr.dbname
            admin_user = self.env['res.users'].search([('groups_id', 'in', self.env.ref('base.group_system').id)],
                                                      limit=1)
            api_data = {
                'adminID': admin_user.id,
                'databaseName': database_name,
                'odooAssessment_id': record.id,
                'candidate_id': record.candidate_id.id,
                'assessment_id': record.coderScout_assessment_name,
                'job_opening': record.job_opening.id,
                'test_start_time': test_start_time_str
            }
            print(f"API Data: {api_data}")
            # CoderScout API URL
            api_url = 'https://api.coderscout.io/api/candidates/recruit-invite_ODOOOOOO'

            # try:
            #     response = requests.post(api_url, json=api_data)
            #
            #     if response.status_code == 200:
            #         coderScoutResponse = response.json()
            #
            #         if coderScoutResponse.get('status') == 'success':
            #             status_message = coderScoutResponse.get('details', {}).get('statusMessage',
            #                                                                        'No status message available')
            return self.display_notification("Assessment", 'success', "status_message")
    #             else:
    #                 status_message = coderScoutResponse.get('details', {}).get('statusMessage',
    #                                                                            'Failed to submit the assessment.')
    #                 return self.display_notification("Error", 'danger', status_message)
    #
    #         else:
    #             return self.display_notification("Error", 'danger',
    #                                              f"Request failed with status code: {response.status_code}")
    #
    #     except requests.exceptions.RequestException as e:
    #         return self.display_notification("Error", 'Please contact your administrator to verify the API key and try again.', f"An error occurred: {e}")
    #
    # return False


class HRCandidate(models.Model):
    _inherit = 'hr.candidate'

    def action_send_assessment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Send Assessment',
            'res_model': 'coder_scout.assessment',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_candidate_id': self.id,
            },
        }
