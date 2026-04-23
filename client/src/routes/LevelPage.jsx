import { Link, useParams } from 'react-router-dom'
import { useApi } from '../hooks/useApi'
import { api } from '../services/api'
import { useLevelProgress } from '../hooks/useProgress'
import { initModulesForLevel } from '../utils/progressStorage'
import { useProgressContext } from '../context/ProgressContext'
import { useEffect } from 'react'
import LoadingSpinner from '../components/shared/LoadingSpinner'
import ErrorMessage from '../components/shared/ErrorMessage'
import Badge from '../components/shared/Badge'
import { CheckCircle2, Circle, Clock, ChevronRight, Award } from 'lucide-react'

export default function LevelPage() {
  const { tech, level } = useParams()
  const { refresh } = useProgressContext()
  const { data: modules, loading, error } = useApi(() => api.getModules(tech, level), [tech, level])
  const levelProg = useLevelProgress(tech, level)

  useEffect(() => {
    if (modules?.length) {
      initModulesForLevel(tech, level, modules.map(m => m.id))
      refresh()
    }
  }, [modules, tech, level]) // eslint-disable-line react-hooks/exhaustive-deps

  if (loading) return <LoadingSpinner />
  if (error) return <div className="p-8"><ErrorMessage message={error} /></div>

  const completed = levelProg?.completedAt
  const quizScore = levelProg?.quiz?.score

  return (
    <div className="max-w-2xl mx-auto px-4 py-10">
      <div className="flex items-center gap-3 mb-8">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <h1 className="text-2xl font-bold text-white capitalize">{tech} — {level}</h1>
            <Badge level={level} />
          </div>
          {completed && <p className="text-green-400 text-sm flex items-center gap-1"><CheckCircle2 className="w-4 h-4" /> Level completed!</p>}
        </div>
      </div>

      <div className="space-y-3 mb-8">
        {modules?.map((mod, idx) => {
          const modProg = levelProg?.modules?.[mod.id]
          const status = modProg?.status || (idx === 0 ? 'available' : 'locked')
          const isCompleted = status === 'completed' || modProg?.completedAt
          const isAvailable = status !== 'locked' || idx === 0
          return (
            <div key={mod.id} className={`card p-5 transition-all ${isAvailable ? 'hover:border-gray-600' : 'opacity-50'}`}>
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-4">
                  {isCompleted
                    ? <CheckCircle2 className="w-6 h-6 text-green-500 shrink-0" />
                    : <Circle className="w-6 h-6 text-gray-700 shrink-0" />
                  }
                  <div>
                    <h3 className="font-medium text-white">{mod.title}</h3>
                    <div className="flex items-center gap-3 mt-1">
                      <span className="text-xs text-gray-500 flex items-center gap-1"><Clock className="w-3 h-3" />{mod.estimatedMinutes}min</span>
                      {mod.tags?.slice(0, 2).map(t => <span key={t} className="text-xs bg-gray-800 text-gray-400 px-2 py-0.5 rounded">{t}</span>)}
                    </div>
                  </div>
                </div>
                {isAvailable && (
                  <Link to={`/technology/${tech}/${level}/module/${mod.id}`}
                    className="flex items-center gap-1 text-sm text-blue-400 hover:text-blue-300 shrink-0">
                    {isCompleted ? 'Review' : 'Start'} <ChevronRight className="w-4 h-4" />
                  </Link>
                )}
              </div>
            </div>
          )
        })}
      </div>

      <div className="card p-5">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Award className={`w-6 h-6 ${quizScore >= 70 ? 'text-yellow-400' : 'text-gray-600'}`} />
            <div>
              <h3 className="font-medium text-white">Level Quiz — 10 Questions</h3>
              {quizScore != null && <p className="text-sm text-gray-400">Best score: {quizScore}%</p>}
            </div>
          </div>
          <Link to={`/technology/${tech}/${level}/quiz`}
            className="btn-primary text-sm">
            {quizScore != null ? 'Retake' : 'Take Quiz'}
          </Link>
        </div>
      </div>
    </div>
  )
}
