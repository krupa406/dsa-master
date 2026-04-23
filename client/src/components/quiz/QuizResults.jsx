import { Link } from 'react-router-dom'
import ProgressRing from '../shared/ProgressRing'
import { CheckCircle2, XCircle, ExternalLink, RefreshCw, Home } from 'lucide-react'

export default function QuizResults({ results, quiz, answers, onRetry, tech, level }) {
  const pct = results?.score ?? 0
  const passed = results?.passed
  const color = passed ? '#22c55e' : '#ef4444'

  return (
    <div className="space-y-6">
      <div className="card p-8 text-center">
        <ProgressRing percent={pct} size={100} stroke={8} color={color} />
        <h2 className={`text-2xl font-bold mt-4 ${passed ? 'text-green-400' : 'text-red-400'}`}>
          {passed ? '🎉 Passed!' : 'Not quite — keep going!'}
        </h2>
        <p className="text-gray-400 mt-1">
          {results?.rawScore} / {results?.totalPoints} points · {quiz.questions.length} questions
        </p>
        {!passed && <p className="text-gray-500 text-sm mt-2">Need 70% to pass. Review the explanations below and retry.</p>}
        <div className="flex items-center justify-center gap-3 mt-6">
          <button onClick={onRetry} className="btn-secondary flex items-center gap-2"><RefreshCw className="w-4 h-4" />Retry Quiz</button>
          <Link to={`/technology/${tech}/${level}`} className="btn-secondary flex items-center gap-2"><Home className="w-4 h-4" />Back to Level</Link>
        </div>
      </div>

      <div className="space-y-4">
        <h3 className="font-semibold text-gray-300">Answer Review</h3>
        {results?.results?.map((r, i) => {
          const q = quiz.questions.find(q => q.id === r.questionId)
          if (!q) return null
          return (
            <div key={r.questionId} className={`card p-5 border ${r.correct ? 'border-green-900' : 'border-red-900'}`}>
              <div className="flex items-start gap-3">
                {r.correct ? <CheckCircle2 className="w-5 h-5 text-green-500 shrink-0 mt-0.5" /> : <XCircle className="w-5 h-5 text-red-500 shrink-0 mt-0.5" />}
                <div className="flex-1">
                  <p className="text-sm font-medium text-gray-200 mb-2">{i + 1}. {q.text}</p>
                  {!r.correct && (
                    <p className="text-xs text-gray-500 mb-1">
                      Your answer: <span className="text-red-400">{q.options.find(o => o.id === r.selectedOption)?.text || 'Not answered'}</span>
                      {' · '}Correct: <span className="text-green-400">{q.options.find(o => o.id === r.correctOption)?.text}</span>
                    </p>
                  )}
                  <p className="text-sm text-gray-400 leading-relaxed">{r.explanation}</p>
                  {r.citations?.map((c, j) => (
                    <a key={j} href={c.url} target="_blank" rel="noopener noreferrer"
                      className="inline-flex items-center gap-1 text-xs text-blue-400 hover:text-blue-300 mt-2 mr-2">
                      <ExternalLink className="w-3 h-3" />{c.label}
                    </a>
                  ))}
                </div>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
