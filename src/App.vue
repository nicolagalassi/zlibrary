<script setup>
import { ref, onMounted, computed, watchEffect } from 'vue'
import { RouterView, RouterLink } from 'vue-router'

const isDark = ref(false)
const showBanner = ref(true)

const toggleTheme = () => {
  isDark.value = !isDark.value
  if (isDark.value) {
    document.documentElement.classList.add('dark')
    localStorage.setItem('theme', 'dark')
  } else {
    document.documentElement.classList.remove('dark')
    localStorage.setItem('theme', 'light')
  }
}

onMounted(() => {
  const savedTheme = localStorage.getItem('theme')
  if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    isDark.value = true
    document.documentElement.classList.add('dark')
  }

  const dismissed = localStorage.getItem('dismissedBannerVersion')
  const currentBannerVer = '0.8.0'
  if (dismissed === currentBannerVer) {
    showBanner.value = false
  } else {
    localStorage.setItem('currentBannerVer', currentBannerVer)
  }
})

const closeBanner = () => {
  showBanner.value = false
  localStorage.setItem('dismissedBannerVersion', localStorage.getItem('currentBannerVer'))
}

watchEffect(() => {
  document.documentElement.style.setProperty('--sticky-top', showBanner.value ? '116px' : '72px')
})
</script>

<template>
  <!-- Header -->
  <header class="bg-white/80 dark:bg-gray-800/80 backdrop-blur-md shadow p-4 sticky top-0 z-10 transition-colors duration-300">
    <div class="max-w-4xl mx-auto flex justify-between items-center">
      <RouterLink to="/" class="flex items-center gap-2 text-2xl font-bold text-gray-700 dark:text-gray-200 hover:scale-105 transition-transform focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:rounded-lg">
        <i class="fa-solid fa-book text-blue-500" aria-hidden="true"></i>
        ZuLibrary
      </RouterLink>
      <div class="flex items-center gap-4">
        <RouterLink to="/" aria-label="Home" title="Home" class="flex items-center justify-center w-10 h-10 text-gray-600 dark:text-gray-300 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500" active-class="bg-blue-100 dark:bg-gray-700 text-blue-600 dark:text-blue-400">
          <i class="fa-solid fa-house-chimney" aria-hidden="true"></i>
        </RouterLink>
        <RouterLink to="/elenco" aria-label="Archivio Sommari" title="Archivio" class="flex items-center justify-center w-10 h-10 text-gray-600 dark:text-gray-300 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500" active-class="bg-blue-100 dark:bg-gray-700 text-blue-600 dark:text-blue-400">
          <i class="fa-solid fa-table-list" aria-hidden="true"></i>
        </RouterLink>
        <button @click="toggleTheme" title="Cambia Tema" aria-label="Cambia tema" class="flex items-center justify-center w-10 h-10 text-gray-600 dark:text-gray-300 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-all hover:rotate-12 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500">
          <i v-if="!isDark" class="fa-solid fa-lightbulb" aria-hidden="true"></i>
          <i v-else class="fa-solid fa-moon" aria-hidden="true"></i>
        </button>
      </div>
    </div>
  </header>

  <!-- Banner -->
  <transition name="slide-fade">
    <div v-if="showBanner" class="bg-gradient-to-r from-blue-100 to-cyan-100 dark:from-blue-900/50 dark:to-cyan-900/50 border-b border-blue-200 dark:border-blue-800 p-3 relative text-sm text-gray-800 dark:text-gray-200 shadow-sm backdrop-blur-sm">
      <div class="max-w-4xl mx-auto flex justify-between items-center gap-4">
        <p class="flex-grow text-center">
          <i class="fa-solid fa-heart mr-2 text-red-500" aria-hidden="true"></i>
          Ti piace ZuLibrary? <a href="https://ko-fi.com/galax95" target="_blank" rel="noopener noreferrer" class="underline font-bold hover:text-blue-700 dark:hover:text-blue-300 transition-colors">Supporta lo sviluppo con una piccola donazione!</a>
        </p>
        <button @click="closeBanner" title="Chiudi" aria-label="Chiudi banner" class="text-gray-500 hover:text-gray-800 hover:bg-gray-200/50 dark:hover:bg-gray-700/50 rounded-full p-1.5 transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500">
          <i class="fa-solid fa-times" aria-hidden="true"></i>
        </button>
      </div>
    </div>
  </transition>

  <!-- Main Content -->
  <main class="flex-grow flex flex-col p-4">
    <RouterView v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </RouterView>
  </main>

  <!-- Footer -->
  <footer class="bg-gray-200/50 dark:bg-gray-800/50 backdrop-blur-sm text-gray-600 dark:text-gray-400 text-sm border-t border-gray-300 dark:border-gray-700 transition-colors duration-300 mt-auto">
    <div class="max-w-4xl mx-auto py-6 px-4 text-center space-y-4">
      <nav class="flex justify-center gap-x-6 gap-y-2 flex-wrap" aria-label="Navigazione piè di pagina">
        <RouterLink to="/" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors hover:underline">Home</RouterLink>
        <RouterLink to="/privacy" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors hover:underline">Privacy Policy</RouterLink>
        <a href="https://ko-fi.com/galax95" target="_blank" rel="noopener noreferrer" class="flex items-center gap-1.5 text-orange-600 dark:text-orange-400 font-bold hover:scale-105 transition-transform focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-500 focus-visible:rounded">
          <i class="fa-solid fa-mug-hot" aria-hidden="true"></i> Offrimi un caffè
        </a>
      </nav>
      <p class="text-xs text-gray-600 dark:text-gray-400 px-4">ZuLibrary è uno strumento non ufficiale e non è affiliato in alcun modo con Zucchetti S.p.a.</p>
      <p class="text-xs font-mono">
        &copy; {{ new Date().getFullYear() }} ZuLibrary <span class="mx-1 opacity-50">|</span> v0.8.0
      </p>
    </div>
  </footer>
</template>

<style>
/* Page transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}

/* Banner translation */
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}
.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(-20px);
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {
  .fade-enter-active,
  .fade-leave-active,
  .slide-fade-enter-active,
  .slide-fade-leave-active {
    transition: opacity 0.1s ease;
  }
  .fade-enter-from,
  .fade-leave-to,
  .slide-fade-enter-from,
  .slide-fade-leave-to {
    transform: none;
  }
}
</style>
