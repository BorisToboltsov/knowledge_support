from sqlalchemy import UUID, BigInteger, Column, DateTime, ForeignKey

from database.base.model.base import Base


class Profile(Base):
    __tablename__ = "profile"
    __tableargs__ = {"comment": "Profile"}

    activity = Column(name="activity", type_=DateTime, comment="User activity")
    answers_true = Column(name="answers_true", type_=BigInteger, comment="Answers true")
    answers_false = Column(
        name="answers_false", type_=BigInteger, comment="Answers False"
    )
    interface_language_id = Column(
        UUID,
        ForeignKey("entity_language.id", ondelete="NO ACTION"),
        nullable=False,
    )
    account_id = Column(
        UUID,
        ForeignKey("account.id", ondelete="NO ACTION"),
        nullable=False,
    )
    filter_questions_id = Column(
        UUID,
        ForeignKey("filter_questions.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.id}"
