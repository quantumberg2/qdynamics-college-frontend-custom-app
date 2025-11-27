<template>
  <div>
    <!-- Hero Section -->
    <div class="w-full h-full">
      <img src="/group.png" alt="Group Banner" class="w-full h-full object-cover" width="1920" height="600" priority />
    </div>

    <!-- Cards Section -->
    <section class="container bg-gray-100 py-10 px-5">
      <div class="max-w-7xl mx-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">

        <!-- Card 1 -->
        <router-link to="/AnnouncementList" class="no-underline text-inherit">
          <article class="bg-white shadow-md rounded-lg p-3 text-center">
            <img src="/ai.png" alt="Announcements Section" class="mx-auto mb-4 object-contain" loading="lazy" />
            <h2 class="font-semibold text-left text-lg mb-2 flex justify-between items-center">
              Announcement
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="w-5 h-5" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
              </svg>
            </h2>
          </article>
        </router-link>

        <!-- Card 2 -->
        <router-link to="/Blogs" class="no-underline text-inherit">
          <article class="bg-white shadow-md rounded-lg p-3 text-center">
            <img src="/ml.png" alt="Blogs Section" class="mx-auto mb-4 object-contain" loading="lazy" />
            <h2 class="font-semibold text-left text-lg mb-2 flex justify-between items-center">
              Blogs
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="w-5 h-5" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
              </svg>
            </h2>
          </article>
        </router-link>

        <!-- Card 3 -->
        <router-link to="/News" class="no-underline text-inherit">
          <article class="bg-white shadow-md rounded-lg p-3 text-center">
            <img src="/ds.png" alt="News Section" class="mx-auto mb-4 object-contain" loading="lazy" />
            <h2 class="font-semibold text-left text-lg mb-2 flex justify-between items-center">
              News
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="w-5 h-5" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
              </svg>
            </h2>
          </article>
        </router-link>

      </div>
    </section>

    <!-- Foundation Section -->
    <section class="bg-gray-100">
      <div
        class="max-w-7xl mx-auto px-6 sm:px-6 md:px-10 lg:px-20 py-5 flex flex-col md:flex-row items-center md:justify-between gap-y-8">

        <!-- Left Content -->
        <article class="w-full md:w-1/2 text-center md:text-left mb-8 md:mb-0 md:pl-12">
          <h1 class="font-bold mb-4 text-3xl">Foundation and Management</h1>
          <p class="text-gray-700 mb-6">
            Lorem ipsum dolor sit amet cubilia letius non himenaeos mollis sed praesent. Habitant metus malesuada in
            integer ut porttitor nullam magnis dis. Tempus dictum mus est molestie ipsum ullamcorper dapibus montes
            sagittis.
            Nostra urna ex nisl habitasse sociosqu.
          </p>
          <p class="text-gray-700 mb-6">
            Lorem ipsum dolor sit amet netus. Integer at curabitur porttitor lacinia aenean fringilla maecenas.
            Congue tristique elementum sollicitudin integer hac dignissim maximus. Fusce vehicula mus maximus vivamus
            dis ad dignissim. Leo efficitur arcu dapibus vivamus auctor dignissim hendrerit eu nascetur.
          </p>
          <p>
            Lorem ipsum dolor sit amet nulla ultrices ac. Leo mauris hendrerit ultricies sem velit viverra quis
            penatibus dui sagittis. Dictumst nullam duis interdum natoque.
          </p>
        </article>

        <!-- Right Image -->
        <div class="w-full md:w-1/2 flex justify-center md:justify-end">
          <img src="/result.png" alt="Foundation Results"
            class="w-full max-w-sm md:max-w-md h-auto object-cover rounded-lg" loading="lazy" width="400"
            height="400" />
        </div>

      </div>
    </section>
  </div>
</template>

<script>
export default {}
</script>
