<p>订阅询价，对应响应OnRspSubForQuoteRsp；订阅成功后推送OnRtnForQuoteRsp。</p>
<p>询价相关业务请参考：<a href="../../../QTYWGZ/BJHXJ/">做市商询价和报价</a></p>
<span class="anchor" id="eccd6eed-3684-4bea-80f5-b2ea2d7cda9d"></span>
## 1.函数原型
<p>virtual int SubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="436d8f36-f8b0-46db-b41c-93ff0e1604c5"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="e6cb7ab6-e86b-482d-95f5-01a436f11b50"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="9dca816d-67b3-4211-b63b-7eff3adc89aa"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50]; 
ppInstrumentID[0] = “sc1801”;
int result = m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="0b04d9d9-76d5-4b95-80c0-38e91e43700a"></span>
## 5.FAQ
