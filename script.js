const themeToggle = document.getElementById('theme-toggle');
const html = document.documentElement;
const lightIcon = document.querySelector('.light-icon');
const darkIcon = document.querySelector('.dark-icon');
const themeText = document.querySelector('.text');


// Funzione per impostare il tema
function setTheme(theme) {
  if (theme === 'dark') {
    html.classList.add('dark');
    lightIcon.style.display = 'none';
    darkIcon.style.display = 'inline-block';
    themeText.textContent = 'Chiaro';
  } else {
    html.classList.remove('dark');
    lightIcon.style.display = 'inline-block';
    darkIcon.style.display = 'none';
    themeText.textContent = 'Scuro';
  }
  localStorage.setItem('theme', theme);
}

// Funzione per inizializzare il tema all'avvio
function initializeTheme() {
  const savedTheme = localStorage.getItem('theme');
  const userPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

  if (savedTheme) {
    setTheme(savedTheme);
  } else if (userPrefersDark) {
    setTheme('dark');
  } else {
    setTheme('light');
  }
}

initializeTheme();

// Event listener per il cambio tema
themeToggle.addEventListener('click', () => {
  const currentTheme = localStorage.getItem('theme');
  setTheme(currentTheme === 'dark' ? 'light' : 'dark');
});


// codice per index.html
async function scaricaCircolare(event) {
  event.preventDefault();
  const versione = document.getElementById('versione').value;
  const errorMessage = document.getElementById('error-message');

  try {
    const response = await fetch('circolari.json');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const circolari = await response.json();
    const circolare = circolari.find(c => c.versione === versione);

    if (circolare) {
      window.location.href = circolare.url;
    } else {
      errorMessage.textContent = 'Circolare non trovata.';
    }
  } catch (error) {
    console.error('Errore nel recupero delle circolari:', error);
    errorMessage.textContent = 'Errore nel recupero delle circolari.';
  }
}

if (document.getElementById('download-form')) {
  document.getElementById('download-form').addEventListener('submit', scaricaCircolare);
}


// codice per elenco.html
async function caricaCircolari() {
  const tableBody = document.getElementById('circolari-table');
  const noDataMessage = document.getElementById('no-data-message');

  try {
    const response = await fetch('circolari.json');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const circolari = await response.json();

    if (circolari.length > 0) {
      circolari.forEach(circolare => {
        const row = tableBody.insertRow();
        const versioneCell = row.insertCell();
        const urlCell = row.insertCell();
        const downloadCell = row.insertCell();

        versioneCell.textContent = circolare.versione;
        urlCell.innerHTML = `<a href="${circolare.url}" target="_blank" class="text-blue-500 hover:text-blue-700">Visualizza</a>`;
        downloadCell.innerHTML = `<a href="${circolare.url}" download class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Scarica</a>`;
      });
    } else {
      noDataMessage.style.display = 'block';
    }
  } catch (error) {
    console.error('Errore nel caricamento delle circolari:', error);
    noDataMessage.textContent = 'Errore nel caricamento delle circolari.';
    noDataMessage.style.display = 'block';
  }
}

if (document.getElementById('circolari-table')) {
  caricaCircolari();
}
