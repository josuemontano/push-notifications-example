// The install handler takes care of precaching the resources we always need.
self.addEventListener("install", (event) => {
  console.warn("installed!", event);
});

// The activate handler takes care of cleaning up old caches.
self.addEventListener("activate", (event) => {
  console.warn("activated!", event);
});

self.addEventListener("push", function (event) {
  var data = event.data.json();

  var options = {
    body: data.body,
    vibrate: [100, 50, 100],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: "2",
    },
    actions: [
      { action: "explore", title: "Explore this new world" },
      { action: "close", title: "Close" },
    ],
  };

  event.waitUntil(self.registration.showNotification(data.title, options));
});

self.addEventListener(
  "notificationclick",
  function (event) {
    if (event.action === "close") {
      event.notification.close();
    } else if (event.action === "explore") {
      clients.openWindow("https://magicbell.io");
    }
  },
  false
);
