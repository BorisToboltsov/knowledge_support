from init_database.add_fixtures import save_fixtures
from init_database.migrate_database import save_question_answers

save_fixtures()
save_question_answers()
