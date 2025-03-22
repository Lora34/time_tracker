from pydantic import BaseModel, Field, model_validator

class Task(BaseModel):
    id: int | None = None
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int = Field(exclude=False)


    @model_validator(mode='after')
    def check_name(self):
        #print(self)
        if self.name is None:
            raise ValueError('Passwords do not match')
        return self