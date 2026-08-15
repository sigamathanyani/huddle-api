from pydantic import BaseModel

class CreateUser(BaseModel):
    email           : str
    username        : str
    plain_password  : str
    profile_picture : str | None = None

class CreateResponse(BaseModel):
    email           : str = ''
    username        : str = ''
    plain_password  : str = ''
    profile_picture : str | None = None

    class Config:
        from_attributes = True

class CompleteUserProfile(BaseModel):
    name            : str = ''
    surname         : str = ''
    gender          : str = ''
    profile_picture : str | None = None

class LoginUser(BaseModel):
    email           : str
    username        : str
    plain_password  : str

class UserResponse(BaseModel):
    email           : str
    username        : str
    name            : str
    surname         : str
    phone_number    : str
    profile_picture : str | None

    class Config:
        from_attributes = True

class UserCompleteProfileResponse(BaseModel):
    name            : str = ''
    surname         : str = ''
    gender          : str = ''
    profile_picture : str | None = None

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token    : str 

    class Config:
        from_attributes = True


class Temp(BaseModel):
    email           : str
    username        : str
    profile_picture : str | None

    class Config:
        from_attributes = True