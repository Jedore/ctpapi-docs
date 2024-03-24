<p>退订行情，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPUNSUBMARKETDATA/">OnRspUnSubMarketData</a>。</p>
<span class="anchor" id="a903d3f1-0b3c-4152-9786-4335229ba0ad"></span>
## 1.函数原型
<p>virtual int UnSubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="10e7286f-8c62-4ddf-ba0c-4f18dfc519f8"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="4ecf41ff-7231-4353-b59c-f8cc98b0fcbe"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="9807de1f-1b8d-48d2-b3ce-0c960d15c055"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = "T1712";
m_pUserMdApi-&gt;UnSubscribeMarketData(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="e98617ad-0cc8-498f-8397-1cd759ef6704"></span>
## 5.FAQ
<p>无</p>
