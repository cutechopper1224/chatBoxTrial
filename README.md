# 遊音文機器人
## 功能簡介：
1. 查詢遊戲角色資料，包括其素質、技能以及立繪
2. 和機器人玩猜歌遊戲，根據機器人提供的歌詞猜歌名
3. 瀏覽批踢踢實業坊的文章，根據推文數進行篩選
4. 輸入英文單字，給予解釋以及例句

## FSM架構：
![fsm](https://github.com/cutechopper1224/chatBoxTrial/blob/master/fsm.png)

## 如何開始：
1. 路線一：輸入**「你好」**和機器人打招呼後，機器人會要求驗證身分，此時若回答**「正妹」**，機器人就會提供核心服務，若是回答**「資訊系肥宅」**，將被機器人強制驅離（回到user state）。如果以上兩種都不選，自行創造身分的話，機器人會以**「我看還是算了吧」**來敷衍並驅離。
2. 路線二：輸入「你是大帥哥」以諂媚機器人，機器人會回覆「你就試著取悅我吧」以探知使用者真實的心意。此時輸入「求您疼我」即可直接獲得機器人的核心服務，否則機器人依然會以「我看還是算了吧」來敷衍。
3. 路線三：輸入一個有意義的英文單字，機器人會告訴你它的英文解釋，如果心情好的話也會附上例句。（此功能使用nltk套件製作）不會進到核心服務。
4. 都不選：如果以上條件均不被滿足，機器人會隨機回覆你一些罐頭訊息。

## 核心服務：
核心服務一共有三個項目：

### 1. 查詢聖火手遊資料：
    
    點擊「查詢聖火手遊資料」按鈕或輸入相應文字可以進入這個服務。成功進入後，系統會詢問你想要查詢的角色的裝備。這時要根據按鈕上文字的提示輸入正確的武器類型（並非點選按鈕，請注意），如果有誤的話，系統將會判定使用者是智障，然後強制遣返至初始狀態。否則角色的武器將被確定，系統會更進一步的詢問角色的移動方式，一共有「步行、騎兵、重甲、飛行」四種可以選擇（一樣必須直接輸入文字），如果有誤依然會被當成智障，否則系統就會開始調查角色們的身家，提供可能有你想要找的人的清單。如果系統發現沒有人符合你選擇的搭配的話，將會告訴你「並沒有符合你的期待的英雄」，並返回讓你重新選擇武器類型。若非如此，只要輸入正確的角色名稱，就可以選擇對這名角色更進一步的操作。否則亂輸入的話仍然會被當成智障處理。

更進一步的操作也有三種：

i. 點選或輸入「英雄標準體質」：將可以看到該名角色在等級40下的標準體質。
ii. 點選或輸入「擁有技能」 ：將可以看到該名角色持有的所有技能，以及推薦給別人繼承的技能是哪幾項。
iii. 點選或輸入「看照片」   ：機器人會把他蒐集到和那名角色有關的照片展示給你看
iv. 亂輸入                 ： 機器人會回應「還有這種操作？」，然後將你驅逐

若以上操作成功（當然不包含第三項），系統將會詢問是否要繼續這三項的操作，如果回答「好、是、對」，將可以繼續瀏覽你有興趣的項目，否則回答「否」、「換別人」
、「想換一個」、「來點別的」，就會切換到詢問武器類型的那一個狀態，以利你對於新角色的查詢。

簡單範例：輸入「杖」->「騎兵」->「ヴェロニカ」->點選「看照片」

### 2. 玩猜歌遊戲：
   
    點擊「玩猜歌遊戲」按鈕或輸入相應文字可以進入這個服務。一開始可以選擇要猜的類型，像是「男歌手」和「女歌手」，點選其中一個之後，系統會隨機挑一首歌，然後出示它的一部分歌詞，接下來使用者必須輸入正確的完整歌名，如果回答無誤，機器人會回覆「你答對了！」，否則回應「你猜錯了，應是xxxx」。無論猜對或猜錯，系統都會詢問是否要繼續遊戲，選擇「好」、「是」、「對」其中一個就可以繼續，選擇「不要」便會跳回選擇核心服務的入口。過程中如果有試圖挑戰機器人智商的行為，都會被判定為智障。

簡單範例：輸入「女歌手」->「（歌名）」->選擇「不要」

### 3. 看ptt的文章：
  
    點擊「看ptt的文章」按鈕或輸入相應文字可以進入這個服務。一開始系統會詢問要瀏覽的看板，請直接輸入看板的名稱，如「Fantasy」、「KoreaDrama」，要注意的是十八禁的看板（如八卦板）會被系統自動屏蔽。若該看板存在，機器人會追問想要看的文章數目，請輸入阿拉伯數字。最後機器人會問想要看到的文章在幾推以上，如果只想看到爆文，可以輸入「99」，若以上操作無誤，系統會列出所要求文章數目的標題及其連結，並詢問是否要繼續看文章，是和上一個服務項目一樣的機制。如果以上的操作有誤，就會被系統歸類為低能用戶。
    
簡單範例：輸入「C_Chat」->「5」->「80」->點選「不要」
