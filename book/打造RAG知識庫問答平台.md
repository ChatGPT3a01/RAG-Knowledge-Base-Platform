# 打造 RAG 知識庫問答平台

---

## 🎯 單元目標

在這個章節中,我們將一起完成一個令人興奮的專案:建立一個具備 RAG(Retrieval-Augmented Generation)技術的 AI 問答平台。這個平台不僅能讓 AI 與你聊天,更能根據你提供的知識庫內容來回答問題,就像是為 AI 配備了一本隨身的百科全書。完成本章後,你將能夠:

- 快速部署一個功能完整的 RAG 知識庫問答平台
- 理解 RAG 技術的運作原理與應用價值
- 掌握向量嵌入(Embedding)與相似度搜尋的核心概念
- 建立並管理自己的 AI 知識庫系統
- 整合 Google 試算表作為知識庫來源
- 實作問答系統中的來源引用與可信度展示

這個專案的特別之處在於,我們將先讓你在 10-15 分鐘內就能看到成果,體驗 RAG 的魔力,然後再深入探討背後的技術細節。這種「先看到效果,再了解原理」的學習方式,能讓你更有動力深入了解每個技術環節。

---

## 🧩 單元簡介

在前面的章節中,我們學會了如何取得 API Key、建立基本的聊天介面,以及如何將程式部署到雲端。但你可能會發現一個問題:AI 雖然知識豐富,卻不一定了解你公司的產品資訊、學校的課程內容,或是你個人整理的專業知識。這就是 RAG 技術要解決的核心問題。

RAG(Retrieval-Augmented Generation)是近年來 AI 應用領域最重要的技術之一,它的概念很簡單卻非常實用:在讓 AI 回答問題之前,先從你的知識庫中「檢索」出相關的資料,然後把這些資料當作參考資料提供給 AI,讓 AI 基於這些可靠的資訊來「生成」答案。

想像一下,你正在準備一場重要的考試,如果只憑自己的記憶回答問題,可能會有些不確定;但如果能先翻閱課本找到相關段落,再根據課本內容來作答,答案就會準確得多。RAG 就是讓 AI 擁有這種「翻閱資料」的能力。

在本章中,我們將建立一個完整的 RAG 知識庫問答平台,這個平台具備以下特色:

首先,它支援多種 AI 模型,包括 OpenAI 的 GPT-4o、O1 系列,以及 Google 的 Gemini 2.0 Flash、Gemini 1.5 Pro 等最新模型。你可以根據需求選擇適合的 AI 引擎。

其次,它提供了完整的知識庫管理功能。你可以透過直覺的網頁介面新增、編輯、刪除知識內容,也可以批次匯入 CSV 或 Excel 檔案,甚至能夠整合 Google 試算表,讓知識庫的更新變得更加便利。

最重要的是,這個平台實作了真正的向量相似度搜尋。當使用者提出問題時,系統會自動將問題轉換成向量,然後在知識庫中尋找最相關的內容,並將這些內容作為上下文提供給 AI。AI 的回答不僅會引用知識庫的內容,還會顯示參考來源和相似度分數,讓使用者清楚知道答案的可信度。

這個專案的架構設計也很完整,前端使用 HTML、CSS、JavaScript 打造了一個現代化的使用者介面,後端則是基於 Python Flask 框架,搭配 Sentence Transformers 進行向量嵌入,以及 scikit-learn 計算相似度。整個系統的資料流清晰、模組化設計良好,非常適合作為學習與延伸開發的基礎。

---

## 🪄 應用情境

RAG 知識庫問答平台的應用範圍非常廣泛,幾乎所有需要「專業知識問答」的場景都適用。讓我們看看幾個實際的應用案例:

**教育領域的智慧助教**

假設你是一位大學教授,每學期都要回答學生大量重複的問題:「期中考範圍是什麼?」、「作業繳交期限到什麼時候?」、「某個程式概念要怎麼理解?」。你可以將課程大綱、常見問題、程式範例等內容整理成知識庫,讓 RAG 平台成為你的 24 小時線上助教。學生提問時,AI 會從你的課程資料中找到答案,不僅減輕了你的負擔,學生也能隨時獲得準確的資訊。

**企業內部的知識管理系統**

許多公司都有大量的內部文件、操作手冊、產品規格書,但這些資料往往散落各處,員工要找資料就像大海撈針。透過 RAG 平台,你可以將這些文件整理成知識庫,員工只要用自然語言提問,系統就能從成千上萬筆資料中找出相關內容,並由 AI 整合成清楚易懂的答案。這不僅提升了工作效率,也讓新進員工能快速上手。

**客服問答的自動化助手**

電商平台、SaaS 服務經常需要處理大量客戶詢問,像是「如何退貨?」、「會員等級有什麼差異?」、「付款方式有哪些?」等問題。將這些常見問答整理成知識庫後,RAG 平台可以作為第一線客服,即時回答客戶問題。當遇到知識庫中沒有的問題時,才轉交給人工客服處理,大幅降低客服成本。

**專業領域的諮詢顧問**

如果你是法律、會計、醫療等專業領域的從業人員,可以將相關法規、案例、專業知識整理成知識庫。當客戶提出問題時,RAG 平台能快速從專業資料中找到相關依據,協助你提供更準確、更有根據的建議。而且,系統會顯示參考來源,讓你能夠追溯資訊的出處,確保專業性。

**個人知識管理與學習輔助**

就算不是企業或組織,個人也可以使用 RAG 平台。你可以將閱讀筆記、學習心得、工作經驗整理成知識庫,打造專屬的 AI 學習助手。無論是準備考試、整理專案經驗,或是建立個人的知識體系,RAG 都能幫助你更有效地管理和提取知識。

**多語言客戶支援**

由於我們使用的 Embedding 模型支援多語言,你可以建立包含中文、英文、日文等多種語言的知識庫。這對於需要服務國際客戶的企業來說特別有用,同一個平台就能處理不同語言的問答需求。

這些應用情境的共同點是:都需要 AI 能夠基於「特定、可靠的資料來源」來回答問題,而不是僅依賴 AI 本身的訓練資料。RAG 技術正是為了滿足這個需求而生,它讓 AI 從「通用知識」延伸到「專業領域」,大大擴展了應用範圍。

---

## 單元 1：快速開始 - 部署 RAG 知識庫平台

在深入了解 RAG 的技術細節之前,讓我們先把平台跑起來,親眼看看它的效果。這個快速部署流程設計成只需 10-15 分鐘,即使是完全沒有經驗的初學者也能順利完成。我們會一步步帶著你從零開始,建立虛擬環境、安裝套件、啟動伺服器、匯入範例知識庫,最後測試 RAG 問答功能。

### 步驟 1:確認專案檔案位置

首先,請確認你已經有本書提供的專案檔案。這些檔案應該位於以下路徑:

```
D:\自己架設AI_零基礎到大師\CH3_打造RAG知識庫問答平台\
```

如果你的檔案放在其他位置,請記住你的實際路徑,待會兒會用到。在這個資料夾中,你應該會看到以下重要檔案:

- `app.py`:Flask 後端主程式
- `requirements.txt`:Python 套件清單
- `templates/`:網頁模板資料夾
- `static/`:CSS、JavaScript 資料夾
- `data/`:知識庫資料夾,包含範例檔案

### 步驟 2:建立並啟動虛擬環境

打開終端機(Windows 用戶請使用「命令提示字元」或「PowerShell」,macOS/Linux 用戶請使用「終端機」),然後切換到專案資料夾:

**Windows 用戶:**

```bash
cd D:\自己架設AI_零基礎到大師\CH3_打造RAG知識庫問答平台
```

**macOS/Linux 用戶:**

```bash
cd ~/自己架設AI_零基礎到大師/CH3_打造RAG知識庫問答平台
```

接下來建立虛擬環境。虛擬環境就像是為這個專案建立一個獨立的 Python 小世界,避免不同專案的套件版本互相干擾:

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

當你看到終端機的提示符號前面出現 `(venv)` 字樣,就表示虛擬環境已經成功啟動了。這個 `(venv)` 是一個重要的提示,告訴你現在所有的 Python 操作都會在這個獨立環境中進行。

> 【註記】請截圖「虛擬環境啟動成功畫面」,命名為 `rag_venv_activated.png`。畫面應顯示提示符號前面有 `(venv)` 標記。

### 步驟 3:安裝必要套件

現在要安裝專案需要的所有 Python 套件。這個步驟會花比較多時間,特別是第一次安裝時:

```bash
pip install -r requirements.txt
```

安裝過程中,你會看到大量的套件名稱和版本訊息在螢幕上滾動,這是正常的。其中最重要的幾個套件包括:

- `flask`:網頁框架,用來建立後端伺服器
- `openai`:OpenAI API 的官方套件
- `google-generativeai`:Google Gemini API 套件
- `sentence-transformers`:向量嵌入模型,這是 RAG 的核心技術
- `pandas`:資料處理工具
- `openpyxl`:Excel 檔案處理

**特別注意**:當系統安裝 `sentence-transformers` 套件時,會自動下載一個約 400MB 的 AI 模型檔案(模型名稱是 `paraphrase-multilingual-MiniLM-L12-v2`,專門用來處理多語言文字向量化)。這個下載過程可能需要 5-10 分鐘,取決於你的網路速度。請耐心等待,不要中斷安裝過程。這個模型只需要下載一次,之後就會快取在本機上,不用重複下載。

如果安裝過程中出現錯誤,通常是 pip 版本太舊造成的。請先執行以下指令升級 pip,然後重新安裝:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

當你看到類似「Successfully installed ...」的訊息,且沒有紅色的錯誤訊息時,就表示安裝完成了。

> 【註記】請截圖「套件安裝完成畫面」,命名為 `rag_packages_installed.png`。畫面應顯示「Successfully installed」訊息。

### 步驟 4:啟動 Flask 伺服器

套件安裝完成後,就可以啟動伺服器了。這個步驟非常簡單,只需要一行指令:

```bash
python app.py
```

幾秒鐘後,你應該會看到類似以下的訊息:

```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
```

這些訊息告訴我們:

1. Flask 應用程式已經啟動
2. 伺服器運行在本機(127.0.0.1)的 5001 埠號
3. 目前處於開發模式(Debug mode),方便我們除錯
4. 按 `Ctrl+C` 可以停止伺服器

看到這些訊息就表示伺服器已經成功啟動了!這時候終端機會保持在「執行中」的狀態,不要關閉它,讓它繼續運作。

> 【註記】請截圖「Flask 伺服器啟動畫面」,命名為 `rag_flask_running.png`。畫面應顯示 Running on http://127.0.0.1:5001 訊息。

### 步驟 5:開啟網頁介面

保持終端機繼續運作,現在開啟你的瀏覽器(建議使用 Chrome、Firefox 或 Edge),在網址列輸入:

```
http://127.0.0.1:5001
```

按下 Enter 鍵後,你應該會看到一個設計精美的聊天介面。畫面上方有平台的標題「RAG 知識庫 AI 問答平台」,右上角有幾個功能按鈕:「⚙️ 設定」、「🗄️ 知識庫管理」、「🗑️ 清空對話」。中間是對話區域,下方則是訊息輸入框。

這個介面就是我們的 RAG 問答平台主畫面。不過在開始提問之前,我們需要先設定 API Key 和匯入知識庫。

> 【註記】請截圖「RAG 平台主畫面」,命名為 `rag_main_interface.png`。畫面應顯示完整的聊天介面。

### 步驟 6:設定 API Key

點擊右上角的「⚙️ 設定」按鈕,會彈出一個設定對話框。這裡有幾個重要的設定項目:

**選擇 AI 服務:**你可以選擇使用 OpenAI 或 Google AI Studio。如果你在 CH1 已經申請了 OpenAI 的 API Key,就選擇「OpenAI」;如果使用的是 Google 的服務,就選擇「Google AI Studio」。

**輸入 API Key:**將你在 CH1 取得的 API Key 貼到輸入框中。記住,API Key 是很重要的憑證,不要分享給其他人。

**選擇 AI 模型:**如果選擇 OpenAI,可以選擇 GPT-4o、GPT-4 Turbo、O1 等模型;如果選擇 Google,可以選擇 Gemini 2.0 Flash、Gemini 1.5 Pro 等模型。建議初學者選擇 GPT-4o 或 Gemini 2.0 Flash,這兩個模型速度快、成本低,很適合測試使用。

**選擇 AI 角色:**這裡有幾種預設角色可以選擇,像是「知識庫助理」、「專業導師」、「程式撰寫助理」等。每個角色都有不同的對話風格和專長。第一次使用建議選擇「知識庫助理」,這個角色特別針對知識庫問答進行了最佳化。

**啟用 RAG 知識庫檢索:**這個選項非常重要!請務必勾選「啟用 RAG 知識庫檢索」。只有勾選這個選項,系統才會在回答問題前先搜尋知識庫。如果沒有勾選,AI 就只會用它本身的知識回答,無法使用你的知識庫內容。

**調整相似度門檻:**這個進階選項可以設定知識庫搜尋的敏感度。數值越高,只有非常相關的內容才會被採用;數值越低,相關性較低的內容也可能被納入。建議保持預設值 0.3,這是經過測試的最佳平衡點。

**設定回傳結果數量:**這個選項決定系統會提供幾筆知識庫內容給 AI 參考。預設是 3 筆,通常已經足夠。如果你的知識庫內容很豐富,可以調高到 5 筆。

設定完成後,點擊「儲存設定」按鈕。系統會將這些設定儲存在瀏覽器的 localStorage 中,下次開啟網頁時就不用重新設定了。

> 【註記】請截圖「API Key 設定畫面」,命名為 `rag_api_settings.png`。畫面應顯示設定對話框,並勾選「啟用 RAG 知識庫檢索」選項。

### 步驟 7:匯入範例知識庫

現在要匯入一些範例資料,讓我們可以測試 RAG 功能。點擊右上角的「🗄️ 知識庫管理」按鈕,會開啟知識庫管理介面。

這個介面分成幾個區塊:

**頂部的統計資訊:**顯示目前知識庫中有幾筆資料、最後更新時間等資訊。現在應該是 0 筆,因為我們還沒有匯入任何資料。

**操作按鈕區:**包含「➕ 新增知識」、「📤 匯入 CSV/Excel」、「📥 匯出 CSV」、「☁️ 同步試算表」等按鈕。

