<template>
  <div>
    <div class="bg-slate-50">
      <div
        class="max-w-7xl mx-auto px-6 sm:px-6 md:px-10 lg:px-20 py-5 flex flex-col md:flex-row items-center md:justify-between gap-y-8"
        aria-label="Hero Section">
        <!-- Left Content -->
        <div class="w-full md:w-1/2 text-center md:text-left mb-8 md:mb-0 md:pl-12">
          <h1 class="font-bold mb-4 text-[25px] md:text-[50px] leading-tight">
            Build your <span class="text-[#20B486]">skills</span><br />
            and <span class="text-[#20B486]">Unlock</span> your
            <span class="text-[#20B486]">True</span> potential
          </h1>
          <p class="text-gray-700 mb-6">
            Join [School/College Name], where modern education, expert faculty,
            and real-world learning experiences prepare you for a successful future.
          </p>
        </div>

        <!-- Right Image -->
        <div class="w-full md:w-1/2 flex justify-center md:justify-end">
          <img src="/newlogo.png" alt="Hero Image" class="w-full max-w-sm md:max-w-xl h-auto object-cover rounded-lg"
            loading="lazy" decoding="async" />
        </div>
      </div>
    </div>

    <!-- 2nd Section -->
    <AboutContentHome />

    <!-- 3rd Section -->
    <Acedemics />

    <!-- 4th Section -->
    <secondAboutUsHome />
  </div>
</template>

<script>
import AboutContentHome from './AboutContentHome.vue';
import Acedemics from './Acedemics.vue';
import secondAboutUsHome from './secondAboutUsHome.vue';

export default {
  components: {
    AboutContentHome,
    Acedemics,
    secondAboutUsHome,
  },
};
</script>

<style>
/* Optional: hide scrollbar */
.carousel::-webkit-scrollbar {
  display: none;
}
</style>
