-- Generating answers json from an old database
SELECT ta.questions_id, ta.answer, ta.answer_en, ta.is_correct FROM taskapp_answer AS ta;