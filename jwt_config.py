from jwt import encode, decode

def solicita_token(dato: dict) -> str:
    # El método encode no presenta problemas en su uso
    token: str = encode(payload=dato, key='TYPE-ORT-MERCURY', algorithm='HS256')
    return token

def valida_token(token: str) -> dict:
    try:
        # El método decode debe usar el argumento `algorithms` como lista
        dato: dict = decode(token, key='TYPE-ORT-MERCURY', algorithms=['HS256'])
        return dato
    except Exception as e:
        # Manejo de errores en caso de fallo en la decodificación
        print(f"Error al decodificar el token: {e}")
        raise
