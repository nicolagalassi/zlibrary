<script setup>
import { ref, nextTick, onMounted } from 'vue'

const formData = ref({
  applicativo: 'HR1',
  versione: '',
  upd: ''
})

const errors = ref({
  versione: '',
  upd: '',
  submit: ''
})

const isOpening = ref(false)
const versioniRecenti = ref([])

onMounted(() => {
  try {
    const saved = localStorage.getItem('versioniRecenti')
    if (saved) versioniRecenti.value = JSON.parse(saved)
  } catch {
    versioniRecenti.value = []
  }
})

function salvaVersioneRecente(versione) {
  const lista = [versione, ...versioniRecenti.value.filter(v => v !== versione)].slice(0, 4)
  versioniRecenti.value = lista
  localStorage.setItem('versioniRecenti', JSON.stringify(lista))
}

function selezionaVersioneRecente(versione) {
  formData.value.versione = versione
  errors.value.versione = ''
  nextTick(() => document.getElementById('upd')?.focus())
}

// Gestione Maschera Versione Ripensata
const handleVersioneInput = (e) => {
  const el = e.target
  const oldVal = el.value
  const cursor = el.selectionStart
  
  // 1. Estrai solo i numeri
  let digits = oldVal.replace(/\D/g, '').slice(0, 6)
  
  // 2. Formatta come ##.##.##
  let newVal = ''
  for (let i = 0; i < digits.length; i++) {
    if (i === 2 || i === 4) newVal += '.'
    newVal += digits[i]
  }

  // 3. Calcola nuova posizione cursore
  // Se abbiamo aggiunto un punto "dietro" al cursore, dobbiamo spostarlo avanti
  let newCursor = cursor
  const addedDots = newVal.split('.').length - oldVal.split('.').length
  if (addedDots > 0) {
    // Se il cursore era esattamente dopo dove è apparso un punto
    if ((cursor === 3 && digits.length >= 3) || (cursor === 6 && digits.length >= 5)) {
      newCursor++
    }
  }

  formData.value.versione = newVal
  
  // Sincronizza il valore visualizzato e ripristina il cursore nel prossimo task
  nextTick(() => {
    el.value = newVal
    el.setSelectionRange(newCursor, newCursor)
  })

  // Validazione in tempo reale se completo
  if (newVal.length === 8) {
    validateForm()
  }
}

// Gestione cancellazione intelligente (Backspace su punti)
const handleKeyDown = (e) => {
  if (e.key === 'Backspace') {
    const el = e.target
    const cursor = el.selectionStart
    const val = el.value
    
    // Se il cursore è subito dopo un punto (pos 3 o 6), cancella anche il numero precedente
    if (cursor === 3 || cursor === 6) {
      e.preventDefault()
      const digits = val.replace(/\D/g, '')
      // Se cursor è 3, siamo dopo "##.", vogliamo togliere la seconda cifra
      // Se cursor è 6, siamo dopo "##.##.", vogliamo togliere la quarta cifra
      let indexToRemove = (cursor === 3) ? 1 : 3
      let newDigits = digits.split('')
      newDigits.splice(indexToRemove, 1)
      
      let newVal = ''
      const d = newDigits.join('')
      for (let i = 0; i < d.length; i++) {
        if (i === 2 || i === 4) newVal += '.'
        newVal += d[i]
      }
      
      formData.value.versione = newVal
      nextTick(() => {
        el.value = newVal
        const pos = (cursor === 3) ? 2 : 5
        el.setSelectionRange(pos, pos)
      })
    }
  }
}

const validateForm = () => {
  let isValid = true
  errors.value = { versione: '', upd: '', submit: '' }

  const regexVersione = /^\d{2}\.\d{2}\.\d{2}$/
  if (!formData.value.versione) {
    errors.value.versione = 'Inserisci la versione nel formato ##.##.## (es. 25.04.00).'
    isValid = false
  } else if (!regexVersione.test(formData.value.versione)) {
    errors.value.versione = 'Formato non riconosciuto. Usa ##.##.## (es. 25.04.00).'
    isValid = false
  }

  const regexUpd = /^\d{3}$/
  if (formData.value.upd && !regexUpd.test(formData.value.upd)) {
    errors.value.upd = 'Usa tre cifre (es. 001). Lascia vuoto per scaricare la versione base.'
    isValid = false
  }

  return isValid
}

const submitForm = () => {
  if (!validateForm()) return

  isOpening.value = true
  const app = formData.value.applicativo
  const updFinale = formData.value.upd || '000'
  const nomeFile = `${app}_${formData.value.versione}_${updFinale}.pdf`
  const url = `https://www.hrzucchetti.it/infoupdate/${app}/${nomeFile}`

  try {
    window.open(url, '_blank', 'noopener,noreferrer')
    salvaVersioneRecente(formData.value.versione)
  } catch (error) {
    errors.value.submit = "Impossibile aprire la nuova scheda. Verifica le impostazioni del browser."
  } finally {
    setTimeout(() => { isOpening.value = false }, 2000)
  }
}
</script>

