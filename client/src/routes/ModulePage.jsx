import { useState, useEffect, useRef } from 'react'
import { useParams, Link } from 'react-router-dom'
import { useApi } from '../hooks/useApi'
import { api } from '../services/api'
import { markModuleStarted, saveLabScore } from '../utils/progressStorage'
import { useModuleProgress } from '../hooks/useProgress'
import { useProgressContext } from '../context/ProgressContext'
import LoadingSpinner from '../components/shared/LoadingSpinner'
import ErrorMessage from '../components/shared/ErrorMessage'
import LabPanel from '../components/module/LabPanel'
import TheoryPanel from '../components/module/TheoryPanel'
import ModuleOutline from '../components/module/ModuleOutline'
import { BookOpen, FlaskConical, ChevronLeft, ChevronRight, Award } from 'lucide-react'

const TECH_ACCENT = { ansible: 'border-red-500', terraform: 'border-purple-500', kubernetes: 'border-blue-500', git: 'border-orange-500' }
const TECH_TAB_ACTIVE = { ansible: 'border-red-400 text-red-400', terraform: 'border-purple-400 text-purple-400', kubernetes: 'border-blue-400 text-blue-400', git: 'border-orange-400 text-orange-400' }

export default function ModulePage() {
  const { tech, level, moduleId } = useParams()
  const { refresh } = useProgressContext()
  const [tab, setTab] = useState('theory')
  const theoryRef = useRef(null)

  const { data: mod, loading: mLoading, error: mError } = useApi(() => api.getModule(tech, level, moduleId), [tech, level, moduleId])
  const { data: lab, loading: lLoading } = useApi(() => api.getLab(tech, level, moduleId), [tech, level, moduleId])
  const { data: modules } = useApi(() => api.getModules(tech, level), [tech, level])
  const modProg = useModuleProgress(tech, level, moduleId)

  useEffect(() => {
    if (mod) { markModuleStarted(tech, level, moduleId); refresh() }
  }, [mod]) // eslint-disable-line

  const currentIdx = modules?.findIndex(m => m.id === moduleId) ?? -1
  const prevModule = currentIdx > 0 ? modules[currentIdx - 1] : null
  const nextModule = modules && currentIdx < modules.length - 1 ? modules[currentIdx + 1] : null

  async function handleLabRun(code) {
    const result = await api.runLab(tech, level, moduleId, code)
    saveLabScore(tech, level, moduleId, result.score, code)
    refresh()
    return result
  }

  if (mLoading) return <LoadingSpinner />
  if (mError) return <div className="p-8"><ErrorMessage message={mError} /></div>

  const accentBorder = TECH_ACCENT[tech] || 'border-gray-700'
  const tabActive = TECH_TAB_ACTIVE[tech] || 'border-blue-400 text-blue-400'

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      {/* Header */}
      <div className={`card p-5 mb-6 border-l-4 ${accentBorder}`}>
        <div className="flex items-start justify-between">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <span className="text-xs font-medium uppercase tracking-wider text-gray-500 capitalize">{tech} / {level}</span>
            </div>
            <h1 className="text-2xl font-bold text-white">{mod?.title}</h1>
            {mod?.learningObjectives?.length > 0 && (
              <details className="mt-3 group">
                <summary className="text-sm text-gray-400 cursor-pointer hover:text-gray-200 transition-colors list-none flex items-center gap-1.5">
                  <span className="text-xs border border-gray-700 rounded px-1.5 py-0.5 group-open:bg-gray-800">▸ Learning objectives ({mod.learningObjectives.length})</span>
                </summary>
                <ul className="mt-2 space-y-1 pl-2">
                  {mod.learningObjectives.map((obj, i) => (
                    <li key={i} className="text-sm text-gray-400 flex items-start gap-2">
                      <span className="text-green-500 mt-0.5 shrink-0">✓</span>{obj}
                    </li>
                  ))}
                </ul>
              </details>
            )}
          </div>
          <div className="text-right shrink-0 ml-4">
            <span className="text-xs text-gray-600">{mod?.estimatedMinutes} min</span>
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex gap-0 mb-6 border-b border-gray-800">
        {[
          ['theory', <BookOpen className="w-4 h-4" />, 'Theory'],
          ['lab', <FlaskConical className="w-4 h-4" />, 'Lab']
        ].map(([id, icon, label]) => (
          <button
            key={id}
            onClick={() => setTab(id)}
            className={`flex items-center gap-2 px-5 py-2.5 text-sm font-medium border-b-2 transition-all -mb-px ${
              tab === id ? tabActive : 'border-transparent text-gray-500 hover:text-gray-300 hover:border-gray-600'
            }`}
          >
            {icon}{label}
          </button>
        ))}
      </div>

      {/* Content area with optional outline */}
      <div className="flex gap-6">
        <div className="flex-1 min-w-0">
          {tab === 'theory' && (
            <div ref={theoryRef} className="card p-8">
              <TheoryPanel content={mod?.theory?.content} sections={mod?.theory?.sections} />
            </div>
          )}
          {tab === 'lab' && !lLoading && lab && (
            <LabPanel
              lab={lab}
              onRun={handleLabRun}
              savedCode={modProg?.labLastCode ?? null}
              savedScore={modProg?.labScore ?? null}
            />
          )}
          {tab === 'lab' && lLoading && <LoadingSpinner message="Loading lab..." />}
        </div>

        {/* Sticky outline — theory only */}
        {tab === 'theory' && (
          <aside className="hidden xl:block w-56 shrink-0">
            <div className="sticky top-20">
              <ModuleOutline contentRef={theoryRef} />
            </div>
          </aside>
        )}
      </div>

      {/* Navigation */}
      <div className="flex items-center justify-between mt-8 pt-6 border-t border-gray-800">
        {prevModule
          ? <Link to={`/technology/${tech}/${level}/module/${prevModule.id}`} className="btn-secondary flex items-center gap-2 text-sm">
              <ChevronLeft className="w-4 h-4" />Previous
            </Link>
          : <div />
        }
        <Link to={`/technology/${tech}/${level}/quiz`} className="btn-primary flex items-center gap-2 text-sm">
          <Award className="w-4 h-4" />Level Quiz
        </Link>
        {nextModule
          ? <Link to={`/technology/${tech}/${level}/module/${nextModule.id}`} className="btn-secondary flex items-center gap-2 text-sm">
              Next<ChevronRight className="w-4 h-4" />
            </Link>
          : <div />
        }
      </div>
    </div>
  )
}
