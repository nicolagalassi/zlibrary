<script setup>
import { ref, onMounted, nextTick } from 'vue'

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
    errors.value.versione = 'Campo obbligatorio. Formato: ##.##.##.'
    isValid = false
  } else if (!regexVersione.test(formData.value.versione)) {
    errors.value.versione = 'Formato non valido. Usa ##.##.##.'
    isValid = false
  }

  const regexUpd = /^\d{3}$/
  if (formData.value.upd && !regexUpd.test(formData.value.upd)) {
    errors.value.upd = 'Formato non valido. Usa ### oppure lascia vuoto per 000.'
    isValid = false
  }

  return isValid
}

const submitForm = () => {
  if (!validateForm()) return

  const app = formData.value.applicativo
  const updFinale = formData.value.upd || '000'
  const nomeFile = `${app}_${formData.value.versione}_${updFinale}.pdf`
  const url = `https://www.hrzucchetti.it/infoupdate/${app}/${nomeFile}`

  try {
    window.open(url, '_blank')
  } catch (error) {
    errors.value.submit = "Impossibile aprire la nuova scheda. Verifica le impostazioni del browser."
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
        <h2 class="text-2xl font-bold text-gray-800 dark:text-white">Scarica Sommario</h2>
        <p class="text-sm text-gray-500 dark:text-gray-400 mt-2">
          Componi l'indirizzo per scaricare rapidamente l'aggiornamento desiderato.
        </p>
      </div>

      <form @submit.prevent="submitForm" class="space-y-5" novalidate>
        
        <div>
          <label for="applicativo" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Applicativo</label>
          <div class="relative">
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-gray-400">
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
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-gray-400">
              <i class="fa-solid fa-code-commit"></i>
            </div>
            <input
              type="text"
              id="versione"
              :value="formData.versione"
              @input="handleVersioneInput"
              @keydown="handleKeyDown"
              placeholder="Es. 26.00.00"
              class="block w-full pl-10 pr-3 py-2.5 bg-gray-50 dark:bg-gray-900 border border-gray-300 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-900 dark:text-white transition-colors"
              :class="{ 'border-red-500 focus:ring-red-500 focus:border-red-500': errors.versione }"
              maxlength="8"
              @blur="validateForm"
            />
          </div>
          <p v-if="errors.versione" class="text-red-500 text-xs mt-1 absolute font-medium">{{ errors.versione }}</p>
        </div>

        <div class="pt-2">
          <label for="upd" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Patch / UPD</label>
          <div class="relative">
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-gray-400">
              <i class="fa-solid fa-screwdriver-wrench"></i>
            </div>
            <input
              type="text"
              id="upd"
              v-model="formData.upd"
              placeholder="000"
              class="block w-full pl-10 pr-3 py-2.5 bg-gray-50 dark:bg-gray-900 border border-gray-300 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-900 dark:text-white transition-colors"
              :class="{ 'border-red-500 focus:ring-red-500 focus:border-red-500': errors.upd }"
              maxlength="3"
              @blur="validateForm"
            />
          </div>
          <p v-if="errors.upd" class="text-red-500 text-xs mt-1 absolute font-medium">{{ errors.upd }}</p>
        </div>

        <div class="pt-4">
          <button type="submit" class="w-full flex justify-center items-center gap-2 py-3 px-4 border border-transparent rounded-xl shadow-sm text-sm font-semibold text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all hover:scale-[1.02] active:scale-95 cursor-pointer">
            <i class="fa-solid fa-download"></i>
            Scarica PDF
          </button>
          <p v-if="errors.submit" class="text-red-500 text-center text-sm font-medium mt-3">{{ errors.submit }}</p>
        </div>
      </form>
    </div>
  </div>
</template>
