/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        ansible: { DEFAULT: '#EE0000', light: '#FF4444', dark: '#CC0000' },
        terraform: { DEFAULT: '#7B42BC', light: '#9B62DC', dark: '#5B22AC' },
        kubernetes: { DEFAULT: '#326CE5', light: '#5288FF', dark: '#2255CC' },
      },
      fontFamily: {
        mono: ['JetBrains Mono', 'Fira Code', 'Consolas', 'monospace'],
      }
    },
  },
  plugins: [],
}
