import { createApp } from 'vue';
import App from './App.vue';
import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';
import Button from "primevue/button";
import AutoComplete from 'primevue/autocomplete';      


const app = createApp(App);

app.use(PrimeVue, {
    theme: {
        preset: Aura,
        options: {
            prefix: 'p',
            darkModeSelector: 'system',
            cssLayer: false
    }
}
}
);
app.component('Button', Button);
app.component("AutoComplete", AutoComplete);
app.mount('#app');
