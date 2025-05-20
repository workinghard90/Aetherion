// apps/aetherion-mobile/App.tsx
import { registerRootComponent } from 'expo';
import EmanationViewer from './screens/EmanationViewer'; // or your main screen

registerRootComponent(EmanationViewer);

import 'dotenv/config';

export default {
  expo: {
    name: "AetherionAI",
    slug: "aetherionai",
    extra: {
      apiUrl: process.env.REACT_NATIVE_API_URL
    }
  }
};
