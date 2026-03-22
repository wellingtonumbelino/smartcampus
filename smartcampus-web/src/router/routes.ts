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
      pageTitle: "Dashboard",
    },
  },
  {
    path: "/rooms",
    name: "Rooms",
    component: lazyLoad("List", "Rooms"),
    meta: {
      pageTitle: "Rooms",
    },
  },
  {
    path: "/devices",
    name: "Devices",
    component: lazyLoad("List", "Devices"),
    meta: {
      pageTitle: "Devices",
    },
  },
];

export default routes;
