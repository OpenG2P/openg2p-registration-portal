{
    "name": "ODK App User Mapping",
    "category": "G2P",
    "version": "17.0.1.0.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "depends": ["base", "account", "g2p_odk_importer"],
    "data": [
        "security/ir.model.access.csv",
        "views/registration_backend_view.xml",
        "views/odk_app_user.xml",
    ],
    "assets": {
        "web.assets_frontend": [],
        "web.assets_common": [],
        "website.assets_wysiwyg": [],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}
