import torch

class MUTOU_SmartAspectRatio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "ratio_list": ("STRING", {
                    "multiline": True, 
                    "default": "1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 21:9",
                    "placeholder": "Input format: 16:9, 4:3..."
                }),
            },
        }

    # ============================================================================
    # 输出定义：全部基于原图真实数据 (绝不修改)
    # 1. width_int:  原图宽度 (INT)
    # 2. height_int: 原图高度 (INT)
    # 3. ratio_name: 匹配到的比例名称 (如 "9:16")
    # 4. width_text: 原图宽度 (STRING)
    # 5. height_text: 原图高度 (STRING)
    # 6. wh_text:    原图尺寸组合文本 (如 "630x1155")
    # ============================================================================
    RETURN_TYPES = ("INT", "INT", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("width_int", "height_int", "ratio_name", "width_text", "height_text", "wh_text")
    FUNCTION = "calculate_ratio"
    CATEGORY = "MUTOU/Image"

    def calculate_ratio(self, image, ratio_list):
        # 1. 获取【原图】真实尺寸
        # ComfyUI 图片格式: [Batch, Height, Width, Channel]
        try:
            orig_h = image.shape[1]
            orig_w = image.shape[2]
        except:
            # 极端情况兜底
            orig_h, orig_w = 512, 512

        # 计算当前图片的实际比例 (仅用于去列表里比对，不用于修改尺寸)
        current_ratio = orig_w / orig_h

        # 2. 解析用户输入的比例列表
        ratios = []
        # 清洗分隔符：把换行、中文逗号都转为英文逗号
        clean_list = ratio_list.replace("\n", ",").replace("，", ",")
        
        for item in clean_list.split(","):
            item = item.strip()
            if not item: continue
            
            try:
                # 兼容中文冒号
                temp_item = item.replace("：", ":")
                if ":" in temp_item:
                    w_str, h_str = temp_item.split(":", 1)
                    w_val = float(w_str)
                    h_val = float(h_str)
                    
                    if h_val != 0:
                        ratios.append({
                            "val": w_val / h_val, # 用于计算的比例值
                            "text": item          # 用于输出的原始文本
                        })
            except ValueError:
                continue

        # 3. 匹配逻辑 (只找名字)
        if not ratios:
            match_text = "Original"
        else:
            # 找差值最小的那个比例
            best = min(ratios, key=lambda x: abs(x["val"] - current_ratio))
            match_text = best["text"]

        # 4. 输出结果 (严格输出原图尺寸)
        final_w_int = int(orig_w)
        final_h_int = int(orig_h)
        
        return (
            final_w_int,        # 原图宽
            final_h_int,        # 原图高
            match_text,         # 匹配到的比例名
            str(final_w_int),   # 原图宽(文本)
            str(final_h_int),   # 原图高(文本)
            f"{final_w_int}x{final_h_int}" # 组合文本
        )