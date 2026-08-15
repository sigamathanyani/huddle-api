from datetime import datetime, timedelta

from fastapi import HTTPException, status
from jose import ExpiredSignatureError, JWTError, jwt

from app.utils.status_codes import StatusCodes


SECRET_KEY = 'SECRET_KEY'
ALGORITHM = 'HS256'



def generate_token(payload: dict, token_type: str):
    try:
        payload_copy = payload.copy()
        expire = datetime.now() + timedelta(minutes=10)

        payload_copy.update({'exp': expire, 'token_type': token_type})
    except ExpiredSignatureError as ex:
        ex.add_note("TEST")
        raise
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    return jwt.encode(claims=payload_copy, key=SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str):
    try:
        return jwt.decode(token=token, key=SECRET_KEY, algorithms=ALGORITHM)
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "message": "Token has expired please log in again",
                "error_code": StatusCodes.AUTH_TOKEN_EXPIRED
            }
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "message": "Invalid Token",
                "error_code": StatusCodes.AUTH_TOKEN_INVALID
            }
        )