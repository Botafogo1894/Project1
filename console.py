from data_builder import *

engine = create_engine('sqlite:///EPL_fantasy.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add_all(team_results)
session.commit()
