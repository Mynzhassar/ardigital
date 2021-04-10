# ardigital

### How to launch<br>
In the cloned `ardigital` project:
1. Run `docker-compose up`, all services must be in `Up` state.
2. `docker-compose exec ardigital-server python backend/manage.py migrate`
3. `docker-compose exec ardigital-server python backend/manage.py createsuperuser` (optional)


`localhost:80/admin` for admin panel<br>
`127.0.0.1:8080` for client side
