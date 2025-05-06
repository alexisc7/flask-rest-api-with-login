# Funciones auxiliares

def serialize_row(row):
    return {
        key: (row[key].decode("utf-8") if isinstance(row[key], bytes) else row[key])
        for key in row.keys()
    }