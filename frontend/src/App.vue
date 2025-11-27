<template>
  <div class="min-h-screen bg-gray-100 text-gray-800 font-sans">
    <!-- Header -->
    <header aria-label="Main Navigation">
      <Navbar /> <!-- Always visible -->
    </header>

    <!-- Main content -->
    <main class="pt-[150px]" aria-label="Page Content">
      <router-view /> <!-- Page changes here -->
    </main>

    <!-- Footer -->
    <footer aria-label="Footer Section">
      <Footer /> <!-- Always visible -->
    </footer>
  </div>
</template>

<script>
import { defineAsyncComponent } from 'vue'

// Lazy load Navbar & Footer for better performance
const Navbar = defineAsyncComponent(() => import('@/pages/Navbar.vue'))
const Footer = defineAsyncComponent(() => import('@/pages/Footer.vue'))

export default {
  components: {
    Navbar,
    Footer
  }
}
</script>

<style>
/* Apply global font more efficiently */
html,
body {
  font-family: "Roboto", sans-serif;
}
</style>
