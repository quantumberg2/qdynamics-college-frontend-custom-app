<template>
  <div>
    <!-- Loading Screen -->
    <div v-if="isLoading" class="flex items-center justify-center h-64" role="status" aria-live="polite">
      <p class="text-emerald-600 text-lg font-semibold animate-pulse">
        Loading Courses...
      </p>
    </div>

    <!-- Main Content -->
    <section v-else class="py-12 lg:px-20 sm:py-8 sm:px-4 lg:py-12 bg-gray-100" aria-label="Academic Courses">
      <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">

        <!-- Academic Card -->
        <article v-for="(item, index) in items" :key="item.id || index"
          class="bg-white shadow-md rounded-lg p-4 text-center">
          <!-- Image -->
          <img :src="item.thumbnail_image" :alt="item.title || 'Course Thumbnail'" class="mx-auto mb-4 object-contain"
            loading="lazy" decoding="async" width="300" height="200" />

          <!-- Title -->
          <h2 class="font-semibold text-left text-lg mb-2 flex justify-between items-center">
            {{ item.title }}
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-4 h-4"
              aria-hidden="true">
              <path fill-rule="evenodd"
                d="M8.25 3.75H19.5a.75.75 0 0 1 .75.75v11.25a.75.75 0 0 1-1.5 0V6.31L5.03 20.03a.75.75 0 0 1-1.06-1.06L17.69 5.25H8.25a.75.75 0 0 1 0-1.5Z"
                clip-rule="evenodd" />
            </svg>
          </h2>

          <!-- Content -->
          <p class="text-left text-sm">{{ item.content }}</p>
        </article>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      items: [],
      isLoading: true,
    };
  },
  mounted() {
    this.fetchAcademicTypes();
  },
  methods: {
    async fetchAcademicTypes() {
      try {
        const res = await axios.get(
          "/api/method/education_app.api.academic_type.get_academic_types"
        );
        this.items = res.data.message || [];

        // keep loader visible for 1 second
        setTimeout(() => {
          this.isLoading = false;
        }, 1000);
      } catch (err) {
        console.error("Error fetching Academic Types:", err);
        this.isLoading = false;
      }
    },
  },
};
</script>
