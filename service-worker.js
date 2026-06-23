// British TV Hub Service Worker
// Caches visited pages so they load instantly and work offline

const CACHE_NAME = 'bth-cache-v1';

// Core pages to pre-cache on install
const CORE_ASSETS = [
  '/',
  '/index.html',
  '/shows.html',
  '/streaming.html',
  '/cozy.html',
  '/meet-tilly.html'
];

// Install: pre-cache core pages
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(CORE_ASSETS).catch(() => {
        // If some assets fail, don't block install
        return Promise.resolve();
      });
    })
  );
  self.skipWaiting();
});

// Activate: clean up old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

// Fetch: network-first, falling back to cache (good for a content site that updates)
self.addEventListener('fetch', (event) => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  // Skip cross-origin requests (e.g., Chatbase, fonts, affiliate links)
  if (!event.request.url.startsWith(self.location.origin)) return;

  event.respondWith(
    fetch(event.request)
      .then((response) => {
        // Cache a copy of the fresh response
        const responseClone = response.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, responseClone);
        });
        return response;
      })
      .catch(() => {
        // Offline: serve from cache if available
        return caches.match(event.request);
      })
  );
});
