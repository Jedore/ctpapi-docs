<p>退订行情，对应响应OnRspUnSubMarketData。</p>
<span class="anchor" id="b14a9410-e0d2-42fc-9778-7a68c282422c"></span>
## 1.函数原型
<p>virtual int UnSubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="aae43c43-4571-4d80-a89c-b5073163b3f6"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="ce9412ee-d3a6-45ac-8900-791ef09db05a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="481ed961-b6ae-409c-b6b0-92cf00dd6f2a"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = "T1712";
m_pUserMdApi-&gt;UnSubscribeMarketData(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="09336b2b-eea7-46f6-9936-ece6849526aa"></span>
## 5.FAQ
<p>无</p>
