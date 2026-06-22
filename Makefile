deploy:
	@echo "Iniciando el despliegue de la aplicación..."
	docker compose pull
	docker compose up -d --remove-orphans
	@echo "¡Despliegue completado con éxito!"