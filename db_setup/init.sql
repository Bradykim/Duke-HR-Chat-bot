CREATE DATABASE sample_qna;
use sample_qna;

CREATE TABLE questions (
  question VARCHAR(1024),
  intent VARCHAR(1024)
);

INSERT INTO questions
  (question, intent)
VALUES
  ('How do I request a trancript?', 'transcript'),
  ('What is a permission number', 'permission number');
