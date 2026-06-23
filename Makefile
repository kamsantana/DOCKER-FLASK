deploy:
	@echo "==> Desplegando stack en Docker Swarm..."
	docker stack deploy -c stack.yml borrar_kevin