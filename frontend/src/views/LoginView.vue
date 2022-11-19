<script setup lang="ts">
import { ref } from 'vue'
import LoginForm from '@/components/LoginForm.vue'
import { fetchLogin, fetchRegister } from '@/services/login'

const form = ref<boolean | null>(null)
const email = ref<string | null>(null)
const password = ref<string | null>(null)

const onLogin = async () => {
  if (form.value && email.value && password.value) {
    const res = await fetchLogin(email.value, password.value)
    console.log(res)
  }
}
const onRegister = async () => {
  if (form.value && email.value && password.value) {
    const res = await fetchRegister(email.value, password.value)
    console.log(res)
  }
}
</script>

<template>
  <VContainer class="ma-auto">
    <VRow justify="center">
      <VCol cols="5">
        <VSheet class="pa-4">
          <LoginForm
            v-model:form="form"
            v-model:email="email"
            v-model:password="password"
            @login="onLogin"
            @register="onRegister"
          />
        </VSheet>
      </VCol>
    </VRow>
  </VContainer>
</template>
