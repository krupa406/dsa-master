import { useState } from 'react'
import { api } from '../../services/api'
import QuizIntro from './QuizIntro'
import QuestionCard from './QuestionCard'
import QuizResults from './QuizResults'
import QuizProgress from './QuizProgress'

export default function QuizContainer({ quiz, onSubmit, tech, level }) {
  const [phase, setPhase] = useState('intro') // intro | active | results
  const [current, setCurrent] = useState(0)
  const [answers, setAnswers] = useState({})
  // questionResults: { [questionId]: { correct, correctOption, explanation, citations, points } }
  const [questionResults, setQuestionResults] = useState({})
  const [revealed, setRevealed] = useState(false)
  const [checking, setChecking] = useState(false)
  const [finalResults, setFinalResults] = useState(null)

  function startQuiz() {
    setPhase('active')
    setCurrent(0)
    setAnswers({})
    setQuestionResults({})
    setRevealed(false)
  }

  async function handleAnswer(questionId, optionId) {
    if (answers[questionId]) return // already answered
    setAnswers(prev => ({ ...prev, [questionId]: optionId }))
    setChecking(true)
    try {
      const result = await api.answerQuestion(tech, level, questionId, optionId)
      setQuestionResults(prev => ({ ...prev, [questionId]: result }))
    } catch {
      // If per-question API fails, still allow progress (will grade at end)
    } finally {
      setChecking(false)
      setRevealed(true)
    }
  }

  async function handleNext() {
    setRevealed(false)
    if (current < quiz.questions.length - 1) {
      setCurrent(c => c + 1)
    } else {
      // Submit all answers for final score + save progress
      try {
        const res = await onSubmit(answers)
        setFinalResults(res)
      } catch {
        // Build final results from per-question results if submit fails
        const results = quiz.questions.map(q => ({
          ...questionResults[q.id],
          questionId: q.id,
          selectedOption: answers[q.id],
        }))
        const earned = results.reduce((s, r) => s + (r.correct ? (r.points || 10) : 0), 0)
        const total = quiz.questions.reduce((s, q) => s + (q.points || 10), 0)
        setFinalResults({ score: Math.round((earned / total) * 100), results, passed: earned / total >= 0.7 })
      }
      setPhase('results')
    }
  }

  if (phase === 'intro') return <QuizIntro quiz={quiz} tech={tech} level={level} onStart={startQuiz} />
  if (phase === 'results') return <QuizResults results={finalResults} quiz={quiz} answers={answers} onRetry={startQuiz} tech={tech} level={level} />

  const q = quiz.questions[current]
  return (
    <div>
      <QuizProgress current={current + 1} total={quiz.questions.length} answers={answers} questions={quiz.questions} />
      <QuestionCard
        question={q}
        selectedAnswer={answers[q.id]}
        revealed={revealed}
        checking={checking}
        result={questionResults[q.id]}
        onAnswer={(optId) => handleAnswer(q.id, optId)}
        onNext={handleNext}
        isLast={current === quiz.questions.length - 1}
        isSubmitting={false}
      />
    </div>
  )
}
