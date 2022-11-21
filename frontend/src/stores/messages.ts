import { ref } from 'vue'
import { defineStore } from 'pinia'
import { io } from 'socket.io-client'
import { fetchMessages, postMessage } from '@/services/users'
import type { Message, Messages } from '@/types'

const socket = io('http://localhost:5000')

export const useMessagesStore = defineStore('messages', () => {
  socket.on('newMessages', (data: Messages) => {
    messages.value = data.messages
  })
  const messages = ref<Message[]>([])

  const getMessages = async () => {
    const res = await fetchMessages()
    messages.value = res.messages
  }
  const sendMessage = async (username: string, message: string) => {
    await postMessage(username, message)
  }
  return { messages, getMessages, sendMessage }
})
