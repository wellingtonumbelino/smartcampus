import type { RouteRecordRaw } from "vue-router";

function lazyLoad(path: string, view: string) {
  return () => import(`@/views/${path}/${view}.vue`);
}

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "Dashboard",
    component: lazyLoad("Dashboard", "DashboardView"),
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
  // {
  //   path: "/devices",
  //   name: "Devices",
  //   component: lazyLoad("Devices", "devices"),
  //   meta: {
  //     icon: "pi pi-microchip",
  //   },
  // },
];

export default routes;
