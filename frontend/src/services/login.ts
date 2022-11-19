const method = 'POST'
const baseUrl = 'http://localhost:5000'
const headers = { 'Content-Type': 'application/json' }

export const fetchUsers = async () => {
  const res = await fetch('baseUrl +http://localhost:5000/users')
  return await res.json()
}
export const fetchRegister = async (username: string, password: string) => {
  const body = JSON.stringify({ username, password })
  return await fetch(baseUrl + '/register', { method, body, headers })
}
export const fetchLogin = async (username: string, password: string) => {
  const body = JSON.stringify({ username, password })
  return await fetch(baseUrl + '/login', { method, body, headers })
}
