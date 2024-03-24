<p>订阅询价，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPSUBFORQUOTERSP/">OnRspSubForQuoteRsp</a>；订阅成功后推送<a href="../../CTHOSTFTDCMDSPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>。</p>
<p>询价相关业务请参考：<a href="../../../QTYWGZ/BJHXJ/">做市商询价和报价</a></p>
<span class="anchor" id="b9e9103e-4f6d-4b8b-a691-734b0011667f"></span>
## 1.函数原型
<p>virtual int SubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="c9b1cfe2-59ca-41f1-9dc3-4f389df7f94d"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="6867bf6f-1fc8-4b27-a97e-e8ca4ea87ec6"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="f441585d-32c2-450a-b505-7df6bfe90389"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50]; 
ppInstrumentID[0] = “sc1801”;
int result = m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="f8f82990-bd17-4e06-acc6-46a835a8852b"></span>
## 5.FAQ
