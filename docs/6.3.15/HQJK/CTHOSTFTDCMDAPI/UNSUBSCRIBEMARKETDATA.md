<p>退订行情，对应响应OnRspUnSubMarketData。</p>
<span class="anchor" id="11bae682-8574-44ae-bc95-5c2d7d62f985"></span>
## 1.函数原型
<p>virtual int UnSubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="0ad7af37-1b5a-45ab-9cec-39b5f7a1ee71"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="4e31e2db-1694-41d8-85c5-c065c8e496cf"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0edcd6aa-9449-41f0-a2e9-6d87405af1f4"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = "T1712";
m_pUserMdApi-&gt;UnSubscribeMarketData(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="f4e32700-c821-449e-a8cb-0e1cee251bae"></span>
## 5.FAQ
<p>无</p>
