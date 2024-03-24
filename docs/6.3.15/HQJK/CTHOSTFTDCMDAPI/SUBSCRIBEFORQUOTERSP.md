<p>订阅询价，对应响应OnRspSubForQuoteRsp；订阅成功后推送OnRtnForQuoteRsp。</p>
<p>询价相关业务请参考：<a href="../../../QTYWGZ/BJHXJ/">做市商询价和报价</a></p>
<span class="anchor" id="4ecc08f5-12fd-4565-9183-d45f8be6297a"></span>
## 1.函数原型
<p>virtual int SubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="3a555063-ec48-464a-82ba-e4c9b3c0c48f"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="a4c72e67-61c9-4f97-9f41-ea0b29dcf38f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="7cc888f6-45f8-439a-961e-3b429c25aaf1"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50]; 
ppInstrumentID[0] = “sc1801”;
int result = m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="d8b4405d-a1ac-4918-81a0-20f78ad794a4"></span>
## 5.FAQ
