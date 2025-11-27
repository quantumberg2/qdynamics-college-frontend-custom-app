<template>
  <footer class="bg-gray-800 text-white px-20 py-10">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row md:justify-between gap-10">

      <!-- Logo and description -->
      <div class="flex flex-col items-start space-y-2 md:w-1/4">
        <img src="/logo.png" alt="Logo" class="w-20 h-auto object-cover" />
        <p class="text-gray-400 text-sm">Your tagline or short description goes here.</p>
      </div>

      <!-- 4 Columns with 5 rows each -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-6 md:w-3/4">

        <!-- Column 1 -->
        <div class="flex flex-col space-y-2">
          <h4 class="text-slate-50 font-semibold">Product</h4>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">Overview</a>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">Solutions</a>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">Tutorials</a>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">Pricing</a>
        </div>

        <!-- Column 2 -->
        <div class="flex flex-col space-y-2">
          <h4 class="text-slate-50 font-semibold">Company</h4>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">About Us</a>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">Carrers</a>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">Press</a>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">News</a>
        </div>

        <!-- Column 3 -->
        <div class="flex flex-col space-y-2">
          <h4 class="text-slate-50 font-semibold">Social</h4>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">twitter</a>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">Linkedin</a>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">GitHub</a>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">Dribble</a>
        </div>

        <!-- Column 4 -->
        <div class="flex flex-col space-y-2">
          <h4 class="text-slate-50 font-semibold">Legal</h4>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">Terms</a>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">Privacy</a>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">Cookies</a>
          <a href="#" class="text-gray-400 hover:text-emerald-400 text-sm">Contact</a>
        </div>

      </div>
    </div>

    <!-- Powered By -->
    <div class="mt-8 flex flex-col md:flex-row items-center justify-between border-t border-gray-700 pt-4">
      <!-- Left: Powered by -->
      <div class="text-gray-500 text-sm mb-4 md:mb-0">
        Powered & Designed by 
        <a href="https://quantumnberg.com" class="text-emerald-400 hover:underline">Quantumnberg Technologies</a>
      </div>

      <!-- Right: Social Media Icons -->
      <div class="flex space-x-4">
        <a href="#" class="text-gray-400 hover:text-emerald-400">
          <i class="fab fa-facebook-f"></i>
        </a>
        <a href="#" class="text-gray-400 hover:text-emerald-400">
          <i class="fab fa-instagram"></i>
        </a>
        <a href="#" class="text-gray-400 hover:text-emerald-400">
          <i class="fab fa-youtube"></i>
        </a>
      </div>
    </div>
  </footer>

</template>

<script>
export default {
  name: "Footer",
};
</script>
