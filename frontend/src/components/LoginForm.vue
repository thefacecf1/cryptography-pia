<script setup lang="ts">
type FormValue = boolean | null

interface Emits {
  (e: 'login'): void
  (e: 'register'): void
  (e: 'update:username', username: string): void
  (e: 'update:form', form: FormValue): void
  (e: 'update:password', password: string): void
}

const emits = defineEmits<Emits>()
const props = defineProps<{
  form: boolean | null
  username: string | null
  password: string | null
}>()

const defaultRules = [(v: any) => !!v || 'Field is required']

const emitLogin = () => emits('login')
const emitRegister = () => emits('register')

const emitForm = (form: FormValue) => emits('update:form', form)
const emitUsername = (username: string) => emits('update:username', username)
const emitPassword = (password: string) => emits('update:password', password)
</script>
<template>
  <VForm
    :model-value="props.form"
    @update:model-value="emitForm"
    @submit.prevent=""
  >
    <VTextField
      class="mb-2"
      type="text"
      variant="outlined"
      placeholder="Username"
      :value="props.username"
      :rules="defaultRules"
      @input="emitUsername($event.target.value)"
    />
    <VTextField
      class="mb-2"
      type="password"
      variant="outlined"
      placeholder="Password"
      :value="props.password"
      :rules="defaultRules"
      @input="emitPassword($event.target.value)"
    />
    <div class="d-flex">
      <VBtn
        type="submit"
        color="info"
        :disabled="!props.form"
        @click="emitRegister"
      >
        Register
      </VBtn>
      <VBtn
        type="submit"
        color="success"
        class="ml-auto"
        :disabled="!props.form"
        @click="emitLogin"
      >
        Login
      </VBtn>
    </div>
  </VForm>
</template>
