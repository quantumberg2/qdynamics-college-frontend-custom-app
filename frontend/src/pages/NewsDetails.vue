<template>
    <div class="bg-gray-100 py-10 px-5">

        <!-- Loading State -->
        <div v-if="isLoading" class="text-center py-20 text-gray-500 text-lg">
            Loading news details...
        </div>

        <!-- News Details -->
        <div v-else-if="news" class="max-w-6xl mx-auto mb-12">

            <!-- Header Image -->
            <img v-if="news.header_image" :src="news.header_image" alt="News Image"
                class="w-full h-96 object-cover rounded-lg mb-6" loading="lazy" />

            <!-- Description Headings & Content -->
            <div v-for="n in 10" :key="n">
                <template v-if="news[`description_heading_${n}`]">
                    <h2 class="text-2xl font-bold text-gray-800 mb-3">{{ news[`description_heading_${n}`] }}</h2>
                    <p class="text-gray-700 text-lg leading-relaxed" v-html="news[`description_${n}`]"></p>
                </template>
            </div>

            <!-- Custom HTML -->
            <div v-if="news.custom_html" v-html="news.custom_html"></div>
        </div>

        <!-- Fallback if no news found -->
        <div v-else class="text-center text-gray-500">Exploring News</div>

    </div>
</template>

<script>
import axios from 'axios'
import { useRoute } from 'vue-router'

export default {
    name: "NewsDetails",
    data() {
        return {
            news: null,
            isLoading: true
        }
    },
    setup() {
        const route = useRoute()
        return { route }
    },
    mounted() {
        this.fetchNewsDetails()
    },
    methods: {
        async fetchNewsDetails() {
            const newsName = this.route.query.name
            if (!newsName) {
                this.isLoading = false
                return
            }

            try {
                const res = await axios.get('/api/method/education_app.api.education_news.get_news_item', {
                    params: { news_name: newsName }
                })

                // Handle array or object
                if (Array.isArray(res.data.message)) {
                    this.news = res.data.message[0] || null
                } else {
                    this.news = res.data.message || null
                }

            } catch (err) {
                console.error('Error fetching news details:', err)
                this.news = null
            } finally {
                this.isLoading = false
            }
        }
    }
}
</script>
