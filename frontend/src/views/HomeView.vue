<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useMessagesStore } from '@/stores/messages'
import { storeToRefs } from 'pinia'

const store = useMessagesStore()
const { getMessages, sendMessage } = store
const { messages } = storeToRefs(store)

const { params } = useRoute()
const text = ref<string | null>(null)

const onClick = () => {
  if (!text.value) return
  if (typeof params.username !== 'string') return
  sendMessage(params.username, text.value)
  text.value = ''
}

getMessages()
</script>
<template>
  <v-card class="ma-auto pa-4 rounded" max-width="60%">
    <v-list lines="two">
      <v-list-subheader>Chat</v-list-subheader>

      <v-list-item v-if="!messages">
        <v-list-item-subtitle>Not messages yet :(</v-list-item-subtitle>
        <template #prepend>
          <v-avatar class="mt-auto" color="info">
            <v-icon icon="mdi-account-circle"></v-icon>
          </v-avatar>
        </template>
      </v-list-item>
      <v-list-item
        v-for="message in messages"
        v-else
        :key="message.id"
        :title="message.username"
        :subtitle="message.message"
      >
        <template #prepend>
          <v-avatar class="mt-auto" color="info">
            <v-icon icon="mdi-account-circle"></v-icon>
          </v-avatar>
        </template>
      </v-list-item>
    </v-list>
    <v-textarea
      v-model="text"
      hide-details
      auto-grow
      rows="1"
      label="Mensaje"
      variant="outlined"
      append-icon="mdi-send"
      @click:append="onClick"
    />
  </v-card>
</template>
