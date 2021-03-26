dependencies = {
    'definitions': {
        'db_read': {
            'item': 'app_name.db.create_session',
            'init': {
                'connection_string': 'mssql+pyodbc://Teste'
            }
        },
        'db_write': {
            'item': 'app_name.db.create_session',
            'init': {
                'connection_string': 'mssql+pyodbc://Teste'
            }
        }
    }
}