import routes from '@/router/routes';

const items = routes.map((route) => {
  if (route.children && route.children.length > 0) {
    return {
      label: route.name,
      items: route.children.map((child) => ({
        label: child.name,
        icon: child.icon ?? '',
        route: route.path + '/' + child.path,
      })),
    };
  } else {
    return {
      label: route.name,
      route: route.path,
      icon: route.icon ?? '',
    };
  }
});

export default items;
