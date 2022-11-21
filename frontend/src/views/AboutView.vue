<script setup lang="ts">
import { io } from 'socket.io-client'

const socket = io('http://localhost:5000')

socket.on('connect', () => {
  console.log(socket.id) // true
  console.log(socket.connected) // true
})

socket.on('my event', (data) => {
  console.log(data)
})
socket.on('disconnect', () => {
  console.log(socket.connected) // false
})
</script>
<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>
