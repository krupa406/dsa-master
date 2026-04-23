import { createContext, useContext, useState, useCallback } from 'react'
import { getProgress } from '../utils/progressStorage'

const ProgressContext = createContext(null)

export function ProgressProvider({ children }) {
  const [progress, setProgress] = useState(() => getProgress())

  const refresh = useCallback(() => {
    setProgress(getProgress())
  }, [])

  return (
    <ProgressContext.Provider value={{ progress, refresh }}>
      {children}
    </ProgressContext.Provider>
  )
}

export function useProgressContext() {
  const ctx = useContext(ProgressContext)
  if (!ctx) throw new Error('useProgressContext must be used within ProgressProvider')
  return ctx
}
