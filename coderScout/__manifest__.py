{
    "name": "CoderSount",
    "author": "DIVY PATEL",
    "license": "LGPL-3",
    'category': 'Human Resources',
    "version": "18.0.1.0",
    'depends': ['base','hr_recruitment','web'],
    "data": [
        "security/ir.model.access.csv",
        # "views/menu.xml",
        "views/assessment.xml",
        "views/sendAssessmentButton.xml",
        'views/res_config_settings_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
