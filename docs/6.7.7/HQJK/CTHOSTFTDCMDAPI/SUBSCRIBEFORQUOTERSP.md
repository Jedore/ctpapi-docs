<p>订阅询价，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPSUBFORQUOTERSP/">OnRspSubForQuoteRsp</a>；订阅成功后推送<a href="../../CTHOSTFTDCMDSPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>。</p>
<p>询价相关业务请参考：<a href="../../../QTYWGZ/BJHXJ/">做市商询价和报价</a></p>
<span class="anchor" id="c7a43d52-9f04-43a7-8d7e-9d430a08264c"></span>
## 1.函数原型
<p>virtual int SubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="d6181e38-ed43-4ac9-be11-01a521ca3d38"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="37412689-7a65-4efc-a0da-484d1949dcbc"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="979c44bd-e37b-4544-8873-ef1af2122595"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50]; 
ppInstrumentID[0] = “sc1801”;
int result = m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="3ef3cafa-c0b2-4a2f-89a9-fbbda4c800fb"></span>
## 5.FAQ
