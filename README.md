# BopomoBERT

### requirements: 
- transformers
- torch

### model (download before finetuning)
bert-base-chinese (huggingface): https://drive.google.com/file/d/1r1XkgZv6lCL7R9ZWpQ2c8dyNhtv0W4ft/view?usp=sharing

pretrained model (on aishell): 
- bert: https://drive.google.com/file/d/1MzIP0BXfHsIloOoN8hqNLQtW3qm1kTuh/view?usp=sharing
- zhuyin embedding layer: https://drive.google.com/file/d/1kosMyMPSC13Sm_eBiuTEr-b_ebIcVjzk/view?usp=sharing

### data format

see data-aishell-train.txt

Line-by-line, each line contains one sentence. All words are in `中:ㄓㄨㄥ- 文:ㄨㄣˊ` format.
