<script setup lang="ts">
import { ref } from 'vue'
import { isMappedStatusCode } from '@/utils/typeGuards'
import { fetchLogin, fetchRegister } from '@/services/users'
import { SNACKBAR_MESSAGES, SNACKBAR_THEMES } from '@/constants'

import LoginForm from '@/components/LoginForm.vue'
import LoginSnackbar from '@/components/LoginSnackbar.vue'
import { useRouter } from 'vue-router'

const { push } = useRouter()
const form = ref<boolean | null>(null)
const username = ref<string | null>(null)
const password = ref<string | null>(null)

const snackbar = ref(false)
const snackbarTheme = ref('')
const snackbarMessage = ref('')
const closeSnackbar = () => (snackbar.value = false)
const showSnackbar = () => (snackbar.value = true)
const openSnackbar = (message = 'Default Message', theme = 'Success') => {
  snackbarMessage.value = message
  snackbarTheme.value = theme
  showSnackbar()
}
const onLogin = async () => {
  if (form.value && username.value && password.value) {
    const res = await fetchLogin(username.value, password.value)
    if (isMappedStatusCode(res.status)) {
      openSnackbar(SNACKBAR_MESSAGES[res.status], SNACKBAR_THEMES[res.status])
    }
    if (res.status !== 200) return
    push({ name: 'chat', params: { username: username.value } })
  }
}
const onRegister = async () => {
  if (form.value && username.value && password.value) {
    const res = await fetchRegister(username.value, password.value)
    if (!isMappedStatusCode(res.status)) return
    openSnackbar(SNACKBAR_MESSAGES[res.status], SNACKBAR_THEMES[res.status])
  }
}
</script>

<template>
  <VContainer class="ma-auto">
    <VRow justify="center">
      <VCol cols="5">
        <VSheet class="pa-4 rounded">
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
    <LoginSnackbar
      :theme="snackbarTheme"
      :model-value="snackbar"
      :message="snackbarMessage"
      @click:actions="closeSnackbar"
    />
  </VContainer>
</template>
