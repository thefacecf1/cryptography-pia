export const fetchUsers = async () => {
  const res = await fetch('http://localhost:5000/users')
  return await res.json()
}
export const fetchRegister = async (username: string, password: string) => {
  const method = 'POST'
  const body = JSON.stringify({ username, password })
  const headers = { 'Content-Type': 'application/json' }
  const res = await fetch('http://localhost:5000/register', { method, body, headers })
  return await res.text()
}
export const fetchLogin = async (username: string, password: string) => {
  const method = 'POST'
  const body = JSON.stringify({ username, password })
  const headers = { 'Content-Type': 'application/json' }
  const res = await fetch('http://localhost:5000/login', { method, body, headers })
  return await res.json()
}
