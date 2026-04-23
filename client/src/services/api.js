const BASE = '/api'

async function request(path, options = {}) {
  const res = await fetch(`${BASE}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })
  if (!res.ok) {
    const err = await res.json().catch(() => ({ error: res.statusText }))
    throw new Error(err.error || `HTTP ${res.status}`)
  }
  return res.json()
}

export const api = {
  getTechnologies: () => request('/technologies'),
  getTechnology: (tech) => request(`/technologies/${tech}`),
  getLevels: (tech) => request(`/technologies/${tech}/levels`),
  getLevel: (tech, level) => request(`/technologies/${tech}/levels/${level}`),
  getModules: (tech, level) => request(`/technologies/${tech}/levels/${level}/modules`),
  getModule: (tech, level, moduleId) => request(`/technologies/${tech}/levels/${level}/modules/${moduleId}`),
  getLab: (tech, level, moduleId) => request(`/technologies/${tech}/levels/${level}/modules/${moduleId}/lab`),
  runLab: (tech, level, moduleId, code) => request(`/technologies/${tech}/levels/${level}/modules/${moduleId}/lab/run`, { method: 'POST', body: JSON.stringify({ code }) }),
  getQuiz: (tech, level) => request(`/technologies/${tech}/levels/${level}/quiz`),
  answerQuestion: (tech, level, questionId, answer) => request(`/technologies/${tech}/levels/${level}/quiz/answer`, { method: 'POST', body: JSON.stringify({ questionId, answer }) }),
  submitQuiz: (tech, level, answers) => request(`/technologies/${tech}/levels/${level}/quiz/submit`, { method: 'POST', body: JSON.stringify({ answers }) }),
}
