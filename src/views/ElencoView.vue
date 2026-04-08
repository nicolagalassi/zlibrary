<script setup>
import { ref, onMounted, computed } from 'vue'

const circolari = ref([])
const loading = ref(true)
const errorMsg = ref(null)

const selectedApp = ref('HR1')
const apps = ['HR1', 'ERM', 'MD7', 'HRC', 'DWH']

const tipoFiltro = ref('Tutti') // 'Tutti', 'Master', 'UPD'
const searchQuery = ref('')

onMounted(async () => {
  try {
    const res = await fetch('/js/circolari.json')
    if (!res.ok) throw new Error('Network response was not ok')
    circolari.value = await res.json()
  } catch (e) {
    errorMsg.value = "Impossibile recuperare l'archivio. Riprova più tardi."
  } finally {
    loading.value = false
  }
})

// Raggruppa i dati per Anno e filtra internamente
const raggruppatiPerAnno = computed(() => {
  if (!circolari.value.length) return []

  // Applica filtri su App, Tipo e Ricerca Testuale
  const filterData = circolari.value.filter(c => {
    // Filtro Applicativo
    if (!c.url.includes(`/${selectedApp.value}/`)) return false
    
    // Filtro Tipo
    const isMaster = c.versione.includes('_000')
    if (tipoFiltro.value === 'Master' && !isMaster) return false
    if (tipoFiltro.value === 'UPD' && isMaster) return false

    // Filtro Testo
    if (searchQuery.value.trim() !== '') {
      if (!c.versione.toLowerCase().includes(searchQuery.value.toLowerCase())) {
        return false
      }
    }
    
    return true
  })

  // Raggruppa
  const raggruppati = {}
  filterData.forEach(item => {
    let anno = "Sconosciuto"
    const vMatch = item.versione.match(/^(\d{2})\./)
    if (vMatch) anno = `20${vMatch[1]}`

    if (!raggruppati[anno]) raggruppati[anno] = []
    raggruppati[anno].push(item)
  })

  // Ordina versioni internamente decrescente
  Object.keys(raggruppati).forEach(anno => {
    raggruppati[anno].sort((a, b) => {
      const parseV = v => v.versione.split(/[\._]/).map(Number)
      const av = parseV(a)
      const bv = parseV(b)
      return bv[0] - av[0] || bv[1] - av[1] || bv[2] - av[2] || bv[3] - av[3]
    })
  })

  // Array decrescente per anno
  return Object.keys(raggruppati)
    .sort((a, b) => b - a)
    .map(anno => ({
      anno,
      circolari: raggruppati[anno]
    }))
})

