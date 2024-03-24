<p>订阅询价，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPSUBFORQUOTERSP/">OnRspSubForQuoteRsp</a>；订阅成功后推送<a href="../../CTHOSTFTDCMDSPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>。</p>
<p>询价相关业务请参考：<a href="../../../QTYWGZ/BJHXJ/">做市商询价和报价</a></p>
<span class="anchor" id="e694e5f9-cd2f-4b30-88c9-85db1e1a88cb"></span>
## 1.函数原型
<p>virtual int SubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="d99951cf-3524-4249-a077-99d907e03074"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="a1e03b36-e86b-4313-959c-17010aca2ac7"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="27997c2d-d993-426f-a49e-aaa9ddcee8f1"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50]; 
ppInstrumentID[0] = “sc1801”;
int result = m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="e1c47684-2fce-4a1d-b743-00628cb7ffc1"></span>
## 5.FAQ