**知識庫表格:**以表格形式顯示所有知識內容,包含問題、答案、分類、更新時間等欄位,每筆資料都有「編輯」和「刪除」按鈕。

**搜尋功能:**可以輸入關鍵字搜尋知識庫,使用的是向量相似度搜尋,不是單純的關鍵字比對。

現在,讓我們匯入範例資料。點擊「📤 匯入 CSV/Excel」按鈕,會彈出檔案上傳對話框。

你可以用兩種方式選擇檔案:

1. 點擊「點擊選擇檔案」按鈕,從檔案瀏覽器中選擇 `data/knowledge_base_example.csv`
2. 或者直接將 `knowledge_base_example.csv` 檔案拖曳到上傳區域

選擇好檔案後,點擊「上傳」按鈕。系統會讀取 CSV 檔案中的內容,並將每一筆問答資料加入知識庫。匯入過程通常只需要幾秒鐘。

匯入完成後,你應該會看到知識庫表格中出現了幾十筆資料,內容涵蓋 Python 程式設計、AI 技術、網頁開發等主題。每筆資料都包含:

- **問題:**使用者可能會問的問題
- **答案:**對應的答案內容
- **分類:**這筆知識的分類(如「程式設計」、「AI 技術」等)
- **更新時間:**資料的建立或更新時間
- **來源:**資料的來源標記

這個範例知識庫是特別設計來展示 RAG 功能的,涵蓋了各種不同類型的問題,你可以用它來測試系統的搜尋能力。

> 【註記】請截圖「知識庫匯入成功畫面」,命名為 `rag_knowledge_imported.png`。畫面應顯示知識庫管理介面,表格中有範例資料。

### 步驟 8:測試 RAG 問答功能

所有設定都完成了,現在是最令人期待的時刻:測試 RAG 功能!關閉知識庫管理介面,回到主聊天畫面。

在訊息輸入框中,試著輸入一個問題,例如:

```
什麼是 Flask?
```

按下 Enter 鍵或點擊「發送」按鈕,然後觀察系統的運作過程:

1. **問題提交:**你的問題會立刻顯示在對話區域的右側(使用者訊息)
2. **向量搜尋:**系統會將你的問題轉換成向量,然後在知識庫中搜尋相關內容(這個過程很快,通常不到 1 秒)
3. **AI 回應:**AI 會根據檢索到的知識庫內容產生回答,回答會顯示在對話區域的左側(AI 訊息)
4. **來源引用:**在 AI 回答的下方,你會看到「📚 參考來源」區塊,顯示 AI 參考了哪些知識庫內容

特別注意「參考來源」區塊,這裡會顯示:

- **問題:**知識庫中最相關的問題
- **分類:**這筆知識的分類
- **相似度:**一個百分比數值,表示使用者問題與知識庫問題的相似程度

例如,當你問「什麼是 Flask?」時,系統可能會找到知識庫中「Flask 是什麼?」這個問題,相似度可能是 95% 以上。AI 就會根據這筆知識庫的答案來回應你。

你可以多試幾個問題,觀察系統的表現:

```
RAG 是什麼技術?
```

```
如何部署 Flask 應用到雲端?
```

```
Python 虛擬環境的作用是什麼?
```

每次提問,都會看到系統如何從知識庫中檢索資料,以及 AI 如何基於這些資料產生答案。這就是 RAG 技術的魅力所在:AI 不再只是憑藉訓練資料回答,而是能夠參考你提供的專業知識,給出更準確、更可靠的答案。

> 【註記】請截圖「RAG 問答測試畫面」,命名為 `rag_rag_testing.png`。畫面應顯示一個問答對話,且下方有「參考來源」區塊,顯示相似度資訊。

### 步驟 9:體驗知識庫管理功能

除了問答功能,我們也可以體驗一下知識庫的管理功能。再次開啟「🗄️ 知識庫管理」介面,試著執行以下操作:

**新增一筆知識:**點擊「➕ 新增知識」按鈕,填寫問題(例如「今天學到了什麼?」)、答案(例如「今天學會了如何建立 RAG 知識庫問答平台」)、分類(例如「學習筆記」),然後點擊「儲存」。新增的知識會立刻出現在表格中,並且可以馬上用於問答。

**搜尋知識:**在搜尋框中輸入關鍵字(例如「Flask」),點擊搜尋按鈕。系統會使用向量相似度搜尋,找出所有與「Flask」相關的知識,並依照相似度排序。這個搜尋功能使用的是跟問答相同的技術,所以即使關鍵字不完全一樣,只要語意相近就能找到。

**編輯知識:**點擊任一筆資料的「編輯」按鈕,修改問題或答案,然後儲存。修改會立即生效。

**刪除知識:**點擊「刪除」按鈕可以移除不需要的知識。系統會要求你確認,避免誤刪。

**匯出知識庫:**點擊「📥 匯出 CSV」按鈕,可以將目前的知識庫匯出成 CSV 檔案,方便備份或分享。

這些管理功能讓你可以輕鬆維護知識庫,隨時新增最新的資訊、修正錯誤的內容,或是移除過時的資料。而且所有的修改都會即時反映在問答系統中,不需要重新啟動伺服器。

> 【註記】請截圖「知識庫管理操作畫面」,命名為 `rag_kb_management.png`。畫面應顯示知識庫管理介面的各種操作功能。

### 步驟 10:理解運作流程(快速版)

恭喜!你已經成功部署並測試了 RAG 知識庫問答平台。在進入後續章節的詳細技術說明之前,讓我們快速回顧一下整個系統的運作流程:

1. **使用者提問:**使用者在網頁介面輸入問題
2. **向量化:**系統將問題轉換成一個數學向量(一串數字)
3. **相似度搜尋:**將問題向量與知識庫中所有問答的向量進行比對,找出最相似的幾筆資料
4. **上下文注入:**將檢索到的知識庫內容整合成「上下文」,一併提供給 AI
5. **AI 生成答案:**AI 基於上下文中的資訊產生回答
6. **顯示結果:**將 AI 的回答和參考來源一起呈現給使用者

這個流程的核心就是「檢索-增強-生成」(Retrieval-Augmented Generation),也就是 RAG 這個縮寫的由來。

在接下來的章節中,我們會深入探討每個環節的技術細節:什麼是向量嵌入?相似度是如何計算的?Flask 如何處理 API 請求?前端如何與後端溝通?這些問題都會逐一解答。但現在,你已經親眼見證了 RAG 的效果,這會讓後續的學習更有方向感。

### 常見問題快速排除

在快速部署過程中,你可能會遇到一些問題。這裡整理了最常見的狀況和解決方法:

**問題 1:套件安裝失敗**

如果 `pip install` 過程中出現錯誤,先確認:
- Python 版本是否為 3.8 以上(執行 `python --version` 檢查)
- pip 是否為最新版本(執行 `python -m pip install --upgrade pip` 升級)
- 網路連線是否穩定(特別是下載 Embedding 模型時)

**問題 2:無法開啟網頁**

如果瀏覽器無法連線到 http://127.0.0.1:5001,檢查:
- Flask 伺服器是否確實在運行(終端機應該顯示 Running on... 訊息)
- 埠號 5001 是否被其他程式佔用(可以修改 app.py 中的埠號設定)
- 防火牆是否阻擋了連線

**問題 3:AI 沒有使用知識庫**

如果 AI 回答時沒有參考知識庫,確認:
- 設定中是否勾選了「啟用 RAG 知識庫檢索」
- 知識庫是否有匯入資料
- 問題與知識庫內容的相似度是否足夠(系統預設門檻是 0.3)

**問題 4:Embedding 模型下載很慢**

首次啟動時下載模型可能需要較長時間,建議:
- 確保網路連線穩定
- 耐心等待,不要中斷下載
- 如果多次失敗,可能是網路限制,可以嘗試使用 VPN 或更換網路環境

這些問題在初次部署時很常見,不用擔心,按照排除步驟逐一檢查,通常都能順利解決。

---

## 單元 2：RAG 是什麼？為何需要知識庫

在上一節中,我們快速體驗了 RAG 知識庫問答平台的功能。你可能已經注意到,當 AI 回答問題時,下方會顯示「參考來源」,標明答案是基於知識庫中的哪些內容。這個設計背後,正是 RAG 技術的核心理念。現在,讓我們深入了解 RAG 到底是什麼,以及為什麼它對現代 AI 應用如此重要。

### RAG 的全名與核心概念

RAG 是「Retrieval-Augmented Generation」的縮寫,中文可以翻譯為「檢索增強生成」。這個名稱本身就精確地描述了這項技術的運作方式:

- **Retrieval(檢索):**在回答問題之前,先從資料庫或知識庫中「檢索」相關資訊
- **Augmented(增強):**用檢索到的資訊「增強」AI 的背景知識
- **Generation(生成):**AI 基於增強後的背景知識「生成」答案

簡單來說,RAG 就是「先找資料,再回答」的概念。這聽起來很像人類的學習和回答模式:當我們遇到不熟悉的問題時,會先翻閱書籍、查詢資料,然後根據找到的資訊整理出答案。RAG 讓 AI 也能做到同樣的事。

傳統的 AI 對話模型(像是純粹的 GPT、Gemini)只能依賴訓練時學習到的知識來回答問題。這些知識雖然廣泛,但有幾個明顯的限制:

**時效性限制:**AI 模型的訓練資料有截止日期,無法得知最新發生的事件或最新發布的資訊。例如,如果模型的訓練資料截止於 2023 年,它就不會知道 2024 年推出的新技術。

**專業性限制:**AI 的知識雖然廣泛,但對於特定領域的專業知識可能不夠深入。例如,它可能知道一般的醫學常識,但對於你公司特有的產品規格、內部流程,它完全不了解。

**可靠性限制:**AI 有時會產生「幻覺」(Hallucination),也就是自信滿滿地說出錯誤的資訊。因為它是基於統計模型產生文字,而不是真正「理解」知識,所以可能會組合出看似合理但實際錯誤的答案。

**來源不明:**當 AI 回答問題時,使用者無法確認答案的依據是什麼,也無法追溯資訊來源,這在需要可信度的場景中是個大問題。

RAG 技術正是為了解決這些限制而發展出來的。透過在回答前先檢索外部知識庫,RAG 可以:

- 提供最新的、即時更新的資訊
- 存取專業領域或特定組織的內部知識
- 減少 AI 幻覺,因為答案是基於真實的文件內容
- 提供答案來源,讓使用者可以追溯和驗證資訊

### RAG 與傳統 AI 對話的差異

為了更清楚地理解 RAG 的價值,讓我們用一個具體的例子來比較傳統 AI 對話和 RAG 系統的差異。

**情境:公司內部的 IT 支援系統**

假設你的公司有一套內部的 IT 系統,員工經常需要查詢各種操作流程,例如「如何申請新電腦?」、「VPN 連線失敗怎麼辦?」、「差旅費用如何報銷?」等問題。

**使用傳統 AI 對話:**

員工問:「公司的 VPN 連線步驟是什麼?」

AI 可能會這樣回答:「一般來說,VPN 連線的步驟包括:1. 下載 VPN 客戶端軟體 2. 輸入伺服器位址和帳號密碼 3. 點擊連線按鈕...」

這個答案聽起來很合理,但問題是:它是「通用」的 VPN 連線說明,不是你公司「特定」的流程。你們公司可能使用的是特定的 VPN 軟體,有特定的伺服器位址,有特定的設定要求。AI 給的答案雖然不算錯,但對實際操作沒什麼幫助。

**使用 RAG 系統:**

員工問同樣的問題:「公司的 VPN 連線步驟是什麼?」

系統會先從知識庫中檢索,找到公司 IT 部門撰寫的「VPN 連線指南」文件,然後AI 基於這份文件回答:「根據公司 IT 部門的指南,VPN 連線步驟如下:1. 從公司內網下載 Cisco AnyConnect VPN 軟體 2. 安裝後開啟軟體,輸入伺服器位址 vpn.yourcompany.com 3. 使用你的員工帳號(工號@yourcompany.com)和密碼登入 4. 連線成功後,系統會顯示綠色勾勾...」

而且,回答下方會顯示「參考來源:VPN 連線指南,更新日期:2025-01-15」,員工可以追溯到原始文件查看更詳細的說明。

這就是 RAG 的威力:它讓 AI 從「通用助手」變成「專屬顧問」,能夠提供精準、可靠、符合實際需求的答案。

### 為什麼需要知識庫?

理解了 RAG 的運作原理後,我們就能明白「知識庫」在整個系統中扮演的關鍵角色。知識庫不是單純的資料存儲,而是 RAG 系統的「靈魂」,它決定了系統能夠回答什麼問題、回答的準確度如何。

**知識庫是 AI 的記憶延伸**

AI 模型本身的「記憶」是固定的,就是它在訓練時學習到的資料。這些記憶無法隨時更新,也無法根據不同的應用場景客製化。知識庫就像是給 AI 配備了一個「外接硬碟」,裡面存放著特定領域或特定組織的專業知識。當 AI 需要回答問題時,它可以隨時從這個外接硬碟中讀取資訊。

而且,這個外接硬碟是可以隨時更新的。當你的產品推出新功能、政策有所調整、或是發現了錯誤資訊需要修正,你只需要更新知識庫,AI 馬上就能獲得最新的資訊,不需要重新訓練模型。

**知識庫是答案品質的保證**

AI 產生的答案品質,很大程度上取決於它參考的資料品質。如果餵給它的是錯誤或過時的資料,它自然會給出錯誤的答案。透過精心整理的知識庫,你可以確保 AI 參考的都是經過驗證、值得信賴的資訊。

例如,在醫療諮詢場景中,如果知識庫是由專業醫師審核的醫學資料,AI 的回答就會具備一定的專業性和可靠性。相反地,如果知識庫充斥著未經驗證的網路謠言,AI 也會跟著傳播錯誤資訊。

這也是為什麼在建立 RAG 系統時,知識庫的建立和維護是最重要的工作之一。系統的技術再先進,如果知識庫品質不佳,整個系統的價值就會大打折扣。

**知識庫提供了可追溯性**

在許多應用場景中,「答案從哪裡來」和「答案是什麼」一樣重要。例如,在法律諮詢、醫療建議、金融分析等領域,使用者需要知道答案的依據,才能判斷是否採納。

RAG 系統透過顯示「參考來源」,讓每個答案都有跡可循。使用者可以查看 AI 參考了知識庫中的哪些內容,甚至可以進一步閱讀原始文件。這種透明度大幅提升了系統的可信度。

