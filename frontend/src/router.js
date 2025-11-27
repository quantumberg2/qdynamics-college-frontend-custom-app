import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },
  {
    path: '/about',
    name: 'Aboutus',
    component: () => import('@/pages/Aboutus.vue'),
  },
  {
    path: '/AcademicsCourses',
    name: 'AcademicsCourses',
    component: () => import('@/pages/AcademicsCourses.vue'),
  },
  {
    path: '/Announcements',
    name: 'Announcements',
    component: () => import('@/pages/Announcements.vue'),
  },
  {
    path: '/AnnouncementList',
    name: 'AnnouncementList',
    component: () => import('@/pages/AnnouncementList.vue'),
  },
  {
    path: '/Blogs',
    name: 'Blogs',
    component: () => import('@/pages/Blogs.vue'),
  },
  {
    path: '/BlogDetails',
    name: 'BlogDetails',
    component: () => import('@/pages/BlogDetails.vue'),
  },
  {
    path: '/News',
    name: 'News',
    component: () => import('@/pages/News.vue'),
  },
  {
    path: '/NewsDetails',
    name: 'NewsDetails',
    component: () => import('@/pages/NewsDetails.vue'),
  },
  {
    path: '/contact',
    name: 'Contactus',
    component: () => import('@/pages/Contactus.vue'),
  },
  {
    path: '/admission',
    name: 'Admission',
    component: () => import('@/pages/Admission.vue'),
  },
  {
    path: '/gallery',
    name: 'Gallery',
    component: () => import('@/pages/Gallery.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/'),
  routes,
})

export default router
