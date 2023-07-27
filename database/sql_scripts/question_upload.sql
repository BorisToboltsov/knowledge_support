-- Generating questions json from an old database
SELECT tq.id, tq.multi_answer, image, question_text, question_text_en, execution_time, explanation, explanation_en, tp.programming_language FROM taskapp_question AS tq
JOIN taskapp_programminglanguage AS tp ON tq.programming_language_id = tp.id;