import { useState } from 'react'
import { useParams } from 'react-router-dom'
import { useApi } from '../hooks/useApi'
import { api } from '../services/api'
import { saveQuizResult } from '../utils/progressStorage'
import { useProgressContext } from '../context/ProgressContext'
import LoadingSpinner from '../components/shared/LoadingSpinner'
import ErrorMessage from '../components/shared/ErrorMessage'
import QuizContainer from '../components/quiz/QuizContainer'

export default function QuizPage() {
  const { tech, level } = useParams()
  const { refresh } = useProgressContext()
  const { data: quiz, loading, error } = useApi(() => api.getQuiz(tech, level), [tech, level])
  const { data: levelMeta } = useApi(() => api.getLevel(tech, level), [tech, level])

  async function handleSubmit(answers) {
    const result = await api.submitQuiz(tech, level, answers)
    saveQuizResult(tech, level, levelMeta?.moduleOrder || [], result.score, answers)
    refresh()
    return result
  }

  if (loading) return <LoadingSpinner />
  if (error) return <div className="p-8"><ErrorMessage message={error} /></div>

  return (
    <div className="max-w-3xl mx-auto px-4 py-8">
      <div className="mb-6">
        <h1 className="text-2xl font-bold text-white capitalize">{tech} {level} Quiz</h1>
        <p className="text-gray-400 text-sm mt-1">10 questions · 70% to pass · Official docs cited for every answer</p>
      </div>
      {quiz && <QuizContainer quiz={quiz} onSubmit={handleSubmit} tech={tech} level={level} />}
    </div>
  )
}
