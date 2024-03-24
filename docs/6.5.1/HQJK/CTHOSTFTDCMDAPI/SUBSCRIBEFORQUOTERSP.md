<p>订阅询价，对应响应OnRspSubForQuoteRsp；订阅成功后推送OnRtnForQuoteRsp。</p>
<p>询价相关业务请参考：<a href="../../../QTYWGZ/BJHXJ/">做市商询价和报价</a></p>
<span class="anchor" id="669afd33-13cc-450b-a905-25a57ccdddaa"></span>
## 1.函数原型
<p>virtual int SubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="30d83d0a-ed32-4761-9530-c498942d61ef"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="2a179fc6-aad4-484f-9949-f77e20c40540"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="5e75badb-7bda-4218-86a2-3b97cddc6320"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50]; 
ppInstrumentID[0] = “sc1801”;
int result = m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="0d2c088d-410e-4b12-a205-568437e6cf3e"></span>
## 5.FAQ
