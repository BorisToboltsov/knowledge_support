from database.init_database.add_fixtures import save_fixtures
from database.init_database.migrate_database import save_question_answers

save_fixtures()
save_question_answers()
