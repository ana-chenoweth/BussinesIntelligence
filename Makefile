run:
        sudo docker run -d -p 80:8080 -e WEBUI_AUTH=False -e OPEN_WEBUI_DISABLE_CHAT_TITLE_GENERATION=true -e OPEN_WEBUI_REQUEST_TIMEOUT=600000 -v open-webui>
        sudo docker cp /home/ec2-user/datos/* open-webui:/app/

down:
        sudo docker stop open-webui
        sudo docker rm open-webui
logs:
        sudo docker logs open-webui --tail 100

pull:
        docker pull ghcr.io/open-webui/open-webui:main-slim
