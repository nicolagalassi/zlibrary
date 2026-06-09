<script setup>
</script>

<template>
  <div class="max-w-4xl mx-auto w-full flex-grow py-8 animate-fade-in">
    <div class="bg-white/90 dark:bg-gray-800/90 backdrop-blur-md rounded-2xl shadow-lg p-8 md:p-12 border border-gray-100 dark:border-gray-700">
      <div class="text-center mb-10">
        <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-blue-100 dark:bg-blue-900/50 text-blue-600 mb-6 shadow-inner" aria-hidden="true">
          <i class="fa-solid fa-shield-halved text-3xl"></i>
        </div>
        <h1 class="text-3xl font-bold text-gray-800 dark:text-white mb-3">Privacy Policy</h1>
        <p class="text-gray-500 dark:text-gray-400">Come trattiamo i tuoi dati in ZuLibrary</p>
      </div>

      <div class="prose dark:prose-invert max-w-none text-gray-600 dark:text-gray-300 space-y-8">
        <section>
          <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 border-b border-gray-200 dark:border-gray-700 pb-2 mb-4">Informazioni Generali</h2>
          <p>
            ZuLibrary è uno strumento non ufficiale creato per facilitare il download e l'archiviazione dei sommari e delle circolari,
            senza alcuno scopo di lucro e senza nessuna affiliazione diretta con Zucchetti S.p.a.
          </p>
          <p>
            La tua privacy è importante per noi. Questa pagina descrive le tipologie di dati che raccogliamo durante la navigazione e
            come li utilizziamo.
          </p>
        </section>

        <section>
          <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 border-b border-gray-200 dark:border-gray-700 pb-2 mb-4">Dati Raccolti</h2>
          <p>
            Al fine di offrirti un'esperienza di navigazione fluida, salviamo localmente sul tuo browser:
          </p>
          <ul class="list-disc pl-5 mt-2 space-y-1">
            <li><strong>Preferenze Tema:</strong> Salviamo nel <code>localStorage</code> del tuo dispositivo il tema scelto (Chiaro o Scuro) per mantenerlo attivo durante la navigazione.</li>
            <li><strong>Stato Banner:</strong> Sempre nel <code>localStorage</code>, memorizziamo se hai chiuso l'ultimo banner per le novità, così da non dartene fastidio nuovamente.</li>
          </ul>
          <div class="mt-4 bg-gray-50 dark:bg-gray-900/50 p-4 rounded-lg border border-gray-200 dark:border-gray-700 text-sm">
            <i class="fa-solid fa-cookie-bite mr-2 text-yellow-500" aria-hidden="true"></i> Nessun cookie di profilazione personale viene installato.
          </div>
        </section>

        <section>
          <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 border-b border-gray-200 dark:border-gray-700 pb-2 mb-4">Tracciamento Analitico</h2>
          <p>
            Sfruttiamo <a href="https://umami.is" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:rounded">Umami Analytics</a> (hostato sul cloud) per raccogliere dati <strong>completamente anonimizzati</strong> riguardo le visualizzazioni di pagina della nostra piattaforma.
          </p>
          <p>
            Questo sistema rispetta il GDPR, non raccoglie dati personali identificabili e non usa cookie intrusivi. Ci serve esclusivamente
            per capire quanta affluenza ha lo strumento e mantenerlo nel tempo in virtù del suo utilizzo.
          </p>
        </section>

        <section>
          <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 border-b border-gray-200 dark:border-gray-700 pb-2 mb-4">Link a Servizi di Terze Parti</h2>
          <p>
            La nostra piattaforma reindirizza per lo scaricamento sui sistemi ufficiali di Zucchetti. Tali siti hanno le proprie policy sulla Privacy
            di cui noi non possiamo farci garanti. Non intercettiamo nessun contenuto da quelle direzioni.
          </p>
        </section>

      </div>
      
      <div class="mt-12 pt-6 border-t border-gray-200 dark:border-gray-700 text-center">
        <p class="text-sm text-gray-500">Ultimo aggiornamento: Aprile 2026</p>
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
@media (prefers-reduced-motion: reduce) {
  .animate-fade-in {
    animation: none;
  }
}
</style>
