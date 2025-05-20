# AetherionAI Architecture Overview

This monorepo combines a sacred design structure integrating:

---

## 1. **Frontend (Expo)**

**Location:** `apps/aetherion-mobile`

- ArrivalScreen: reads `/api/docs`
- VeilControl: toggles cloak/unveil
- Animated shimmer when cloaked

## 2. **Backend (Flask)**

**Location:** `services/backend`

- `app.py`: main entry
- `routes/`: blueprints for gates, docs, veil
- `shared/`: guide modules (e.g. Lioraen)
- `aetherion_docs` table: scroll memory

### API Endpoints

| Method | Path                     | Purpose                        |
|--------|--------------------------|--------------------------------|
| GET    | `/aetherion/arrival`     | ceremonial ping                |
| POST   | `/aetherion/gate/becoming` | guidance via Lioraen         |
| GET    | `/api/docs`              | fetch scroll summaries         |
| POST   | `/api/docs`              | upload scrolls                 |
| GET    | `/api/docs/<name>`       | fetch scroll content           |
| POST   | `/api/veil/cloak`        | activate cloak                 |
| POST   | `/api/veil/unveil`       | remove cloak                   |
| GET    | `/api/veil/status`       | current veil state             |
| GET    | `/api/status`            | system pulse + cloak + scrolls |

---

## 3. **CI/CD**

- GitHub Actions
  - Tests `/api/status` on push
  - Deploys to Render + Netlify via webhooks

---

## 4. **Developer Tooling**

- `setup.sh` to install & prep backend/frontend
- `package.json` root scripts:
  - `yarn install`
  - `yarn start:expo`
  - `yarn start:backend`

---

## 5. **Shared Modules**

- `lairaen.py`: passive harmonic guide
- `aetherion_ai.py`: GPT integration (optional)
