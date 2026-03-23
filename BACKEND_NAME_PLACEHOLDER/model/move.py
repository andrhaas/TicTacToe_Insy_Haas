from typing import override
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from _base import Base


class Move(Base):
    __tablename__ = "moves"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    position: Mapped[int] = mapped_column(nullable=False)
    move_number: Mapped[int] = mapped_column(nullable=False)
    played_at: Mapped[str] = mapped_column(nullable=False, server_default="now()")

    game: Mapped["Game"] = relationship("Game", back_populates="moves")
    player: Mapped["User"] = relationship("User", back_populates="moves")

    @override
    def __repr__(self) -> str:
        return f"Move(id={self.id}, game_id={self.game_id}, user_id={self.user_id}, position={self.position}, move_number={self.move_number})"