import { Award, Clock, BookOpen } from 'lucide-react'
import Badge from '../shared/Badge'

export default function QuizIntro({ quiz, tech, level, onStart }) {
  return (
    <div className="card p-8 text-center">
      <Award className="w-14 h-14 text-yellow-400 mx-auto mb-4" />
      <h2 className="text-2xl font-bold text-white mb-2 capitalize">{tech} {level} Quiz</h2>
      <Badge level={level} className="mb-4" />
      <div className="flex items-center justify-center gap-6 text-sm text-gray-400 my-6">
        <div className="flex items-center gap-2"><BookOpen className="w-4 h-4" />{quiz.questions.length} questions</div>
        <div className="flex items-center gap-2"><Clock className="w-4 h-4" />~10 minutes</div>
        <div className="flex items-center gap-2"><Award className="w-4 h-4" />70% to pass</div>
      </div>
      <p className="text-gray-400 text-sm mb-8 max-w-md mx-auto">
        Every answer shows an explanation citing the official documentation. You can review all answers at the end.
      </p>
      <button onClick={onStart} className="btn-primary text-base px-8 py-3">Start Quiz</button>
    </div>
  )
}
