<script setup lang="ts">
import { ref } from 'vue'
import LoginForm from '@/components/LoginForm.vue'
import { fetchLogin, fetchRegister } from '@/services/login'

const form = ref<boolean | null>(null)
const username = ref<string | null>(null)
const password = ref<string | null>(null)

const snackbar = ref(false)
const snackbarTheme = ref('')
const snackbarMessage = ref('')
const closeSnackbar = () => (snackbar.value = false)
const showSnackbar = () => (snackbar.value = true)

const onLogin = async () => {
  if (form.value && username.value && password.value) {
    const res = await fetchLogin(username.value, password.value)
    const json = await res.json()
    console.log(json)
    openLoginSnackbar(res.status)

  }
}
const onRegister = async () => {
  if (form.value && username.value && password.value) {
    const res = await fetchRegister(username.value, password.value)
    openRegisterSnackbar(res.status)
  }
}
const openLoginSnackbar = (status: number) => {
  if (status !== 404 && status !== 401 && status !== 200) return

  const messages = {
    200: 'Success login',
    404: 'User not exists',
    401: 'Incorrect password',
  }
  const theme = {
    200: 'success',
    404: 'error',
    401: 'error',
  }
  snackbarMessage.value = messages[status]
  snackbarTheme.value = theme[status]
  showSnackbar()
}
const openRegisterSnackbar = (status: number) => {
  if (status !== 403 && status !== 201) return

  const messages = {
    403: 'User already exists',
    201: 'User register success',
  }
  const theme = {
    403: 'error',
    201: 'success',
  }
  snackbarMessage.value = messages[status]
  snackbarTheme.value = theme[status]
  showSnackbar()
}
</script>

<template>
  <VContainer class="ma-auto">
    <VRow justify="center">
      <VCol cols="5">
        <VSheet class="pa-4">
          <LoginForm
            v-model:username="username"
            v-model:password="password"
            v-model:form="form"
            @login="onLogin"
            @register="onRegister"
          />
        </VSheet>
      </VCol>
    </VRow>
    <v-snackbar v-model="snackbar">
      {{ snackbarMessage }}
      <template #actions>
        <v-btn :color="snackbarTheme" variant="text" @click="closeSnackbar">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </VContainer>
</template>
