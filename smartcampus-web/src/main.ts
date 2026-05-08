import { createApp } from "vue";
import PrimeVue from "primevue/config";
import Aura from "@primeuix/themes/aura";
import App from "./App.vue";
import router from "./router";
import HeaderTitle from "./ui/HeaderTitle.vue";
import "./assets/main.scss";
import {
  Button,
  Card,
  Column,
  DataTable,
  Dialog,
  Divider,
  InputText,
} from "primevue";
import { createPinia } from "pinia";

const app = createApp(App);

app.component("Button", Button);
app.component("DataTable", DataTable);
app.component("Dialog", Dialog);
app.component("Divider", Divider);
app.component("Card", Card);
app.component("Column", Column);
app.component("HeaderTitle", HeaderTitle);
app.component("InputText", InputText);

app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
  ripple: true,
});
app.use(router);
app.use(createPinia());
app.mount("#app");
