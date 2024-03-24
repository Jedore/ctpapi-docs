<p>退订询价，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPUNSUBFORQUOTERSP/">OnRspUnSubForQuoteRsp</a></p>
<span class="anchor" id="c39a1c73-9f60-43d2-8fa8-9fb9f41a49da"></span>
## 1.函数原型
<p>virtual int UnSubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="b55e2453-5bab-438a-b6c2-61dfeb93119a"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="ce79fe27-1d39-48e1-9825-a375fade7b87"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6edd6f6f-4bed-431c-8f2e-7f028a846a43"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = “sc1801”;
m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="cda62456-4375-42df-afb6-ae72a88e135a"></span>
## 5.FAQ
<p>无</p>
