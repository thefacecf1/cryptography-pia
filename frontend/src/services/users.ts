import type { Messages } from '@/types'

const method = 'POST'
const baseUrl = 'http://localhost:5000'
const headers = { 'Content-Type': 'application/json' }

export const fetchUsers = async () => {
  const res = await fetch(baseUrl + '/users')
  return await res.json()
}
export const fetchMessages = async (): Promise<Messages> => {
  const res = await fetch(baseUrl + '/messages')
  return await res.json()
}
export const postMessage = async (username: string, message: string) => {
  const body = JSON.stringify({ username, message })
  return await fetch(baseUrl + '/messages', { method, body, headers })
}
export const fetchRegister = async (username: string, password: string) => {
  const body = JSON.stringify({ username, password })
  return await fetch(baseUrl + '/users', { method, body, headers })
}
export const fetchLogin = async (username: string, password: string) => {
  const body = JSON.stringify({ username, password })
  return await fetch(baseUrl + '/login', { method, body, headers })
}
