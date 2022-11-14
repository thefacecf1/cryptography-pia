<script setup lang="ts">
import { ref } from "vue";

const message = ref("");
const fetchMessage = async () => {
  const res = await fetch("http://localhost:5000/");
  const text = await res.text();
  message.value = text;
};
fetchMessage();
</script>

<template>
  <main>
    <div>This message is from backend: </div>
    <h1>{{ message }}</h1>
  </main>
</template>
