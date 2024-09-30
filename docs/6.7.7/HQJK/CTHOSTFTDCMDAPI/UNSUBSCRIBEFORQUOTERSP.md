<p>退订询价，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPUNSUBFORQUOTERSP/">OnRspUnSubForQuoteRsp</a></p>
<span class="anchor" id="0c3ba65f-5a4d-4f2b-8a98-0ce26d47ac6e"></span>
## 1.函数原型
<p>virtual int UnSubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="e3538e9a-a02d-44df-9532-4237a54529f1"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="df0cc847-ec58-43e8-a364-5dcbb632533a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c75b1127-dfce-4643-9282-853f83449855"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = “sc1801”;
m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="5a09adf5-7f90-4e15-807f-b95f3ec6dc8e"></span>
## 5.FAQ
<p>无</p>
