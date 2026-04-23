const express = require('express');
const router = express.Router();
const { getTechnologies, getTechnology } = require('../services/contentService');

router.get('/', (req, res, next) => {
  try { res.json(getTechnologies()); } catch(e) { next(e); }
});

router.get('/:tech', (req, res, next) => {
  try {
    const tech = getTechnology(req.params.tech);
    if (!tech) return res.status(404).json({ error: 'Technology not found' });
    res.json(tech);
  } catch(e) { next(e); }
});

module.exports = router;
