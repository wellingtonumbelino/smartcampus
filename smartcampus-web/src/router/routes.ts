import type { RouteRecordRaw } from "vue-router";

function lazyLoad(view: string, path: string) {
  return () => import(`@/views/${path}/${view}.vue`);
}

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "Home",
    component: lazyLoad("Home", "Home"),
    meta: {
      pageTitle: "Home",
    },
  },
  {
    path: "/rooms",
    name: "Rooms",
    children: [
      {
        path: "all",
        name: "List of Rooms",
        component: lazyLoad("List", "Rooms"),
        meta: {
          pageTitle: "Rooms",
        },
      },
    ],
  },
  {
    path: "/devices",
    name: "Devices",
    children: [
      {
        path: "all",
        name: "List of Devices",
        component: lazyLoad("List", "Devices"),
        meta: {
          pageTitle: "Devices",
        },
      },
      // {
      //   path: "groups",
      //   name: "List of Device Groups",
      //   component: lazyLoad("ListDevicesGroupView", "DevicesGroup"),
      //   meta: {
      //     pageTitle: "Device Groups",
      //   },
      // },
    ],
  },
];

export default routes;
