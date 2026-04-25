const KEY = 'devlearn_progress'

const defaultTechProgress = () => ({
  levels: {
    beginner: defaultLevelProgress(),
    intermediate: defaultLevelProgress(),
    expert: defaultLevelProgress(),
  },
  overallProgressPercent: 0,
})

const defaultLevelProgress = () => ({
  startedAt: null,
  completedAt: null,
  modules: {},
  progressPercent: 0,
})

const defaultModuleProgress = () => ({
  status: 'locked',
  startedAt: null,
  completedAt: null,
  labScore: null,
  labAttempts: 0,
  labLastCode: null,
  quizScore: null,
  quizAttempts: 0,
  quizAnswers: {},
})

function load() {
  try {
    const raw = localStorage.getItem(KEY)
    if (!raw) return initDefault()
    return migrate(JSON.parse(raw))
  } catch {
    return initDefault()
  }
}

const ALL_TECHS = ['ansible', 'terraform', 'kubernetes', 'git']

function initDefault() {
  const data = {
    schemaVersion: 1,
    lastUpdated: new Date().toISOString(),
    technologies: Object.fromEntries(ALL_TECHS.map(t => [t, defaultTechProgress()])),
    globalStats: {
      totalModulesCompleted: 0,
      totalQuizzesTaken: 0,
      averageQuizScore: 0,
      lastActivityAt: new Date().toISOString(),
    },
  }
  save(data)
  return data
}

// Migrate existing localStorage that pre-dates a new technology being added
function migrate(data) {
  let changed = false
  for (const tech of ALL_TECHS) {
    if (!data.technologies[tech]) {
      data.technologies[tech] = defaultTechProgress()
      changed = true
    }
  }
  if (changed) save(data)
  return data
}

function save(data) {
  data.lastUpdated = new Date().toISOString()
  localStorage.setItem(KEY, JSON.stringify(data))
}

export function getProgress() {
  return load()
}

export function getTechProgress(tech) {
  const data = load()
  return data.technologies[tech] || defaultTechProgress()
}

export function getLevelProgress(tech, level) {
  const data = load()
  return data.technologies[tech]?.levels[level] || defaultLevelProgress()
}

export function getModuleProgress(tech, level, moduleId) {
  const data = load()
  return data.technologies[tech]?.levels[level]?.modules[moduleId] || defaultModuleProgress()
}

export function initModulesForLevel(tech, level, moduleIds) {
  const data = load()
  const levelData = data.technologies[tech].levels[level]
  if (!levelData.modules[moduleIds[0]]) {
    // First module available, rest locked
    moduleIds.forEach((id, idx) => {
      if (!levelData.modules[id]) {
        levelData.modules[id] = { ...defaultModuleProgress(), status: idx === 0 ? 'available' : 'locked' }
      }
    })
    save(data)
  }
  return data
}

export function markModuleStarted(tech, level, moduleId) {
  const data = load()
  const mod = data.technologies[tech].levels[level].modules[moduleId] || defaultModuleProgress()
  if (!mod.startedAt) mod.startedAt = new Date().toISOString()
  mod.status = 'in-progress'
  data.technologies[tech].levels[level].modules[moduleId] = mod
  if (!data.technologies[tech].levels[level].startedAt) {
    data.technologies[tech].levels[level].startedAt = new Date().toISOString()
  }
  save(data)
}

export function saveLabScore(tech, level, moduleId, score, code) {
  const data = load()
  const mod = data.technologies[tech].levels[level].modules[moduleId] || defaultModuleProgress()
  mod.labScore = score
  mod.labAttempts = (mod.labAttempts || 0) + 1
  mod.labLastCode = code
  data.technologies[tech].levels[level].modules[moduleId] = mod
  save(data)
}

export function saveQuizResult(tech, level, moduleIds, score, answers) {
  const data = load()
  const levelData = data.technologies[tech].levels[level]

  // Store against the level itself
  if (!levelData.quiz) levelData.quiz = {}
  levelData.quiz.score = score
  levelData.quiz.attempts = (levelData.quiz.attempts || 0) + 1
  levelData.quiz.completedAt = new Date().toISOString()
  levelData.quiz.answers = answers

  // Mark all modules in level as completed if quiz passed
  if (score >= 70) {
    for (const modId of moduleIds) {
      const mod = levelData.modules[modId] || defaultModuleProgress()
      if (mod.status !== 'completed') {
        mod.status = 'completed'
        mod.completedAt = new Date().toISOString()
        levelData.modules[modId] = mod
      }
    }
    levelData.completedAt = new Date().toISOString()
    data.globalStats.totalModulesCompleted += moduleIds.length
    data.globalStats.totalQuizzesTaken += 1
    // Unlock next level
    const levels = ['beginner', 'intermediate', 'expert']
    const idx = levels.indexOf(level)
    if (idx < levels.length - 1) {
      const nextLevel = levels[idx + 1]
      const nextLevelData = data.technologies[tech].levels[nextLevel]
      if (!nextLevelData.startedAt) {
        // Module IDs for next level will be initialized when user visits
        nextLevelData.unlocked = true
      }
    }
  }

  // Recalculate progress
  const allLevels = ['beginner', 'intermediate', 'expert']
  let completedLevels = 0
  for (const lvl of allLevels) {
    if (data.technologies[tech].levels[lvl].completedAt) completedLevels++
  }
  data.technologies[tech].overallProgressPercent = Math.round((completedLevels / 3) * 100)

  data.globalStats.lastActivityAt = new Date().toISOString()
  const scores = allLevels.map(l => data.technologies[tech].levels[l].quiz?.score).filter(s => s != null)
  if (scores.length) data.globalStats.averageQuizScore = Math.round(scores.reduce((a, b) => a + b, 0) / scores.length)

  save(data)
  return data
}

export function isLevelUnlocked(tech, level) {
  if (level === 'beginner') return true
  const data = load()
  const levels = ['beginner', 'intermediate', 'expert']
  const idx = levels.indexOf(level)
  if (idx <= 0) return true
  const prevLevel = levels[idx - 1]
  return !!(data.technologies[tech]?.levels[prevLevel]?.completedAt || data.technologies[tech]?.levels[prevLevel]?.unlocked)
}

export function resetProgress() {
  localStorage.removeItem(KEY)
}
