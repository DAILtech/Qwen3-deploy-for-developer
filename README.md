# Qwen3-deploy-for-developer
Guidance of Qwen3 local-deploying for developer, and Interactive CLI chat script.

**1. Create a new environment (strong recommanded):**
  ```bash
  conda create -n qwen python=3.10 -y
  # reset terminal
  source ~/.bashrc
  # activate llava
  conda activate qwen
  ```

**2. Install modelscope**
  ```bash
  pip install modelscope
  ```

**Install requirements**
  ```bash
  pip install transformers==4.51.0 accelerate==0.24.0 peft==0.4.0 bitsandbytes==0.41.1 protobuf==3.20.3
  pip install gradio==3.50.2 scipy tqdm
  pip install protobuf==3.20.3
  ```
**Create Qwen3 folders and download the model**
  
  Take Qwen3-8B as an example
  
  ```bash
  mkdir ./Qwen3
  cd ./Qwen3
  mkdir ./Qwen3-8B
  modelscope download -- Qwen/Qwen3-8B --local_dir ./Qwen3-8B
  ```

**Using CLI to interact with the model**
  default parameters:  
  model path: ./Qwen3-8B  
  max output tokens: 4096  
  temperature: 0.7  
  top-p: 0.9    
  example:  
  ```bash
  # default:
  python qwen_cli.py                 # default ./Qwen3-8B
  # customization
  python qwen_cli.py --model qwen/Qwen1.5-7B-Chat --max-tokens 2048
  ```
Type `quit` or `ctrl-c` to quit.
  
  
  
