from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, Sequence
from sqlalchemy.orm import Session

from app.db.models import Base


class Site(Base):
    """
    站点表
    """
    id = Column(Integer, Sequence('id'), primary_key=True, index=True)
    name = Column(String, nullable=False)
    domain = Column(String, index=True)
    url = Column(String, nullable=False)
    pri = Column(Integer)
    rss = Column(String)
    cookie = Column(String)
    ua = Column(String)
    proxy = Column(Integer)
    filter = Column(String)
    render = Column(Integer)
    note = Column(String)
    limit_interval = Column(Integer, default=0)
    limit_count = Column(Integer, default=0)
    limit_seconds = Column(Integer, default=0)
    is_active = Column(Boolean(), default=True)
    lst_mod_date = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    @staticmethod
    def get_by_domain(db: Session, domain: str):
        return db.query(Site).filter(Site.domain == domain).first()

    @staticmethod
    def get_actives(db: Session):
        return db.query(Site).filter(Site.is_active == 1).all()


class SiteIcon(Base):
    """
    站点图标表
    """
    id = Column(Integer, Sequence('id'), primary_key=True, index=True)
    name = Column(String, nullable=False)
    domain = Column(String, index=True)
    url = Column(String, nullable=False)
    base64 = Column(String)

    @staticmethod
    def get_by_domain(db: Session, domain: str):
        return db.query(SiteIcon).filter(SiteIcon.domain == domain).first()
