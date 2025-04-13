// script.js

// Tema scuro/chiaro
const toggle = document.getElementById('theme-toggle');
const html = document.documentElement;
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') html.classList.add('dark');

if (toggle) {
  toggle.addEventListener('click', () => {
    html.classList.toggle('dark');
    localStorage.setItem('theme', html.classList.contains('dark') ? 'dark' : 'light');
  });
}

// Funzione per scaricare circolare
function scaricaCircolare(e) {
  e.preventDefault();
  const versione = document.getElementById("versione").value.trim();
  if (versione) {
    const url = `https://www.hrzucchetti.it/infoupdate/HR1/HR1_${versione}.pdf`;
    window.open(url, "_blank");
  }
}

// Elenco circolari
if (document.getElementById("circolari-table")) {
  fetch('circolari.json')
    .then(response => response.json())
    .then(data => {
      data.sort((a, b) => {
        const parseVersion = v => v.versione.split(/[\._]/).map(Number);
        const [a1,a2,a3,a4] = parseVersion(a);
        const [b1,b2,b3,b4] = parseVersion(b);
        return b1 - a1 || b2 - a2 || b3 - a3 || b4 - a4;
      }).reverse();

      const table = document.getElementById('circolari-table');
      data.forEach(c => {
        const patch = c.versione.split('_')[1];
        const badge = patch === '000'
          ? `<span class="ml-2 inline-block bg-blue-200 text-blue-800 text-xs px-2 py-0.5 rounded">Master</span>`
          : `<span class="ml-2 inline-block bg-yellow-200 text-yellow-800 text-xs px-2 py-0.5 rounded">UPD</span>`;

        const row = document.createElement('tr');
        row.innerHTML = `
          <td class="py-2 px-4 font-mono">${c.versione}${badge}</td>
          <td class="py-2 px-4">
            <a href="${c.url}" class="text-blue-600 hover:underline" target="_blank">Scarica PDF</a>
          </td>
        `;
        table.appendChild(row);
      });
    })
    .catch(err => {
      console.error("Errore nel caricamento delle circolari:", err);
    });
}
