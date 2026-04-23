import { useProgressContext } from '../context/ProgressContext'
import { getLevelProgress, getModuleProgress, getTechProgress, isLevelUnlocked } from '../utils/progressStorage'

export function useProgress() {
  const { progress, refresh } = useProgressContext()
  return { progress, refresh }
}

export function useTechProgress(tech) {
  const { progress } = useProgressContext()
  return getTechProgress(tech)
}

export function useLevelProgress(tech, level) {
  const { progress } = useProgressContext()
  return getLevelProgress(tech, level)
}

export function useModuleProgress(tech, level, moduleId) {
  const { progress } = useProgressContext()
  return getModuleProgress(tech, level, moduleId)
}

export function useIsLevelUnlocked(tech, level) {
  const { progress } = useProgressContext()
  return isLevelUnlocked(tech, level)
}
