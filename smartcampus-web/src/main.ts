import { createApp } from "vue";
import PrimeVue from "primevue/config";
import Aura from "@primeuix/themes/aura";
import App from "./App.vue";
import router from "./router";
import HeaderTitle from "./shared/components/HeaderTitle.vue";
import "./styles/main.scss";
import {
  Avatar,
  Button,
  Card,
  Column,
  DataTable,
  Dialog,
  Divider,
  InputText,
  Menu,
  Menubar,
  Skeleton,
  Tag,
} from "primevue";
import { createPinia } from "pinia";

const app = createApp(App);

app.component("Avatar", Avatar);
app.component("Button", Button);
app.component("DataTable", DataTable);
app.component("Dialog", Dialog);
app.component("Divider", Divider);
app.component("Card", Card);
app.component("Column", Column);
app.component("Menu", Menu);
app.component("Menubar", Menubar);
app.component("HeaderTitle", HeaderTitle);
app.component("InputText", InputText);
app.component("Skeleton", Skeleton);
app.component("Tag", Tag);

app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
  ripple: true,
});
app.use(router);
app.use(createPinia());
app.mount("#app");
