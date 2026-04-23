import { useEffect, useRef } from 'react'
import mermaid from 'mermaid'
import hljs from 'highlight.js'

mermaid.initialize({
  startOnLoad: false,
  theme: 'dark',
  darkMode: true,
  themeVariables: {
    background: '#030712',
    mainBkg: '#0f172a',
    nodeBorder: '#334155',
    clusterBkg: '#0f172a',
    titleColor: '#e2e8f0',
    edgeLabelBackground: '#1e293b',
    nodeTextColor: '#e2e8f0',
    lineColor: '#475569',
    primaryColor: '#1e3a5f',
    primaryTextColor: '#93c5fd',
    primaryBorderColor: '#3b82f6',
    secondaryColor: '#1e293b',
    tertiaryColor: '#1a2744',
  },
  flowchart: { curve: 'basis', useMaxWidth: true },
  sequence: { useMaxWidth: true, mirrorActors: false },
})

export default function TheoryPanel({ content, sections }) {
  const ref = useRef(null)

  useEffect(() => {
    if (!ref.current || !content) return

    // Run highlight.js on all code blocks
    ref.current.querySelectorAll('pre code').forEach(el => {
      hljs.highlightElement(el)
    })

    // Run mermaid on all diagram divs
    const diagrams = ref.current.querySelectorAll('.mermaid')
    if (diagrams.length > 0) {
      mermaid.run({ nodes: diagrams }).catch(() => {})
    }

    // Add copy button to code blocks
    ref.current.querySelectorAll('pre').forEach(pre => {
      if (pre.querySelector('.copy-btn')) return
      const btn = document.createElement('button')
      btn.className = 'copy-btn'
      btn.textContent = 'Copy'
      btn.onclick = () => {
        navigator.clipboard.writeText(pre.querySelector('code')?.textContent || pre.textContent)
        btn.textContent = 'Copied!'
        setTimeout(() => { btn.textContent = 'Copy' }, 2000)
      }
      pre.style.position = 'relative'
      pre.appendChild(btn)
    })

    // Make h2/h3 headings have anchor IDs
    ref.current.querySelectorAll('h2, h3').forEach(h => {
      if (!h.id) {
        h.id = h.textContent.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')
      }
    })
  }, [content])

  if (!content) return null

  return (
    <div ref={ref} className="theory-content" dangerouslySetInnerHTML={{ __html: content }} />
  )
}
