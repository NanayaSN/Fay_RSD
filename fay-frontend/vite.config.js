import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  build: {
    rollupOptions: {
      input: {
        control: 'src/pages/control/index.html',
        avatar: 'src/pages/avatar/index.html'
      }
    }
  }
})
