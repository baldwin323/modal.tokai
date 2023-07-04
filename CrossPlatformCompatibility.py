import os
import platform
import docker

class CrossPlatformCompatibility:

    def __init__(self, app):
        self.app = app
        self.development_team = ["dev1", "dev2", "dev3"]
        self.docker_client = docker.from_env()

    def check_os_compatibility(self):
        os_name = platform.system()
        if os_name in self.app.supported_os:
            print(f"The app is compatible with the current OS: {os_name}")
        else:
            print(f"The app is not compatible with the current OS: {os_name}")

    def create_docker_container(self):
        try:
            container = self.docker_client.containers.run(self.app.docker_image, detach=True)
            print(f"Docker container created with ID: {container.short_id}")
        except docker.errors.ContainerError as e:
            print(f"Error in creating Docker container: {str(e)}")

    def check_app_compatibility(self):
        self.check_os_compatibility()
        self.create_docker_container()

if __name__ == "__main__":
    app = App()  # Assuming App is a class defined in another file with attributes supported_os and docker_image
    cross_platform_compatibility = CrossPlatformCompatibility(app)
    cross_platform_compatibility.check_app_compatibility()