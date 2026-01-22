import subprocess
import os

def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"SUCCESS: {command}")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"ERROR while executing: {command}")
        print(e.stderr)


def docker_cleanup():
    commands = [
        "docker container prune -f",
        "docker image prune -f",
        "docker volume prune -f",
        "docker network prune -f"
    ]

    for cmd in commands:
        run_command(cmd)


if __name__ == "__main__":

    if os.system("docker --version > /dev/null 2>&1") != 0:
        print("Docker is not installed or not running.")
    else:
        print("Starting Docker Cleanup Automation...\n")
        docker_cleanup()
        print("\nDocker cleanup completed successfully.")
