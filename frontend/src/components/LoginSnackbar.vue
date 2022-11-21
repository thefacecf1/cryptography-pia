<script setup lang="ts">
const props = defineProps<{
  theme: string
  message: string
  modelValue: boolean
}>()
const emits = defineEmits<{
  (e: 'click:actions'): void
}>()
</script>
<template>
  <v-snackbar :model-value="props.modelValue">
    {{ props.message }}
    <template #actions>
      <v-btn
        variant="text"
        :color="props.theme"
        @click="emits('click:actions')"
      >
        Close
      </v-btn>
    </template>
  </v-snackbar>
</template>