**知識庫支援持續學習與改進**

當你開始使用 RAG 系統後,會逐漸發現哪些問題被頻繁提問、哪些知識內容需要補充、哪些答案需要修正。透過持續地更新知識庫,系統會越來越符合使用者的需求,答案品質也會不斷提升。

這種「持續改進」的機制,在傳統 AI 模型中是很難實現的,因為更新模型需要重新訓練,成本高昂且耗時。但在 RAG 系統中,你只需要編輯知識庫,就能立即看到改進效果。

### RAG 的應用價值

總結來說,RAG 技術和知識庫的結合,為 AI 應用帶來了以下核心價值:

**專業化:**讓 AI 從通用助手變成領域專家,能夠提供深入、專業的答案。

**即時性:**知識庫可以隨時更新,AI 總是能獲取最新資訊。

**可靠性:**答案基於可驗證的文件,減少了 AI 幻覺的問題。

**透明性:**提供答案來源,使用者可以追溯和驗證資訊。

**可控性:**你可以精確控制 AI 能夠存取哪些資訊,避免洩漏敏感資料。

**經濟性:**不需要訓練專屬模型,只需要建立知識庫,就能讓 AI 具備專業能力,大幅降低了開發成本。

這些價值讓 RAG 成為當前企業 AI 應用的主流技術之一。無論是客服系統、內部知識管理、教育平台,還是專業諮詢服務,RAG 都展現出巨大的應用潛力。

在下一節中,我們會深入探討本專案的技術架構,了解這些價值是如何透過程式碼實現的。

---

## 單元 3：專案架構與技術堆疊

理解了 RAG 的概念與價值後,讓我們來看看如何實際建構一個 RAG 系統。本節會介紹專案的整體架構、使用的技術堆疊,以及各個元件之間的協作關係。這會幫助你建立一個「全局視角」,在後續深入程式碼細節時,能夠清楚知道每個部分在整體系統中的定位。

### 整體系統架構

本專案採用經典的「前後端分離」架構,整個系統可以分成三個主要層次:

**前端層(Frontend Layer)**

這是使用者直接接觸的部分,負責呈現使用者介面和處理互動邏輯。前端由以下元件組成:

- **HTML 模板**(`templates/index.html`):定義了網頁的結構,包含聊天介面、設定對話框、知識庫管理介面等所有視覺元素。
- **CSS 樣式**(`static/style.css`):負責網頁的視覺設計,包含配色、排版、動畫效果等,讓介面看起來美觀且易用。
- **JavaScript 腳本**(`static/script.js`):處理所有前端邏輯,包括按鈕點擊事件、表單驗證、AJAX 請求、動態更新畫面等。

前端使用的是純粹的 HTML/CSS/JavaScript,沒有引入 React、Vue 等現代框架。這樣的設計有幾個好處:簡單易懂,適合初學者學習;沒有額外的編譯步驟,修改後重新整理瀏覽器就能看到效果;不需要安裝 Node.js 等額外工具,降低了學習門檻。

**後端層(Backend Layer)**

後端是整個系統的核心,負責處理業務邏輯、API 呼叫、資料處理等工作。後端由 Python Flask 框架建構,主要元件包括:

- **Flask 應用程式**(`app.py`):這是整個後端的主程式,定義了所有的 API 端點(Endpoint),處理前端發送的 HTTP 請求。
- **RAG 核心模組**:包含向量嵌入、相似度計算、知識庫檢索等 RAG 技術的實作。
- **AI API 整合**:處理與 OpenAI、Google Gemini 等 AI 服務的通訊。
- **知識庫管理**:負責知識庫的增刪改查、批次匯入、資料匯出等功能。
- **資料持久化**:將知識庫儲存為 JSON 檔案,確保資料不會在伺服器重啟後遺失。

Flask 是一個輕量級的 Python 網頁框架,它的特色是簡單、彈性、容易上手。相比於 Django 等大型框架,Flask 的學習曲線較平緩,非常適合用來建立中小型的 Web 應用。

**資料層(Data Layer)**

資料層負責儲存系統運作所需的各種資料:

- **知識庫檔案**(`data/knowledge_base.json`):以 JSON 格式儲存所有的問答知識,包含問題、答案、分類、向量等資訊。
- **Embedding 模型快取**:Sentence Transformers 下載的向量嵌入模型會快取在本機,避免重複下載。
- **範例資料**(`data/knowledge_base_example.csv`):提供的範例知識庫,方便快速測試系統功能。

這三個層次透過 HTTP 協定進行溝通:前端發送 HTTP 請求到後端,後端處理後回傳 JSON 格式的回應,前端再將回應內容呈現在畫面上。這種架構的好處是各層職責清晰、容易維護,而且未來如果要將前端和後端部署到不同的伺服器,也很容易實現。

### 技術堆疊詳解

現在讓我們更詳細地看看每個技術的選擇與用途:

**Python 3.8+**

Python 是整個後端的基礎語言。選擇 Python 的原因有:

1. 擁有豐富的 AI/ML 生態系,像是 sentence-transformers、scikit-learn 等套件都是 Python 寫的
2. 語法簡潔易懂,適合初學者學習
3. 社群龐大,遇到問題容易找到解決方案
4. 與 Flask、OpenAI SDK、Google AI SDK 等工具整合良好

版本要求 3.8 以上,是因為許多套件(特別是 sentence-transformers)需要較新版本的 Python 特性。

**Flask 3.0.3**

Flask 是後端的網頁框架,負責處理 HTTP 請求與回應。Flask 的核心概念包括:

- **路由(Routing)**:將 URL 路徑對應到 Python 函式,例如 `/api/chat` 對應到聊天處理函式
- **請求處理**:接收前端發送的資料(JSON、表單、檔案等)
- **回應生成**:將處理結果包裝成 JSON 格式回傳給前端
- **靜態檔案服務**:提供 CSS、JavaScript、圖片等靜態資源

專案中使用的 Flask-CORS 套件,則是用來處理跨域資源共享(CORS)問題,讓前端可以順利向後端發送請求。

**OpenAI SDK 2.0+**

OpenAI 官方提供的 Python 套件,用來呼叫 GPT 系列模型。版本 2.0 是一個重大更新,API 介面有大幅改變,支援了 GPT-4o、O1 等最新模型。套件的主要功能包括:

- 發送聊天訊息到 GPT 模型
- 處理串流回應(Streaming Response)
- 管理對話歷史(Chat History)
- 錯誤處理與重試機制

**Google Generative AI SDK 0.8.3**

Google 提供的 AI 套件,用來呼叫 Gemini 系列模型。功能類似 OpenAI SDK,但針對 Gemini 模型進行了最佳化。支援 Gemini 2.0 Flash、Gemini 1.5 Pro 等模型,提供高品質的對話生成能力。

**Sentence Transformers 3.3.1**

這是整個 RAG 系統最核心的套件,負責將文字轉換成向量(Vector Embedding)。專案使用的模型是 `paraphrase-multilingual-MiniLM-L12-v2`,這個模型的特色是:

- **多語言支援**:支援包含中文在內的 50 多種語言
- **語意理解**:不是單純的關鍵字比對,而是理解句子的語意
- **體積適中**:模型大小約 400MB,在效能與精確度之間取得平衡
- **速度快**:嵌入一個句子只需要幾十毫秒

向量嵌入是 RAG 技術的基礎。簡單來說,它將文字轉換成一串數字(向量),語意相近的文字會有相近的向量。透過比較向量之間的距離,就能找出語意相關的內容。

**Pandas 2.2.3**

Pandas 是 Python 中最常用的資料處理套件,在專案中主要用於:

- 讀取 CSV、Excel 檔案
- 處理知識庫資料的新增、刪除、篩選
- 資料格式轉換(例如將 DataFrame 轉換成 JSON)
- 批次匯入時的資料驗證

**NumPy 1.26.4**

NumPy 提供了高效能的數學運算功能,在專案中主要用於:

- 向量的數學運算
- 陣列操作
- 配合 scikit-learn 計算相似度

**Scikit-learn 1.5.2**

Scikit-learn 是 Python 的機器學習套件,專案中使用它的「餘弦相似度」(Cosine Similarity)功能,用來計算問題向量與知識庫向量之間的相似程度。餘弦相似度的值介於 -1 到 1 之間,數值越接近 1 表示越相似。

**Openpyxl 3.1.5**

用來處理 Excel 檔案(.xlsx 格式)的套件,讓使用者可以用 Excel 整理知識庫資料,然後直接匯入系統。

**Python-dotenv 1.0.1**

這個套件讓我們可以使用 `.env` 檔案來管理環境變數,例如 API Key、資料庫連線字串等敏感資訊。雖然在目前的版本中,API Key 是儲存在前端的 localStorage,但 python-dotenv 為未來可能的後端儲存方案預留了空間。

**Requests 2.32.3**

Python 的 HTTP 客戶端套件,用來發送 HTTP 請求。在專案中主要用於與 Google Sheets API 整合,從 Google Apps Script 部署的 API 端點讀取知識庫資料。

### 資料流與互動流程

了解了各個技術元件後,讓我們看看一個完整的「使用者提問」流程是如何運作的:

**步驟 1:使用者輸入問題**

使用者在前端網頁的輸入框中輸入問題,例如「Flask 是什麼?」,然後按下發送按鈕。

**步驟 2:前端發送 API 請求**

JavaScript 捕捉到發送事件,讀取輸入框的內容,組成一個 JSON 格式的請求:

```json
{
  "message": "Flask 是什麼?",
  "api_key": "使用者的 API Key",
  "api_type": "openai",
  "role": "知識庫助理",
  "history": [...之前的對話],
  "use_rag": true
}
```

然後透過 `fetch` API 發送 POST 請求到 `/api/chat` 端點。

**步驟 3:後端接收請求並進行 RAG 檢索**

Flask 後端的 `/api/chat` 路由接收到請求,首先判斷 `use_rag` 是否為 `true`。如果是,就啟動 RAG 流程:

1. 使用 Sentence Transformers 將問題「Flask 是什麼?」轉換成向量
2. 將這個向量與知識庫中所有問答的向量進行比對
3. 使用 scikit-learn 計算餘弦相似度
4. 找出相似度最高的前 3 筆知識(假設門檻是 0.3 以上)

假設找到了以下知識:
- 問題:「Flask 是什麼?」,相似度:0.95
- 問題:「如何安裝 Flask?」,相似度:0.72
- 問題:「Flask 與 Django 的差異」,相似度:0.65

**步驟 4:組成 AI 提示詞(Prompt)**

後端將檢索到的知識整合成「上下文」,組成完整的提示詞:

```
你是一個知識庫助理,請根據以下知識庫內容回答使用者的問題。

知識庫內容:
1. 問題:Flask 是什麼?
   答案:Flask 是一個輕量級的 Python 網頁框架...

2. 問題:如何安裝 Flask?
   答案:可以使用 pip install flask...

3. 問題:Flask 與 Django 的差異
   答案:Flask 較輕量、彈性高,Django 較完整...

使用者問題:Flask 是什麼?

請根據上述知識庫內容回答,並保持專業且友善的語氣。
```

**步驟 5:呼叫 AI API**

後端使用 OpenAI SDK(或 Google Generative AI SDK)將提示詞發送給 AI 模型,等待模型生成回應。

**步驟 6:處理 AI 回應**

AI 模型根據提示詞中的知識庫內容產生答案,例如:「Flask 是一個輕量級的 Python 網頁框架,它的特色是簡單、彈性、容易上手。相比於 Django 等大型框架,Flask 的學習曲線較平緩,非常適合用來建立中小型的 Web 應用...」

後端接收到 AI 的回應後,組成回應 JSON:

```json
{
  "response": "Flask 是一個輕量級的 Python 網頁框架...",
  "sources": [
    {
      "question": "Flask 是什麼?",
      "category": "程式設計",
      "similarity": 0.95
    },
    {
      "question": "如何安裝 Flask?",
      "category": "程式設計",
      "similarity": 0.72
    },
    {
      "question": "Flask 與 Django 的差異",
      "category": "程式設計",
      "similarity": 0.65
    }
  ],
  "timestamp": "2025-01-19 14:30:00"
}
```

**步驟 7:前端顯示結果**

前端接收到回應後,將 AI 的答案顯示在對話區域,並在下方顯示「參考來源」區塊,列出知識庫中被參考的內容及其相似度。

整個流程從使用者按下發送到看到答案,通常只需要 2-3 秒,其中大部分時間是花在 AI 模型生成回應上。RAG 的檢索過程非常快,通常不到 1 秒就能完成。

### 專案檔案結構

最後,讓我們看看專案的檔案組織結構:

```
CH3_打造RAG知識庫問答平台/
│
├── app.py                      # Flask 後端主程式(約 800 行)
├── requirements.txt            # Python 套件依賴清單
├── README.md                   # 專案說明文件
│
├── templates/
│   └── index.html             # 前端 HTML 模板(約 600 行)
│
├── static/
│   ├── style.css              # CSS 樣式表(約 500 行)
│   └── script.js              # JavaScript 前端邏輯(約 700 行)
│
├── data/
│   ├── knowledge_base.json    # 本地知識庫儲存(動態生成)
│   └── knowledge_base_example.csv  # 範例知識庫(約 50 筆資料)
│
├── gas_scripts/
│   ├── 知識庫API.gs           # Google Apps Script 程式碼
│   └── 部署說明.md            # Google Sheets 整合說明
│
└── venv/                       # 虛擬環境(執行 venv 指令後產生)
```

每個檔案都有明確的職責:

- **app.py**:整個系統的「大腦」,處理所有後端邏輯
- **templates/index.html**:網頁的「骨架」,定義畫面結構
- **static/style.css**:網頁的「外觀」,讓介面美觀易用
- **static/script.js**:前端的「神經系統」,處理使用者互動
- **data/knowledge_base.json**:系統的「記憶體」,儲存所有知識
- **data/knowledge_base_example.csv**:範例資料,幫助快速上手

這種模組化的結構讓每個檔案的大小都保持在可管理的範圍內(除了 app.py 較大外,其他檔案都在 700 行以內),也讓我們在修改某個功能時,能夠快速定位到對應的檔案。

### 架構設計的考量

為什麼要採用這樣的架構設計?這裡有幾個重要的考量:

**簡單性優先:**沒有使用複雜的微服務架構或訊息佇列,所有功能都整合在一個 Flask 應用中。這讓初學者容易理解全貌,也降低了部署的複雜度。