function getBadge(versione) {
  if (versione.includes('_000')) {
    return { class: 'bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-200 border-blue-200 dark:border-blue-700', text: 'Master' }
  }
  return { class: 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900/50 dark:text-yellow-200 border-yellow-200 dark:border-yellow-700', text: 'UPD' }
}
</script>

<template>
  <div class="max-w-5xl mx-auto w-full flex-grow py-4 animate-fade-in">
    
    <div class="mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-white mb-2">Archivio Sommari</h1>
      <p class="text-gray-500 dark:text-gray-400">Ricerca e consulta lo storico di tutti gli aggiornamenti.</p>
    </div>

    <!-- Pannello Filtri -->
    <div class="bg-white/80 dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 p-4 sm:p-6 mb-8 flex flex-col gap-6">
      
      <!-- Selettore Applicativo Visivamente Separato -->
      <div>
        <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-3">Scegli l'Applicativo</label>
        <div class="flex flex-wrap gap-2">
          <button
            v-for="app in apps"
            :key="app"
            @click="selectedApp = app"
            :class="[
              'px-6 py-2.5 rounded-lg text-sm font-semibold transition-all duration-200 cursor-pointer border',
              selectedApp === app 
                ? 'bg-blue-600 text-white border-blue-600 shadow-md transform scale-[1.02]' 
                : 'bg-gray-50 dark:bg-gray-900 text-gray-600 dark:text-gray-300 border-gray-200 dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-700 hover:border-gray-300 dark:hover:border-gray-600'
            ]"
          >
            {{ app }}
          </button>
        </div>
      </div>

      <div class="h-px bg-gray-100 dark:bg-gray-700 w-full"></div>

      <!-- Filtri Avanzati -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <!-- Tipo Master/UPD -->
        <div>
          <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-3">Filtro Tipologia</label>
          <div class="flex p-1 bg-gray-100 dark:bg-gray-900 rounded-lg w-fit border border-gray-200 dark:border-gray-700">
            <button
              v-for="tipo in ['Tutti', 'Master', 'UPD']"
              :key="tipo"
              @click="tipoFiltro = tipo"
              :class="[
                'px-4 py-1.5 rounded-md text-sm font-medium transition-colors cursor-pointer',
                tipoFiltro === tipo
                  ? 'bg-white dark:bg-gray-700 text-gray-900 dark:text-white shadow-sm'
                  : 'text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200'
              ]"
            >
              {{ tipo }}
            </button>
          </div>
        </div>

        <!-- Cerca Versione -->
        <div>
          <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-3">Cerca Versione</label>
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-gray-400">
              <i class="fa-solid fa-magnifying-glass"></i>
            </div>
            <input 
              type="text" 
              v-model="searchQuery" 
              placeholder="Es. 25.04..." 
              class="block w-full pl-10 pr-3 py-2 border border-gray-200 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-900 dark:text-white transition-colors"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- Stato di caricamento o errore -->
    <div v-if="loading" class="flex justify-center items-center py-20">
      <div class="animate-spin text-blue-600 text-4xl">
        <i class="fa-solid fa-circle-notch"></i>
      </div>
    </div>

    <div v-else-if="errorMsg" class="bg-red-50 dark:bg-red-900/30 text-red-600 dark:text-red-400 p-6 rounded-xl text-center border border-red-200 dark:border-red-800 shadow-sm">
      <i class="fa-solid fa-triangle-exclamation text-3xl mb-2"></i>
      <p class="font-medium">{{ errorMsg }}</p>
    </div>

    <div v-else-if="!raggruppatiPerAnno.length" class="text-center py-20 bg-white/50 dark:bg-gray-800/50 rounded-xl border border-gray-200 dark:border-gray-700 border-dashed">
      <div class="inline-flex items-center justify-center w-20 h-20 rounded-full bg-gray-100 dark:bg-gray-900 text-gray-400 mb-4 shadow-inner">
        <i class="fa-solid fa-ghost text-3xl"></i>
      </div>
      <h3 class="text-xl font-medium text-gray-800 dark:text-gray-200">Nessun elemento trovato</h3>
      <p class="text-gray-500 mt-1 max-w-sm mx-auto">Non ci sono circolari di tipo {{ tipoFiltro }} relative a {{ selectedApp }} che corrispondono alla tua ricerca.</p>
      <button @click="searchQuery = ''; tipoFiltro = 'Tutti'" class="mt-4 text-blue-600 hover:text-blue-700 font-medium pb-1 border-b border-blue-200 hover:border-blue-500 transition-colors cursor-pointer">Reimposta filtri</button>
    </div>

    <!-- Lista Verticale per Anni -->
    <div v-else class="space-y-10">
      <div v-for="gruppo in raggruppatiPerAnno" :key="gruppo.anno" class="relative">
        
        <div class="flex items-center h-10 mb-2 sticky top-[72px] bg-gray-100 dark:bg-gray-900 z-10 p-2 -mx-2 rounded-lg">
          <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 w-24">
            {{ gruppo.anno }}
          </h2>
          <div class="flex-grow h-px bg-gray-300 dark:bg-gray-700"></div>
          <span class="text-xs font-semibold text-gray-500 ml-4 py-1 px-2 rounded bg-gray-200 dark:bg-gray-800">
            {{ gruppo.circolari.length }} file
          </span>
        </div>

        <ul class="flex flex-col gap-2">
          <li v-for="c in gruppo.circolari" :key="c.versione" 
               class="group bg-white dark:bg-gray-800/80 rounded-lg p-3 sm:p-4 shadow-sm hover:shadow-md border border-gray-200 dark:border-gray-700 transition-all hover:bg-blue-50/50 dark:hover:bg-gray-800 flex items-center justify-between">
            
            <div class="flex items-center gap-4">
              <div class="hidden sm:flex flex-col items-center justify-center bg-gray-100 dark:bg-gray-900 text-gray-400 rounded-md w-12 h-12 border border-gray-200 dark:border-gray-700 group-hover:text-blue-500 group-hover:border-blue-200 transition-colors">
                <i class="fa-regular fa-file-pdf text-2xl"></i>
              </div>
              <div class="flex flex-col">
                <div class="flex items-center gap-2 mb-1">
                  <span class="text-lg font-mono font-medium text-gray-900 dark:text-gray-100">{{ c.versione }}</span>
                  <span :class="['text-[10px] uppercase font-bold px-2 py-0.5 rounded-md border', getBadge(c.versione).class]">
                    {{ getBadge(c.versione).text }}
                  </span>
                </div>
                <span class="text-xs text-gray-500 dark:text-gray-400 font-medium">Aggiornamento {{ selectedApp }}</span>
              </div>
            </div>

            <a :href="c.url" target="_blank" title="Scarica PDF" 
               class="flex items-center gap-2 px-4 py-2 rounded-md bg-blue-100 dark:bg-blue-900/40 text-blue-700 dark:text-blue-300 hover:bg-blue-600 hover:text-white dark:hover:bg-blue-600 dark:hover:text-white transition-all font-medium text-sm group-hover:scale-[1.02]">
              <i class="fa-solid fa-download"></i>
              <span class="hidden sm:inline">Scarica</span>
            </a>

          </li>
        </ul>

      </div>
    </div>

  </div>
</template>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.4s ease-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
