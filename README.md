# RAG 知識庫 AI 問答平台（進階版）

一個整合 RAG（Retrieval-Augmented Generation）技術的地端 AI 問答平台，支援 Google 試算表作為知識庫來源，具備完整的知識庫管理介面。

## 🌟 功能特色

### 核心功能
- ✅ **RAG 知識庫系統**：使用向量相似度搜尋提供精確回答
- ✅ **最新 AI 模型**：
  - OpenAI：GPT-4o、GPT-4 Turbo、O1
  - Google：Gemini 2.0 Flash、Gemini 1.5 Pro
- ✅ **Google 試算表整合**：可將 Google Sheets 作為知識庫來源
- ✅ **GAS API 部署**：提供完整的 Google Apps Script API

### 知識庫管理
- 📝 **表格式編輯**：直覺的表格介面新增/編輯/刪除知識
- 📤 **批次匯入**：支援 CSV/Excel 檔案批次上傳
- 📥 **資料匯出**：可匯出為 CSV 格式
- 🔄 **試算表同步**：一鍵同步 Google 試算表資料
- 🔍 **智慧搜尋**：基於向量相似度的語意搜尋

### 進階功能
- 🎯 **來源引用**：AI 回答時顯示知識庫來源與相似度
- 📊 **統計儀表板**：顯示知識庫筆數、最後更新時間
- 🎨 **現代化介面**：漂亮的 UI 設計，支援響應式佈局
- 💾 **本地儲存**：知識庫自動儲存為 JSON 檔案
- 🤖 **多角色切換**：內建多種 AI 助理角色

## 📋 系統需求

- Python 3.8 或更高版本
- 網路連線（用於呼叫 AI API）
- 支援的瀏覽器（Chrome、Firefox、Edge 等）
- （可選）Google 帳號（用於 Google Sheets 整合）

## 🚀 快速開始

### 0. 建置虛擬環境（首次執行必做）

#### Windows
```bash
# 進入專案資料夾
cd D:\AI_聊天互動平台\進階

# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境
venv\Scripts\activate

# 確認虛擬環境已啟動（提示符號前面會出現 (venv)）
```

#### macOS / Linux
```bash
# 進入專案資料夾
cd ~/AI_聊天互動平台/進階

# 建立虛擬環境
python3 -m venv venv

# 啟動虛擬環境
source venv/bin/activate

# 確認虛擬環境已啟動（提示符號前面會出現 (venv)）
```

**重要提醒：**
- ✅ 首次執行時，請務必先建立虛擬環境
- ✅ 每次啟動專案前，都要先啟動虛擬環境
- ✅ 虛擬環境可以避免套件版本衝突，確保專案穩定運行
- ✅ 看到 `(venv)` 表示虛擬環境已正確啟動

### 1. 安裝依賴套件

**在啟動虛擬環境後**，安裝所有需要的套件：

```bash
pip install -r requirements.txt
```

**注意**：
- 首次安裝 `sentence-transformers` 會自動下載 embedding 模型（約 400MB），請確保網路連線穩定
- 已將 `openai` 套件升級到 2.x 版本，支援最新的 GPT-5、GPT-4.1、GPT-4o 模型
- 如果安裝失敗，請先升級 pip：`python -m pip install --upgrade pip`

### 2. 啟動伺服器

```bash
python app.py
```

伺服器將在 `http://127.0.0.1:5001` 啟動。

### 3. 開啟瀏覽器

在瀏覽器中開啟：

```
http://127.0.0.1:5001
```

### 4. 設定 API Key

1. 點擊右上角「⚙️ 設定」按鈕
2. 選擇 AI 服務（OpenAI 或 Google AI Studio）
3. 輸入您的 API Key
4. 選擇 AI 角色
5. 勾選「啟用 RAG 知識庫檢索」
6. 點擊「儲存設定」

### 5. 匯入範例知識庫

#### 方法一：使用範例檔案

1. 點擊右上角「🗄️ 知識庫管理」按鈕
2. 點擊「📤 匯入 CSV/Excel」
3. 選擇 `data/knowledge_base_example.csv`
4. 點擊「上傳」

#### 方法二：手動新增

1. 在知識庫管理介面點擊「➕ 新增知識」
2. 填寫問題、答案、分類
3. 點擊「儲存」

### 6. 開始問答

在主畫面的輸入框中輸入問題，AI 將根據知識庫內容回答並顯示參考來源。

## 📚 Google 試算表整合

### 設定步驟

詳細說明請參考：[gas_scripts/部署說明.md](gas_scripts/部署說明.md)

