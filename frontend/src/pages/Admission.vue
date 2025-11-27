<template>
<section class="relative w-full h-screen mb-8">
  <!-- Background Image -->
  <img src="/admi.jpg" alt="Admission Banner" class="absolute inset-0 w-full h-full object-cover opacity-90" />

  <!-- Overlay (optional for dark effect) -->
  <div class="absolute inset-0 bg-black bg-opacity-40"></div>

  <!-- Content -->
  <div class="relative z-10 flex items-center justify-end h-full px-6 md:px-20">
    <!-- Form Card -->
    <div class="bg-white rounded-2xl shadow-lg p-8 max-w-md w-full">
      <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">Admission Form</h2>
      <form action="#" method="POST" class="space-y-4">
        
        <input type="text" placeholder="Name" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 outline-none" />

        <input type="email" placeholder="Email" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 outline-none" />

        <input type="text" placeholder="Course" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 outline-none" />

        <input type="tel" placeholder="Phone Number" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 outline-none" />

        <textarea placeholder="Message" rows="4" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 outline-none"></textarea>

        <button type="submit" class="w-full bg-[#20b486] text-white py-2 px-4 rounded-lg hover:bg-green-700 transition">
          Send Message
        </button>
      </form>
    </div>
  </div>
</section>


</template>

<script>

</script>