import { computed } from "vue";
import { useRouter } from "vue-router";
import type { SideMenuItemType } from "../types/layout.types";

export function useNavigation() {
  const router = useRouter();

  const sideMenuItems = computed<SideMenuItemType[]>(() => {
    const routes = router.options.routes;

    return routes.map((route) => {
      // if (route.children && route.children.length > 0) {
      //   return {
      //     label: (route.name ?? "") as string,
      //     items: route.children?.map((child) => ({
      //       label: (child.name ?? "") as string,
      //       route: `${route.path}/${child.path}`.replace(/\/+/g, "/"),
      //       icon: child.meta?.icon as string,
      //     })),
      //   };
      // }

      return {
        label: (route.name ?? "") as string,
        route: route.path,
        icon: route.meta?.icon as string,
      };
    });
  });

  return { sideMenuItems };
}
