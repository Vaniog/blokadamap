from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, joinedload

from app.authors.models import (
    Author,
    Card,
    Education,
    FamilyStatus,
    Nationality,
    Occupation,
    PoliticalParty,
    Religion,
    SocialClass,
    author2card,
    author2education,
    author2nationality,
    author2occupation,
    author2political_party,
    author2religion,
    author2social_class,
)
from app.authors.validations import Author as AuthorValidation


class AuthorService:
    db: Session

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_filters(self):
        return {
            "family_statuses": self.db.query(FamilyStatus).all(),
            "social_classes": self.db.query(SocialClass).all(),
            "nationalities": self.db.query(Nationality).all(),
            "religions": self.db.query(Religion).all(),
            "educations": self.db.query(Education).all(),
            "occupations": self.db.query(Occupation).all(),
            "political_parties": self.db.query(PoliticalParty).all(),
            "cards": self.db.query(Card).all(),
        }

    def get_all(self):
        return self.db.query(Author).all()

    def get_by_id(self, id: int, extended: bool):
        if not extended:
            return (
                self.db.query(
                    Author.author_id,
                    Author.first_name,
                    Author.middle_name,
                    Author.last_name,
                )
                .filter(Author.author_id == id)
                .first()
                ._asdict()  # type: ignore
            )

        return (
            self.db.query(Author)
            .filter(Author.author_id == id)
            .options(
                joinedload(Author.social_classes),
                joinedload(Author.nationalities),
                joinedload(Author.religions),
                joinedload(Author.education),
                joinedload(Author.occupation),
                joinedload(Author.political_parties),
                joinedload(Author.cards),
            )
            .first()
        )

    def create(self, author: AuthorValidation):
        try:
            new_author = Author(
                last_name=author.last_name,
                first_name=author.first_name,
                middle_name=author.middle_name,
                sex=author.sex,
                birth_date=author.birth_date,
                biography=author.biography,
                has_children=author.has_children,
                family_status=self.db.query(FamilyStatus)
                .filter(FamilyStatus.family_status_id == author.family_status)
                .first(),
            )
            self.db.add(new_author)
            self.db.commit()
            self.db.refresh(new_author)
            self.db.execute(
                author2social_class.insert().values(
                    author_id=new_author.author_id, social_class_id=author.social_class
                )
            )
            self.db.execute(
                author2nationality.insert().values(
                    author_id=new_author.author_id, nationality_id=author.nationality
                )
            )
            self.db.execute(
                author2religion.insert().values(
                    author_id=new_author.author_id, religion_id=author.religion
                )
            )
            self.db.execute(
                author2education.insert().values(
                    author_id=new_author.author_id, education_id=author.education
                )
            )
            self.db.execute(
                author2occupation.insert().values(
                    author_id=new_author.author_id, occupation_id=author.occupation
                )
            )
            self.db.execute(
                author2political_party.insert().values(
                    author_id=new_author.author_id,
                    political_party_id=author.political_party,
                )
            )
            self.db.execute(
                author2card.insert().values(
                    author_id=new_author.author_id, card_id=author.card
                )
            )
            self.db.commit()
            return new_author
        except IntegrityError as e:
            raise Exception(str(e.orig))
