<template>
    <!-- Carousel Section -->
    <div class="py-12 lg:px-20 sm:py-8 sm:px-4 lg:py-12 bg-gray-100">
        <div class="max-w-7xl mx-auto px-8 sm:px-4 md:px-6 lg:px-8">
            <h5 class="font-bold p-2" style="color: #20B486;">Explore Programs</h5>
            <h3 class="font-semibold px-2 py-1 text-3xl">Our Most Popular Class</h3>
            <h5 class="p-2 font-medium">
                Let's join our famous class, the knowledge provided will definitely be useful for you.
            </h5>

            <div class="relative w-full overflow-hidden">
                <!-- Carousel container -->
                <div class="flex transition-transform duration-500 carousel"
                    :style="{ transform: `translateX(-${currentIndex * cardWidth}px)` }" ref="carousel">
                    <!-- Carousel cards -->
                    <div v-for="(item, index) in items" :key="index" class="flex-shrink-0 w-full sm:w-1/3 p-2">
                        <div class="bg-white shadow-md rounded-lg p-4 text-center">
                            <img :src="item.image" alt="Card Image" class="mx-auto mb-4 object-contain" />
                            <h2 class="font-semibold text-left text-lg mb-2 flex justify-between items-center">
                                {{ item.title }}
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                                    class="w-4 h-4">
                                    <path fill-rule="evenodd"
                                        d="M8.25 3.75H19.5a.75.75 0 0 1 .75.75v11.25a.75.75 0 0 1-1.5 0V6.31L5.03 20.03a.75.75 0 0 1-1.06-1.06L17.69 5.25H8.25a.75.75 0 0 1 0-1.5Z"
                                        clip-rule="evenodd" />
                                </svg>
                            </h2>
                            <p class="text-left text-sm">{{ item.content }}</p>
                        </div>
                    </div>
                </div>

                <!-- Dots -->
                <div class="flex justify-center mt-4 space-x-2">
                    <span v-for="(dot, index) in totalDots" :key="'dot-' + index" @click="goTo(index)" :class="[
                        'w-3 h-3 rounded-full cursor-pointer',
                        currentIndex === index ? 'bg-[#20B486]' : 'bg-gray-400'
                    ]"></span>
                </div>

                <!-- Explore Button -->
                <div class="text-center mt-4">
                    <button class="rounded-lg p-2" style="background-color: #20B486; color:#ffffff;">
                        Explore All Programs
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            items: [
                {
                    image: "/ai.png",
                    title: "Artificial Intelligence",
                    content:
                        "AI enables machines to simulate human intelligence and decision-making.",
                },
                {
                    image: "/ds.png",
                    title: "Data Scientist",
                    content:
                        "Data Science extracts insights from raw data to drive smarter decisions.",
                },
                {
                    image: "/ml.png",
                    title: "Machine Learning",
                    content:
                        "ML allows systems to learn from data and improve automatically.",
                },
                {
                    image: "/ai.png",
                    title: "Artificial Intelligence",
                    content:
                        "AI enables machines to simulate human intelligence and decision-making.",
                },
                {
                    image: "/ds.png",
                    title: "Data Scientist",
                    content:
                        "Data Science extracts insights from raw data to drive smarter decisions.",
                },
                {
                    image: "/ml.png",
                    title: "Machine Learning",
                    content:
                        "ML allows systems to learn from data and improve automatically.",
                },
            ],
            currentIndex: 0,
            cardWidth: 0,
            visibleCards: 1,
        };
    },
    computed: {
        totalDots() {
            return Math.ceil(this.items.length / this.visibleCards);
        },
    },
    mounted() {
        this.updateCardWidth();
        window.addEventListener("resize", this.updateCardWidth);
    },
    beforeUnmount() {
        window.removeEventListener("resize", this.updateCardWidth);
    },
    methods: {
        updateCardWidth() {
            const container = this.$refs.carousel;
            if (window.innerWidth >= 640) {
                this.visibleCards = 3;
            } else {
                this.visibleCards = 1;
            }
            if (container) {
                this.cardWidth = container.offsetWidth / this.visibleCards;
            }
        },
        next() {
            if (this.currentIndex < this.totalDots - 1) {
                this.currentIndex++;
            } else {
                this.currentIndex = 0;
            }
        },
        prev() {
            if (this.currentIndex > 0) {
                this.currentIndex--;
            } else {
                this.currentIndex = this.totalDots - 1;
            }
        },
        goTo(index) {
            this.currentIndex = index;
        },
    },
};
</script>

<style>
/* Hide scrollbar */
.carousel::-webkit-scrollbar {
    display: none;
}
</style>
