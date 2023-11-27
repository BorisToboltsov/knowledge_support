from services.init_database.add_entity_language import InitDbEntityLanguage
from services.init_database.add_filter_questions import save_filter_questions
from services.init_database.add_language import save_language
from services.init_database.migrate_database import save_question_answers

save_language()

init_db_entity_language = InitDbEntityLanguage()
init_db_entity_language.write_entity_language()

save_filter_questions()
save_question_answers()
