import { defineConfig } from 'vite'

// https://vite.dev/config/
const isVercel = !!process.env.VERCEL;
const outDir = isVercel ? 'dist' : '/Users/luxfajah/Documents/Duas mâos/Larissa';

export default defineConfig({
  base: './', // Enable relative paths so index.html is double-clickable locally
  build: {
    outDir,
    emptyOutDir: false, // CRITICAL: Do not delete existing files (e.g. the PDF) in the target folder
  }
})
