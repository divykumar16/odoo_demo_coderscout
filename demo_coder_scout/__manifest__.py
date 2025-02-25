{
    "name": "CoderScout",
    "version": "18.0.0.0",
    'category': 'Human Resources',
    "author": "CoderScout.io",
    'depends': ['base', 'hr_recruitment'],
    'website': 'https://www.coderscout.io/',
    "summary": "Leverage AI-Powered Assessments to Find the Right Talent Faster, Smarter, and with Confidence. Simplify hiring for programmers, data scientists, and IT specialists—one smart test at a time.",
    'description': """
        Efficiently hire at scale with minimal monitoring using browser-based IDEs with code completion, real-time collaboration, and AI-driven oversight.
        Screen more candidates quickly and confidently, ensuring you hire the best programmers without the hassle.
   """,
    "data": [
        "security/ir.model.access.csv",
        "views/assessment.xml",
        "views/ir_send_assessment_button.xml",
        'views/res_config_settings_view.xml',
    ],
    # 'price': 49.99,
    # 'currency': 'USD',
    "installable": True,
    "application": True,
    "license": "OPL-1"
}
