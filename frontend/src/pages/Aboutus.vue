<template>
  <div>
    <!-- About Us Section 1 -->
    <section class="bg-slate-50" aria-label="About Us - History">
      <div
        class="max-w-7xl mx-auto px-6 sm:px-6 md:px-10 lg:px-20 py-5 flex flex-col md:flex-row items-center md:justify-between gap-y-8">

        <!-- Left Content -->
        <div class="w-full md:w-1/2 text-center md:text-left mb-8 md:mb-0 md:pl-12">
          <h1 class="font-bold mb-4 text-3xl">About Us</h1>
          <h3 class="font-bold mb-4">Great History Of Our College</h3>
          <p class="text-gray-700 mb-6">
            Sri Chaitanya Junior College was founded in the year 1991. It has since grown across geographies and is now
            present not only in Telangana, but also in Andhra Pradesh & Karnataka. We provide quality education right
            from
            playgroup and kindergarten, all the way to undergraduate levels and groom students for competitive fields
            such
            as Medicine, Engineering,
            Chartered Accountancy, Law and Civil Services.
          </p>
          <button class="text-center rounded-lg p-2 bg-[#20B486] text-white hover:opacity-90 transition">
            Know more
          </button>
        </div>

        <!-- Right Image -->
        <div class="w-full md:w-1/2 flex justify-center md:justify-end">
          <img src="/about.png" alt="About Our College"
            class="w-full max-w-sm md:max-w-md h-auto object-cover rounded-lg" loading="lazy" decoding="async"
            width="400" height="300" />
        </div>
      </div>
    </section>

    <!-- About Us Section 2 -->
    <section class="bg-gray-100" aria-label="About Us - Mission and Vision">
      <div
        class="max-w-7xl mx-auto px-6 sm:px-6 md:px-10 lg:px-20 py-5 flex flex-col md:flex-row items-center md:justify-between gap-y-8">

        <!-- Left Image -->
        <div class="w-full md:w-1/2 md:justify-start md:ml-8">
          <img src="/secimg.png" alt="College Mission"
            class="w-full max-w-sm md:max-w-md h-auto object-cover rounded-lg" loading="lazy" decoding="async"
            width="400" height="300" />
        </div>

        <!-- Right Content -->
        <div class="w-full md:w-1/2 text-center md:text-left mb-8 md:mb-0">
          <h1 class="font-bold mb-2 text-3xl">About Us</h1>
          <h3 class="font-bold mb-3">Great History Of Our College</h3>
          <p class="text-gray-700 mb-3">
            To empower students with knowledge, skills, and values to become confident, responsible, and successful
            individuals in a global society. We provide high-quality education through innovative teaching, fostering
            holistic development, and nurturing a lifelong love for learning.
          </p>
          <p class="text-gray-700 mb-3">
            Our vision is to nurture curious minds, creative thinkers, and compassionate hearts. By cultivating a
            lifelong
            love for learning, we aim to equip students not only for academic achievement but also for personal growth,
            social responsibility, and meaningful contribution to the world around them.
          </p>
          <button class="text-center rounded-lg p-2 bg-[#20B486] text-white hover:opacity-90 transition">
            Know more
          </button>
        </div>
      </div>
    </section>

    <!-- Benefits Section -->
    <section class="py-12 lg:px-20 sm:py-8 sm:px-4 lg:py-12 bg-gray-100" aria-label="Our Benefits">
      <div class="max-w-7xl mx-auto px-8 sm:px-4 md:px-6 lg:px-8 text-center">
        <h5 class="font-bold p-2 text-[#20B486]">Our Benefits</h5>
        <h3 class="font-semibold px-2 py-1 text-3xl">
          By Joining WEEKENS College, One Can Avail a Lot Of Opportunities.
        </h3>
        <h5 class="p-2 text-sm">
          Install our top-rated dropshipping app to your e-commerce site and get access to US Suppliers, AliExpress
          vendors, and the best.
        </h5>

        <!-- Benefits Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 p-4">

          <article v-for="n in 6" :key="n" class="bg-white shadow-lg rounded-xl p-6 text-left">
            <h2 class="text-3xl font-bold text-[#20b486]">0{{ n }}</h2>
            <h3 class="text-xl font-semibold mt-2">Standardization</h3>
            <p class="text-gray-600 mt-2">
              When working in a global workplace, it’s often difficult to gauge learners’ training experiences, which
              are
              ...
            </p>
            <a href="#" class="inline-block mt-4 text-[#20b486] font-medium hover:underline">
              Read More about Standardization
            </a>
          </article>

        </div>
      </div>
    </section>
  </div>
</template>
