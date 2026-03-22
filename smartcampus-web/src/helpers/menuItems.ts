import routes from "../router/routes";

const items = routes.map((route) => {
  if (route.children && route.children.length > 0) {
    return {
      label: route.name as string,
      items: route.children.map((child) => ({
        label: child.name as string,
        route: route.path + "/" + child.path,
      })),
    };
  } else {
    return {
      label: route.name as string,
      route: route.path,
    };
  }
});

export default items;
