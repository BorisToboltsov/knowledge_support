from services.init_database.add_entity_language import InitDbEntityLanguage
from services.init_database.add_filter_questions import InitDbFilterQuestions
from services.init_database.add_language import InitDbSaveLanguage
from services.init_database.migrate_database import save_question_answers

init_db_save_language = InitDbSaveLanguage()
init_db_save_language.write_language()

init_db_entity_language = InitDbEntityLanguage()
init_db_entity_language.write_entity_language()

init_db_filter_questions = InitDbFilterQuestions()
init_db_filter_questions.write_filter_questions()

save_question_answers()
