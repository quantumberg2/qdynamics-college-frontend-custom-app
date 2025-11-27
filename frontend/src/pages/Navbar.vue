<template>
  <nav class="w-full fixed top-0 left-0 z-50 shadow">
    <!-- Top Header -->
    <div class="nav-header py-2 px-5 bg-[#20B486] text-white">
      <div class="grid grid-cols-3 gap-8">
        <div class="flex items-center justify-center space-x-2">
          <PhoneIcon class="w-5 h-4" />
          <span class="text-sm md:text-lg">+91 9876543567</span>
        </div>
        <div class="flex items-center justify-center space-x-2">
          <EnvelopeIcon class="w-5 h-5" />
          <span class="text-sm md:text-xl">info@example.com</span>
        </div>
        <div class="flex items-center justify-center space-x-4">
          <i class="fab fa-facebook text-1x"></i>
          <i class="fab fa-youtube text-1x"></i>
          <i class="fab fa-instagram text-1x"></i>
        </div>
      </div>
    </div>

    <!-- Main Navbar -->
    <div class="bg-slate-50 px-4 py-3 relative" ref="navbar">
      <div class="max-w-7xl mx-auto flex items-center justify-between">
        <!-- Logo -->
        <div class="text-black font-bold text-xl px-5">
          <img src="/logo.png" alt="Logo" class="w-18 h-16 md:w-25 md:h-20 md:pl-20 object-cover" />
        </div>

        <!-- Desktop Nav -->
        <div class="hidden md:flex space-x-6 px-20">
          <router-link v-for="link in navLinks" :key="link.name" :to="link.to"
            class="py-2 !text-black no-underline hover:!text-emerald-400"
            exact-active-class="!text-emerald-400 font-semibold">
            {{ link.name }}
          </router-link>
          <router-link to="/admission"
            class="bg-[#20b486] text-white px-2 py-2 rounded-md hover:!bg-emerald-600 transition no-underline"
            exact-active-class="!bg-emerald-600">
            For New Admission
          </router-link>
        </div>

        <!-- Mobile Menu Button -->
        <div class="md:hidden ml-auto">
          <button @click="toggleMenu" class="text-black focus:outline-none">
            <Bars3Icon class="h-6 w-6 text-black" />
          </button>
        </div>
      </div>

      <!-- Mobile Nav -->
      <div ref="mobileMenu" :class="[
        'md:hidden flex flex-col space-y-2 mt-0 overflow-hidden transition-all duration-300 ease-in-out bg-slate-50 px-4 absolute top-full left-0 w-full z-50',
        isOpen ? 'max-h-96 opacity-100 py-3' : 'max-h-0 opacity-0 py-0'
      ]">
        <router-link v-for="link in navLinks" :key="link.name + '-mobile'" @click="closeMenu" :to="link.to"
          class="!text-black no-underline hover:!text-emerald-400" exact-active-class="!text-emerald-400 font-semibold">
          {{ link.name }}
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
import { PhoneIcon, EnvelopeIcon, Bars3Icon } from '@heroicons/vue/24/solid'

export default {
  name: "Navbar",
  components: { PhoneIcon, EnvelopeIcon, Bars3Icon },
  data() {
    return {
      isOpen: false,
      navLinks: [
        { name: "Home", to: "/" },
        { name: "About", to: "/about" },
        { name: "Academic", to: "/AcademicsCourses" },
        { name: "Announcements", to: "/Announcements" },
        { name: "Gallery", to: "/gallery" },
        { name: "Contact Us", to: "/contact" }
      ]
    };
  },
  mounted() {
    document.addEventListener("click", this.handleClickOutside);
  },
  beforeUnmount() {
    document.removeEventListener("click", this.handleClickOutside);
  },
  methods: {
    toggleMenu() {
      this.isOpen = !this.isOpen;
    },
    closeMenu() {
      this.isOpen = false;
    },
    handleClickOutside(event) {
      if (this.isOpen && !this.$refs.navbar.contains(event.target)) {
        this.isOpen = false;
      }
    }
  }
}
</script>
