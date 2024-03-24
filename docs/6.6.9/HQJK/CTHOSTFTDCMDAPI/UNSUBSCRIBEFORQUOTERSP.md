<p>退订询价，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPUNSUBFORQUOTERSP/">OnRspUnSubForQuoteRsp</a></p>
<span class="anchor" id="bd6606e2-6c33-4cd3-9df4-9b928705a7c2"></span>
## 1.函数原型
<p>virtual int UnSubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="7670acf6-7d7e-46bc-90f1-8f187171e0de"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="5d79c794-4035-4837-875f-867a5ac5c411"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6703f8c5-1612-485b-b354-68ce815d99fd"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = “sc1801”;
m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="2e5653bb-3679-4a23-8ab4-1f6b82ba3a73"></span>
## 5.FAQ
<p>无</p>
