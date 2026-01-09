import { createApp } from 'vue';
import { createPinia } from 'pinia';
import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';
import App from './App.vue';
import router from './router';
import HeaderTitle from './ui/HeaderTitle.vue';
import './assets/sass/main.scss';
import { Button, Column, DataTable, Dialog, InputText } from 'primevue';

const app = createApp(App);

app.component('Button', Button);
app.component('DataTable', DataTable);
app.component('Dialog', Dialog);
app.component('Column', Column);
app.component('HeaderTitle', HeaderTitle);
app.component('InputText', InputText);

app.use(createPinia());
app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
  ripple: true,
});
app.use(router);

app.mount('#app');