**可擴展性:**雖然目前是單一應用,但架構設計上已經為未來的擴展預留空間。例如,RAG 檢索邏輯可以輕易抽離成獨立模組,知識庫可以從 JSON 檔案遷移到資料庫,前端可以改用 React 等框架重寫。

**學習友善:**選用的技術都是業界常用且學習資源豐富的,像是 Flask、Pandas、Sentence Transformers 等,學會這些技術後,可以應用到其他專案。

**成本效益:**不需要昂貴的硬體或雲端服務,一台普通電腦就能跑起來。也不需要訓練自己的 AI 模型,直接使用現成的 OpenAI/Google API 和 Sentence Transformers 模型。

這樣的架構設計,讓我們能夠在「簡單易學」與「功能完整」之間取得平衡,非常適合作為學習 RAG 技術的起點。

---

## 單元 4：向量嵌入與相似度搜尋原理

在快速部署和整體架構的介紹之後,現在讓我們深入探討 RAG 技術最核心的部分:向量嵌入(Vector Embedding)與相似度搜尋(Similarity Search)。這兩項技術決定了系統能否準確地找到相關知識,是整個 RAG 系統的「靈魂」。

### 什麼是向量嵌入?

在日常生活中,我們用文字來表達意思,但對電腦來說,文字只是一串字元,它無法「理解」文字的意義。向量嵌入技術就是要解決這個問題:將文字轉換成一串數字(向量),而且這些數字能夠「表達」文字的語意。

想像一下,假設我們要用數字來表達水果的特性。我們可以定義兩個維度:「甜度」和「酸度」,每個水果就可以用一對數字來表示。例如:

- 蘋果:[5, 3] (甜度 5,酸度 3)
- 檸檬:[2, 9] (甜度 2,酸度 9)
- 西瓜:[8, 1] (甜度 8,酸度 1)
- 橘子:[6, 4] (甜度 6,酸度 4)

這樣一來,我們就能用數字來比較水果。蘋果 [5, 3] 和橘子 [6, 4] 的數字比較接近,代表它們的特性相似;而蘋果和檸檬 [2, 9] 的數字差很多,代表特性差異大。

向量嵌入做的就是類似的事情,只是它不是用兩個維度,而是用幾百個維度來表達文字的語意。本專案使用的 `paraphrase-multilingual-MiniLM-L12-v2` 模型,會將每個句子轉換成 384 個數字組成的向量。這 384 個數字涵蓋了句子的各種語意特徵,像是主題、情感、語氣、專業程度等等。

**為什麼向量嵌入這麼重要?**

傳統的關鍵字搜尋有很大的限制。假設知識庫中有一筆資料:「Flask 是一個 Python 網頁框架」,如果使用者問「什麼是 Flask?」,關鍵字搜尋可以找到;但如果問「Flask 這個東西是幹嘛的?」,因為措辭不同,關鍵字搜尋可能就找不到了。

向量嵌入解決了這個問題。無論使用者用什麼樣的措辭,只要語意相近,轉換出來的向量就會相似。「什麼是 Flask?」、「Flask 是什麼?」、「Flask 這個東西是幹嘛的?」、「請介紹一下 Flask」,這些問題的向量都會很接近,系統就能準確地找到相關答案。

### 向量嵌入的實作

在我們的專案中,向量嵌入是透過 Sentence Transformers 套件實現的。讓我們看看 `app.py:47-54` 中的核心程式碼:

```python
def init_embedding_model():
    """初始化 Embedding 模型"""
    global embedding_model
    if embedding_model is None:
        print("正在載入 Embedding 模型...")
        embedding_model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
        print("Embedding 模型載入完成！")
    return embedding_model
```

這段程式碼做了幾件事:

**載入預訓練模型:**`SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')` 會載入一個已經訓練好的模型。這個模型是由 Hugging Face 提供的,它已經學習了大量多語言文本的語意特徵,包含中文、英文、日文等 50 多種語言。

**全域快取:**使用 `global embedding_model` 將模型儲存為全域變數,這樣模型只需要載入一次,後續的向量轉換就可以直接使用,不用重複載入,大幅提升效能。

**延遲載入:**模型不是在程式啟動時就載入,而是在第一次需要時才載入。這樣的設計讓伺服器啟動更快,只有當真正需要進行向量轉換時,才會花時間載入模型。

當知識庫有新增或修改時,系統會呼叫 `app.py:83-89` 的 `update_embeddings()` 函式來更新所有知識的向量:

```python
def update_embeddings():
    """更新知識庫的 embeddings"""
    global embeddings
    model = init_embedding_model()
    texts = [f"{item.get('question', '')} {item.get('answer', '')}" for item in knowledge_base]
    embeddings = model.encode(texts)
    print(f"已生成 {len(embeddings)} 個 embeddings")
```

這段程式碼的重點是:

**組合問答文字:**`f"{item.get('question', '')} {item.get('answer', '')}"` 將每筆知識的問題和答案組合在一起。這樣做的好處是,不管使用者的問法接近問題還是答案,都能被搜尋到。

**批次轉換:**`model.encode(texts)` 一次處理所有文字,轉換成向量陣列。批次處理的效率比逐一轉換高得多,特別是當知識庫有幾百筆資料時,差異會很明顯。

**結果快取:**轉換後的向量儲存在全域變數 `embeddings` 中,這樣在搜尋時就不需要重新計算,直接使用即可。

### 相似度搜尋的運作

有了向量嵌入後,下一個問題是:如何判斷兩個向量是否相似?這就需要用到「相似度計算」。最常用的方法是「餘弦相似度」(Cosine Similarity)。

**餘弦相似度的概念**

餘弦相似度衡量的是兩個向量的「方向」有多接近。想像兩個向量都是從原點出發的箭頭,如果兩個箭頭指向的方向幾乎一樣,代表它們很相似;如果指向完全不同的方向,代表不相似。

餘弦相似度的值介於 -1 到 1 之間:
- **1.0**:完全相同的方向,代表語意幾乎一致
- **0.5-0.9**:方向相近,代表語意相關
- **0.0**:完全不相關
- **負值**:方向相反,代表語意對立(在文字相似度中很少出現)

在實務應用中,我們通常設定一個「相似度門檻」。在本專案中,門檻設定為 0.3,也就是說,只有相似度大於 0.3 的知識才會被採納為參考資料。這個數值是經過實驗調整的,太高會漏掉相關內容,太低會納入不相關的內容。

**相似度搜尋的實作**

讓我們看看 `app.py:91-113` 的 `search_knowledge_base()` 函式,這是整個 RAG 系統最核心的函式:

```python
def search_knowledge_base(query, top_k=3):
    """在知識庫中搜尋相關內容"""
    if not knowledge_base or len(embeddings) == 0:
        return []

    model = init_embedding_model()
    query_embedding = model.encode([query])

    # 計算相似度
    similarities = cosine_similarity(query_embedding, embeddings)[0]

    # 取得前 k 個最相關的結果
    top_indices = np.argsort(similarities)[::-1][:top_k]

    results = []
    for idx in top_indices:
        if similarities[idx] > 0.3:  # 相似度閾值
            results.append({
                'data': knowledge_base[idx],
                'similarity': float(similarities[idx])
            })

    return results
```

讓我們逐步分析這段程式碼的運作流程:

**第 1 步:檢查知識庫**

```python
if not knowledge_base or len(embeddings) == 0:
    return []
```

如果知識庫是空的,或是向量還沒有生成,就直接回傳空陣列,避免後續的計算出錯。

**第 2 步:將問題轉換成向量**

```python
model = init_embedding_model()
query_embedding = model.encode([query])
```

使用相同的模型,將使用者的問題轉換成向量。注意 `[query]` 是一個陣列,因為 `encode()` 函式設計成可以一次處理多個文字,所以即使只有一個問題,也要包裝成陣列。

**第 3 步:計算相似度**

```python
similarities = cosine_similarity(query_embedding, embeddings)[0]
```

這是最關鍵的一行。`cosine_similarity()` 是 scikit-learn 提供的函式,它會計算問題向量與每一個知識庫向量之間的餘弦相似度,回傳一個陣列,陣列的每個元素代表問題與對應知識的相似度。

舉例來說,如果知識庫有 50 筆資料,`similarities` 就會是一個包含 50 個數字的陣列,像是 `[0.92, 0.15, 0.68, 0.33, ...]`,每個數字表示問題與該筆知識的相似度。

**第 4 步:排序並取前 k 筆**

```python
top_indices = np.argsort(similarities)[::-1][:top_k]
```

這行程式碼做了三件事:

1. `np.argsort(similarities)`:將相似度由小到大排序,回傳的是「索引」陣列。例如 `[0.92, 0.15, 0.68]` 排序後的索引是 `[1, 2, 0]`(第 1 個最小,第 2 個中等,第 0 個最大)。

2. `[::-1]`:將陣列反轉,變成由大到小。上面的例子會變成 `[0, 2, 1]`。

3. `[:top_k]`:取前 k 個。如果 `top_k=3`,就取前 3 個相似度最高的索引。

**第 5 步:篩選並回傳結果**

```python
results = []
for idx in top_indices:
    if similarities[idx] > 0.3:  # 相似度閾值
        results.append({
            'data': knowledge_base[idx],
            'similarity': float(similarities[idx])
        })
```

遍歷排序後的索引,但只有相似度大於 0.3 的才會被納入結果。這樣可以避免相似度太低、幾乎不相關的知識被誤判為參考資料。

每個結果包含兩個部分:
- `data`:知識庫的完整資料(問題、答案、分類等)
- `similarity`:相似度分數,前端會用這個數字顯示百分比

### 向量嵌入的優勢與限制

理解了技術細節後,讓我們總結一下向量嵌入相對於傳統關鍵字搜尋的優勢:

**語意理解:**能夠理解句子的意思,不受措辭限制。「什麼是 Flask?」和「Flask 是幹嘛用的?」會被視為相同的問題。

**多語言支援:**我們使用的模型支援多語言,中英文混用也能正確處理。

**模糊匹配:**即使問題描述不完全準確,只要大致意思對,也能找到相關內容。

**語意相近性:**能夠找到「概念相關」的內容,不是只有「字面相同」的內容。例如搜尋「Python 框架」可能會找到 Flask、Django 等相關知識。

但向量嵌入也有一些限制:

**模型大小:**Embedding 模型需要幾百 MB 的空間,首次下載需要時間和穩定的網路。

**運算成本:**將文字轉換成向量需要運算,雖然現代硬體已經很快,但如果知識庫有上萬筆資料,更新向量還是需要一些時間。

**語意飄移:**有時候語意判斷不一定完全準確,特別是在專業術語或特定領域時,可能會有誤判。

**無法處理精確匹配:**如果使用者要找的是「特定的產品編號」或「精確的日期」,向量搜尋反而不如關鍵字搜尋精準。

在實務應用中,有時會結合向量搜尋和關鍵字搜尋,兩者各取所長,達到最佳效果。

### 實際運作範例

讓我們用一個具體的例子來理解整個流程:

**場景:**使用者問「如何部署 Flask 應用?」

**步驟 1:**系統將問題「如何部署 Flask 應用?」轉換成一個 384 維的向量,例如 `[0.12, -0.34, 0.56, ..., 0.23]`(實際向量很長,這裡只是示意)。

**步驟 2:**系統將這個向量與知識庫中所有知識的向量進行比對。假設知識庫有 50 筆資料,就會計算 50 個相似度分數。

**步驟 3:**計算結果可能是這樣:
- 知識 #12「Flask 如何部署到 Render 平台?」:相似度 0.87
- 知識 #25「部署 Python 網頁應用的步驟」:相似度 0.72
- 知識 #8「Flask 是什麼?」:相似度 0.65
- 知識 #3「Python 虛擬環境設定」:相似度 0.42
- 其他知識:相似度 < 0.3

**步驟 4:**系統取相似度最高的前 3 筆,且相似度 > 0.3:
- 知識 #12(0.87)
- 知識 #25(0.72)
- 知識 #8(0.65)

**步驟 5:**系統將這 3 筆知識的內容整合成上下文,提供給 AI:

```
參考資料:

[資料 1]
問題:Flask 如何部署到 Render 平台?
答案:首先在 Render 建立新的 Web Service...

[資料 2]
問題:部署 Python 網頁應用的步驟
答案:第一步是建立 requirements.txt...

[資料 3]
問題:Flask 是什麼?
答案:Flask 是一個輕量級的 Python 網頁框架...
```

**步驟 6:**AI 基於這些參考資料生成答案,並在回答中引用來源:「根據知識庫資料,部署 Flask 應用主要有以下步驟...[資料1][資料2]...」

**步驟 7:**前端顯示 AI 的回答,並在下方列出參考來源,顯示相似度:87%、72%、65%。使用者可以清楚看到答案的依據。

透過這個完整的流程,我們可以看到向量嵌入和相似度搜尋如何讓 RAG 系統準確地找到相關知識,並提供可靠的答案。

> 【註記】請製作「向量相似度搜尋流程圖」,命名為 `rag_vector_search_flow.png`。圖中應包含:問題向量化、相似度計算、排序篩選、上下文組成、AI 生成回答等步驟。

---

## 單元 5：後端程式碼解析 - Flask API 設計

理解了 RAG 的核心技術後,現在讓我們深入後端程式碼,看看整個系統是如何組織的。本節將解析 `app.py` 的設計邏輯,讓你了解 Flask 如何處理 API 請求、如何整合 AI 服務,以及如何實現知識庫的管理功能。

### Flask 應用程式的初始化

`app.py` 的開頭定義了整個應用程式的基礎設定。讓我們看看 `app.py:1-26` 的初始化程式碼:

```python
from flask import Flask, render_template, request, jsonify, session, send_file
from flask_cors import CORS
import openai
import google.generativeai as genai
# ... 其他 import

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
CORS(app)

# 全域變數
knowledge_base = []
embeddings = []
embedding_model = None
google_sheets_client = None
```

**Flask 應用程式建立:**`Flask(__name__)` 建立一個 Flask 應用程式實例,`__name__` 讓 Flask 知道從哪裡尋找模板和靜態檔案。

**Secret Key 設定:**`app.secret_key = secrets.token_hex(16)` 生成一個隨機的密鑰,這是 Flask session 功能所需的。雖然目前專案沒有大量使用 session,但這是 Flask 應用的標準設定。

