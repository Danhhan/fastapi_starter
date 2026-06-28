**Run database migrations** (if you add models):
**if you want to generate migration:**
```bash

alembic revision --autogenerate
```

**if you want to upgrade:**

```bash
alembic upgrade head
```

**if you want to downgrade:**

```bash
alembic downgrade -1
```