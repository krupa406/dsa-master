const express = require('express');
const router = express.Router();
const { getModules, getModule } = require('../services/contentService');

router.get('/:tech/levels/:level/modules', (req, res, next) => {
  try {
    const modules = getModules(req.params.tech, req.params.level);
    if (!modules) return res.status(404).json({ error: 'Not found' });
    res.json(modules);
  } catch(e) { next(e); }
});

router.get('/:tech/levels/:level/modules/:moduleId', (req, res, next) => {
  try {
    const mod = getModule(req.params.tech, req.params.level, req.params.moduleId);
    if (!mod) return res.status(404).json({ error: 'Module not found' });
    res.json(mod);
  } catch(e) { next(e); }
});

module.exports = router;
