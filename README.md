## Getting started

1. Start the `web` service (and any others) in the background:
    ```bash
    docker-compose up -d
    ```
   
2. Import data to database:
    ```bash
    docker exec -it web python manage.py shell
   
   from world import load
   load.run()
   exit()
    ```
   
3. Create superuser:
    ```bash
    docker exec -it web python manage.py createsuperuser
    ```