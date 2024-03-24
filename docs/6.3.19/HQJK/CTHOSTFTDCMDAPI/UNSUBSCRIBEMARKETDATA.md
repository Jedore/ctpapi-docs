<p>退订行情，对应响应OnRspUnSubMarketData。</p>
<span class="anchor" id="3883850f-7874-4ab6-b2b6-e42c4e7ba5b5"></span>
## 1.函数原型
<p>virtual int UnSubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="e76807c0-71c3-4368-a895-c37416361d76"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="e70668b3-0cf9-4fa2-81e0-a14d2f054b03"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="4f0a9eb4-da1d-46e4-8eca-9c6452bb98b4"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = "T1712";
m_pUserMdApi-&gt;UnSubscribeMarketData(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="d52fbe24-c8fe-4123-a5ca-7aa90656f5fd"></span>
## 5.FAQ
<p>无</p>
