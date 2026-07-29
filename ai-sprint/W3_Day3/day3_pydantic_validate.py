from pydantic import BaseModel, Field, field_validator


class UserAccount(BaseModel):
    username: str = Field(min_length=3)

    @field_validator("username")
    @classmethod
    def validate_no_spaces(cls, v: str) -> str:
        if " " in v:
            raise ValueError("User name cannot contain spaces")
        return v.lower()


user1 = '{"username":"John Doe"}'
user2 = '{"username":"Alice}'
try:
    UserAccount.model_validate_json(user1)
except ValueError as e:
    print(e.errors())
