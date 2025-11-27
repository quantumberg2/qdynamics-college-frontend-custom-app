<template>
    <div>
        <div class="w-full bg-[#F0FAF7] py-12 px-4">

            <!-- Loading State -->
            <div v-if="loading" class="flex justify-center items-center py-12">
                <div class="w-10 h-10 border-4 border-emerald-500 border-t-transparent rounded-full animate-spin"></div>
                <span class="ml-3 text-emerald-600 font-medium">Loading images...</span>
            </div>

            <!-- Gallery -->
            <div v-else class="container">
                <div class="row">
                    <div class="col-md-4 mb-2" v-for="(col, index) in imageColumns" :key="index">
                        <img v-for="(img, i) in col" :key="i" :src="img" alt="Gallery Image" class="img-fluid mb-2"
                            loading="lazy" />
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            images: [],
            loading: true,
        };
    },
    computed: {
        // Pre-compute 3 columns with 2 images each
        imageColumns() {
            const cols = [[], [], []];
            for (let i = 0; i < Math.min(this.images.length, 6); i++) {
                cols[Math.floor(i / 2)].push(this.images[i]);
            }
            return cols;
        },
    },
    mounted() {
        this.fetchGalleryImages();
    },
    methods: {
        async fetchGalleryImages() {
            try {
                const startTime = Date.now();
                const res = await axios.get(
                    "/api/method/education_app.api.galleryImages.get_gallery_images"
                );

                // Convert object to array and remove null/undefined
                this.images = Object.values(res.data.message || {}).filter(Boolean);

                // Keep loader visible at least 1 second for smoother UX
                const elapsed = Date.now() - startTime;
                const delay = Math.max(1000 - elapsed, 0);
                setTimeout(() => {
                    this.loading = false;
                }, delay);

            } catch (err) {
                console.error("Error fetching gallery images:", err);
                this.loading = false;
            }
        },
    },
};
</script>
