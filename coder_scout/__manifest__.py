{
    "name": "CoderScout",
    "version": "18.0.1.0",
    'category': 'Human Resources',
    "author": "DIVY PATEL",
    'depends': ['base', 'hr_recruitment'],

    'website': 'https://www.coderscout.io/',
    "summary": """Leverage AI-Powered Assessments to Find the Right Talent Faster, Smarter, and with Confidence.
                  Simplify hiring for programmers, data scientists, and IT specialists—one smart test at a time.""",
    "data": [
        "security/ir.model.access.csv",
        "views/assessment.xml",
        "views/ir_send_assessment_button.xml",
        'views/res_config_settings_view.xml',
    ],
    'price': 49.99,
    'currency': 'USD',
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}