<template>
  <div class="flex-grow flex items-center justify-center">
    <div class="bg-white/80 dark:bg-gray-800/80 backdrop-blur-md shadow-xl rounded-2xl p-8 w-full max-w-md border border-gray-100 dark:border-gray-700">
      
      <div class="text-center mb-8">
        <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-blue-100 dark:bg-blue-900/50 text-blue-500 mb-4 shadow-inner">
          <i class="fa-solid fa-cloud-arrow-down text-2xl"></i>
        </div>
        <h1 class="text-2xl font-bold text-gray-800 dark:text-white text-balance">Scarica Sommario</h1>
        <p class="text-base text-gray-500 dark:text-gray-400 mt-2">
          Seleziona applicativo, versione e patch: il PDF si apre direttamente dal server Zucchetti.
        </p>
      </div>

      <form @submit.prevent="submitForm" class="space-y-5" novalidate>
        
        <div>
          <label for="applicativo" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Applicativo</label>
          <div class="relative">
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-gray-400" aria-hidden="true">
              <i class="fa-solid fa-box-open"></i>
            </div>
            <select
              id="applicativo"
              v-model="formData.applicativo"
              class="block w-full pl-10 pr-3 py-2.5 bg-gray-50 dark:bg-gray-900 border border-gray-300 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-900 dark:text-white transition-colors"
            >
              <option value="HR1">Paghe Infinity</option>
              <option value="ERM">Portale HR</option>
              <option value="MD7">CU770</option>
              <option value="HRC">HR Comunicazioni</option>
              <option value="DWH">HR Analytics</option>
            </select>
          </div>
        </div>

        <div>
          <label for="versione" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Versione Master</label>
          <div class="relative">
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-gray-400" aria-hidden="true">
              <i class="fa-solid fa-code-commit"></i>
            </div>
            <input
              type="text"
              id="versione"
              :value="formData.versione"
              @input="handleVersioneInput"
              @keydown="handleKeyDown"
              placeholder="Es. 26.00.00"
              inputmode="numeric"
              autocomplete="off"
              class="block w-full pl-10 pr-3 py-2.5 bg-gray-50 dark:bg-gray-900 border border-gray-300 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-900 dark:text-white placeholder:text-gray-600 dark:placeholder:text-gray-400 transition-colors"
              :class="{ 'border-red-500 focus:ring-red-500 focus:border-red-500': errors.versione }"
              maxlength="8"
              @blur="validateForm"
            />
          </div>
          <div class="min-h-[1.25rem] mt-1" aria-live="polite">
            <p v-if="errors.versione" class="text-red-600 text-xs font-medium">{{ errors.versione }}</p>
          </div>
          <div v-if="versioniRecenti.length" class="flex items-center gap-2 flex-wrap mt-1">
            <span class="text-xs text-gray-500 dark:text-gray-400 shrink-0">Recenti:</span>
            <button
              v-for="v in versioniRecenti"
              :key="v"
              type="button"
              @click="selezionaVersioneRecente(v)"
              class="font-mono text-xs px-2 py-1.5 rounded border border-gray-200 dark:border-gray-600 bg-gray-50 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:border-gray-300 dark:hover:border-gray-500 transition-colors cursor-pointer focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500"
            >
              {{ v }}
            </button>
          </div>
        </div>

        <div>
          <label for="upd" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
            Patch / UPD <span class="text-gray-500 dark:text-gray-400 font-normal">(opzionale, default 000)</span>
          </label>
          <div class="relative">
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-gray-400" aria-hidden="true">
              <i class="fa-solid fa-screwdriver-wrench"></i>
            </div>
            <input
              type="text"
              id="upd"
              v-model="formData.upd"
              placeholder="000"
              inputmode="numeric"
              autocomplete="off"
              class="block w-full pl-10 pr-3 py-2.5 bg-gray-50 dark:bg-gray-900 border border-gray-300 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-900 dark:text-white placeholder:text-gray-600 dark:placeholder:text-gray-400 transition-colors"
              :class="{ 'border-red-500 focus:ring-red-500 focus:border-red-500': errors.upd }"
              maxlength="3"
              @blur="validateForm"
            />
          </div>
          <div class="min-h-[1.25rem] mt-1" aria-live="polite">
            <p v-if="errors.upd" class="text-red-600 text-xs font-medium">{{ errors.upd }}</p>
          </div>
        </div>

        <div class="pt-2">
          <button
            type="submit"
            :disabled="isOpening"
            class="w-full flex justify-center items-center gap-2 py-3 px-4 border border-transparent rounded-xl shadow-sm text-sm font-semibold text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all hover:scale-[1.02] active:scale-95 cursor-pointer disabled:opacity-75 disabled:cursor-default disabled:hover:scale-100"
          >
            <i :class="isOpening ? 'fa-solid fa-circle-notch animate-spin' : 'fa-solid fa-download'" aria-hidden="true"></i>
            {{ isOpening ? 'Apertura in corso...' : 'Scarica PDF' }}
          </button>
          <p v-if="errors.submit" role="alert" class="text-red-600 text-center text-sm font-medium mt-3">{{ errors.submit }}</p>
          <p class="text-xs text-gray-600 dark:text-gray-400 text-center mt-2">Se il PDF non si apre, la versione potrebbe non essere disponibile sul server Zucchetti.</p>
        </div>
      </form>
    </div>
  </div>
</template>
