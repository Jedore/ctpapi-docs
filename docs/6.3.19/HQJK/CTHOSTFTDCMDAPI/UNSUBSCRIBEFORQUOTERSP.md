<p>退订询价，对应响应OnRspUnSubForQuoteRsp</p>
<span class="anchor" id="447ae233-64eb-4983-85d2-7046691516fd"></span>
## 1.函数原型
<p>virtual int UnSubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="c32c991a-4b0d-4f1a-a7a2-7e57c2783fad"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="35dfd134-afbe-4e52-b57c-5da77f45f154"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="29fad1d1-d752-4a27-b469-c763771a86a8"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = “sc1801”;
m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="ea6e462e-95d4-489d-baf5-39b36c5659d2"></span>
## 5.FAQ
<p>无</p>
