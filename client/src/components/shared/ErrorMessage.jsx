import { AlertCircle } from 'lucide-react'

export default function ErrorMessage({ message }) {
  return (
    <div className="flex items-center gap-3 p-4 bg-red-950 border border-red-800 rounded-lg text-red-300">
      <AlertCircle className="w-5 h-5 shrink-0" />
      <p className="text-sm">{message}</p>
    </div>
  )
}
