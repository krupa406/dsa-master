import { useState, useEffect } from 'react'
import { List } from 'lucide-react'

export default function ModuleOutline({ contentRef }) {
  const [headings, setHeadings] = useState([])
  const [active, setActive] = useState('')

  useEffect(() => {
    if (!contentRef?.current) return
    const els = Array.from(contentRef.current.querySelectorAll('h2, h3'))
    setHeadings(els.map(el => ({
      id: el.id || el.textContent.toLowerCase().replace(/[^a-z0-9]+/g, '-'),
      text: el.textContent,
      level: el.tagName === 'H2' ? 2 : 3
    })))
  }, [contentRef])

  useEffect(() => {
    const observer = new IntersectionObserver(
      entries => {
        entries.forEach(e => { if (e.isIntersecting) setActive(e.target.id) })
      },
      { rootMargin: '-20% 0px -70% 0px' }
    )
    document.querySelectorAll('h2[id], h3[id]').forEach(el => observer.observe(el))
    return () => observer.disconnect()
  }, [headings])

  if (headings.length < 2) return null

  return (
    <div className="module-outline">
      <div className="flex items-center gap-2 text-xs text-gray-500 mb-3 font-medium uppercase tracking-wider">
        <List className="w-3.5 h-3.5" />On this page
      </div>
      <nav className="space-y-1">
        {headings.map(h => (
          <a
            key={h.id}
            href={`#${h.id}`}
            onClick={e => {
              e.preventDefault()
              document.getElementById(h.id)?.scrollIntoView({ behavior: 'smooth', block: 'start' })
            }}
            className={`outline-link ${h.level === 3 ? 'pl-3' : ''} ${active === h.id ? 'outline-link-active' : ''}`}
          >
            {h.text}
          </a>
        ))}
      </nav>
    </div>
  )
}
