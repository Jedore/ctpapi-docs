<p>退订询价，对应响应OnRspUnSubForQuoteRsp</p>
<span class="anchor" id="70dc5bfb-e7a8-41fe-8934-c9d03c65f096"></span>
## 1.函数原型
<p>virtual int UnSubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="3fa66682-b47d-4f74-93dd-1c38435075c2"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="41e1cf6a-5ee0-404d-b304-109c0b2b617a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="e131384f-f0bd-4d4e-ba47-d9c98124c9ce"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = “sc1801”;
m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="37ce8e64-ff94-476b-8db5-9f893ba4e659"></span>
## 5.FAQ
<p>无</p>
