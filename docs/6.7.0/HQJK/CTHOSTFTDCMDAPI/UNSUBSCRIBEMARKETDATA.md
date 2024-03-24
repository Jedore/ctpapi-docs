<p>退订行情，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPUNSUBMARKETDATA/">OnRspUnSubMarketData</a>。</p>
<span class="anchor" id="ec1158df-da30-4c37-8883-3e3d32b1baca"></span>
## 1.函数原型
<p>virtual int UnSubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="e90ba996-2389-4273-9423-2b537b4b5d51"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="fdf5f905-4048-43aa-aca0-8c327dbea0a0"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a2610c72-b482-4664-9954-069f04523d8b"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = "T1712";
m_pUserMdApi-&gt;UnSubscribeMarketData(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="67dc3b9f-0aad-48f8-b007-d2f90ac2dbb5"></span>
## 5.FAQ
<p>无</p>
