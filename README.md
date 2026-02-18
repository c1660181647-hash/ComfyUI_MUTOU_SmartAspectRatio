# 🧩 ComfyUI MUTOU Smart Aspect Ratio

A smart custom node for ComfyUI that automatically detects the aspect ratio of an input image and matches it to the closest ratio from a user-defined list.
一个用于 ComfyUI 的智能节点，自动检测输入图像的宽高比，并匹配用户定义列表中最接近的比例名称。

**Note**: This node outputs the **original** dimensions of the image. It does NOT resize or crop the image.
**注意**：本节点输出图像的**原始**尺寸。它不会缩放或裁切图像。

## ✨ Features (功能特点)

* **Smart Matching**: Calculates the current aspect ratio and finds the closest match from your list (e.g., identifies a 1000x1000 image as "1:1").
    **智能匹配**：计算当前比例并从列表中找出最接近的匹配项（例如：将 1000x1000 的图像识别为 "1:1"）。
* **Original Data**: Outputs strictly the **original** width and height (INT & STRING), perfect for logic control without altering pixels.
    **原始数据**：严格输出**原始**宽高（整数和文本），适合在不修改像素的情况下进行逻辑控制。
* **Flexible Input**: Supports unlimited custom ratios (e.g., `21:9, 3:4, 1.85:1`).
    **灵活输入**：支持无限自定义比例列表。

## 🛠️ Installation (安装方法)

1.  Go to your ComfyUI `custom_nodes` directory.
    进入 ComfyUI 的 `custom_nodes` 目录。
2.  Clone this repository:
    克隆本仓库：
    ```bash
    git clone https://github.com/c1660181647-hash/ComfyUI_MUTOU_SmartAspectRatio.git
    ```
3.  Restart ComfyUI.
    重启 ComfyUI。

## 🚀 Usage (使用方法)

1.  **Search Node**: Double click on canvas and search for `MUTOU`.
    **搜索节点**：双击画布搜索 `MUTOU`。
2.  **Connect Image**: Connect your image to the `image` input.
    **连接图片**：将图片连入 `image` 输入点。
3.  **Set Ratios**: Edit the `ratio_list` text widget (supports multiline).
    **设置比例**：编辑 `ratio_list` 文本框（支持多行输入）。
4.  **Outputs**:
    **输出端口**：
    * `width_int` / `height_int`: Original dimensions (INT).
    * `ratio_name`: The matched ratio text (e.g., "16:9").
    * `wh_text`: Original resolution string (e.g., "1024x768").

## 👨‍💻 About

Developed by **MUTOU**.

Designed for Easy-Use ComfyUI workflows.
