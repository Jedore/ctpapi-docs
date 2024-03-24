<p>退订行情，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPUNSUBMARKETDATA/">OnRspUnSubMarketData</a>。</p>
<span class="anchor" id="461d7891-7f99-4b60-9e90-e528402da780"></span>
## 1.函数原型
<p>virtual int UnSubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="326f75ae-6a53-456e-b3e2-32f3169c7f83"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="e762adbf-ac39-46a3-84a4-0d11e79d559a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="fc53ba87-618f-4e76-9d75-9e89da143bf5"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = "T1712";
m_pUserMdApi-&gt;UnSubscribeMarketData(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="3abc1c9e-1fd6-46e6-8b4e-0578d00e82ac"></span>
## 5.FAQ
<p>无</p>
