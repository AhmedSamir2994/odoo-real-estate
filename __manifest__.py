{
    'name':"Real Estate",
    'author':'Ahmed Samir',
    'category':'',
    'version':'17.0.0.1.0',
    'depends':['base', 'sale_management' , 'account_accountant','mail','contacts'
               ],
    'data':[
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order.xml',
        'views/res_partner_view.xml',
        'views/base_menu.xml',

    ],
    'assets': {
    'web.assets_backend': [
        'Real_Estate/static/src/css/property.css',
    ],
}
,
    'application':True,
}
