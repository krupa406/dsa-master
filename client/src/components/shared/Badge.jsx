const LEVEL_STYLES = {
  beginner: 'bg-green-950 text-green-400 border border-green-800',
  intermediate: 'bg-yellow-950 text-yellow-400 border border-yellow-800',
  expert: 'bg-red-950 text-red-400 border border-red-800',
}

export default function Badge({ level, className = '' }) {
  const style = LEVEL_STYLES[level] || 'bg-gray-800 text-gray-300'
  return (
    <span className={`badge ${style} ${className}`}>
      {level ? level.charAt(0).toUpperCase() + level.slice(1) : ''}
    </span>
  )
}
