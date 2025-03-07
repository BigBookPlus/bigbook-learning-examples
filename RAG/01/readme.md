# create container

```bash
mkdir /home/x/models
mkdir /home/x/projects/qwen_rag_demo
docker pull pytorch/pytorch:2.1.0-cuda11.8-cudnn8-devel
docker run -it --runtime nvidia --ipc host --gpus all -v /home/x/models:/workspace/models -v /home/x/projects/qwen_rag_demo:/workspace/qwen_rag_demo --name qwen_rag pytorch/pytorch:2.1.0-cuda11.8-cudnn8-devel
```

# download models

```bash
cd /workspace/models
pip install -U huggingface_hub
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download --resume-download Qwen/Qwen2.5-7B-Instruct-GPTQ-Int4 --local-dir  Qwen2.5-7B-Instruct-GPTQ-Int4   --local-dir-use-symlinks False
huggingface-cli download --resume-download BAAI/bge-m3 --local-dir  bge-m3   --local-dir-use-symlinks False
```
# install vim in container

```bash
apt update
apt install vim
mkdir document
cd document/
```
then we can create a python file qwen_rag.py to run the qwen demo for llama index.

# fix zh_CN locale for docker container

```bash
apt install -y locales fonts-wqy-zenhei
locale-gen zh_CN.UTF-8
echo "LANG=zh_CN.UTF-8" >> /etc/default/locale
echo "LANGUAGE=zh_CN:zh" >> /etc/default/locale
echo "LC_ALL=zh_CN.UTF-8" >> /etc/default/locale
export LANG=zh_CN.UTF-8
export LANGUAGE=zh_CN:zh
export LC_ALL=zh_CN.UTF-8
locale
```

# install llama index

```bash
pip install llama-index
pip install llama-index-readers-web
pip install llama-index-llms-huggingface
pip install llama-index-embeddings-huggingface
pip install optimum
pip install auto-gptq
pip install docx2txt
export HF_ENDPOINT=https://hf-mirror.com
```

# run

```bash
python qwen_rag.py
```

