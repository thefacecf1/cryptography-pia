<script setup lang="ts">
type FormValue = boolean | null

interface Emits {
  (e: 'login'): void
  (e: 'register'): void
  (e: 'update:email', email: string): void
  (e: 'update:form', form: FormValue): void
  (e: 'update:password', password: string): void
}

const emits = defineEmits<Emits>()
const props = defineProps<{
  form: boolean | null
  email: string | null
  password: string | null
}>()

const defaultRules = [(v: any) => !!v || 'Field is required']

const emitLogin = () => emits('login')
const emitRegister = () => emits('register')

const emitForm = (form: FormValue) => emits('update:form', form)
const emitEmail = (email: string) => emits('update:email', email)
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
      type="email"
      variant="outlined"
      placeholder="Email"
      :value="props.email"
      :rules="defaultRules"
      @input="emitEmail($event.target.value)"
    />
    <VTextField
      class="mb-2"
      type="text"
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
