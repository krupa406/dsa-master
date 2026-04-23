import { useState } from 'react'
import CodeEditor from './CodeEditor'
import { Play, Lightbulb, CheckCircle2, XCircle, RefreshCw } from 'lucide-react'

export default function LabPanel({ lab, onRun }) {
  const [code, setCode] = useState(lab.starterCode || '')
  const [result, setResult] = useState(null)
  const [running, setRunning] = useState(false)
  const [showHints, setShowHints] = useState(false)

  async function handleRun() {
    setRunning(true)
    try {
      const res = await onRun(code)
      setResult(res)
    } finally {
      setRunning(false)
    }
  }

  return (
    <div className="space-y-4">
      <div className="card p-4">
        <div className="flex items-start justify-between mb-3">
          <div>
            <h3 className="font-semibold text-white">{lab.title}</h3>
            <p className="text-gray-400 text-sm mt-0.5">{lab.description}</p>
          </div>
          <button onClick={() => setShowHints(!showHints)}
            className="flex items-center gap-1.5 text-xs text-yellow-400 hover:text-yellow-300 bg-yellow-950 px-3 py-1.5 rounded-lg border border-yellow-900">
            <Lightbulb className="w-3.5 h-3.5" />
            {showHints ? 'Hide' : 'Hints'}
          </button>
        </div>

        {showHints && (
          <div className="mb-4 space-y-1.5">
            {lab.hints?.map((h, i) => (
              <div key={i} className="flex items-start gap-2 text-sm text-yellow-300 bg-yellow-950/40 px-3 py-2 rounded border border-yellow-900/50">
                <span className="text-yellow-500 font-mono text-xs mt-0.5">{i + 1}.</span>{h}
              </div>
            ))}
          </div>
        )}
      </div>

      <div className="monaco-host border border-gray-800 rounded-xl overflow-hidden">
        <CodeEditor value={code} onChange={setCode} language={lab.monacoLanguage || 'yaml'} height="380px" />
      </div>

      <div className="flex items-center gap-3">
        <button onClick={handleRun} disabled={running}
          className="btn-primary flex items-center gap-2">
          {running ? <RefreshCw className="w-4 h-4 animate-spin" /> : <Play className="w-4 h-4" />}
          {running ? 'Running…' : 'Run Lab'}
        </button>
        <button onClick={() => setCode(lab.starterCode || '')} className="btn-secondary text-sm">Reset</button>
        {result && (
          <span className={`flex items-center gap-1.5 text-sm font-medium ${result.passed ? 'text-green-400' : 'text-red-400'}`}>
            {result.passed ? <CheckCircle2 className="w-4 h-4" /> : <XCircle className="w-4 h-4" />}
            Score: {result.score}%
          </span>
        )}
      </div>

      {result && (
        <div className="card p-4 space-y-3">
          <div className="flex items-center gap-2 mb-2">
            {result.passed
              ? <><CheckCircle2 className="w-5 h-5 text-green-500" /><span className="text-green-400 font-medium">Passed!</span></>
              : <><XCircle className="w-5 h-5 text-red-500" /><span className="text-red-400 font-medium">Not quite — review the feedback below</span></>
            }
          </div>
          <pre className="bg-gray-950 text-green-300 text-xs p-4 rounded-lg overflow-x-auto font-mono leading-relaxed whitespace-pre-wrap">{result.output}</pre>
          {result.feedback?.length > 0 && (
            <div className="space-y-2">
              <h4 className="text-sm font-medium text-gray-300">What to fix:</h4>
              {result.feedback.map((f, i) => (
                <div key={i} className="text-sm text-red-300 bg-red-950/40 border border-red-900/50 px-3 py-2 rounded">
                  {f.message}
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  )
}