**CORS 啟用:**`CORS(app)` 啟用跨域資源共享,讓前端可以從不同的網域向後端發送請求。這在開發階段特別重要,因為前端和後端可能運行在不同的埠號。

**全域變數定義:**
- `knowledge_base`:儲存所有知識庫資料的陣列
- `embeddings`:儲存對應向量的陣列
- `embedding_model`:Sentence Transformers 模型實例
- `google_sheets_client`:Google Sheets API 客戶端(用於試算表整合)

使用全域變數的好處是這些資料在記憶體中持久存在,不會因為每次請求而重新載入,大幅提升效能。

### 角色設定與個性化

`app.py:28-45` 定義了不同的 AI 角色設定:

```python
ROLES = {
    "專業導師": {
        "system_prompt": "你是一位專業、耐心的導師，擅長用清晰易懂的方式解釋複雜概念...",
        "color": "#FFE4B5"
    },
    "程式撰寫助理": {
        "system_prompt": "你是一位經驗豐富的程式開發專家...",
        "color": "#E0F7FA"
    },
    # ... 其他角色
}
```

這個設計讓使用者可以根據需求切換不同的 AI 角色。每個角色都有自己的 `system_prompt`(系統提示詞)和 `color`(顯示顏色)。系統提示詞會影響 AI 的回答風格,例如「專業導師」會用教學的口吻,「幽默風趣的聊天夥伴」則會用輕鬆有趣的方式回應。

### 核心 API:聊天功能

最重要的 API 端點是 `/api/chat`,它處理使用者的問答請求並整合 RAG 功能。讓我們仔細分析 `app.py:138-205` 的 `chat()` 函式:

```python
@app.route('/api/chat', methods=['POST'])
def chat():
    """AI 聊天 API（整合 RAG）"""
    try:
        data = request.json
        message = data.get('message')
        api_key = data.get('api_key')
        api_type = data.get('api_type')
        model_name = data.get('model_name')
        role = data.get('role', '知識庫助理')
        history = data.get('history', [])
        use_rag = data.get('use_rag', True)
```

**路由定義:**`@app.route('/api/chat', methods=['POST'])` 定義了這個函式處理的路徑和 HTTP 方法。只接受 POST 請求,因為我們需要從請求體中讀取資料。

**參數提取:**從 `request.json` 中提取所有必要的參數:
- `message`:使用者的問題
- `api_key`:AI 服務的 API 金鑰
- `api_type`:使用 OpenAI 還是 Google
- `model_name`:具體的模型名稱(如 gpt-4o、gemini-2.5-flash)
- `role`:AI 角色
- `history`:對話歷史
- `use_rag`:是否啟用 RAG 檢索

**RAG 檢索邏輯:**

```python
context = ""
sources = []
if use_rag and knowledge_base:
    search_results = search_knowledge_base(message)
    if search_results:
        context = "\n\n參考資料：\n"
        for i, result in enumerate(search_results, 1):
            item = result['data']
            context += f"\n[資料 {i}]\n"
            context += f"問題：{item.get('question', '')}\n"
            context += f"答案：{item.get('answer', '')}\n"
            # ... 組成 sources 陣列
```

如果啟用了 RAG(`use_rag=True`)且知識庫不為空,系統會:

1. 呼叫 `search_knowledge_base(message)` 搜尋相關知識
2. 將檢索到的知識組成「參考資料」文字區塊
3. 同時建立 `sources` 陣列,儲存來源資訊供前端顯示

如果找不到相關資料,系統會回傳提示訊息,告訴使用者知識庫中沒有相關內容:

```python
else:
    return jsonify({
        'response': '抱歉,我在知識庫中找不到相關的資料來回答您的問題...',
        'sources': [],
        'no_knowledge': True,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }), 200
```

**組成 AI 提示詞:**

```python
role_config = ROLES.get(role, ROLES['知識庫助理'])
system_prompt = role_config['system_prompt']

if use_rag and context:
    system_prompt += f"\n\n【重要】請「嚴格」根據以下知識庫內容回答問題...{context}"
```

系統會根據選擇的角色獲取對應的 `system_prompt`,如果有檢索到知識庫內容,就將參考資料附加到提示詞中,並強調 AI 要「嚴格根據知識庫內容」回答,避免 AI 憑藉自己的知識擅自發揮。

**呼叫 AI API:**

```python
if api_type == 'openai':
    response_text = call_openai(api_key, message, system_prompt, history, model_name)
elif api_type == 'google':
    response_text = call_google(api_key, message, system_prompt, history, model_name)
```

根據使用者選擇的 API 類型,呼叫對應的函式。這兩個函式分別在 `app.py:207-242` 定義。

**OpenAI API 呼叫:**

```python
def call_openai(api_key, message, system_prompt, history, model_name="gpt-4o"):
    client = openai.OpenAI(api_key=api_key)

    messages = [{"role": "system", "content": system_prompt}]

    for item in history:
        messages.append({"role": "user", "content": item['user']})
        messages.append({"role": "assistant", "content": item['assistant']})

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.7,
        max_tokens=2000
    )

    return response.choices[0].message.content
```

這段程式碼展示了 OpenAI API 2.x 版本的標準呼叫方式:

1. 建立 OpenAI 客戶端實例
2. 組成訊息陣列,包含系統提示詞、對話歷史、當前問題
3. 呼叫 `chat.completions.create()` 發送請求
4. 從回應中提取 AI 生成的文字

`temperature=0.7` 控制回答的創意度,0.7 是一個平衡值,既不會太死板也不會太天馬行空。`max_tokens=2000` 限制回答的長度,避免生成過長的文字。

**Google Gemini API 呼叫:**

```python
def call_google(api_key, message, system_prompt, history, model_name="gemini-2.5-flash"):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)

    full_prompt = f"{system_prompt}\n\n"

    for item in history:
        full_prompt += f"使用者: {item['user']}\n助理: {item['assistant']}\n\n"

    full_prompt += f"使用者: {message}\n助理: "

    response = model.generate_content(full_prompt)
    return response.text
```

Google 的 API 設計較簡單,直接將所有內容組成一個完整的提示詞,然後呼叫 `generate_content()` 生成回應。

### 知識庫管理 API

除了聊天功能,系統還提供了完整的知識庫管理 API。讓我們看看幾個關鍵端點:

**取得知識庫列表(`app.py:244-251`)**

```python
@app.route('/api/knowledge-base', methods=['GET'])
def get_knowledge_base():
    """取得知識庫列表"""
    return jsonify({
        'data': knowledge_base,
        'count': len(knowledge_base),
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
```

這是一個簡單的 GET 請求,回傳整個知識庫陣列和統計資訊。前端會用這個 API 來載入知識庫管理介面的表格。

**新增知識(`app.py:253-271`)**

