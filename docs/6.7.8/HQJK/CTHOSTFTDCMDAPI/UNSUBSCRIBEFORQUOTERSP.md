<p>退订询价，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPUNSUBFORQUOTERSP/">OnRspUnSubForQuoteRsp</a></p>
<span class="anchor" id="e2778bc8-3635-4d29-a159-7823c878a576"></span>
## 1.函数原型
<p>virtual int UnSubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="87805027-852a-423e-8955-6d7d8e96f680"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="75a2bf48-1e2d-43f5-ba7a-e9a9dc03bd19"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="800aec28-6d0a-4f38-bba7-0a992665cb92"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = “sc1801”;
m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="2108920c-61aa-4a87-9e58-880ef317a70d"></span>
## 5.FAQ
<p>无</p>
