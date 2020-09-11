## Scene Classifier: A Streamlit Web Application
Containerized web app (deployable on Kubernetes) that takes as input an image [JPG or PNG] and produces a classification output [Buildings, Forest, Glaciers, Mountains, Sea, Street]

---

### To run container:
Requirement: Docker
1. Pull container from Docker Hub:
    >docker pull guolin1/sceneclassifier:1.1.4
2. Run container:
    > docker run -p 8501:8501 guolin1/sceneclassifier:1.1.4
3. Access web app in browser:
    > URL: localhost:8501

---

### To deploy on kubernetes:
1. Pull repository using Git:
    > git clone https://github.com/guolin1/WebApp_Kubernetes.git
2. Deploy (after CD into SceneClassifier Directory):
    > kubectl create -f deployment.yml -f service.yml
3. Obtain Access Url:
    > kubectl get services
    - URL is EXTERNAL-IP for sceneclassifier-service
---