```python
@app.route('/api/knowledge-base', methods=['POST'])
def add_knowledge():
    """新增知識庫項目"""
    try:
        data = request.json
        item = {
            'id': len(knowledge_base) + 1,
            'question': data.get('question', ''),
            'answer': data.get('answer', ''),
            'category': data.get('category', '一般'),
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        knowledge_base.append(item)
        update_embeddings()
        save_knowledge_base_to_json()

        return jsonify({'success': True, 'item': item})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

新增知識的流程:

1. 從請求中提取問題、答案、分類
2. 建立新的知識項目,ID 自動遞增
3. 加入 `knowledge_base` 陣列
4. **重新生成向量**(`update_embeddings()`):這很重要,確保新知識也能被搜尋到
5. **儲存到檔案**(`save_knowledge_base_to_json()`):持久化資料,避免重啟後遺失

**批次匯入(`app.py:306-353`)**

```python
@app.route('/api/knowledge-base/upload', methods=['POST'])
def upload_knowledge_base():
    """上傳知識庫檔案（CSV/Excel）"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': '沒有上傳檔案'}), 400

        file = request.files['file']

        # 讀取檔案
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.filename.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file)

        # 批次新增
        added_count = 0
        for _, row in df.iterrows():
            item = {
                'id': len(knowledge_base) + 1,
                'question': str(row['question']),
                'answer': str(row['answer']),
                'category': str(row.get('category', '一般')),
                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            knowledge_base.append(item)
            added_count += 1

        update_embeddings()
        save_knowledge_base_to_json()

        return jsonify({
            'success': True,
            'added_count': added_count,
            'total_count': len(knowledge_base)
        })
```

批次匯入功能使用 Pandas 來處理 CSV 和 Excel 檔案:

1. 檢查檔案是否存在
2. 根據副檔名選擇對應的讀取函式(`read_csv` 或 `read_excel`)
3. 驗證必要欄位(`question`、`answer`)是否存在
4. 逐行讀取並建立知識項目
5. 批次完成後,一次性更新向量和儲存檔案(比每筆都更新效率高得多)

**知識庫搜尋(`app.py:424-443`)**

```python
@app.route('/api/knowledge-base/search', methods=['POST'])
def search_kb():
    """搜尋知識庫"""
    try:
        data = request.json
        query = data.get('query', '')
        top_k = data.get('top_k', 5)

        results = search_knowledge_base(query, top_k)

        return jsonify({
            'results': results,
            'count': len(results)
        })
```

這個端點允許前端直接使用向量搜尋功能,在知識庫管理介面中提供智慧搜尋。使用者可以輸入關鍵字,系統會用語意搜尋找到相關知識,比傳統的字串比對更準確。

### 資料持久化

知識庫的資料需要持久化儲存,否則重啟伺服器後就會遺失。`app.py:56-81` 實作了載入和儲存功能:

**載入知識庫:**

```python
def load_knowledge_base_from_json(file_path='data/knowledge_base.json'):
    """從 JSON 檔案載入知識庫"""
    global knowledge_base, embeddings
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                knowledge_base = json.load(f)
            # 重新生成 embeddings
            if knowledge_base:
                update_embeddings()
            return True
    except Exception as e:
        print(f"載入知識庫失敗: {e}")
    return False
```

載入時不僅讀取 JSON 檔案,還會重新生成向量。這是因為向量不適合儲存在 JSON 中(體積太大),每次啟動時重新計算是更好的選擇。

**儲存知識庫:**

```python
def save_knowledge_base_to_json(file_path='data/knowledge_base.json'):
    """儲存知識庫到 JSON 檔案"""
    try:
        os.makedirs('data', exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(knowledge_base, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"儲存知識庫失敗: {e}")
        return False
```

`ensure_ascii=False` 確保中文字元正確儲存,不會被轉換成 Unicode 編碼。`indent=2` 讓 JSON 檔案格式化,方便人工閱讀和除錯。

**程式啟動時自動載入:**

```python
# app.py:450-451
load_knowledge_base_from_json()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
```

在程式最後,會自動呼叫 `load_knowledge_base_from_json()`,確保伺服器啟動時就載入已儲存的知識庫資料。

### Flask 應用程式的優勢

透過這個專案,我們可以看到 Flask 的幾個主要優勢:

**簡單直覺:**定義 API 端點只需要一個裝飾器 `@app.route()`,非常直覺。

**彈性設計:**不像 Django 有固定的專案結構,Flask 讓你自由組織程式碼。

**輕量快速:**Flask 核心很小,只提供必要功能,額外需求可以透過套件擴充(如 Flask-CORS)。

**易於測試:**每個端點都是獨立的函式,容易單獨測試和除錯。

這些特性讓 Flask 成為建立中小型 API 服務的理想選擇。

> 【註記】請截圖「Flask API 測試工具畫面」,命名為 `rag_flask_api_test.png`。可使用 Postman 或 Insomnia 測試 `/api/chat` 端點,顯示請求和回應的 JSON 格式。

---

## 單元 6：前端介面與互動設計

完成了後端 API 的探討後,現在讓我們轉向前端,看看使用者介面是如何設計的,以及前端如何與後端溝通。本節將解析 `static/script.js` 的核心邏輯,讓你理解一個現代化網頁應用的前端架構。

### JavaScript 的全域狀態管理

`script.js` 的開頭定義了整個前端應用程式的狀態,這些變數在整個應用中共享,讓不同函式能夠存取和修改資料。讓我們看看 `script.js:1-15` 的全域變數定義:

```javascript
// 全域變數
let chatHistory = [];
let knowledgeBase = [];
let currentEditId = null;
let selectedFile = null;

// 設定相關
let config = {
    apiKey: localStorage.getItem('apiKey') || '',
    apiType: localStorage.getItem('apiType') || 'google',
    modelName: localStorage.getItem('modelName') || 'gemini-2.5-flash',
    aiRole: localStorage.getItem('aiRole') || '知識庫助理',
    useRAG: localStorage.getItem('useRAG') !== 'false',
    gasApiUrl: localStorage.getItem('gasApiUrl') || ''
};
```

**狀態變數:**
- `chatHistory`:儲存對話歷史,讓 AI 能夠記住上下文
- `knowledgeBase`:前端快取的知識庫資料
- `currentEditId`:正在編輯的知識項目 ID
- `selectedFile`:使用者選擇要上傳的檔案

**設定物件:**`config` 物件儲存所有使用者設定,並使用 `localStorage` 實現持久化。`localStorage` 是瀏覽器提供的本地儲存功能,資料會保存在使用者的電腦上,即使關閉瀏覽器也不會遺失。

注意 `useRAG: localStorage.getItem('useRAG') !== 'false'` 這行,因為 localStorage 只能儲存字串,所以用 `!== 'false'` 來判斷,預設為 `true`(除非明確設為 `'false'` 字串)。

### DOM 元素快取

為了提升效能和程式碼可讀性,`script.js:17-85` 將所有常用的 DOM 元素預先快取在 `elements` 物件中:

```javascript
const elements = {
    settingsPanel: document.getElementById('settingsPanel'),
    kbPanel: document.getElementById('kbPanel'),
    messages: document.getElementById('messages'),
    messageInput: document.getElementById('messageInput'),
    sendBtn: document.getElementById('sendBtn'),
    // ... 更多元素
};
```

這種做法的好處是:

**效能提升:**`document.getElementById()` 需要在整個 DOM 樹中搜尋元素,雖然很快,但如果頻繁呼叫還是有成本。預先快取後,只需要搜尋一次。

**程式碼簡潔:**使用 `elements.sendBtn` 比每次都寫 `document.getElementById('sendBtn')` 簡潔得多。

**易於維護:**如果元素 ID 改變,只需要修改 `elements` 物件的定義,不用到處修改程式碼。

### 事件監聽器的初始化

`script.js:88-169` 的 `initEventListeners()` 函式設定了所有互動事件:

```javascript
function initEventListeners() {
    elements.sendBtn.addEventListener('click', sendMessage);
    elements.messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    elements.btnAddKB.addEventListener('click', () => openKBDialog());
    elements.btnImportCSV.addEventListener('click', () => openPanel('uploadDialog'));

    // 拖放上傳
    elements.uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        elements.uploadArea.classList.add('dragover');
    });
    // ...
}
```

這個函式展示了幾種常見的事件處理模式:

**按鈕點擊:**最基本的事件,點擊按鈕執行對應函式。

**鍵盤事件:**監聽 Enter 鍵送出訊息,但要排除 Shift+Enter(讓使用者能夠換行)。`e.preventDefault()` 阻止預設行為(例如表單提交)。

**拖放事件:**實現檔案拖放上傳功能,包含 `dragover`(拖曳經過)、`dragleave`(拖曳離開)、`drop`(放下檔案)三個事件。

**API 類型切換:**當使用者切換 AI 服務時,自動更新可用的模型選項。

### 核心功能:發送訊息

`script.js:232-292` 的 `sendMessage()` 函式是整個前端最核心的功能,處理使用者提問的完整流程:

```javascript
async function sendMessage() {
    const message = elements.messageInput.value.trim();
    if (!message) return;

    if (!config.apiKey) {
        showNotification('請先設定 API Key', 'error');
        openPanel('settingsPanel');
        return;
    }

    elements.messageInput.value = '';
    elements.sendBtn.disabled = true;

    addMessage(message, 'user');
    const loadingMsg = addLoadingMessage();

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message: message,
                api_key: config.apiKey,
                api_type: config.apiType,
                model_name: config.modelName,
                role: config.aiRole,
                history: chatHistory,
                use_rag: config.useRAG
            })
        });

        const data = await response.json();
        loadingMsg.remove();

        if (data.error) {
            showNotification(data.error, 'error');
            addMessage('抱歉，發生錯誤：' + data.error, 'assistant');
        } else {
            addMessage(data.response, 'assistant', data.sources);
            chatHistory.push({
                user: message,
                assistant: data.response
            });
        }
    } catch (error) {
        loadingMsg.remove();
        showNotification('發送失敗: ' + error.message, 'error');
    } finally {
        elements.sendBtn.disabled = false;
    }
}
```

讓我們逐步分析這個函式的流程:

**第 1 步:驗證與準備**

檢查訊息是否為空、API Key 是否已設定。如果沒有 API Key,顯示提示並開啟設定面板。清空輸入框、禁用發送按鈕(避免重複發送)。

**第 2 步:更新 UI**

呼叫 `addMessage(message, 'user')` 將使用者訊息加入對話區域,呼叫 `addLoadingMessage()` 顯示「AI 正在思考中...」的載入動畫。

**第 3 步:發送 HTTP 請求**

使用 `fetch` API 發送 POST 請求到後端的 `/api/chat` 端點。請求體包含所有必要資訊:問題、API Key、模型設定、對話歷史、RAG 開關等。

`await` 關鍵字讓程式等待伺服器回應,這是處理非同步操作的現代 JavaScript 語法。

**第 4 步:處理回應**

收到回應後,先移除載入動畫。如果有錯誤(`data.error`),顯示錯誤提示;否則顯示 AI 的回答和參考來源,並更新對話歷史。

**第 5 步:錯誤處理與復原**

`try-catch` 捕捉可能的錯誤(例如網路斷線、伺服器錯誤)。`finally` 區塊確保無論成功或失敗,都會重新啟用發送按鈕,讓使用者可以繼續對話。

### 訊息顯示與來源引用

`script.js:294-340` 的 `addMessage()` 函式負責將訊息顯示在對話區域,並且處理參考來源的顯示:

```javascript
function addMessage(content, type, sources = null) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;

    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.textContent = content;

    messageDiv.appendChild(contentDiv);

    // 顯示來源
    if (sources && sources.length > 0) {
        const sourcesDiv = document.createElement('div');
        sourcesDiv.className = 'message-sources';
        sourcesDiv.innerHTML = '<h4><i class="fas fa-book"></i> 參考來源:</h4>';

        sources.forEach((source, index) => {
            const sourceItem = document.createElement('div');
            sourceItem.className = 'source-item';
            sourceItem.innerHTML = `
                <strong>來源 ${index + 1}:</strong> ${source.question}
                <span class="similarity-badge">${(source.similarity * 100).toFixed(0)}% 相似</span>
                <div style="margin-top: 5px; color: #666; font-size: 12px;">
                    分類: ${source.category || '一般'}
                </div>
            `;
            sourcesDiv.appendChild(sourceItem);
        });

        messageDiv.appendChild(sourcesDiv);
    }

    elements.messages.appendChild(messageDiv);
    elements.messages.scrollTop = elements.messages.scrollHeight;
}
```

這個函式展示了如何動態建立 HTML 元素:

**建立訊息容器:**使用 `createElement()` 建立 `<div>` 元素,設定 class 名稱為 `message user` 或 `message assistant`,CSS 會根據不同 class 套用不同樣式。

**顯示參考來源:**如果有 `sources` 陣列,遍歷每個來源建立來源區塊。特別注意 `(source.similarity * 100).toFixed(0)}%`,將 0.87 這樣的相似度轉換成「87%」的顯示格式。

**自動捲動:**`elements.messages.scrollTop = elements.messages.scrollHeight` 讓對話區域自動捲動到最底部,確保新訊息可見。

### 知識庫管理功能

前端提供了完整的知識庫管理介面,讓使用者可以在網頁上直接操作知識庫。讓我們看看幾個關鍵函式:

**載入知識庫(`script.js:388-403`)**

```javascript
async function loadKnowledgeBase() {
    showLoading(true);
    try {
        const response = await fetch('/api/knowledge-base');
        const data = await response.json();

        knowledgeBase = data.data || [];
        renderKnowledgeBaseTable(knowledgeBase);
        updateStats(data);
    } catch (error) {
        showNotification('載入知識庫失敗: ' + error.message, 'error');
    } finally {
        showLoading(false);
    }
}
```

這是一個簡單的 GET 請求,從後端獲取知識庫資料,然後更新前端的表格和統計資訊。

**渲染表格(`script.js:405-436`)**

```javascript
function renderKnowledgeBaseTable(data) {
    if (data.length === 0) {
        elements.kbTableBody.innerHTML = `
            <tr>
                <td colspan="6" style="text-align: center; padding: 40px;">
                    <i class="fas fa-inbox" style="font-size: 48px; color: #ccc;"></i>
                    <p style="color: #999; margin-top: 10px;">暫無知識庫資料</p>
                </td>
            </tr>
        `;
        return;
    }

    elements.kbTableBody.innerHTML = data.map(item => `
        <tr>
            <td>${item.id}</td>
            <td>${item.question}</td>
            <td>${item.answer.substring(0, 100)}${item.answer.length > 100 ? '...' : ''}</td>
            <td>${item.category || '一般'}</td>
            <td style="font-size: 11px;">${item.created_at || '-'}</td>
            <td>
                <button class="action-btn btn-edit" onclick="editKnowledge(${item.id})">
                    <i class="fas fa-edit"></i> 編輯
                </button>
                <button class="action-btn btn-delete" onclick="deleteKnowledge(${item.id})">
                    <i class="fas fa-trash"></i> 刪除
                </button>
            </td>
        </tr>
    `).join('');
}
```

這個函式展示了如何用 JavaScript 動態生成表格:

**空狀態處理:**如果知識庫為空,顯示友善的提示訊息和圖示。

**陣列映射:**`data.map()` 將每筆資料轉換成一個 `<tr>` 字串,然後用 `.join('')` 串接成完整的 HTML。

**答案截斷:**`item.answer.substring(0, 100)` 只顯示答案的前 100 字元,避免表格過長。

**內聯事件:**按鈕的 `onclick="editKnowledge(${item.id})"` 是一種簡單但有效的事件綁定方式,適合動態生成的元素。

**檔案上傳(`script.js:575-607`)**

```javascript
async function uploadFile() {
    if (!selectedFile) return;

    const formData = new FormData();
    formData.append('file', selectedFile);

    showLoading(true);

    try {
        const response = await fetch('/api/knowledge-base/upload', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.success) {
            showNotification(`成功匯入 ${data.added_count} 筆資料`, 'success');
            closePanel('uploadDialog');
            loadKnowledgeBase();
        }
    } catch (error) {
        showNotification('上傳失敗: ' + error.message, 'error');
    } finally {
        showLoading(false);
    }
}
```

檔案上傳需要使用 `FormData` 物件,這是瀏覽器提供的專門用來處理檔案上傳的 API。不需要設定 `Content-Type` header,瀏覽器會自動設定為 `multipart/form-data`。

### 使用者體驗優化

專案中有許多提升使用者體驗的細節設計:

**載入動畫(`script.js:664-666`)**

```javascript
function showLoading(show) {
    elements.loadingOverlay.style.display = show ? 'flex' : 'none';
}
```

在等待伺服器回應時顯示半透明的載入遮罩,讓使用者知道系統正在處理,避免焦慮感。

**通知訊息(`script.js:669-691`)**

```javascript
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 25px;
        background: ${type === 'success' ? '#4CAF50' : type === 'error' ? '#f44336' : '#2196F3'};
        color: white;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        z-index: 10000;
        animation: slideIn 0.3s;
    `;
    notification.textContent = message;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}
```

這個函式實作了一個輕量級的通知系統,不需要額外套件。根據訊息類型(`success`、`error`、`info`)顯示不同顏色,3 秒後自動消失,搭配滑入滑出動畫,提升視覺體驗。

**歡迎訊息與快速操作(`script.js:356-386`)**

```javascript
function clearChat() {
    if (confirm('確定要清空對話記錄嗎？')) {
        chatHistory = [];
        elements.messages.innerHTML = `
            <div class="welcome-message">
                <i class="fas fa-robot" style="font-size: 64px; color: #4CAF50;"></i>
                <h2>歡迎使用 RAG 知識庫 AI 問答平台</h2>
                <p>我會根據知識庫內容為您提供精確的回答</p>
                <div class="quick-actions">
                    <button class="quick-btn" onclick="quickAction('管理')">
                        <i class="fas fa-database"></i> 管理知識庫
                    </button>
                    <button class="quick-btn" onclick="quickAction('設定')">
                        <i class="fas fa-cog"></i> 系統設定
                    </button>
                </div>
            </div>
        `;
    }
}
```

當對話區域為空時,顯示友善的歡迎訊息和快速操作按鈕,引導使用者開始使用系統。

### 前端架構的優勢

透過這個專案,我們可以看到現代前端開發的幾個最佳實踐:

**模組化函式:**每個功能都是獨立的函式,職責單一,易於測試和維護。

**狀態管理:**使用全域變數統一管理應用狀態,配合 localStorage 實現持久化。

**事件驅動:**透過事件監聽器處理使用者互動,保持程式流程清晰。

**非同步處理:**使用 `async/await` 處理 API 請求,程式碼簡潔易讀。

**錯誤處理:**完整的 try-catch 機制,確保錯誤不會導致整個應用崩潰。

**使用者回饋:**載入動畫、通知訊息、確認對話框等,讓使用者清楚知道系統狀態。

雖然這個專案沒有使用 React、Vue 等現代框架,但透過良好的程式設計,純 JavaScript 也能實現完整且易於維護的前端應用。

> 【註記】請截圖「瀏覽器開發者工具 - Network 面板」,命名為 `rag_network_panel.png`。畫面應顯示發送 `/api/chat` 請求的 Headers、Payload 和 Response,讓讀者理解前後端的資料交換格式。

---

## 單元 7：知識庫內容的品質管理

理解了系統的技術實作後,現在讓我們探討一個同樣重要但經常被忽略的主題:知識庫的品質管理。再先進的 RAG 技術,如果知識庫的內容品質不佳,系統的表現也會大打折扣。就像再厲害的廚師,如果食材不新鮮,也做不出美味的料理。本節將分享如何建立和維護高品質的知識庫。

### 為什麼知識庫品質如此重要?

在實際應用 RAG 系統的過程中,你可能會發現一個有趣的現象:系統有時候回答得很準確,有時候卻答非所問。這種不穩定的表現,通常不是技術問題,而是知識庫內容的問題。

**知識庫是 AI 的「教科書」**

當我們啟用 RAG 功能時,AI 就像是一個學生,在回答問題前先翻閱教科書(知識庫)找參考資料。如果教科書內容詳實、條理清晰,學生自然能給出好答案;但如果教科書內容含糊不清、錯誤百出,學生再聰明也無能為力。

**相似度搜尋的侷限**

雖然向量嵌入技術能夠進行語意搜尋,但它不是萬能的。如果知識庫中的問題描述不夠清楚,或是答案內容過於簡略,即使搜尋到了相關內容,AI 也無法給出完整的答案。而且,如果知識庫中有多筆內容都「有點相關但都不太精準」,反而會混淆 AI 的判斷。

**使用者信任度的建立**

RAG 系統的一大優勢是能夠顯示答案來源,讓使用者追溯資訊的依據。但如果使用者點開來源一看,發現知識庫的內容品質不佳,或是與 AI 的回答對不上,使用者對整個系統的信任就會下降。長期來看,這會嚴重影響系統的採用率。

### 高品質知識的特徵

那麼,什麼樣的知識庫內容才算高品質?讓我們透過對比來理解:

**問題的完整性**

❌ **不良範例:**「Flask?」
✅ **良好範例:**「Flask 是什麼?它有哪些主要特點?」

第一個問題太過簡略,使用者可能會用各種不同的方式提問,如「什麼是 Flask」、「Flask 框架介紹」、「Flask 的用途」等,但「Flask?」這個問題與這些提問的語意相似度都不會太高。

第二個問題完整且清晰,涵蓋了主要的提問方式,而且問題本身就包含了關鍵資訊,提高了被搜尋到的機會。

**答案的詳實度**

❌ **不良範例:**
問題:「如何安裝 Flask?」
答案:「用 pip 安裝。」

✅ **良好範例:**
問題:「如何安裝 Flask?」
答案:「安裝 Flask 需要以下步驟:1. 確認已安裝 Python 3.8 或以上版本 2. 開啟終端機 3. 執行指令 `pip install flask` 4. 等待安裝完成,出現 "Successfully installed" 訊息即表示成功。如果遇到權限問題,可能需要使用 `pip install --user flask` 或在虛擬環境中安裝。」

第一個答案雖然沒錯,但過於簡略,AI 很難基於這麼少的資訊產生完整的回答。第二個答案提供了完整的步驟、注意事項和可能的問題解決方案,AI 可以基於這些內容給出詳盡且實用的回答。

**資訊的準確性**

❌ **不良範例:**
問題:「Python 的最新版本是什麼?」
答案:「Python 的最新版本是 3.9。」(已過時的資訊)

✅ **良好範例:**
問題:「Python 的穩定版本建議」
答案:「建議使用 Python 3.10 或 3.11 版本,這些版本穩定且廣泛支援。實際的最新版本資訊請參考 Python 官方網站 python.org。」

第一個答案包含了具體的版本號,但這種資訊很容易過時,導致系統提供錯誤的資訊。第二個答案採用較通用的描述,並引導使用者查閱官方資訊,避免了時效性問題。

**避免重複與矛盾**

❌ **不良範例:**
- 問題1:「Flask 是什麼?」答案:「Flask 是一個 Python 框架。」
- 問題2:「什麼是 Flask?」答案:「Flask 是輕量級的網頁開發工具。」
- 問題3:「Flask 框架介紹」答案:「Flask 是用來建立 Web 應用的框架。」

這三筆知識在語意上非常相近,會導致向量搜尋時都被檢索出來,但答案的描述又有些微差異,可能會讓 AI 產生混淆或重複的內容。

✅ **良好範例:**
- 問題:「Flask 是什麼?它的主要特點有哪些?」
- 答案:「Flask 是一個用 Python 開發的輕量級網頁框架,主要特點包括:1. 核心功能簡潔,容易上手 2. 高度模組化,可根據需求擴充 3. 內建開發伺服器和除錯工具 4. 靈活的路由系統 5. 支援 Jinja2 模板引擎。Flask 適合用來建立中小型 Web 應用、API 服務等。」

將相似的問題合併成一筆完整的知識,避免重複,也讓答案更有系統性。

### 知識庫的組織策略

除了個別知識的品質,知識庫的整體組織方式也很重要。以下是幾個有效的策略:

**按主題分類**

使用「分類」欄位將知識庫內容系統化。例如:
- **技術文件**:程式語言、框架、工具的使用說明
- **操作流程**:具體的工作流程、步驟指南
- **FAQ**:常見問題與解答
- **政策規範**:公司政策、規則、標準
- **故障排除**:常見錯誤與解決方法

良好的分類不僅方便管理,也能在搜尋時提供額外的上下文資訊。使用者看到「參考來源:技術文件類」會比單純看到一個答案更有信心。

**建立知識層次**

知識庫可以包含不同深度的內容:

**第一層:概念性知識**
- 問題:「什麼是 RAG?」
- 答案:簡明扼要的定義和核心概念

**第二層:實作性知識**
- 問題:「如何實作 RAG 系統?」
- 答案:具體的步驟、技術選擇、程式範例

**第三層:深入性知識**
- 問題:「RAG 系統的向量相似度計算原理」
- 答案:技術細節、數學原理、最佳化技巧

這樣的層次設計能夠滿足不同背景使用者的需求。初學者問基本概念會得到簡單的答案,專業人士問技術細節會得到深入的解釋。

**保持資訊時效性**

定期審查知識庫內容,更新過時的資訊:

- **版本相關資訊**:軟體版本、API 變更等,需要定期更新
- **政策性內容**:公司政策、法規條文等,變更時立即更新
- **最佳實踐**:技術領域的最佳實踐會隨時間演進,需要追蹤
- **外部連結**:確認連結有效性,失效的連結要更新或移除

可以在知識項目中加入「更新時間」和「審查狀態」等欄位,建立定期審查機制。例如,每季度檢視一次所有知識,標記需要更新的項目。

### 知識庫的測試與優化

建立知識庫後,需要持續測試和優化。以下是幾個實用的方法:

**使用實際問題測試**

不要只是建立知識庫就結束了,要實際測試系統的表現。收集真實使用者可能提出的問題,輸入系統中測試:

1. **觀察搜尋結果**:系統找到的知識是否相關?相似度分數如何?
2. **檢視 AI 回答**:AI 的回答是否準確?是否完整?
3. **追蹤來源**:顯示的參考來源是否正確?

如果發現問題,可能的優化方向包括:
- 調整問題的措辭,增加關鍵字
- 豐富答案內容,提供更多資訊
- 合併或拆分知識項目
- 調整相似度門檻值(預設 0.3 可能需要根據實際情況調整)

**收集使用者回饋**

如果系統有多個使用者,建立回饋機制很重要:

- **評分系統**:讓使用者對答案的品質評分
- **回報錯誤**:提供簡單的方式讓使用者回報錯誤或不完整的答案
- **建議新增**:使用者可以建議新增哪些知識
- **使用分析**:追蹤哪些問題被頻繁提問,哪些知識經常被檢索

這些回饋能夠幫助你了解知識庫的盲點,持續改進內容。

**建立品質檢查清單**

在新增或修改知識時,使用檢查清單確保品質:

- [ ] 問題是否清晰完整?
- [ ] 答案是否詳實且準確?
- [ ] 是否包含必要的背景資訊?
- [ ] 是否有實際範例或步驟?
- [ ] 資訊是否為最新的?
- [ ] 分類是否正確?
- [ ] 是否與現有知識重複?
- [ ] 措辭是否容易理解?

養成使用檢查清單的習慣,能夠系統性地提升知識庫品質。

### 常見的知識庫問題與解決方案

在實務應用中,經常會遇到一些典型問題。讓我們看看如何解決:

**問題 1:使用者問的問題找不到答案**

**原因:**知識庫覆蓋範圍不足,或問題措辭與知識庫內容差異太大。

**解決方案:**
- 記錄所有「找不到答案」的問題
- 定期分析這些問題,識別知識缺口
- 優先補充高頻問題的知識
- 嘗試用不同的措辭表達同一個問題,增加命中率

**問題 2:搜尋到的知識不相關**

**原因:**相似度門檻設定太低,或知識的問題描述不夠精確。

**解決方案:**
- 檢視相似度分數,如果經常出現 0.3-0.5 這種低分結果,考慮提高門檻到 0.4
- 重新撰寫知識的問題,使用更精確的措辭
- 增加關鍵字,幫助向量嵌入捕捉正確的語意

**問題 3:AI 回答內容重複或混亂**

**原因:**檢索到的多筆知識內容重複或矛盾。

**解決方案:**
- 搜尋並合併語意相近的知識
- 確保每筆知識都有明確且獨特的焦點
- 減少 `top_k` 值(預設是 3,可以嘗試降低到 2)

**問題 4:答案太籠統,缺乏細節**

**原因:**知識庫的答案內容過於簡略。

**解決方案:**
- 豐富答案內容,加入具體步驟、範例、注意事項
- 將複雜問題拆分成多個子問題,每個都有詳細答案
- 在答案中加入「更多資訊請參考...」的延伸資源

### 知識庫管理的實踐建議

基於實務經驗,以下是一些具體的管理建議:

**起步階段(1-50 筆知識)**

當知識庫剛建立時,重點是「質量」而非「數量」:

- 從最常被問到的 20-30 個問題開始
- 每筆知識都要仔細撰寫,確保高品質
- 建立清楚的分類體系
- 測試每筆知識的檢索效果

**成長階段(50-200 筆知識)**

當知識庫逐漸擴充時,要開始系統化管理:

- 建立知識新增流程,確保品質一致性
- 定期審查舊知識,更新過時內容
- 開始追蹤使用數據,了解哪些知識最有價值
- 處理重複知識,保持資料庫整潔

**成熟階段(200 筆以上知識)**

當知識庫規模較大時,需要更進階的管理:

- 考慮引入專業的向量資料庫(如 ChromaDB、Pinecone)提升效能
- 建立知識審查團隊,定期檢視內容品質
- 實作更細緻的分類和標籤系統
- 使用分析工具追蹤知識庫的使用情況和效能指標

**協作管理**

如果有多人共同維護知識庫:

- 建立明確的編輯規範和格式指南
- 使用 Google 試算表進行協作,方便多人同時編輯
- 定期召開知識審查會議,討論需要新增或修改的內容
- 指派專人負責品質控制

### 知識庫品質的長期價值

投資時間建立高品質的知識庫,帶來的價值是長期且累積的:

**減少重複性問答**

一旦建立了完善的知識庫,相同的問題就不需要人工重複回答,大幅降低支援成本。而且,知識庫的答案是一致的,不會因為不同人回答而有差異。

**知識的累積與傳承**

知識庫成為組織的知識資產,即使有人員異動,重要的知識也不會流失。新人可以透過查詢知識庫快速上手,減少培訓成本。

**持續改進的基礎**

透過追蹤使用數據,可以了解哪些領域的知識最常被查詢,哪些答案最有幫助。這些洞察能夠指引組織的知識管理策略,形成良性循環。

記住,RAG 系統的成功,技術只是基礎,真正的關鍵在於知識庫的內容品質。就像圖書館的價值不在於建築本身,而在於館藏的書籍品質一樣。投入心力建立和維護高品質的知識庫,才能讓 RAG 系統發揮最大的價值。

> 【註記】請製作「知識庫品質優化流程圖」,命名為 `rag_kb_quality_flow.png`。圖中應包含:建立初始知識、測試檢索效果、收集使用者回饋、分析問題、優化內容、持續監控等循環流程。

---

## 單元 8：Google 試算表整合應用

到目前為止,我們都是在本地管理知識庫,透過網頁介面新增、編輯、匯入資料。但在實際應用中,你可能會需要更靈活的協作方式,讓團隊成員能夠共同維護知識庫,或是讓非技術人員也能輕鬆新增內容。這時候,Google 試算表就是一個理想的解決方案。

### 為什麼選擇 Google 試算表?

Google 試算表(Google Sheets)在知識庫管理上有幾個獨特的優勢:

**協作友善**

Google 試算表支援多人即時協作,團隊成員可以同時編輯內容,變更會立即同步。你可以設定不同的權限等級,讓某些人只能檢視,某些人可以編輯,還可以追蹤誰修改了什麼內容。這對於需要多人共同維護知識庫的組織來說非常實用。

**介面簡單**

試算表的介面是大家都熟悉的表格形式,不需要學習新的工具。即使是完全不懂程式的人,也能輕鬆新增和編輯知識。這大幅降低了知識庫維護的門檻。

**版本控制**

Google 試算表會自動儲存歷史版本,你可以隨時查看過去的修改記錄,甚至還原到某個時間點的狀態。這個功能在知識庫管理中非常重要,萬一有人誤刪或誤改內容,都能輕易復原。

**公式與函式**

試算表提供強大的公式功能,可以自動計算、篩選、排序資料。例如,你可以用公式自動標記「超過 3 個月未更新」的知識,提醒團隊進行審查。

**無縫整合**

透過 Google Apps Script(GAS),試算表可以變成一個 API 端點,讓我們的 RAG 系統能夠讀取試算表中的資料。這個整合過程比想像中簡單許多。

### Google 試算表的基本設定

在開始整合之前,讓我們先準備 Google 試算表。

**建立知識庫試算表**

1. 前往 [Google Sheets](https://sheets.google.com)
2. 點擊「新增空白試算表」
3. 將試算表命名為「RAG 知識庫」或其他你喜歡的名稱

**設定表格結構**

在第一列建立標題,這些欄位名稱要與系統的資料格式對應:

| 問題 | 答案 | 分類 | 更新時間 | 來源 | 備註 |
|------|------|------|----------|------|------|
| Flask 是什麼? | Flask 是一個輕量級的... | 程式設計 | 2025-01-19 | 技術文件 | 已審查 |
| 如何安裝 Python? | 安裝 Python 的步驟... | 環境設定 | 2025-01-18 | 操作手冊 | 待更新 |

**必填欄位:**
- **問題**:使用者可能提出的問題
- **答案**:對應的答案內容

**選填欄位:**
- **分類**:知識的分類(預設為「一般」)
- **更新時間**:最後修改的日期
- **來源**:資料的來源標記
- **備註**:其他說明或審查狀態

**填入範例資料**

為了測試整合功能,先在試算表中填入幾筆範例資料。可以參考專案中的 `data/knowledge_base_example.csv` 檔案,將內容複製到試算表中。

**設定共用權限**

點擊右上角的「共用」按鈕,設定誰可以存取這個試算表:

- **檢視者**:只能查看,不能編輯
- **評論者**:可以新增評論,但不能修改內容
- **編輯者**:可以修改內容

根據團隊需求設定適當的權限。如果要讓系統能夠讀取試算表,需要將權限設為「知道連結的使用者可以檢視」或「公開」。

### Google Apps Script API 部署

現在讓我們建立一個 API 端點,讓 RAG 系統能夠讀取試算表資料。這是透過 Google Apps Script(GAS)實現的。

**開啟 Apps Script 編輯器**

1. 在試算表中,點擊上方選單的「擴充功能」→「Apps Script」
2. 會開啟一個新視窗,這就是 GAS 編輯器
3. 將預設的程式碼刪除,準備貼上我們的程式碼

**貼上 API 程式碼**

專案的 `gas_scripts/知識庫API.gs` 檔案包含了完整的 GAS 程式碼。讓我們看看核心的部分:

```javascript
function doGet(e) {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const data = sheet.getDataRange().getValues();

  // 第一列是標題
  const headers = data[0];
  const rows = data.slice(1);

  // 轉換成 JSON 格式
  const jsonData = rows.map(row => {
    const obj = {};
    headers.forEach((header, index) => {
      obj[header] = row[index];
    });
    return obj;
  });

  return ContentService
    .createTextOutput(JSON.stringify({
      success: true,
      data: jsonData,
      count: jsonData.length
    }))
    .setMimeType(ContentService.MimeType.JSON);
}
```

這段程式碼做了幾件事:

1. `getActiveSheet()` 獲取當前的工作表
2. `getDataRange().getValues()` 讀取所有資料
3. 將第一列作為標題,其餘列作為資料內容
4. 將每一列轉換成 JSON 物件,鍵名是標題,值是對應的儲存格內容
5. 回傳 JSON 格式的資料

**部署為 Web 應用程式**

1. 點擊編輯器上方的「部署」→「新增部署作業」
2. 選擇類型為「網頁應用程式」
3. 設定「執行身分」為「我」
4. 設定「具有存取權的使用者」為「所有人」(這樣系統才能讀取)
5. 點擊「部署」

**複製 API URL**

部署完成後,會顯示一個 URL,類似:

```
https://script.google.com/macros/s/ABCDEFG.../exec
```

這就是你的 API 端點。複製這個 URL,等等會用到。

**測試 API**

在瀏覽器中直接開啟這個 URL,應該會看到 JSON 格式的資料,包含試算表中的所有內容。如果看到類似以下的結果,就表示 API 部署成功:

```json
{
  "success": true,
  "data": [
    {
      "問題": "Flask 是什麼?",
      "答案": "Flask 是一個輕量級的...",
      "分類": "程式設計",
      "更新時間": "2025-01-19"
    }
  ],
  "count": 1
}
```

### 在 RAG 系統中同步試算表

現在讓我們在 RAG 平台中使用這個 API,將試算表的資料同步到本地知識庫。

**開啟同步對話框**

1. 啟動 RAG 平台(`python app.py`)
2. 在瀏覽器中開啟 `http://127.0.0.1:5001`
3. 點擊右上角「🗄️ 知識庫管理」
4. 點擊「☁️ 同步試算表」按鈕

**輸入 API URL**

在彈出的對話框中,貼上剛才複製的 GAS API URL,然後點擊「立即同步」。

**同步過程**

前端會發送請求到 GAS API,獲取試算表資料,然後批次新增到本地知識庫。讓我們看看 `script.js:614-661` 的同步程式碼:

```javascript
async function syncGoogleSheets() {
    const gasApiUrl = elements.gasApiUrl.value.trim();

    try {
        // 從 GAS 取得資料
        const response = await fetch(gasApiUrl + '?action=list');
        const result = await response.json();

        const gasData = result.data;

        // 批次新增到本地
        for (const item of gasData) {
            await fetch('/api/knowledge-base', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    question: item['問題'] || item['question'],
                    answer: item['答案'] || item['answer'],
                    category: item['分類'] || item['category'] || '一般'
                })
            });
        }

        showNotification(`成功同步 ${gasData.length} 筆資料`, 'success');
        loadKnowledgeBase();
    } catch (error) {
        showNotification('同步失敗: ' + error.message, 'error');
    }
}
```

這個函式會:
1. 向 GAS API 發送請求,獲取試算表資料
2. 遍歷每筆資料,呼叫本地的 `/api/knowledge-base` 端點新增
3. 同時處理中文和英文欄位名稱(試算表可能用「問題」或「question」)
4. 同步完成後重新載入知識庫列表

**驗證同步結果**

同步完成後,在知識庫管理介面中應該會看到新增的資料。可以:
- 檢查筆數是否正確
- 確認問題、答案、分類是否正確匯入
- 測試搜尋功能,看看新資料能否被檢索到

### 試算表協作的最佳實踐

當使用 Google 試算表作為知識庫來源時,有一些實踐建議:

**建立編輯規範**

在試算表的第一個工作表(Sheet1)放知識資料,可以另外建立一個「編輯指南」工作表,說明:
- 每個欄位的用途和格式要求
- 問題和答案的撰寫原則
- 分類的標準選項
- 審查流程

**使用資料驗證**

在「分類」欄位設定下拉選單,避免分類名稱不一致:
1. 選擇「分類」欄位
2. 點擊「資料」→「資料驗證」
3. 設定允許的值:程式設計、環境設定、FAQ、故障排除等
4. 勾選「拒絕無效資料」

這樣能確保分類的一致性,方便後續分析和管理。

**定期同步**

建立定期同步的習慣:
- 每次團隊會議後同步一次
- 新增大量資料後立即同步
- 定期(例如每週)檢查並同步

也可以在試算表中加入「同步狀態」欄位,標記哪些資料已經同步、哪些是新增待同步的。

**版本管理**

利用試算表的版本歷史功能:
- 點擊「檔案」→「版本記錄」→「查看版本記錄」
- 可以看到所有修改記錄,包含誰在何時修改了什麼
- 必要時可以還原到舊版本

建議在每次大規模修改前,先手動建立一個具名版本(點擊版本旁的「...」→「為這個版本命名」),方便日後追溯。

**權限管理**

妥善設定權限:
- **核心團隊**:編輯權限,可以自由新增修改
- **審查人員**:評論權限,可以提出修改建議
- **一般員工**:檢視權限,只能查看內容
- **系統帳號**:透過 GAS API 讀取,不需要編輯權限

### 進階應用:雙向同步

目前的整合是「單向」的:從試算表同步到系統。但你也可以實作「雙向同步」,讓在系統中新增的知識也能同步回試算表。

這需要在 GAS 中實作 `doPost` 函式,接受系統發送的新知識:

```javascript
function doPost(e) {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const data = JSON.parse(e.postData.contents);

  // 在試算表末尾新增一列
  sheet.appendRow([
    data.question,
    data.answer,
    data.category || '一般',
    new Date().toLocaleString('zh-TW'),
    '系統新增'
  ]);

  return ContentService
    .createTextOutput(JSON.stringify({success: true}))
    .setMimeType(ContentService.MimeType.JSON);
}
```

然後在系統的 `add_knowledge()` 函式中,新增知識後也發送到 GAS API,實現雙向同步。

不過要注意,雙向同步會增加系統複雜度,可能會有同步衝突的問題。在實務應用中,建議選擇一個主要的資料來源(通常是試算表),其他地方作為輔助新增管道,定期合併即可。

### Google 試算表整合的價值

透過 Google 試算表整合,RAG 系統的知識庫管理變得更加靈活和開放:

- **降低維護門檻**:不懂技術的團隊成員也能貢獻知識
- **提升協作效率**:多人可以同時編輯,快速擴充知識庫
- **便於審查管理**:透過評論和版本記錄,建立完善的審查機制
- **簡化備份還原**:試算表本身就有完整的歷史記錄和還原功能

這個整合展示了 RAG 系統的開放性:它不是一個封閉的系統,而是可以與各種工具和平台整合,適應不同組織的工作流程。

> 【註記】請截圖「Google 試算表知識庫範例」,命名為 `rag_google_sheets_kb.png`。畫面應顯示格式良好的知識庫試算表,包含問題、答案、分類等欄位,以及幾筆範例資料。

> 【註記】請截圖「GAS 部署成功畫面」,命名為 `rag_gas_deploy.png`。畫面應顯示 Google Apps Script 的部署對話框和產生的 API URL。

---

## 單元 9：小結與延伸應用

恭喜你完成了 RAG 知識庫問答平台的學習!在這個章節中,我們從零開始建立了一個功能完整的 AI 問答系統。現在讓我們回顧一下學到了什麼,以及可以如何延伸應用。

### 本章重點回顧

**從快速部署到深入理解**

我們採用了「先實作,再教學」的學習方式。在 3.1 節,你在 10-15 分鐘內就部署了一個可運作的 RAG 平台,親眼看到了向量搜尋和知識庫引用的效果。這種「先看到成果」的方式,讓後續的技術學習更有動力和方向感。

接著,我們逐步深入探討每個技術環節:RAG 的概念與價值、系統架構設計、向量嵌入原理、Flask 後端實作、JavaScript 前端開發,最後到知識庫品質管理和 Google 試算表整合。這種由淺入深的學習路徑,讓複雜的技術變得可以理解和掌握。

**掌握的核心技術**

透過這個專案,你實際掌握了以下技術:

- **RAG 技術**:理解檢索增強生成的原理,知道如何將外部知識整合到 AI 回答中
- **向量嵌入**:學會使用 Sentence Transformers 將文字轉換成向量,理解語意搜尋的運作方式
- **相似度計算**:掌握餘弦相似度的概念,知道如何找出最相關的知識
- **Flask 框架**:能夠使用 Flask 建立 RESTful API,處理前後端資料交換
- **前端開發**:使用 JavaScript 實作動態網頁、處理非同步請求、管理應用狀態
- **API 整合**:整合 OpenAI 和 Google Gemini API,知道如何呼叫大型語言模型
- **資料管理**:實作知識庫的 CRUD 操作、批次匯入、資料持久化

**建立的實用系統**

更重要的是,你建立了一個真正實用的系統。這不是一個教學用的玩具專案,而是可以實際應用的平台:

- 完整的知識庫管理介面
- 支援多種 AI 模型切換
- 向量相似度搜尋與來源引用
- 批次匯入與資料匯出
- Google 試算表整合
- 對話歷史管理
- 響應式使用者介面

這個系統可以直接部署使用,也可以作為基礎進行客製化開發。

### 延伸應用方向

基於這個專案,你可以往多個方向延伸發展:

**1. 企業知識管理系統**

將這個平台應用到企業內部,建立專業的知識管理系統:

- **整合企業文件**:將公司的操作手冊、政策文件、產品規格整理成知識庫
- **部門專屬知識庫**:為不同部門建立獨立的知識庫,支援切換查詢
- **權限管理**:加入使用者認證,不同員工可以存取不同的知識範圍
- **使用分析**:追蹤哪些問題最常被查詢,哪些知識最有價值,優化知識庫內容

**2. 客戶服務機器人**

將平台改造成客戶服務系統:

- **即時聊天整合**:整合到網站的即時聊天視窗,提供 24/7 自動回覆
- **多語言支援**:由於 Embedding 模型支援多語言,可以建立多語言知識庫
- **人工轉接**:當 AI 無法回答時,自動轉接給真人客服
- **對話評分**:讓使用者為每次對話評分,持續優化服務品質

**3. 教育學習平台**

轉化為教育領域的應用:

- **課程助教系統**:為每門課程建立知識庫,學生可以隨時提問
- **學習歷程追蹤**:記錄學生的提問歷史,分析學習盲點
- **個人化推薦**:根據學生的問題,推薦相關的學習資源
- **作業輔導**:整合程式範例和常見錯誤,協助學生解決作業問題

**4. 技術文件問答系統**

特別適合開發者社群或開源專案:

- **API 文件問答**:將 API 文件整理成知識庫,開發者可以快速查詢使用方法
- **故障排除助手**:整理常見錯誤和解決方案,協助開發者除錯
- **版本更新說明**:當產品更新時,自動加入新功能的說明到知識庫
- **程式碼範例庫**:提供豐富的程式碼範例,並能根據需求檢索

**5. 個人知識助理**

將平台用於個人知識管理:

- **讀書筆記整理**:將閱讀的書籍、文章整理成知識庫,隨時複習
- **專案經驗總結**:記錄專案中的問題和解決方案,建立個人知識資產
- **興趣學習助手**:整理學習某個領域的資源和心得,系統化學習
- **靈感收集**:將日常的想法、靈感記錄下來,需要時可以快速檢索

### 技術進階方向

如果你想在技術上更進一步,可以考慮以下改進:

**效能最佳化**

- **使用專業向量資料庫**:當知識庫規模超過 1000 筆,考慮使用 ChromaDB、Pinecone 或 Milvus
- **實作快取機制**:將常見問題的答案快取起來,減少重複計算
- **非同步處理**:使用 asyncio 處理 AI API 呼叫,提升回應速度
- **CDN 加速**:將前端資源部署到 CDN,加快載入速度

**功能擴充**

- **多輪對話記憶**:改進對話歷史管理,讓 AI 能夠理解更複雜的多輪對話
- **檔案上傳解析**:支援上傳 PDF、Word 文件,自動解析成知識庫
- **圖片與多媒體**:擴充知識庫支援圖片、影片連結
- **知識圖譜**:建立知識之間的關聯,提供更豐富的上下文

**安全性強化**

- **API Key 後端儲存**:將 API Key 移到後端管理,避免前端洩漏
- **使用者認證**:加入登入機制,保護知識庫不被未授權存取
- **輸入驗證**:防範 SQL 注入、XSS 等安全風險
- **速率限制**:限制 API 呼叫頻率,防止濫用

**部署與維運**

- **容器化部署**:使用 Docker 打包應用,簡化部署流程
- **雲端部署**:部署到 Render、Heroku、Railway 等平台
- **監控與日誌**:加入應用監控和錯誤追蹤,及時發現問題
- **自動化測試**:撰寫單元測試和整合測試,確保程式品質

### 學習資源推薦

想要繼續深入學習相關技術,以下是一些推薦資源:

**RAG 與向量搜尋**
- Sentence Transformers 官方文件:了解更多 Embedding 模型選項
- LangChain 框架:專門用於建立 LLM 應用的 Python 框架
- Pinecone Learning Center:向量資料庫的概念與應用

**Flask 與 Python**
- Flask 官方教學:深入學習 Flask 的進階功能
- Real Python:高品質的 Python 教學文章
- Python Web Development with Flask:完整的 Flask 開發指南

**前端開發**
- MDN Web Docs:最權威的網頁技術文件
- JavaScript.info:現代 JavaScript 教學
- CSS-Tricks:CSS 技巧與最佳實踐

**AI 與 LLM**
- OpenAI Cookbook:OpenAI 提供的實用範例集
- Google AI for Developers:Google AI 技術文件
- Hugging Face Course:機器學習與 NLP 課程

### 結語

RAG 技術正在改變 AI 應用的開發方式。過去,如果要讓 AI 具備專業領域的知識,需要重新訓練模型,成本高昂且技術門檻高。現在,透過 RAG,我們只需要建立知識庫,就能讓通用的 AI 模型具備專業能力。這大幅降低了 AI 應用的開發成本,也讓更多人能夠參與 AI 的應用創新。

你在本章建立的不只是一個技術專案,更是一個可以持續成長的知識系統。隨著知識庫的擴充和優化,系統的價值會不斷提升。無論是用於工作、學習還是個人興趣,這個平台都能成為你的得力助手。

在下一章中,我們將探討如何將這個系統部署到雲端,讓它能夠 24/7 運行,並能夠被更多人使用。我們也會學習如何整合 LINE Bot,將 RAG 能力帶到更多使用情境中。

但在繼續之前,建議你先實際使用這個系統一段時間,建立自己的知識庫,體驗 RAG 技術的實際效果。唯有透過實踐,你才能真正理解技術的價值,也才能發現更多創新的應用可能。

讓我們繼續前進,探索 AI 應用開發的更多精彩內容!

> 【註記】請製作「RAG 系統延伸應用示意圖」,命名為 `rag_extension_diagram.png`。圖中應包含核心的 RAG 平台,以及連接到企業知識管理、客戶服務、教育學習、技術文件等不同應用場景的延伸路徑。

---

