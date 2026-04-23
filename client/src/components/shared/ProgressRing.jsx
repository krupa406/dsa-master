export default function ProgressRing({ percent = 0, size = 60, stroke = 5, color = '#3b82f6' }) {
  const r = (size - stroke * 2) / 2
  const circ = 2 * Math.PI * r
  const offset = circ - (percent / 100) * circ
  return (
    <svg width={size} height={size} className="-rotate-90">
      <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke="#1f2937" strokeWidth={stroke} />
      <circle
        cx={size / 2} cy={size / 2} r={r} fill="none"
        stroke={color} strokeWidth={stroke}
        strokeDasharray={circ} strokeDashoffset={offset}
        strokeLinecap="round"
        style={{ transition: 'stroke-dashoffset 0.5s ease' }}
      />
      <text x="50%" y="50%" dominantBaseline="middle" textAnchor="middle"
        className="rotate-90 origin-center fill-white text-xs font-bold"
        style={{ transform: 'rotate(90deg)', transformOrigin: 'center', fontSize: size < 50 ? '10px' : '13px' }}>
        {percent}%
      </text>
    </svg>
  )
}
