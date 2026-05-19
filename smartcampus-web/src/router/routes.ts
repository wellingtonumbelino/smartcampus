import type { RouteRecordRaw } from "vue-router";

function lazyLoad(view: string, path: string) {
  return () => import(`@/views/${path}/${view}.vue`);
}

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "Dashboard",
    component: lazyLoad("Dashboard", "Dashboard"),
    meta: {
      icon: "pi pi-objects-column",
    },
  },
  {
    path: "/rooms",
    name: "Rooms",
    component: lazyLoad("List", "Rooms"),
    meta: {
      icon: "pi pi-building",
    },
  },
  {
    path: "/devices",
    name: "Devices",
    component: lazyLoad("List", "Devices"),
    meta: {
      icon: "pi pi-wifi",
    },
  },
];

export default routes;
