<template>
    <div class="container bg-gray-100 py-10 px-5">

        <!-- Loading State -->
        <div v-if="isLoading" class="text-center py-20 text-gray-500 text-lg">
            Loading blogs...
        </div>

        <!-- No Blogs -->
        <div v-else-if="blogs.length === 0" class="text-center py-20 text-gray-500 text-lg">
            No blogs available at the moment.
        </div>

        <!-- Blogs Grid -->
        <div v-else class="max-w-7xl mx-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
            <div v-for="blog in blogs" :key="blog.name"
                class="bg-white shadow-md rounded-lg p-3 text-center cursor-pointer hover:shadow-lg transition"
                @click="goToBlogDetails(blog.name)">
                <!-- Thumbnail Image -->
                <img v-if="blog.thumbnail_img" :src="blog.thumbnail_img" alt="Blog Thumbnail"
                    class="mx-auto mb-4 object-contain" loading="lazy" width="300" height="200" />

                <!-- Blog Title -->
                <h2 class="font-semibold text-left text-lg mb-2">{{ blog.description_heading_1 }}</h2>

                <!-- Blog Preview -->
                <p class="text-left text-sm">{{ blog.description_1 }}...</p>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router'

const stripHtml = (html) => {
    if (!html) return ''
    const tmp = document.createElement("DIV")
    tmp.innerHTML = html
    return tmp.textContent || tmp.innerText || ""
}

export default {
    name: 'Blogs',
    data() {
        return {
            blogs: [],
            isLoading: true
        }
    },

    setup() {
        const router = useRouter()
        const goToBlogDetails = (blogName) => {
            router.push({ name: 'BlogDetails', query: { name: blogName } })
        }
        return { goToBlogDetails }
    },

    mounted() {
        this.fetchBlogs()
    },

    methods: {
        async fetchBlogs() {
            this.isLoading = true
            try {
                const res = await axios.get('/api/method/education_app.api.education_blog.get_blogs')
                const blogsData = res.data.message || []

                this.blogs = blogsData.map(blog => ({
                    name: blog.name,
                    thumbnail_img: blog.thumbnail_image || '',
                    description_heading_1: blog.description_heading_1,
                    description_1: stripHtml(blog.description_1).substring(0, 100)
                }))
            } catch (err) {
                console.error('Error fetching blogs:', err)
                this.blogs = []
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
