<p>订阅询价，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPSUBFORQUOTERSP/">OnRspSubForQuoteRsp</a>；订阅成功后推送<a href="../../CTHOSTFTDCMDSPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>。</p>
<p>询价相关业务请参考：<a href="../../../QTYWGZ/BJHXJ/">做市商询价和报价</a></p>
<span class="anchor" id="6073844e-71f0-488b-b4a5-6367d08f5d0b"></span>
## 1.函数原型
<p>virtual int SubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="04341a5e-b401-4368-ad64-8249f57992c4"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="47b4ac85-5a67-4da5-aeb8-29149f70d4b6"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="076c8328-3163-4d88-86a6-292cce3f29f2"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50]; 
ppInstrumentID[0] = “sc1801”;
int result = m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="4ef4a07b-1b87-4a6e-b8ea-3b44b54f4f0a"></span>
## 5.FAQ
