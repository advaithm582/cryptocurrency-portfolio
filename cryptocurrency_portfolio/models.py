from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, REAL
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from cryptocurrency_portfolio.constants import DB_URL

engine = create_engine(DB_URL)
# Session = sessionmaker(bind=engine)
Base = declarative_base()

class CryptocoinPortfolio(Base):
	__tablename__ = 'ccportfolio'

	id = Column(Integer, primary_key=True)
	symbol = Column(String)
	num_owned = Column(Integer)
	price_per_coin = Column(REAL)
	def __repr__(self):
		return "<Portfolio(symbol='%s', num_owned='%s', price_per_coin='%s')>" % (self.symbol, self.num_owned, self.price_per_coin)

Base.metadata.create_all(engine)

# session = Session()
# # ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# # session.add(ed_user)

# session.commit()