1. **建立 Google 試算表**
   - 前往 [Google Sheets](https://sheets.google.com)
   - 建立新試算表，命名為「RAG 知識庫」

2. **部署 Google Apps Script**
   - 在試算表中點擊「擴充功能」→「Apps Script」
   - 複製 `gas_scripts/知識庫API.gs` 的內容並貼上
   - 點擊「部署」→「新增部署作業」
   - 選擇「網頁應用程式」
   - 設定存取權限為「所有人」
   - 複製部署後的 URL

3. **在平台中同步**
   - 點擊「🗄️ 知識庫管理」
   - 點擊「☁️ 同步試算表」
   - 輸入 GAS API URL
   - 點擊「立即同步」

### 試算表格式

知識庫試算表必須包含以下欄位（標題列）：

| 問題 | 答案 | 分類 | 更新時間 | 來源 |
|------|------|------|----------|------|
| Python 是什麼？ | Python 是一種高階程式語言... | 程式設計 | 2025-10-10 12:00:00 | 手動新增 |

- **必填欄位**：問題、答案
- **選填欄位**：分類（預設為「一般」）、更新時間、來源

## 🎯 使用說明

### 知識庫管理

#### 新增知識
1. 點擊「➕ 新增知識」
2. 填寫問題、答案、分類
3. 點擊「儲存」

#### 編輯知識
1. 在表格中找到要編輯的項目
2. 點擊「編輯」按鈕
3. 修改內容後點擊「儲存」

#### 刪除知識
1. 在表格中找到要刪除的項目
2. 點擊「刪除」按鈕
3. 確認刪除

#### 批次匯入
1. 準備 CSV 或 Excel 檔案
   - 必須包含 `question` 和 `answer` 欄位
   - 可選 `category` 欄位
2. 點擊「📤 匯入 CSV/Excel」
3. 選擇檔案或拖曳檔案到上傳區
4. 點擊「上傳」

#### 搜尋知識
1. 在搜尋框中輸入關鍵字
2. 點擊「🔍」或按 Enter
3. 系統會使用向量相似度搜尋

#### 匯出知識庫
- 點擊「📥 匯出 CSV」
- 檔案會自動下載到本地

### AI 問答

#### 基本問答
1. 在輸入框中輸入問題
2. 按 Enter 或點擊「發送」按鈕
3. AI 會根據知識庫內容回答

#### 查看來源
- AI 回答下方會顯示「參考來源」
- 顯示問題、分類、相似度百分比
- 相似度越高表示越相關

#### 切換角色
1. 點擊「⚙️ 設定」
2. 在「AI 角色」下拉選單中選擇
3. 可選角色：
   - 知識庫助理（預設）
   - 專業導師
   - 程式撰寫助理
   - 幽默風趣的聊天夥伴

#### 清空對話
- 點擊右上角「🗑️」按鈕
- 確認清空對話記錄

## 📁 專案結構

```
進階/
│
├── app.py                      # Flask 後端主程式
├── requirements.txt            # Python 套件依賴
├── README.md                   # 本說明文件
│
├── templates/
│   └── index.html             # 主頁面 HTML
│
├── static/
│   ├── style.css              # 樣式表
│   └── script.js              # 前端 JavaScript
│
├── data/
│   ├── knowledge_base.json    # 本地知識庫儲存
│   └── knowledge_base_example.csv  # 範例知識庫
│
└── gas_scripts/
    ├── 知識庫API.gs           # Google Apps Script 程式碼
    └── 部署說明.md            # GAS 部署詳細說明
```

## 🔧 API 端點

### 聊天 API

**POST** `/api/chat`

發送訊息給 AI 並取得回應（整合 RAG）

請求參數：
```json
{
  "message": "使用者訊息",
  "api_key": "您的 API Key",
  "api_type": "openai 或 google",
  "role": "AI 角色名稱",
  "history": [對話歷史],
  "use_rag": true
}
```

回應：
```json
{
  "response": "AI 回應",
  "sources": [
    {
      "question": "相關問題",
      "answer": "相關答案",
      "category": "分類",
      "similarity": 0.85
    }
  ],
  "timestamp": "2025-10-10 12:00:00"
}
```

### 知識庫 API

**GET** `/api/knowledge-base`
- 取得知識庫列表

**POST** `/api/knowledge-base`
- 新增知識庫項目

**PUT** `/api/knowledge-base/<id>`
- 更新知識庫項目

**DELETE** `/api/knowledge-base/<id>`
- 刪除知識庫項目

**POST** `/api/knowledge-base/upload`
- 上傳 CSV/Excel 檔案

**GET** `/api/knowledge-base/export/csv`
- 匯出為 CSV

**POST** `/api/knowledge-base/search`
- 搜尋知識庫

**POST** `/api/knowledge-base/sync-google-sheets`
- 同步 Google 試算表

## 🤖 RAG 技術說明

本平台使用 RAG（Retrieval-Augmented Generation）技術：

1. **向量化（Embedding）**
   - 使用 `sentence-transformers` 將問題和答案轉換為向量
   - 模型：`paraphrase-multilingual-MiniLM-L12-v2`（支援中文）

2. **相似度搜尋**
   - 使用餘弦相似度（Cosine Similarity）計算問題間的相關性
   - 預設取前 3 個最相關的結果（相似度 > 0.3）

3. **上下文注入**
   - 將檢索到的知識庫內容作為上下文提供給 AI
   - AI 根據上下文產生更精確的回答

4. **來源引用**
   - 顯示 AI 參考的知識庫來源
   - 提供相似度百分比供使用者參考

## 💡 使用技巧

### 優化知識庫品質

1. **明確的問題描述**
   - 問題應該清晰、具體
   - 涵蓋可能的提問方式

2. **完整的答案內容**
   - 答案應該詳細、準確
   - 包含必要的背景資訊

3. **適當的分類**
   - 使用一致的分類名稱
   - 便於管理和檢索

4. **定期更新**
   - 保持知識庫內容的時效性
   - 修正錯誤或過時的資訊

### 提高檢索準確度

1. **增加相關問題**
   - 同一主題可以用不同問法
   - 增加同義問題提高命中率

2. **豐富答案內容**
   - 包含關鍵字和相關術語
   - 提供範例和說明

3. **使用結構化資料**
   - 利用 Google 試算表管理
   - 批次匯入整理好的資料

## ⚠️ 注意事項

### API Key 安全

- API Key 儲存在瀏覽器 localStorage
- 不要在公共環境中輸入 API Key
- 定期更換 API Key

### API 費用

- OpenAI API 會產生費用，請注意使用量
- Google AI Studio 目前提供免費額度
- 建議設定 API 使用限制

### 模型下載

- 首次啟動會下載 embedding 模型（約 400MB）
- 需要穩定的網路連線
- 模型會快取在本地，後續啟動無需下載

### 資料備份

- 定期匯出知識庫為 CSV
- Google 試算表可設定自動備份
- 本地 JSON 檔案可手動備份

## 🔍 常見問題

### Q: 為什麼 AI 沒有使用知識庫內容？

A: 請檢查：
- 是否勾選「啟用 RAG 知識庫檢索」
- 知識庫是否有相關資料
- 問題與知識庫內容的相似度是否足夠（>0.3）

### Q: 如何提高檢索準確度？

A:
- 增加更多相關的知識庫資料
- 使用多種問法表達同一問題
- 確保答案內容包含關鍵字

### Q: 可以使用多個 Google 試算表嗎？

A:
- 目前支援同步單一試算表
- 可以多次同步不同試算表到本地知識庫
- 建議將所有資料整合到一個試算表

### Q: 知識庫資料會保存嗎？

A:
- 本地知識庫自動儲存到 `data/knowledge_base.json`
- 重新啟動伺服器會自動載入
- 建議定期匯出備份

### Q: 如何更新 GAS API？

A:
- 修改 Apps Script 程式碼
- 點擊「部署」→「管理部署作業」
- 點擊「編輯」→ 更新版本 → 部署
- URL 不會改變，無需重新設定

## 🎓 進階應用

### 1. 建立專業知識庫

將公司內部文件、FAQ、技術文檔整理成知識庫，讓 AI 成為專業顧問。

### 2. 客服問答系統

整理常見客服問題，提供即時、準確的自動回答。

### 3. 學習輔助工具

建立課程相關的問答知識庫，協助學生學習和複習。

### 4. 多語言支援

embedding 模型支援多語言，可建立多語言知識庫。

## 📊 效能優化

### 大型知識庫（>1000 筆）

- 考慮使用專業向量資料庫（如 ChromaDB、Pinecone）
- 實作分頁和延遲載入
- 優化 embedding 快取機制

### 加速載入

- embedding 模型會在首次查詢時載入
- 可在啟動時預先載入模型
- 使用較小的模型（如 `all-MiniLM-L6-v2`）

## 🆚 與初階版本比較

| 功能 | 初階版 | 進階版 |
|------|--------|--------|
| 多 AI 支援 | ✅ | ✅ |
| 便利貼介面 | ✅ | ❌ |
| RAG 知識庫 | ❌ | ✅ |
| 向量搜尋 | ❌ | ✅ |
| Google Sheets | ❌ | ✅ |
| 知識庫管理 | ❌ | ✅ |
| 批次匯入 | ❌ | ✅ |
| 來源引用 | ❌ | ✅ |
| 統計儀表板 | ❌ | ✅ |

## 📝 授權

本專案為教學用途，可自由使用和修改。

## 🙏 致謝

- OpenAI - GPT API
- Google - Gemini API
- Hugging Face - Sentence Transformers
- Flask - Web Framework

---

## 🚀 下一步

完成基本設定後，建議：

1. ✅ 匯入範例知識庫體驗功能
2. ✅ 建立自己的知識庫內容
3. ✅ 測試不同問法的檢索效果
4. ✅ 設定 Google 試算表整合
5. ✅ 定期備份知識庫資料

祝您使用愉快！如有問題歡迎提出 Issue。
