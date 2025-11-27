<template>
    <div>
        <div class="container bg-gray-100 py-10 px-5">
            <div class="bg-white shadow-md rounded-lg p-3 w-full text-center">

                <!-- Loading Screen -->
                <div v-if="isLoading" class="flex justify-center items-center py-10">
                    <span class="text-gray-600 text-lg animate-pulse">Loading Announcements...</span>
                </div>

                <!-- No Announcements -->
                <div v-else-if="announcements.length === 0" class="py-6 text-gray-500">
                    No announcements available at the moment.
                </div>

                <!-- Dynamic Announcements -->
                <div v-else v-for="announcement in announcements" :key="announcement.name || announcement.id"
                    class="font-semibold text-left text-lg mb-2 flex justify-between w-full">
                    <div>
                        <div class="mb-2">
                            {{ announcement.announcement_title }}
                        </div>
                        <div class="text-gray-600 font-normal">
                            {{ announcement.announcement_contant }}
                        </div>
                    </div>
                    <div class="text-gray-600 font-normal whitespace-nowrap">
                        {{ formatDate(announcement.announcement_created_date) }}
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

// Create formatter once (not inside method to avoid re-instantiating)
const dateFormatter = new Intl.DateTimeFormat("en-GB", {
    day: "2-digit",
    month: "short",
    year: "numeric",
});

export default {
    data() {
        return {
            announcements: [],
            isLoading: true,
        };
    },
    mounted() {
        this.fetchAnnouncements();
    },
    methods: {
        async fetchAnnouncements() {
            this.isLoading = true;
            try {
                const res = await axios.get(
                    "/api/method/education_app.api.education_announcement.get_announcements"
                );
                this.announcements = res.data.message || [];
            } catch (err) {
                console.error("Error fetching announcements:", err);
                this.announcements = [];
            } finally {
                this.isLoading = false;
            }
        },
        formatDate(dateStr) {
            if (!dateStr) return "";
            return dateFormatter.format(new Date(dateStr));
        },
    },
};
</script>
