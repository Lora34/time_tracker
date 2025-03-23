from database import Base
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, declared_attr

class UserProfile(Base):
    __table__= "UserProfile"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    access_token: Mapped[str] = mapped_column(nullable=False)