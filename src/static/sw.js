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
    icon: "images/example.png",
    vibrate: [100, 50, 100],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: "2",
    },
    actions: [
      {
        action: "explore",
        title: "Explore this new world",
        icon: "images/checkmark.png",
      },
      { action: "close", title: "Close", icon: "images/xmark.png" },
    ],
  };

  e.waitUntil(self.registration.showNotification(data.title, options));
});
