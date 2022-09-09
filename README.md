## Getting started

1. Add/Create .env file:

2. Start the `web` and `db`  services:
    ```bash
    docker-compose up -d
    ```
   
3. Import data to database:
    ```bash
    docker exec -it web python manage.py shell
   
   from world import load
   load.run()
   exit()
    ```
   
4. Create superuser:
    ```bash
    docker exec -it web python manage.py createsuperuser
    ```
   
5. The service is available in <http://127.0.0.1:8000>.
