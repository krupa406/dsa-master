const express = require('express');
const router = express.Router();
const { getLab, getLabFull } = require('../services/contentService');
const { runValidation } = require('../services/labValidatorService');

router.get('/:tech/levels/:level/modules/:moduleId/lab', (req, res, next) => {
  try {
    const lab = getLab(req.params.tech, req.params.level, req.params.moduleId);
    if (!lab) return res.status(404).json({ error: 'Lab not found' });
    res.json(lab);
  } catch(e) { next(e); }
});

router.post('/:tech/levels/:level/modules/:moduleId/lab/run', (req, res, next) => {
  try {
    const { code } = req.body;
    if (!code) return res.status(400).json({ error: 'code is required' });
    const lab = getLabFull(req.params.tech, req.params.level, req.params.moduleId);
    if (!lab) return res.status(404).json({ error: 'Lab not found' });
    res.json(runValidation(lab, code));
  } catch(e) { next(e); }
});

module.exports = router;
