#!/usr/bin/env python
# qwen_cli.py
# =========================================
# 与 Qwen3-8B（或其他 Qwen 系列）进行命令行交互 / Command-line interaction
# -----------------------------------------
# 用法举例 / examples：
#   python qwen_cli.py                 # default ./Qwen3-8B
#   python qwen_cli.py --model qwen/Qwen1.5-7B-Chat --max-tokens 2048
# Input exit / quit or Ctrl-C to quit
# =========================================

import argparse
import torch
from modelscope import AutoModelForCausalLM, AutoTokenizer

# ---------- CLI parameter ----------
parser = argparse.ArgumentParser(description="Qwen CLI chat")
parser.add_argument("--model", default="./Qwen3-8B",
                    help="model path")
parser.add_argument("--max-tokens", type=int, default=4096,
                    help="max output token")
parser.add_argument("--temperature", type=float, default=0.7,
                    help="sampling temperature")
parser.add_argument("--top-p", type=float, default=0.9,
                    help=" nucleus sampling top-p")
args = parser.parse_args()

# ---------- 加载模型 / loading ----------
print(f"[INFO] Loading {args.model} …")
tokenizer = AutoTokenizer.from_pretrained(args.model)
model = AutoModelForCausalLM.from_pretrained(
    args.model,
    torch_dtype="auto",
    device_map="auto"
)
model.eval()
print("[INFO] 模型加载完成，开始对话！/ Model loaded—let’s start chatting! (type 'quit' to quit)\n")

# ---------- 对话历史 / conversation ----------
messages = []   # 形如 [{"role":"user","content":...}, {"role":"assistant","content":...}]

# ---------- 主循环 / main loop ----------
try:
    while True:
        user_input = input("You：").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye！")
            break
        if not user_input:
            continue

        # 追加用户消息 / more messages
        messages.append({"role": "user", "content": user_input})

        # 构造提示词（使用 Qwen 官方 chat template）/ built prompt
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=True,   # deep thinking
        )

        # 转张量，放到同一设备 / transfer tensor, assign device
        model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

        # 生成 / generating
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=args.max_tokens,
            temperature=args.temperature,
            top_p=args.top_p,
            do_sample=True
        )

        # 取新生成的部分 / input generating
        resp_ids = generated_ids[0][len(model_inputs.input_ids[0]):]
        response = tokenizer.decode(resp_ids, skip_special_tokens=True).strip()

        # 打印并存历史 / print
        print(f"Qwen：{response}\n")
        messages.append({"role": "assistant", "content": response})

        # 可选：避免显存持续增长 / optional
        torch.cuda.empty_cache()

except KeyboardInterrupt:
    print("\n[INFO] quited。")
