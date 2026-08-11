import type { RouteRecordRaw } from "vue-router";

function lazyLoad(view: string, path: string) {
  return () => import(`@/modules/${path}/views/${view}.vue`);
}

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "Dashboard",
    component: lazyLoad("Dashboard", "dashboard"),
    meta: {
      icon: "pi pi-objects-column",
    },
  },
  // {
  //   path: "/rooms",
  //   name: "Rooms",
  //   component: lazyLoad("List", "Rooms"),
  //   meta: {
  //     icon: "pi pi-building",
  //   },
  // },
  {
    path: "/devices",
    name: "Devices",
    component: lazyLoad("Devices", "devices"),
    meta: {
      icon: "pi pi-microchip",
    },
  },
];

export default routes;
