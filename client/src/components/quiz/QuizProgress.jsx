export default function QuizProgress({ current, total, answers, questions }) {
  const pct = Math.round(((current - 1) / total) * 100)

  return (
    <div className="mb-6">
      <div className="flex justify-between text-sm mb-2">
        <span className="text-gray-400 font-medium">Question <span className="text-white">{current}</span> of {total}</span>
        <span className="text-gray-500">{Object.keys(answers).length} answered</span>
      </div>
      {/* Animated progress bar */}
      <div className="h-1.5 bg-gray-800 rounded-full overflow-hidden mb-3">
        <div
          className="h-full bg-gradient-to-r from-blue-600 to-blue-400 rounded-full transition-all duration-500 ease-out"
          style={{ width: `${pct}%` }}
        />
      </div>
      {/* Dot indicators */}
      <div className="flex gap-1.5 flex-wrap">
        {questions.map((q, i) => {
          const answered = !!answers[q.id]
          const isCurrent = i === current - 1
          return (
            <div
              key={q.id}
              className={`h-1.5 rounded-full transition-all duration-300 ${
                isCurrent ? 'w-6 bg-blue-400' :
                answered ? 'w-3 bg-blue-600' :
                'w-3 bg-gray-700'
              }`}
            />
          )
        })}
      </div>
    </div>
  )
}
