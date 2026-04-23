import { useState } from 'react'
import { CheckCircle2, XCircle, ExternalLink, ChevronRight } from 'lucide-react'

export default function QuestionCard({ question, selectedAnswer, revealed, checking, result, onAnswer, onNext, isLast, isSubmitting }) {
  const [hovered, setHovered] = useState(null)
  const hasAnswered = !!selectedAnswer

  function optionClass(optId) {
    const base = 'option-btn group'
    if (!hasAnswered) {
      return `${base} ${hovered === optId ? 'option-btn-hover' : 'option-btn-default'}`
    }
    if (result) {
      if (optId === result.correctOption) return `${base} option-btn-correct`
      if (optId === selectedAnswer && optId !== result.correctOption) return `${base} option-btn-wrong`
    } else {
      if (optId === selectedAnswer) return `${base} option-btn-selected`
    }
    return `${base} option-btn-dimmed`
  }

  return (
    <div className="card p-6 animate-fadeIn">
      <div className="flex items-center justify-between mb-1">
        <span className="text-xs font-mono text-gray-600">{question.points} pts</span>
        <span className="text-xs text-gray-700">{question.type === 'single-choice' ? 'Single choice' : ''}</span>
      </div>

      <h3 className="text-white font-medium text-base mb-6 leading-relaxed">{question.text}</h3>

      <div className="space-y-2 mb-6">
        {question.options.map(opt => (
          <button
            key={opt.id}
            onClick={() => !hasAnswered && onAnswer(opt.id)}
            onMouseEnter={() => !hasAnswered && setHovered(opt.id)}
            onMouseLeave={() => setHovered(null)}
            className={optionClass(opt.id)}
            disabled={hasAnswered}
          >
            <span className="option-letter">{opt.id.toUpperCase()}</span>
            <span className="flex-1 text-left">{opt.text}</span>
            {result && opt.id === result.correctOption && (
              <CheckCircle2 className="w-4 h-4 text-green-400 shrink-0 ml-2" />
            )}
            {result && opt.id === selectedAnswer && opt.id !== result.correctOption && (
              <XCircle className="w-4 h-4 text-red-400 shrink-0 ml-2" />
            )}
          </button>
        ))}
      </div>

      {hasAnswered && checking && (
        <div className="flex items-center gap-2 text-sm text-gray-500 py-3 animate-pulse">
          <span className="w-4 h-4 border-2 border-gray-500 border-t-transparent rounded-full animate-spin" />
          Checking answer…
        </div>
      )}

      {revealed && result && (
        <div className={`explanation-box animate-slideUp ${result.correct ? 'explanation-correct' : 'explanation-wrong'}`}>
          <div className="flex items-start gap-3 mb-3">
            {result.correct
              ? <CheckCircle2 className="w-5 h-5 text-green-500 shrink-0 mt-0.5" />
              : <XCircle className="w-5 h-5 text-red-500 shrink-0 mt-0.5" />
            }
            <div>
              <p className={`text-sm font-semibold mb-1 ${result.correct ? 'text-green-300' : 'text-red-300'}`}>
                {result.correct ? 'Correct!' : `Correct answer: ${question.options.find(o => o.id === result.correctOption)?.text}`}
              </p>
              <p className="text-sm text-gray-300 leading-relaxed">{result.explanation}</p>
            </div>
          </div>
          {result.citations?.length > 0 && (
            <div className="flex flex-wrap gap-2 mt-3 pt-3 border-t border-gray-700/50">
              <span className="text-xs text-gray-500">Official docs:</span>
              {result.citations.map((c, i) => (
                <a key={i} href={c.url} target="_blank" rel="noopener noreferrer"
                  className="citation-link">
                  <ExternalLink className="w-3 h-3" />{c.label}
                </a>
              ))}
            </div>
          )}
        </div>
      )}

      {revealed && result && !checking && (
        <button onClick={onNext} disabled={isSubmitting}
          className="btn-primary flex items-center gap-2 w-full justify-center mt-4 animate-slideUp">
          {isSubmitting ? (
            <span className="flex items-center gap-2"><span className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />Submitting…</span>
          ) : (
            <>{isLast ? 'Finish Quiz' : 'Next Question'}<ChevronRight className="w-4 h-4" /></>
          )}
        </button>
      )}
    </div>
  )
}
