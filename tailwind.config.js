/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}",
    "./src/careerGPT/forms.py"
  ],
  theme: {
    extend: {
      colors: {
        'copper-canyon': {
          50: '#fff2eb',
          100: '#fedbc7',
          200: '#fdb48a',
          300: '#fc8c4d',
          400: '#fb7224',
          500: '#f5600b',
          600: '#d95206',
          700: '#b44709',
          800: '#923e0e',
          900: '#78350f',
          950: '#451b03',
        },
      }
    },
  },
  plugins: [],
}
