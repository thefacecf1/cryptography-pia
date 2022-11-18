<template>
  <v-card class="ma-auto pa-4" max-width="60%">
    <v-list lines="two">
      <v-list-subheader>Chat</v-list-subheader>
      <v-list-item>
        <v-list-title>User</v-list-title>
        <v-list-item-subtitle>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Odio
          aenean sed adipiscing diam donec adipiscing tristique risus nec.
        </v-list-item-subtitle>
        <template #prepend>
          <v-avatar class="mt-auto" color="info">
            <v-icon icon="mdi-account-circle"></v-icon>
          </v-avatar>
        </template>
      </v-list-item>
    </v-list>
    <v-textarea
      hide-details
      auto-grow
      rows="1"
      label="Mensaje"
      variant="outlined"
      append-icon="mdi-send"
    />
  </v-card>
</template>
<script setup lang="ts"></script>
