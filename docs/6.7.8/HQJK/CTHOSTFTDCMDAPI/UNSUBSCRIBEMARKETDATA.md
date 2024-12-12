<p>退订行情，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPUNSUBMARKETDATA/">OnRspUnSubMarketData</a>。</p>
<span class="anchor" id="62065b36-5dff-43b9-9ec8-b5af82e8c70f"></span>
## 1.函数原型
<p>virtual int UnSubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="6b028968-d9f0-478e-9b8d-ec2e2290d747"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="f4617c61-a688-441f-a8c2-9e900d760700"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="e5e40b3e-ac13-484b-b69c-461189c845de"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = "T1712";
m_pUserMdApi-&gt;UnSubscribeMarketData(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="9b745b70-e2dc-448f-8987-828a7dfa100b"></span>
## 5.FAQ
<p>无</p>
