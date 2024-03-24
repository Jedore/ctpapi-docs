<p>退订询价，对应响应OnRspUnSubForQuoteRsp</p>
<span class="anchor" id="812bd2e6-0fd0-4934-90c2-82333cabaeb3"></span>
## 1.函数原型
<p>virtual int UnSubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="5a098e42-fa53-4869-8ec8-aca0461583e1"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="3d606f8d-c181-4c9f-9194-c6dc428269e6"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c67b373d-c3ad-45a2-bfa3-a484dcad40d3"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = “sc1801”;
m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="c05988e1-c576-47a3-8415-40dfd876a35f"></span>
## 5.FAQ
<p>无</p>
