<template>
  <section class="bg-gray-100 py-12 px-6">
    <div class="max-w-5xl mx-auto bg-white shadow-xl rounded-xl p-8">
      <div class="text-center mb-10">
        <h2 class="text-4xl font-bold text-[#20b486]">CONTACT US</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Left: Contact Form -->
        <div>
          <h2 class="text-gray-600 mb-5 text-lg font-medium">Leave us a message</h2>

          <form @submit.prevent="submitForm" class="space-y-5">
            <div class="flex flex-col sm:flex-row gap-4">
              <input v-model="form.first_name" type="text" placeholder="First Name"
                class="w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-green-500" required />
              <input v-model="form.last_name" type="text" placeholder="Last Name"
                class="w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-green-500" required />
            </div>

            <input v-model="form.email_address" type="email" placeholder="Email Address"
              class="w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-green-500" required />

            <textarea v-model="form.message" rows="4" placeholder="Your Message"
              class="w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-green-500" required></textarea>

            <button type="submit" :disabled="isLoading"
              class="w-full bg-[#20b486] text-white font-semibold py-2 rounded-lg hover:bg-green-700 transition disabled:opacity-50">
              <span v-if="isLoading">Sending...</span>
              <span v-else>Send</span>
            </button>
          </form>

          <!-- Success / Error Message -->
          <p v-if="statusMessage" :class="statusClass" class="mt-4 font-medium">
            {{ statusMessage }}
          </p>
        </div>

        <!-- Right: Address + Map -->
        <div class="space-y-6">
          <div class="flex items-start space-x-3">
            <span class="text-green-600 text-xl">📍</span>
            <p class="text-gray-700">
              <strong>Weekend UX</strong><br>
              B 37/3 Ground Floor Double Story,<br>
              Ramesh Nagar, Near Raja Garden Chowk,<br>
              Delhi: 110015
            </p>
          </div>

          <div class="flex items-center space-x-3">
            <span class="text-green-600 text-xl">📞</span>
            <p class="text-gray-700">+91 9599272754</p>
          </div>

          <div class="flex items-center space-x-3">
            <span class="text-green-600 text-xl">✉️</span>
            <p class="text-gray-700">hello@info.com.ng</p>
          </div>

          <div class="h-32 md:h-40">
            <iframe class="w-full h-full rounded-lg"
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3503.480802961251!2d77.12345!3d28.654321!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390d035f0!2sRamesh%20Nagar%2C%20Delhi!5e0!3m2!1sen!2sin!4v1234567890"
              style="border:0;" allowfullscreen="" loading="lazy"></iframe>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        first_name: "",
        last_name: "",
        email_address: "",
        message: "",
      },
      isLoading: false,
      statusMessage: "",
      statusClass: "",
    };
  },
  methods: {
    async submitForm() {
      this.isLoading = true;
      this.statusMessage = "";
      this.statusClass = "";

      try {
        const res = await axios.post(
          "/api/method/education_app.api.contact.send_contact_message",
          this.form
        );

        let data = res.data;

        // If backend sends wrapped response in "message" or string, parse it
        if (typeof data === "string") {
          data = JSON.parse(data);
        }

        // Check if backend returned "message"
        if (data.message && data.message.status === "success") {
          this.statusMessage = data.message.message;  // inner message text
          this.statusClass = "text-green-600";
          this.form = {
            first_name: "",
            last_name: "",
            email_address: "",
            message: "",
          };
        } else {
          this.statusMessage =
            (data.message && data.message.message) || "Something went wrong!";
          this.statusClass = "text-red-600";
        }

        // Hide message after 3 seconds
        setTimeout(() => {
          this.statusMessage = "";
          this.statusClass = "";
        }, 3000);

      } catch (err) {
        console.error(err);
        this.statusMessage = "Error sending message. Try again later!";
        this.statusClass = "text-red-600";

        // Hide message after 3 seconds
        setTimeout(() => {
          this.statusMessage = "";
          this.statusClass = "";
        }, 3000);

      } finally {
        this.isLoading = false;
      }
    },
  },
};
</script>

<style scoped>
button:hover:enabled {
  cursor: pointer;
}
</style>
