const CACHE_NAME = 'hare-app-v1';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './main.py',
  './pyscript.json',
  './manifest.json',
  './hare_relax.JPG',
  './zorza.jpg',
  './ncprime-mid-nights-sound-291477.mp3 
];

// Instalacja Service Workera i zapisanie plików w pamięci podręcznej (Cache)
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('Zając chowa pliki do cache...');
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
});

// Aktywacja i sprzątanie starych wersji cache
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
      );
    })
  );
});

// Przechwytywanie zapytań - jeśli jesteś offline, bierz pliki z cache
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );

});
