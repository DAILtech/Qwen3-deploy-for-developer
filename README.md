# Qwen3-deploy-for-developer
Guidance of Qwen3 local-deploying for developer, and Interactive CLI chat script.  

Display (Take Qwen3-8B as an example, <think> mode) :  
![image](https://github.com/user-attachments/assets/0d7d10b6-612d-4ae7-9926-f256b38ccdfd)


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

**3. Install requirements**
  ```bash
  pip install transformers==4.51.0 accelerate==0.24.0 peft==0.4.0 bitsandbytes==0.41.1 protobuf==3.20.3
  pip install gradio==3.50.2 scipy tqdm
  pip install protobuf==3.20.3
  ```
**4. Download the model**
  
  Clone repository
  ```bash
  git clone https://github.com/DAILtech/Qwen3-deploy-for-developer
  ```

  Download the model, take Qwen3-8B as an example:  
  
  ```bash
  cd ./Qwen3-deploy-for-developer/Qwen3
  mkdir ./Qwen3-8B
  modelscope download --model Qwen/Qwen3-8B --local_dir ./Qwen3-8B
  ```

**5. Using CLI to interact with the model**  

  default parameters:  
  model path: ./Qwen3-8B  
  max output tokens: 4096  
  temperature: 0.7  
  top-p: 0.9    
  
  example:  
  ```bash
  # default:
  python CLI.py                 # default ./Qwen3-8B
  # customization:
  python CLI.py --model qwen/Qwen1.5-7B-Chat --max-tokens 2048
  ```
Type `quit` or `ctrl-c` to quit.
  
  
  
