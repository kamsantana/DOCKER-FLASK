deploy:
	@echo "Iniciando despliegue..."
	docker compose pull
	docker compose up -d --remove-orphans
	@echo "¡Despliegue completado con éxito!"