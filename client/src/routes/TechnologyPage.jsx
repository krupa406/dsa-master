import { Link, useParams } from 'react-router-dom'
import { useApi } from '../hooks/useApi'
import { api } from '../services/api'
import { useTechProgress, useIsLevelUnlocked } from '../hooks/useProgress'
import LoadingSpinner from '../components/shared/LoadingSpinner'
import ErrorMessage from '../components/shared/ErrorMessage'
import Badge from '../components/shared/Badge'
import ProgressRing from '../components/shared/ProgressRing'
import { Lock, ChevronRight } from 'lucide-react'

const LEVEL_COLORS = { beginner: '#22c55e', intermediate: '#eab308', expert: '#ef4444' }

export default function TechnologyPage() {
  const { tech } = useParams()
  const { data: techData, loading: tLoading, error: tError } = useApi(() => api.getTechnology(tech), [tech])
  const { data: levels, loading: lLoading, error: lError } = useApi(() => api.getLevels(tech), [tech])
  const techProgress = useTechProgress(tech)

  if (tLoading || lLoading) return <LoadingSpinner />
  if (tError || lError) return <div className="p-8"><ErrorMessage message={tError || lError} /></div>

  return (
    <div className="max-w-3xl mx-auto px-4 py-10">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-white">{techData?.displayName}</h1>
        <p className="text-gray-400 mt-2">{techData?.description}</p>
        <a href={techData?.officialDocsBaseUrl} target="_blank" rel="noopener noreferrer"
          className="text-blue-400 hover:text-blue-300 text-sm mt-1 inline-block">
          Official Docs →
        </a>
      </div>

      <div className="space-y-4">
        {levels?.map(level => {
          const lp = techProgress?.levels?.[level.id]
          const pct = lp?.progressPercent || (lp?.completedAt ? 100 : 0)
          const unlocked = level.id === 'beginner' || !!(lp?.unlocked || (techProgress?.levels?.[level.id === 'intermediate' ? 'beginner' : 'intermediate']?.completedAt))
          const color = LEVEL_COLORS[level.id]
          return (
            <div key={level.id} className={`card p-6 transition-all ${unlocked ? 'hover:border-gray-600' : 'opacity-60'}`}>
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-4">
                  {unlocked
                    ? <ProgressRing percent={pct} size={56} stroke={4} color={color} />
                    : <div className="w-14 h-14 rounded-full bg-gray-800 flex items-center justify-center"><Lock className="w-5 h-5 text-gray-600" /></div>
                  }
                  <div>
                    <div className="flex items-center gap-2 mb-1">
                      <h2 className="text-lg font-semibold text-white">{level.displayName}</h2>
                      <Badge level={level.id} />
                    </div>
                    <p className="text-gray-400 text-sm">{level.description}</p>
                    <p className="text-gray-600 text-xs mt-1">{level.estimatedHours}h estimated · {level.moduleOrder?.length} modules</p>
                  </div>
                </div>
                {unlocked && (
                  <Link to={`/technology/${tech}/${level.id}`}
                    className="flex items-center gap-1 px-4 py-2 bg-gray-800 hover:bg-gray-700 rounded-lg text-sm text-gray-200 transition-colors shrink-0">
                    {lp?.completedAt ? 'Review' : pct > 0 ? 'Continue' : 'Start'}
                    <ChevronRight className="w-4 h-4" />
                  </Link>
                )}
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
