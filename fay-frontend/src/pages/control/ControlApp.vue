<template>
  <div class="control-page">
    <h1>控制界面（语音对话）</h1>
    <div class="buttons">
      <button @click="startRecording">开始录音</button>
      <button @click="stopRecording">停止录音</button>
    </div>
    <div class="chat-box">
      <div v-for="(msg, index) in messages" :key="index" class="message">
        {{ msg }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const socket = ref(null)
const messages = ref([])

onMounted(() => {
  socket.value = new WebSocket('ws://localhost:8000/ws') // Fay后端WebSocket
  socket.value.onmessage = (event) => {
    const data = JSON.parse(event.data)
    if (data.content) {
      messages.value.push(data.content)
    }
  }
})

function startRecording() {
  console.log('开始录音')
  // 这里后面可以集成浏览器录音接口或直接调用ASR
}

function stopRecording() {
  console.log('停止录音')
  // 这里模拟发一段固定文本给后端（可以换成真正ASR返回）
  if (socket.value && socket.value.readyState === 1) {
    socket.value.send(JSON.stringify({
      role: 'user',
      content: '你好'
    }))
  }
}
</script>

<style scoped>
.control-page {
  padding: 20px;
}
.buttons {
  margin-bottom: 20px;
}
.chat-box {
  background: #f2f2f2;
  padding: 10px;
  height: 300px;
  overflow-y: auto;
}
.message {
  margin-bottom: 10px;
}
</style>
