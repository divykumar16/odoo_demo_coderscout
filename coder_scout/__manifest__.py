{
    "name": "CoderScout",
    "author": "DIVY PATEL",
    "license": "LGPL-3",
    'category': 'Human Resources',
    "version": "18.0.1.0",
    'depends': ['base','hr_recruitment'],
    "data": [
        "security/ir.model.access.csv",
        "views/assessment.xml",
        "views/ir_send_assessment_button.xml",
        'views/res_config_settings_view.xml',
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}
