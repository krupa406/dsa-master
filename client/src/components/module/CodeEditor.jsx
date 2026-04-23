import Editor from '@monaco-editor/react'

const MONACO_THEME = {
  base: 'vs-dark',
  inherit: true,
  rules: [
    { token: 'comment', foreground: '6b7280', fontStyle: 'italic' },
    { token: 'string', foreground: '86efac' },
    { token: 'keyword', foreground: '818cf8' },
    { token: 'number', foreground: 'fbbf24' },
  ],
  colors: {
    'editor.background': '#030712',
    'editor.foreground': '#e5e7eb',
    'editor.lineHighlightBackground': '#111827',
    'editorLineNumber.foreground': '#374151',
    'editorLineNumber.activeForeground': '#6b7280',
  }
}

export default function CodeEditor({ value, onChange, language = 'yaml', height = '360px' }) {
  function handleMount(editor, monaco) {
    monaco.editor.defineTheme('devlearn-dark', MONACO_THEME)
    monaco.editor.setTheme('devlearn-dark')
  }

  return (
    <Editor
      height={height}
      language={language}
      value={value}
      onChange={v => onChange(v || '')}
      onMount={handleMount}
      options={{
        minimap: { enabled: false },
        fontSize: 13,
        lineHeight: 22,
        padding: { top: 16, bottom: 16 },
        scrollBeyondLastLine: false,
        wordWrap: 'on',
        tabSize: 2,
        renderLineHighlight: 'line',
        smoothScrolling: true,
        cursorSmoothCaretAnimation: 'on',
      }}
    />
  )
}
