from typing import override
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from _base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[str] = mapped_column(nullable=False, server_default="now()")

    games_as_x: Mapped[list["Game"]] = relationship("Game", foreign_keys="[Game.player_x_id]", back_populates="player_x")
    games_as_o: Mapped[list["Game"]] = relationship("Game", foreign_keys="[Game.player_o_id]", back_populates="player_o")
    moves: Mapped[list["Move"]] = relationship("Move", back_populates="player")

    @override
    def __repr__(self) -> str:
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"