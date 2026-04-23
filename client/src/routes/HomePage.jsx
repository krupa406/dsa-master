import { Link } from 'react-router-dom'
import { useApi } from '../hooks/useApi'
import { api } from '../services/api'
import { useProgressContext } from '../context/ProgressContext'
import LoadingSpinner from '../components/shared/LoadingSpinner'
import ErrorMessage from '../components/shared/ErrorMessage'
import ProgressRing from '../components/shared/ProgressRing'

const TECH_COLORS = { ansible: '#EE0000', terraform: '#7B42BC', kubernetes: '#326CE5' }
const TECH_ICONS = {
  ansible: (
    <svg viewBox="0 0 32 32" className="w-12 h-12" fill="currentColor">
      <path d="M16 0C7.163 0 0 7.163 0 16s7.163 16 16 16 16-7.163 16-16S24.837 0 16 0zm6.5 23.5L14 11l-1.5 4.5L18 19l-8 4.5 1-3L7 16l9-9 7.5 14.5-1 2z"/>
    </svg>
  ),
  terraform: (
    <svg viewBox="0 0 32 32" className="w-12 h-12" fill="currentColor">
      <path d="M12.042 6.858L20.5 11.5v9L12.042 25.5V16.5L3.5 11.5l8.542-4.642zM20.5 11.5l8.5-4.5v9l-8.5 4.5V11.5z"/>
    </svg>
  ),
  kubernetes: (
    <svg viewBox="0 0 32 32" className="w-12 h-12" fill="currentColor">
      <path d="M16 2L4 8v8c0 7.732 5.197 14.977 12 16 6.803-1.023 12-8.268 12-16V8L16 2zm0 4.5l8 4v6.5c0 5-3.245 9.5-8 11-4.755-1.5-8-6-8-11V10.5l8-4z"/>
    </svg>
  )
}

export default function HomePage() {
  const { data: techs, loading, error } = useApi(() => api.getTechnologies(), [])
  const { progress } = useProgressContext()

  if (loading) return <LoadingSpinner />
  if (error) return <div className="p-8"><ErrorMessage message={error} /></div>

  return (
    <div className="max-w-5xl mx-auto px-4 py-12">
      <div className="text-center mb-14">
        <h1 className="text-4xl font-bold text-white mb-3">Master DevOps Tools</h1>
        <p className="text-gray-400 text-lg max-w-xl mx-auto">
          Interactive labs and quizzes for Ansible 2.17, Terraform 1.9, and Kubernetes 1.31 — three levels, one goal.
        </p>
      </div>

      <div className="grid md:grid-cols-3 gap-6">
        {techs?.map(tech => {
          const techProg = progress?.technologies?.[tech.id]
          const pct = techProg?.overallProgressPercent || 0
          const color = TECH_COLORS[tech.id]
          return (
            <Link key={tech.id} to={`/technology/${tech.id}`}
              className="card p-6 hover:border-gray-600 transition-all hover:-translate-y-1 group block">
              <div className="flex items-start justify-between mb-4">
                <div style={{ color }} className="transition-transform group-hover:scale-110">
                  {TECH_ICONS[tech.id]}
                </div>
                <ProgressRing percent={pct} size={52} stroke={4} color={color} />
              </div>
              <h2 className="text-xl font-bold text-white mb-1">{tech.displayName}</h2>
              <p className="text-xs text-gray-500 mb-2">v{tech.version}</p>
              <p className="text-gray-400 text-sm leading-relaxed">{tech.tagline}</p>
              <div className="mt-4 flex gap-2">
                {['Beginner', 'Intermediate', 'Expert'].map(l => (
                  <span key={l} className="text-xs px-2 py-0.5 rounded bg-gray-800 text-gray-400">{l}</span>
                ))}
              </div>
            </Link>
          )
        })}
      </div>

      <div className="mt-12 card p-6">
        <h3 className="font-semibold text-gray-300 mb-4">Overall Progress</h3>
        <div className="grid grid-cols-3 gap-4">
          {['ansible', 'terraform', 'kubernetes'].map(tech => {
            const pct = progress?.technologies?.[tech]?.overallProgressPercent || 0
            return (
              <div key={tech}>
                <div className="flex justify-between text-sm mb-1">
                  <span className="capitalize text-gray-400">{tech}</span>
                  <span className="text-gray-500">{pct}%</span>
                </div>
                <div className="h-2 bg-gray-800 rounded-full overflow-hidden">
                  <div className="h-full rounded-full transition-all duration-500" style={{ width: `${pct}%`, backgroundColor: TECH_COLORS[tech] }} />
                </div>
              </div>
            )
          })}
        </div>
      </div>
    </div>
  )
}
