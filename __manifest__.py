# -*- coding: utf-8 -*-

{
    'name' : "Contra-recibo",
    'Category' : "Purchase",
    'summary' : """
    Módulo de reporte contra-recibo
    """, 
    'author' : "ArmandoBeltran", 
    'website' : "https://github.com/ArmandoBeltran", 
    'depends' : [
        'purchase'
    ], 
    'data' : [
        'views/purchase_order.xml',
        
        'report/upon_receipt_template_report.xml',
    ]
}