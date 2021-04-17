# ardigital

### How to launch<br>
In the cloned `ardigital` project:
1. Run `docker-compose up`, all services must be in `Up` state.
2. `docker-compose exec ardigital-server python backend/manage.py migrate`
3. `docker-compose exec ardigital-server python backend/manage.py createsuperuser` (optional)
