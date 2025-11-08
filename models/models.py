from pydantic import BaseModel, EmailStr, field_validator, ValidationError


class User(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    def password_length(cls, v):
        if len(v) < 6:
            raise ValueError("Password must be at least 6 characters long")
        return v
if __name__ == "__main__":
    try:
        tau = User(email="gasg@.com", password="fafaw")
    except ValidationError as e:
        errors = []
        for err in e.errors():
            errors.append(err['loc'][0])
        print(errors)