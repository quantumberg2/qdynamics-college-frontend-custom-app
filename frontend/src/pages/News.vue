<template>
    <div class="container bg-gray-100 py-10 px-5">

        <!-- Loading State -->
        <div v-if="isLoading" class="text-center py-20 text-gray-500 text-lg">
            Loading news...
        </div>

        <!-- News Grid -->
        <div v-else class="max-w-7xl mx-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
            <div v-for="news in newsList" :key="news.name"
                class="bg-white shadow-md rounded-lg p-3 text-center cursor-pointer hover:shadow-lg transition"
                @click="goToNewsDetails(news.name)">
                <!-- Thumbnail -->
                <img v-if="news.thumbnail_img" :src="news.thumbnail_img" alt="Thumbnail"
                    class="mx-auto mb-4 object-contain" loading="lazy" />

                <!-- News Title -->
                <h2 class="font-semibold text-left text-lg mb-2">{{ news.description_heading_1 }}</h2>

                <!-- Preview -->
                <p class="text-left text-sm">{{ news.description_1 }}</p>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router'

const stripHtml = (html) => {
    const tmp = document.createElement("DIV")
    tmp.innerHTML = html
    return tmp.textContent || tmp.innerText || ""
}

export default {
    name: 'News',
    data() {
        return {
            newsList: [],
            isLoading: true
        }
    },
    setup() {
        const router = useRouter()
        const goToNewsDetails = (newsName) => {
            router.push({ name: 'NewsDetails', query: { name: newsName } })
        }
        return { goToNewsDetails }
    },
    mounted() {
        this.fetchNews()
    },
    methods: {
        async fetchNews() {
            try {
                const res = await axios.get('/api/method/education_app.api.education_news.get_news')

                // Directly process the response without artificial delay
                this.newsList = res.data.message.map(news => ({
                    name: news.name,
                    thumbnail_img: news.thumbnail_image,
                    description_heading_1: news.description_heading_1 || "No Title",
                    description_1: stripHtml(news.description_1 || "").substring(0, 100) + "..."
                }))

            } catch (err) {
                console.error('Error fetching news:', err)
            } finally {
                this.isLoading = false
            }
        }
    }
}
</script>

<style scoped>
.cursor-pointer:hover {
    transform: translateY(-2px);
}
</style>
