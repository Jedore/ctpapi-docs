<p>订阅询价，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPSUBFORQUOTERSP/">OnRspSubForQuoteRsp</a>；订阅成功后推送<a href="../../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>。</p>
<p>询价相关业务请参考：<a href="../../../QTYWGZ/BJHXJ/">做市商询价和报价</a></p>
<span class="anchor" id="bd445aeb-293a-468d-8458-6bac66c7b79f"></span>
## 1.函数原型
<p>virtual int SubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="ca40c7f0-7f5e-4368-9f11-a85b82bf76f9"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="01d412de-d443-4ab6-8349-2ea089c8dcb1"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0eba7e5b-c64d-4738-934e-05d5df3d2dbb"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50]; 
ppInstrumentID[0] = “sc1801”;
int result = m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="7eff0d50-598f-487e-b766-173a4eeeb52e"></span>
## 5.FAQ
