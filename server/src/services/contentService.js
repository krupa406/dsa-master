const path = require('path');
const fs = require('fs');

const DATA_DIR = path.join(__dirname, '..', 'data');

function loadJson(filePath) {
  const full = path.join(DATA_DIR, filePath);
  if (!fs.existsSync(full)) return null;
  return JSON.parse(fs.readFileSync(full, 'utf-8'));
}

function getTechnologies() {
  return ['ansible', 'terraform', 'kubernetes']
    .map(t => loadJson(`${t}/meta.json`))
    .filter(Boolean);
}

function getTechnology(tech) {
  return loadJson(`${tech}/meta.json`);
}

function getLevels(tech) {
  const levels = ['beginner', 'intermediate', 'expert'];
  return levels.map(l => loadJson(`${tech}/${l}/level-meta.json`)).filter(Boolean);
}

function getLevel(tech, level) {
  return loadJson(`${tech}/${level}/level-meta.json`);
}

function getModules(tech, level) {
  const meta = getLevel(tech, level);
  if (!meta) return null;
  return meta.moduleOrder.map(moduleId => {
    const m = loadJson(`${tech}/${level}/${moduleId}/module.json`);
    if (!m) return null;
    return { id: m.id, title: m.title, order: m.order, estimatedMinutes: m.estimatedMinutes, tags: m.tags };
  }).filter(Boolean);
}

function getModule(tech, level, moduleId) {
  return loadJson(`${tech}/${level}/${moduleId}/module.json`);
}

function getLab(tech, level, moduleId) {
  const lab = loadJson(`${tech}/${level}/${moduleId}/lab.json`);
  if (!lab) return null;
  const { solutionCode, ...safe } = lab;
  return safe;
}

function getLabFull(tech, level, moduleId) {
  return loadJson(`${tech}/${level}/${moduleId}/lab.json`);
}

function getQuiz(tech, level) {
  const levelMeta = getLevel(tech, level);
  if (!levelMeta) return null;
  const questions = [];
  for (const moduleId of levelMeta.moduleOrder) {
    const quiz = loadJson(`${tech}/${level}/${moduleId}/quiz.json`);
    if (quiz) questions.push(...quiz.questions);
  }
  const sanitized = questions.map(({ correctOptionId, ...q }) => q);
  return { tech, level, questions: sanitized.slice(0, 10), total: Math.min(questions.length, 10), passingScore: 70 };
}

function getQuizWithAnswers(tech, level) {
  const levelMeta = getLevel(tech, level);
  if (!levelMeta) return null;
  const questions = [];
  for (const moduleId of levelMeta.moduleOrder) {
    const quiz = loadJson(`${tech}/${level}/${moduleId}/quiz.json`);
    if (quiz) questions.push(...quiz.questions);
  }
  return questions.slice(0, 10);
}

module.exports = { getTechnologies, getTechnology, getLevels, getLevel, getModules, getModule, getLab, getLabFull, getQuiz, getQuizWithAnswers };
