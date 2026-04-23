import { Link, useLocation } from 'react-router-dom'
import { BookOpen, Home, RotateCcw } from 'lucide-react'
import { resetProgress } from '../../utils/progressStorage'
import { useProgressContext } from '../../context/ProgressContext'

export default function Navbar() {
  const location = useLocation()
  const { refresh } = useProgressContext()
  const parts = location.pathname.split('/').filter(Boolean)

  function handleReset() {
    if (window.confirm('Reset all progress? This cannot be undone.')) {
      resetProgress()
      refresh()
    }
  }

  return (
    <nav className="bg-gray-900 border-b border-gray-800 px-4 py-3 flex items-center justify-between sticky top-0 z-50">
      <Link to="/" className="flex items-center gap-2 font-bold text-lg text-white hover:text-blue-400 transition-colors">
        <BookOpen className="w-6 h-6 text-blue-400" />
        DevLearn
      </Link>

      <div className="flex items-center gap-2 text-sm text-gray-400">
        {parts.length > 0 && (
          <>
            <Link to="/" className="hover:text-white transition-colors flex items-center gap-1"><Home className="w-3.5 h-3.5" />Home</Link>
            {parts[0] === 'technology' && parts[1] && (
              <>
                <span>/</span>
                <Link to={`/technology/${parts[1]}`} className="hover:text-white capitalize transition-colors">{parts[1]}</Link>
              </>
            )}
            {parts[2] && !['module', 'quiz'].includes(parts[2]) && (
              <>
                <span>/</span>
                <Link to={`/technology/${parts[1]}/${parts[2]}`} className="hover:text-white capitalize transition-colors">{parts[2]}</Link>
              </>
            )}
            {parts[2] === 'quiz' && (
              <><span>/</span><span className="text-white capitalize">{parts[1]}</span><span>/</span><span className="text-white">Quiz</span></>
            )}
            {parts[2] === 'module' && parts[3] && (
              <><span>/</span><span className="text-white capitalize">Module</span></>
            )}
          </>
        )}
      </div>

      <button onClick={handleReset} title="Reset progress" className="text-gray-600 hover:text-red-400 transition-colors p-1">
        <RotateCcw className="w-4 h-4" />
      </button>
    </nav>
  )
}
