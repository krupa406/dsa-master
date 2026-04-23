const express = require('express');
const router = express.Router();
const { getQuiz, getQuizWithAnswers } = require('../services/contentService');

router.get('/:tech/levels/:level/quiz', (req, res, next) => {
  try {
    const quiz = getQuiz(req.params.tech, req.params.level);
    if (!quiz) return res.status(404).json({ error: 'Quiz not found' });
    res.json(quiz);
  } catch(e) { next(e); }
});

// Per-question answer check — returns feedback immediately
router.post('/:tech/levels/:level/quiz/answer', (req, res, next) => {
  try {
    const { questionId, answer } = req.body;
    if (!questionId || !answer) return res.status(400).json({ error: 'questionId and answer required' });
    const questions = getQuizWithAnswers(req.params.tech, req.params.level);
    if (!questions) return res.status(404).json({ error: 'Quiz not found' });
    const q = questions.find(q => q.id === questionId);
    if (!q) return res.status(404).json({ error: 'Question not found' });
    const correct = answer === q.correctOptionId;
    res.json({ questionId, correct, correctOption: q.correctOptionId, explanation: q.explanation, citations: q.citations, points: q.points });
  } catch(e) { next(e); }
});

router.post('/:tech/levels/:level/quiz/submit', (req, res, next) => {
  try {
    const { answers } = req.body;
    if (!answers) return res.status(400).json({ error: 'answers required' });
    const questions = getQuizWithAnswers(req.params.tech, req.params.level);
    if (!questions) return res.status(404).json({ error: 'Quiz not found' });

    let score = 0;
    const results = questions.map(q => {
      const selected = answers[q.id];
      const correct = selected === q.correctOptionId;
      if (correct) score += q.points;
      return { questionId: q.id, selectedOption: selected, correctOption: q.correctOptionId, correct, explanation: q.explanation, citations: q.citations, points: q.points };
    });
    const totalPoints = questions.reduce((s, q) => s + q.points, 0);
    const pct = Math.round((score / totalPoints) * 100);
    res.json({ score: pct, rawScore: score, totalPoints, passed: pct >= 70, results });
  } catch(e) { next(e); }
});

module.exports = router;
