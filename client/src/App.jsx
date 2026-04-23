import { Routes, Route } from 'react-router-dom'
import { ProgressProvider } from './context/ProgressContext'
import AppShell from './components/layout/AppShell'
import HomePage from './routes/HomePage'
import TechnologyPage from './routes/TechnologyPage'
import LevelPage from './routes/LevelPage'
import ModulePage from './routes/ModulePage'
import QuizPage from './routes/QuizPage'

export default function App() {
  return (
    <ProgressProvider>
      <Routes>
        <Route element={<AppShell />}>
          <Route path="/" element={<HomePage />} />
          <Route path="/technology/:tech" element={<TechnologyPage />} />
          <Route path="/technology/:tech/:level" element={<LevelPage />} />
          <Route path="/technology/:tech/:level/module/:moduleId" element={<ModulePage />} />
          <Route path="/technology/:tech/:level/quiz" element={<QuizPage />} />
        </Route>
      </Routes>
    </ProgressProvider>
  )
}
