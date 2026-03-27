# 🩺 Medical QLoRA Fine-Tuning with Unsloth

A medical chatbot built by fine-tuning **Llama 3.2-3B-Instruct** on clinical Q&A data using **QLoRA (4-bit quantization)** and **Unsloth** — all running on Google Colab (Free T4 GPU).

---

## 📋 Project Overview

This project fine-tunes a large language model (LLM) on a medical dataset to create a domain-specific medical assistant that can answer clinical questions accurately.

| Detail | Value |
|--------|-------|
| **Base Model** | Llama 3.2-3B-Instruct |
| **Fine-tuning Method** | QLoRA (4-bit) |
| **Framework** | Unsloth + HuggingFace TRL |
| **Dataset** | medalpaca/medical_meadow_medqa |
| **Platform** | Google Colab (T4 GPU) |
| **VRAM Used** | ~6.5 GB (out of 14.6 GB) |
| **Trainable Parameters** | 24,313,856 (0.75% of total) |
| **Training Loss** | 4.79 → 0.26 |

---

## 📁 Project Structure

```
medical-qlora-finetuning/
│
├── medical_chatbot.ipynb        # Main Colab notebook (all cells)
├── medical_qlora_adapter/       # Saved LoRA adapter weights
│   ├── adapter_config.json
│   ├── adapter_model.safetensors
│   └── tokenizer files
├── README.md                    # This file
└── requirements.txt             # All dependencies
```

---

## 🚀 How to Run

### Step 1 — Open in Google Colab
- Go to [colab.research.google.com](https://colab.research.google.com)
- Upload `medical_chatbot.ipynb`
- Set runtime: **Runtime → Change runtime type → T4 GPU**

### Step 2 — Run Cells in Order

| Cell | Description |
|------|-------------|
| Cell 1 | Install Unsloth and all dependencies |
| Cell 2 | Load Llama 3.2-3B-Instruct in 4-bit |
| Cell 3 | Attach LoRA adapter (r=16) |
| Cell 4 | Load and format medical dataset |
| Cell 5 | Train the model (3 epochs, ~20 mins) |
| Cell 6 | Save fine-tuned adapter |
| Cell 7 | Run medical chatbot inference |

---

## 🧠 Model Architecture

```
Base Model (Frozen, 4-bit quantized)
    └── LoRA Adapters (Trainable)
            ├── q_proj, k_proj, v_proj, o_proj  (Attention)
            └── gate_proj, up_proj, down_proj    (FFN)

LoRA Config:
    - Rank (r)        : 16
    - Alpha           : 16
    - Dropout         : 0
    - Target modules  : 7 projection layers
```

---

## 💬 Sample Chatbot Output

**Q: What are the early signs of a heart attack?**
> The early signs of a heart attack include chest pain or discomfort, shortness of breath, pain in the arms/back/neck/jaw, cold sweats, lightheadedness, fatigue, nausea, rapid heartbeat, and palpitations...

**Q: What is the difference between ibuprofen and paracetamol?**
> Ibuprofen is an NSAID that inhibits prostaglandin production and has anti-inflammatory effects. Paracetamol is a non-opioid analgesic that works in the brain without anti-inflammatory properties...

---

## ⚙️ Training Configuration

```python
TrainingArguments(
    per_device_train_batch_size = 2,
    gradient_accumulation_steps = 4,   # Effective batch = 8
    num_train_epochs            = 3,
    learning_rate               = 2e-4,
    optim                       = "adamw_8bit",
    lr_scheduler_type           = "cosine",
    warmup_steps                = 50,
)
```

---

## 📊 Training Results

| Metric | Value |
|--------|-------|
| Total Steps | 750 |
| Starting Loss | 4.79 |
| Final Loss | 0.26 |
| Training Time | ~18 minutes |
| GPU | Tesla T4 |
| Peak VRAM | ~6.5 GB |

---

## 🔧 Key Technologies

- **Unsloth** — 2x faster fine-tuning with custom CUDA kernels
- **QLoRA** — 4-bit quantized Low-Rank Adaptation
- **PEFT** — Parameter Efficient Fine-Tuning
- **TRL SFTTrainer** — Supervised Fine-Tuning Trainer
- **BitsAndBytes** — 4-bit NF4 quantization
- **HuggingFace Transformers** — Model loading and inference

---

## ⚠️ Important Notes

- This chatbot is for **educational purposes only**
- Always consult a qualified physician for medical advice
- Model responses should not be used for actual diagnosis or treatment

---

## 👤 Author

Submitted as part of AI/ML coursework — Medical Fine-Tuning with QLoRA using Unsloth
