CONFIG = {
    'sqlite': {
        'database': 'topzeit',
    },
    'die_zeit': {
        'endpoint': 'http://api.zeit.de/content',
        'api_key': '4dc7a859b685d0e9b0ec20fd4382e349e6c734f5c02b7b5ba400',
    },
}

def get_database_credentials():
    return CONFIG['sqlite']

def get_die_zeit_credentials():
    return CONFIG['die_zeit']

