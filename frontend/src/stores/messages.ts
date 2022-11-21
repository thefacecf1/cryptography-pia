import { ref } from 'vue'
import { defineStore } from 'pinia'
import { fetchMessages, postMessage } from '@/services/users'
import type { Message } from '@/types'

export const useMessagesStore = defineStore('messages', () => {
  const messages = ref<Message[]>([])

  const getMessages = async () => {
    const res = await fetchMessages()
    messages.value = res.messages
  }
  const sendMessage = async (username: string, message: string) => {
    await postMessage(username, message)
    await getMessages()
  }
  return { messages, getMessages, sendMessage }
})
