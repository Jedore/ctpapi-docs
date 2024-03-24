<p>退订行情，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPUNSUBMARKETDATA/">OnRspUnSubMarketData</a>。</p>
<span class="anchor" id="1aea974f-0187-438e-b281-04fdfbd825b5"></span>
## 1.函数原型
<p>virtual int UnSubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="3aefd32d-abc3-4433-8ac7-805ab32c40db"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="963f8cc7-e3e4-4343-96ef-a1651cd29f24"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2d9a7460-779f-4084-a379-a6b688418174"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = "T1712";
m_pUserMdApi-&gt;UnSubscribeMarketData(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="76ac3800-6d13-4baf-a246-9a50d3a76e13"></span>
## 5.FAQ
<p>无</p>
