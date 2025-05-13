<template>
  <div class="avatar-page">
    <h1>虚拟人页面</h1>
    <div id="avatarCanvas">这里渲染虚拟人模型</div>
    <div class="action-log">
      当前动作: {{ currentAction }}
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const socket = ref(null)
const currentAction = ref('无')

onMounted(() => {
  socket.value = new WebSocket('ws://localhost:8000/ws')
  socket.value.onmessage = (event) => {
    const data = JSON.parse(event.data)
    if (data.action) {
      playAvatarAction(data.action)
    }
  }
})

function playAvatarAction(actionName) {
  console.log('执行动作:', actionName)
  currentAction.value = actionName
  // TODO: 调用Three.js或Unity的接口播放动作
}
</script>

<style scoped>
.avatar-page {
  padding: 20px;
}
#avatarCanvas {
  width: 600px;
  height: 400px;
  background: #ddd;
  margin-bottom: 20px;
}
.action-log {
  font-size: 18px;
}
</style>
