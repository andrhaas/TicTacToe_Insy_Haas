import enum
from typing import Optional, override
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from _base import Base


class GameStatus(str, enum.Enum):
    waiting = "waiting"
    in_progress = "in_progress"
    x_won = "x_won"
    o_won = "o_won"
    draw = "draw"


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    player_x_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    player_o_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), nullable=True)
    status: Mapped[GameStatus] = mapped_column(Enum(GameStatus), nullable=False, default=GameStatus.waiting, server_default=GameStatus.waiting.value)
    created_at: Mapped[str] = mapped_column(nullable=False, server_default="now()")
    updated_at: Mapped[str] = mapped_column(nullable=False, server_default="now()", onupdate="now()")

    player_x: Mapped["User"] = relationship("User", foreign_keys=[player_x_id], back_populates="games_as_x")
    player_o: Mapped[Optional["User"]] = relationship("User", foreign_keys=[player_o_id], back_populates="games_as_o")
    moves: Mapped[list["Move"]] = relationship("Move", back_populates="game", cascade="all, delete-orphan")

    @override
    def __repr__(self) -> str:
        return f"Game(id={self.id}, status='{self.status.value}', player_x_id={self.player_x_id}, player_o_id={self.player_o_id})"