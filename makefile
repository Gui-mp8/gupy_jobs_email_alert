
build:
	@docker login -u $(DOCKER_USERNAME) -p $(DOCKER_PASSWORD)
	docker build -t gupy-jobs-alert .

run: build
	docker run gupy-jobs-alert
