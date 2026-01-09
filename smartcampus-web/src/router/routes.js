function lazyLoad(view, path = '') {
  return path ? () => import(`@/views/${path}/${view}.vue`) : () => import(`@/views/${view}.vue`);
}

const routes = [
  {
    path: '/',
    name: 'Home',
    icon: 'pi pi-home',
    component: lazyLoad('HomeView'),
    meta: {
      pageTitle: 'Home',
    },
  },
  {
    path: '/rooms',
    name: 'Rooms',
    children: [
      {
        path: 'all',
        name: 'List of Rooms',
        icon: 'pi pi-building',
        component: lazyLoad('ListRoomsView', 'Rooms'),
        meta: {
          pageTitle: 'Rooms',
        },
      },
    ],
  },
  {
    path: '/devices',
    name: 'Devices',
    children: [
      {
        path: 'all',
        name: 'List of Devices',
        icon: 'pi pi-wifi',
        component: lazyLoad('ListDevicesView', 'Devices'),
        meta: {
          pageTitle: 'Devices',
        },
      },
      {
        path: 'groups',
        name: 'List of Device Groups',
        icon: 'pi pi-th-large',
        component: lazyLoad('ListDevicesGroupView', 'DevicesGroup'),
        meta: {
          pageTitle: 'Device Groups',
        },
      },
    ],
  },
];

export default routes;
