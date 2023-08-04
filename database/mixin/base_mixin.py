from database.connect_db import engine, get_session

session = get_session(engine)


class CRUDMixin(object):
    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        session.add(obj)
        session.commit()
