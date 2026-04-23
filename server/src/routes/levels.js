const express = require('express');
const router = express.Router();
const { getLevels, getLevel } = require('../services/contentService');

router.get('/:tech/levels', (req, res, next) => {
  try { res.json(getLevels(req.params.tech)); } catch(e) { next(e); }
});

router.get('/:tech/levels/:level', (req, res, next) => {
  try {
    const level = getLevel(req.params.tech, req.params.level);
    if (!level) return res.status(404).json({ error: 'Level not found' });
    res.json(level);
  } catch(e) { next(e); }
});

module.exports = router;
